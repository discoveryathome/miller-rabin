"""Exact checks for PROOF.md; Python standard library only.

Run from the repository root: python3 research/least-prime-progression/constants.py
No floating-point value participates in a certificate decision.
"""

import math
import sys
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "verify"))
from check import ln_bounds  # noqa: E402


def require(condition, message):
    if not condition:
        raise ValueError(message)


def ln_rational_bounds(x):
    nlo, nhi = ln_bounds(x.numerator)
    dlo, dhi = ln_bounds(x.denominator)
    return nlo - dhi, nhi - dlo


def arctan_bounds(x, terms=16):
    total = sum(((-1) ** k * x ** (2 * k + 1) / (2 * k + 1)
                 for k in range(terms)), F(0))
    following = (-1) ** terms * x ** (2 * terms + 1) / (2 * terms + 1)
    return min(total, total + following), max(total, total + following)


def elementary_constants():
    # Machin's identity and alternating-series bounds enclose pi.
    a0, a1 = arctan_bounds(F(1, 5))
    b0, b1 = arctan_bounds(F(1, 239))
    pi_lo, pi_hi = 16 * a0 - 4 * b1, 16 * a1 - 4 * b0
    require(3 < pi_lo < pi_hi < F(22, 7), "pi enclosure")

    # Trapezoid error for 1/x gives 0 < gamma - d_N < 1/(8 N^2),
    # where d_N = H_N - log N - 1/(2N); see PROOF.md, Appendix.
    n = 256
    harmonic = sum((F(1, k) for k in range(1, n + 1)), F(0))
    log_lo, log_hi = ln_bounds(n)
    gamma_lo = harmonic - log_hi - F(1, 2 * n)
    gamma_hi = harmonic - log_lo - F(1, 2 * n) + F(1, 8 * n * n)
    require(F(57, 100) < gamma_lo < gamma_hi < F(58, 100), "gamma enclosure")
    require(F(2, 3) < ln_bounds(2)[0] < ln_bounds(2)[1] < F(7, 10), "log 2")
    require(ln_bounds(3)[0] > 1, "log q > 1 for q >= 3")
    require(ln_rational_bounds(2 * pi_hi)[1] < 2, "log(2 pi) < 2")
    zeta_b_hi = 1 + gamma_hi / 2 - ln_rational_bounds(4 * pi_lo)[0] / 2
    require(0 < zeta_b_hi < F(231, 10000), "|B_zeta| < 231/10000")
    x = 64
    tail0 = F(1, x ** 3) / (1 - F(1, x ** 2))
    tail1 = F(1, x ** 2) / (1 - F(1, x ** 2))
    require(-F(2, 3) + (6 * F(7, 10) + 1) / x < 0, "E_0 sign")
    require(-F(57, 200) * F(x - 1, x) + F(7, 10) / x < 0, "E_1 sign")
    require(F(7, 10) + F(29, 100) + tail0 < 1, "|E_0| < 1")
    require(F(29, 100) + tail1 < 1, "|E_1| < 1")
    require(pi_hi ** 2 < 10, "pi^2 < 10 for Etilde bounds")
    return F(231, 10000)


def analytic_certificate(y_min=80, c2=F(189, 125)):
    """Certify the stated uniform envelope, rather than sample real inputs."""
    require(7 * c2 ** 2 >= 16, "c2 must dominate 4/sqrt(7)")
    b_zeta = elementary_constants()
    u = 2 ** 16
    complex_denominator = 1 - F(1, u) - c2 * (F(1, 4) + F(1, 256))
    require(complex_denominator > F(3, 5), "complex B absorption")
    require(ln_bounds(u)[1] < 12, "log u < 12")

    y = F(y_min)
    require(y >= 2 and ln_bounds(y_min)[0] > 1, "pairing and monotonicity range")
    log_hi = F(22, 5)
    require(ln_bounds(y_min)[1] < log_hi, "log y_min < 22/5")
    d_lo = 1 - c2 * (1 / y + 1 / y ** 4)
    require(d_lo > F(49, 50), "d(X) > 49/50")
    f_factor = F(1001, 1000)
    require(1 + 7 / y ** 6 + 8 / y ** 7 < f_factor, "F(X)/X envelope")
    zero_error = f_factor * (F(1, 2) + 8 * log_hi / y) / F(49, 50)
    zeta_error = b_zeta * f_factor / y
    power_error = 32 * log_hi ** 2 / y ** 3

    # Every summand is y^{-a} (8 log y)^b with a >= 6, b <= 2.
    # It decreases for y >= y_min, so this endpoint charges the full R/X.
    t_hi = 8 * log_hi
    residual_numerator = (2 * t_hi + 1 + y ** 2 * t_hi ** 2 / 2
                          + y * ((3 * y / 4 + 26) * t_hi + t_hi ** 2 / 2 + 3))
    residual_error = residual_numerator / y ** 8
    require(residual_error < F(1, 10 ** 8), "residual envelope")
    total = zero_error + zeta_error + power_error + F(1, 10 ** 8)
    require(total < 1, "positive margin over proper prime powers")
    require(9 * ln_bounds(2)[0] > 6, "log 512 > 6")
    require(16 * 6 > y_min, "phi(q) log q > y_min for q >= 512")
    return complex_denominator, total


def primes_up_to(limit):
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[:2] = b"\x00\x00"
    for p in range(2, math.isqrt(limit) + 1):
        if sieve[p]:
            sieve[p * p::p] = b"\x00" * ((limit - p * p) // p + 1)
    return [p for p in range(2, limit + 1) if sieve[p]]


def least_primes(q, primes):
    reduced = {a for a in range(1, q) if math.gcd(a, q) == 1}
    first = {}
    for p in primes:
        a = p % q
        if a in reduced and a not in first:
            first[a] = p
        if len(first) == len(reduced):
            return first
    raise ValueError(f"prime list does not cover every reduced class modulo {q}")


def finite_certificate(primes, moduli=range(3, 512), scale=F(1)):
    classes = 0
    largest = (0, 0, 0)
    for q in moduli:
        first = least_primes(q, primes)
        phi = len(first)
        bound_lo = (scale * phi * ln_bounds(q)[0]) ** 8
        for a, p in first.items():
            require(p < bound_lo, f"progression bound fails at q={q}, a={a}, p={p}")
            largest = max(largest, (p, q, a))
        classes += phi
    return classes, largest


def failure_controls():
    trial_primes = [n for n in range(2, 513)
                    if all(n % d for d in range(2, math.isqrt(n) + 1))]
    require(primes_up_to(512) == trial_primes, "sieve versus trial division")
    require(least_primes(3, trial_primes) == {2: 2, 1: 7}, "q=3 positive control")
    for label, check in [
        ("insufficient pairing constant", lambda: analytic_certificate(c2=F(3, 2))),
        ("too small analytic cutoff", lambda: analytic_certificate(y_min=64)),
        ("missing reduced class", lambda: least_primes(3, [2, 3, 5])),
        ("false progression coefficient", lambda: finite_certificate(trial_primes, [3], F(1, 2))),
    ]:
        try:
            check()
        except ValueError:
            print(f"REJECT control: {label}")
        else:
            raise ValueError(f"failure control was accepted: {label}")


def main():
    denominator, total = analytic_certificate()
    classes, (p, q, a) = finite_certificate(primes_up_to(65536))
    failure_controls()
    print(f"complex B denominator: {denominator} > 3/5")
    print(f"normalized total error bound: {total} < 1")
    print(f"positive normalized margin: {1 - total}")
    print(f"finite fallback: q=3..511, {classes} reduced classes checked exactly")
    print(f"largest least prime in fallback: p={p}, q={q}, a={a}")
    print("all constants and finite checks pass")


if __name__ == "__main__":
    main()
