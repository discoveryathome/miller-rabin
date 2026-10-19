#!/usr/bin/env python3
"""Verifier for claims in this project. Exact rational arithmetic; stdlib only.

    python3 verify/check.py exponent CLAIM.json
    python3 verify/check.py explicit CLAIM.json
    python3 verify/check.py smalln [--limit N]
    python3 verify/check.py all            # every claim in candidates/ + smalln

Exit status 0 means every check passed. See docs/verifier.md for the claim
formats and docs/template-T1.md for what the `explicit` check proves.
"""

import argparse
import json
import math
import sys
from fractions import Fraction
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import mr  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent

# Exponent of the cost of one base: log n squarings mod n, each
# O(log n * log log n) bit operations (Harvey-van der Hoeven multiplication).
PER_BASE_EXPONENT = Fraction(2)


class Reject(Exception):
    pass


def rat(value, name):
    """Parse an exact rational from a JSON string like "7/8" or "0.125"."""
    if not isinstance(value, str):
        raise Reject(f"{name} must be a string holding an exact rational, got {value!r}")
    try:
        return Fraction(value)
    except (ValueError, ZeroDivisionError):
        raise Reject(f"{name}: cannot parse {value!r} as a rational")


def parse_theta(claim):
    theta = rat(claim.get("theta"), "theta")
    if not (Fraction(1, 2) <= theta < 1):
        raise Reject(f"theta must satisfy 1/2 <= theta < 1, got {theta}")
    return theta


# --- rigorous rational bounds on natural logarithms -----------------------

def _atanh_bounds(z, terms=60):
    """Bounds on atanh(z) for rational 0 <= z <= 1/3; error < z^(2*terms+1)."""
    lo = Fraction(0)
    p = z
    for j in range(terms):
        lo += p / (2 * j + 1)
        p *= z * z
    # Tail sum_{j>=terms} z^(2j+1)/(2j+1) <= p / ((2*terms+1) * (1 - z^2)).
    return lo, lo + p / ((2 * terms + 1) * (1 - z * z))


def ln_bounds(n):
    """Rational (lo, hi) with lo <= ln(n) <= hi, for an integer n >= 1."""
    if n < 1:
        raise ValueError("n must be >= 1")
    k = n.bit_length() - 1  # n = 2^k * y with 1 <= y < 2
    y = Fraction(n, 1 << k)
    l2lo, l2hi = _atanh_bounds(Fraction(1, 3))  # ln 2 = 2 atanh(1/3)
    ylo, yhi = _atanh_bounds((y - 1) / (y + 1))  # z < 1/3 since y < 2
    return 2 * (k * l2lo + ylo), 2 * (k * l2hi + yhi)


# --- claim checks ----------------------------------------------------------

def mr_exponent(theta):
    """Running-time exponent of deterministic MR under H(theta)."""
    return PER_BASE_EXPONENT + 1 / (1 - theta)


def check_exponent(claim):
    """A claimed exponent must be an upper bound on 2 + 1/(1 - theta)."""
    theta = parse_theta(claim)
    claimed = rat(claim.get("claimed_exponent"), "claimed_exponent")
    exact = mr_exponent(theta)
    if claimed < exact:
        raise Reject(
            f"claimed exponent {claimed} ({float(claimed):.10f}) is below the exact "
            f"value 2 + 1/(1 - theta) = {exact} ({float(exact):.10f}); rounding down "
            f"overstates the result"
        )
    return {
        "theta": str(theta),
        "witness_exponent": str(1 / (1 - theta)),
        "mr_exponent_exact": str(exact),
        "mr_exponent_decimal": f"{float(exact):.10f}",
        "claimed_exponent": str(claimed),
        "slack": f"{float(claimed - exact):.3g}",
    }


def check_explicit(claim):
    """Check that W(n) = (C ln n + D)^(1/(1-theta)) satisfies Template T1 for all n >= n0.

    With y = C L + D (L = ln n) and x = y^(1/(1-theta)), the T1 inequality
        w1 x - x^theta (alpha L + beta) - (gamma L + delta) > 0
    divided by x^theta = y^m (m = theta/(1-theta)) becomes
        g(L) = (C w1 - alpha) L + (D w1 - beta) - (gamma L + delta) y^(-m) > 0.
    We show g is nondecreasing on [l0, oo) and g(l0) > 0, where l0 <= ln n0.
    """
    theta = parse_theta(claim)
    C = rat(claim.get("C"), "C")
    D = rat(claim.get("D"), "D")
    t = claim.get("template")
    if not isinstance(t, dict):
        raise Reject("missing 'template' object with w1, alpha, beta, gamma, delta, y_min")
    w1, alpha, beta, gamma, delta, y_min = (
        rat(t.get(k), f"template.{k}") for k in ("w1", "alpha", "beta", "gamma", "delta", "y_min")
    )
    n0 = claim.get("n0")
    if not isinstance(n0, int) or isinstance(n0, bool) or n0 < 9:
        raise Reject("n0 must be an integer >= 9")
    if n0 > mr.PSI_13:
        raise Reject(
            f"n0 = {n0} exceeds PSI_13 = {mr.PSI_13}; below n0 the algorithm relies on "
            f"the first 13 prime bases, which is only known to suffice for n < PSI_13"
        )
    if w1 <= 0 or C <= 0:
        raise Reject("need w1 > 0 and C > 0")
    if min(alpha, beta, gamma, delta) < 0:
        raise Reject("alpha, beta, gamma, delta must be >= 0")
    if y_min < 1:
        raise Reject("y_min must be >= 1")

    l0, _ = ln_bounds(n0)
    m = theta / (1 - theta)  # >= 1 because theta >= 1/2
    y0 = C * l0 + D
    if y0 < y_min:
        raise Reject(f"C ln n0 + D = {float(y0):.6g} is below y_min = {y_min}; T1 does not apply at n0")

    slope = C * w1 - alpha
    if slope < 0:
        raise Reject(f"C*w1 - alpha = {slope} < 0: the bound fails for large n")

    if gamma or delta:
        # d/dL log((gamma L + delta) y^-m) <= 0  <=>  gamma D - m C delta <= (m - 1) C gamma L,
        # and the right side is nondecreasing in L since m >= 1.
        if gamma * D - m * C * delta > (m - 1) * C * gamma * l0:
            raise Reject("cannot show the lower-order term is nonincreasing on [ln n0, oo)")

    # y0 >= 1, so y0^-m <= y0^-floor(m).
    tail_hi = (gamma * l0 + delta) / y0 ** math.floor(m)
    g0 = slope * l0 + (D * w1 - beta) - tail_hi
    if g0 <= 0:
        raise Reject(f"g(ln n0) lower bound is {float(g0):.6g} <= 0: inequality not established at n0")

    k = 1 / (1 - theta)
    ln_ref = 1024 * math.log(2)
    return {
        "theta": str(theta),
        "C": str(C),
        "D": str(D),
        "n0": n0,
        "witness_exponent": str(k),
        "g_at_n0_lower_bound": f"{float(g0):.6g}",
        "log10_W_at_2^1024": f"{float(k) * math.log10(float(C) * ln_ref + float(D)):.4f}",
        "theorem": (
            f"Assuming H({theta}) and Template T1 with the stated constants: every odd "
            f"composite n >= {n0} has a prime Miller-Rabin witness p <= "
            f"({C} ln n + {D})^({k}); every odd composite n < {n0} has one among "
            f"the primes <= 41."
        ),
    }


def check_smalln(limit):
    """Sanity checks on the small-n fallback (bases = primes <= 41)."""
    out = {}
    worst = 0
    for n in range(9, limit + 1, 2):
        if mr.is_prime_trial(n):
            if mr.least_prime_witness(n) is not None:
                raise Reject(f"prime {n} reported composite: is_witness is broken")
            continue
        p = mr.least_prime_witness(n)
        if p is None:
            raise Reject(f"odd composite {n} has no witness among primes <= 41")
        worst = max(worst, p)
    out["checked_odd_up_to"] = limit
    out["largest_least_witness_seen"] = worst

    for name, psi, factors, k in (
        ("PSI_12", mr.PSI_12, mr.PSI_12_FACTORS, 12),
        ("PSI_13", mr.PSI_13, mr.PSI_13_FACTORS, 13),
    ):
        if factors[0] * factors[1] != psi:
            raise Reject(f"{name} factorization does not multiply out")
        bases = mr.FIRST_13_PRIMES[:k]
        if any(mr.is_witness(b, psi) for b in bases):
            raise Reject(f"{name} is not a strong pseudoprime to the first {k} primes")
    if not mr.is_witness(41, mr.PSI_12):
        raise Reject("41 should be a witness for PSI_12 (else PSI_13 would equal PSI_12)")
    out["psi_table"] = "PSI_12, PSI_13 factor correctly and are strong pseudoprimes to the first 12 / 13 primes"
    return out


CHECKS = {"exponent": check_exponent, "explicit": check_explicit}


def run_claim(path):
    claim = json.loads(Path(path).read_text())
    kind = claim.get("kind")
    if kind == "mr-exponent":
        return check_exponent(claim)
    if kind == "explicit-witness-bound":
        return check_explicit(claim)
    raise Reject(f"unknown claim kind {kind!r}")


def report(label, fn):
    try:
        result = fn()
    except Reject as e:
        print(f"REJECT {label}: {e}")
        return False
    print(f"PASS   {label}")
    for k, v in result.items():
        print(f"       {k}: {v}")
    return True


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    for name in CHECKS:
        sub.add_parser(name).add_argument("claim")
    sm = sub.add_parser("smalln")
    sm.add_argument("--limit", type=int, default=2_000_001)
    al = sub.add_parser("all")
    al.add_argument("--limit", type=int, default=2_000_001)
    args = ap.parse_args(argv)

    if args.cmd == "smalln":
        ok = report("smalln", lambda: check_smalln(args.limit))
    elif args.cmd == "all":
        ok = True
        for path in sorted((ROOT / "candidates").glob("*.json")):
            ok &= report(str(path.relative_to(ROOT)), lambda p=path: run_claim(p))
        ok &= report("smalln", lambda: check_smalln(args.limit))
    else:
        claim = json.loads(Path(args.claim).read_text())
        ok = report(args.claim, lambda: CHECKS[args.cmd](claim))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
