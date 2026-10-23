"""Exact recomputation and direct small-prime checks for PROOF.md (stdlib only)."""

import math
import sys
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "verify"))
from check import ln_bounds  # noqa: E402
from mr import is_prime_trial  # noqa: E402

PRIME_C = F(339, 500)  # 0.678
GENERAL_C = F(683, 1000)
Q0 = 65536
SMALLER_THETA = F(8748867, 10000000)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def analytic_certificate(c=PRIME_C, y_min=7, c2=F(189, 125)):
    # b and c2 are the accepted pairing/zeta inputs, not new L-function estimates.
    b, y, d, factor = F(231, 10000), F(y_min), F(39, 50), F(1001, 1000)
    require(c > 0, "positive coefficient")
    require(c2 > 0 and 7 * c2 ** 2 >= 16, "pairing constant must dominate 4/sqrt(7)")
    require(y ** 8 >= 256, "paired zero-sum range")
    require(ln_bounds(y_min)[0] > 1 and ln_bounds(y_min)[1] < 2, "log endpoint")
    require(1 - c2 * (1 / y + 1 / y ** 4) > d, "d(X) > 39/50")
    require(1 + 7 / y ** 6 + 8 / y ** 7 < factor, "F(X)/X envelope")
    require(ln_bounds(2)[0] > F(2, 3), "log 2 > 2/3")
    require(c * 16 * F(2, 3) > y, "analytic cutoff reaches y_min")
    t = F(16)  # 8 log y_min < 16
    residual = ((y / (2 * c * d) + y / (2 * c) + 2) * t
                + 1 + (2 * y / c) * t ** 2) / y ** 8
    total = factor * (b / y + 1 / (2 * c * d)) + residual
    require(total < 1, "positive analytic margin")
    return total


def small_range_certificate(prime_c=PRIME_C, general_c=GENERAL_C):
    require(prime_c <= general_c, "general coefficient dominates prime coefficient")
    require((prime_c * ln_bounds(7)[0]) ** 8 > 7, "small-range lower endpoint")
    require(prime_c * 16 * ln_bounds(2)[0] > 7 and 7 ** 8 > Q0,
            "small-range upper endpoint")
    # (C log q)^8/q has a single interior maximum, so the endpoints suffice.
    require((prime_c * ln_bounds(5)[0]) ** 8 > 2, "q=5 endpoint")
    require((general_c * ln_bounds(6)[0]) ** 8 > 5, "q=6 endpoint")
    require({pow(2, k, 5) for k in range(4)} == {1, 2, 3, 4}, "generator mod 5")
    require({pow(5, k, 6) for k in range(2)} == {1, 5}, "generator mod 6")
    require((F(677, 1000) * ln_bounds(5)[1]) ** 8 < 2,
            "prime coefficient 0.677 is impossible")
    require((F(341, 500) * ln_bounds(6)[1]) ** 8 < 5,
            "general coefficient 0.682 is impossible")


def least_quadratic_nonresidue(q):
    require(q >= 5 and is_prime_trial(q), "modulus must be prime and at least 5")
    for a in range(2, q):
        if pow(a, (q - 1) // 2, q) == q - 1:
            require(is_prime_trial(a), "least nonresidue must itself be prime")
            return a
    raise ValueError("no quadratic nonresidue found")


def theta_certificate(theta=SMALLER_THETA):
    k = 1 / (1 - theta)
    require(F(799, 100) < k < 8, "refined exponent interval")
    require(theta - F(1, 2) > F(11, 30), "paired main-zero range")
    require(256 ** 11 > 7 ** 30, "integer pairing range comparison")
    require(theta * (1 - theta) >= F(7, 64), "same positive pairing coefficient")
    y, d, factor, t = F(7), F(77, 100), F(1001, 1000), F(16)
    require(1 - F(189, 125) * (1 / y + 1 / y ** 3) > d, "refined d envelope")
    require(1 + 7 / y ** 5 + 8 / y ** 6 < factor, "refined F envelope")
    error = (factor * (F(231, 10000) / y + 1 / (2 * PRIME_C * d))
             + ((y / (2 * PRIME_C * d) + y / (2 * PRIME_C) + 2) * t
                + 1 + (2 * y / PRIME_C) * t ** 2) / y ** 7)
    require(error < 1, "smaller-theta analytic margin")
    for q, c, p in [(5, PRIME_C, 2), (6, GENERAL_C, 5), (7, PRIME_C, 7)]:
        lo = ln_bounds(q)[0]
        short = F((lo.numerator * 10 ** 8) // lo.denominator, 10 ** 8)
        base = c * short
        require(base > 1 and base ** 799 > p ** 100, f"refined q={q} endpoint")
    require(7 ** 7 > Q0, "refined upper interval endpoint")
    for q, c in [(5, F(677, 1000)), (6, F(341, 500))]:
        require(c * ln_bounds(q)[0] > 1, "old obstructions transfer to k<8")
    return k, error


def direct_prime_checks():
    count, largest = 0, (0, 0)
    for q in range(5, Q0, 2):
        if is_prime_trial(q):
            ell = least_quadratic_nonresidue(q)
            lo = ln_bounds(q)[0]
            require(ell < (PRIME_C * lo) ** 8,
                    f"quadratic bound fails at q={q}, ell={ell}")
            if q == 5:
                short = F((lo.numerator * 10 ** 8) // lo.denominator, 10 ** 8)
                require((PRIME_C * short) ** 799 > ell ** 100, "refined q=5 direct check")
            else:
                require(ell < (PRIME_C * lo) ** 7, f"refined direct bound fails at q={q}")
            count += 1
            largest = max(largest, (ell, q))
    return count, largest


def failure_controls():
    require(least_quadratic_nonresidue(5) == 2, "q=5 positive control")
    require(least_quadratic_nonresidue(7) == 3, "q=7 positive control")
    for label, check in [
        ("insufficient pairing constant", lambda: analytic_certificate(c2=F(3, 2))),
        ("negative pairing constant", lambda: analytic_certificate(c2=-F(189, 125))),
        ("insufficient y cutoff", lambda: analytic_certificate(y_min=6)),
        ("false prime coefficient", lambda: small_range_certificate(prime_c=F(677, 1000))),
        ("false general coefficient", lambda: small_range_certificate(general_c=F(341, 500))),
        ("composite Legendre modulus", lambda: least_quadratic_nonresidue(9)),
        ("uncovered weaker zero-free line", lambda: theta_certificate(F(9, 10))),
    ]:
        try:
            check()
        except ValueError:
            print(f"REJECT control: {label}")
        else:
            raise ValueError(f"bad control accepted: {label}")


def main():
    error = analytic_certificate()
    require(analytic_certificate(c=GENERAL_C) < 1, "general analytic certificate")
    small_range_certificate()
    k, theta_error = theta_certificate()
    count, (ell, q) = direct_prime_checks()
    failure_controls()
    print(f"analytic normalized error: {error} < 1")
    print(f"analytic normalized margin: {1-error}")
    print(f"general coefficient: {GENERAL_C}; prime coefficient: {PRIME_C}")
    print(f"smaller theta: {SMALLER_THETA}; exact exponent: {k}")
    print(f"smaller-theta error: {theta_error}; margin: {1-theta_error}")
    print(f"direct check: {count} primes q with 5 <= q < {Q0}")
    print(f"largest least quadratic nonresidue in direct range: {ell} (last at q={q})")
    print("all constants and direct checks pass")


if __name__ == "__main__":
    main()
