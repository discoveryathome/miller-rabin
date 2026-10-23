"""Exact arithmetic for PROOF.md; no floating-point certificate decisions."""

import sys
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "verify"))
from check import ln_bounds  # noqa: E402


def require(condition, message):
    if not condition:
        raise ValueError(message)


def elementary_constants():
    l2, u2 = ln_bounds(2)
    require(F(27, 40) < l2 < u2 < F(7, 10), "log 2 enclosure")
    harmonic6 = sum((F(1, k) for k in range(1, 7)), F(0))
    require(harmonic6 - ln_bounds(7)[1] > F(1, 2), "gamma lower bound")
    # gamma < H_1=1 and 3<pi<4 are elementary inputs proved/described in PROOF.
    require(ln_bounds(12)[0] > 2, "log(4 pi)>2 from pi>3")
    require(ln_bounds(4)[1] < 2, "log pi<2 from pi<4")
    require(ln_bounds(8)[1] < 3, "log(2 pi)<3 from pi<4")
    require(ln_bounds(100)[0] > F(9, 2) and ln_bounds(100)[1] < 5,
            "log 100 enclosure")
    require(u2 < F(3, 4) and ln_bounds(6)[1] < 6, "Chebyshev induction inputs")
    require(-F(1, 2) + F(6, 100) < 0, "E_0 sign")
    require(-F(1, 4) * F(99, 100) + F(1, 100) < 0, "E_1 sign")


def euler_certificate(h_hi=F(7, 4500)):
    # Coefficients of Q_k(z)=(1-cos(k phi))/(1-cos phi), z=cos(phi).
    q = [[1], [2, 2], [1, 4, 4], [0, 0, 8, 8], [1, -4, -4, 16, 16]]
    even_tail = 2 * F(1, 4) ** 3 * (3 - 2 * F(1, 4)) / (1 - F(1, 4)) ** 2
    require(even_tail == F(5, 36), "p=2 even tail")
    p, h = [], []
    for j in range(5):
        p.append(sum((F((-1) ** (k - 1), k * 2 ** k) * (q[k - 1][j] if j < len(q[k - 1]) else 0)
                      for k in range(1, 6)), F(0)) - (even_tail if j == 0 else 0))
        h.append(sum(((-1) ** k * (q[k - 1][j] if j < len(q[k - 1]) else 0)
                      for k in range(1, 6)), 0))
    require(p == [F(229, 1440), -F(13, 120), F(1, 60), -F(1, 40), F(1, 10)],
            "p=2 P polynomial coefficients")
    require(h == [-1, 2, 8, -8, -16], "p=2 H polynomial coefficients")
    cubic = [14, 16, 24, 16]
    product = [cubic[0]] + [cubic[j] - cubic[j - 1] for j in range(1, 4)] + [-cubic[-1]]
    require(product == [h[0] + 15] + h[1:], "H+15 factorization")
    require(sum(cubic[j] * (-1) ** j for j in range(4)) == 6, "cubic minimum")
    require([cubic[1], 2 * cubic[2], 3 * cubic[3]] == [16, 48, 48],
            "cubic derivative 48(z+1/2)^2+4")
    require(F(229, 1440) - F(13, 120) - F(1, 40) == F(37, 1440), "P lower bound")
    gap = F(37, 1440) - 15 * h_hi
    require(gap > 0, "positive p=2 minimum envelope")
    r = F(1, 3)
    require(1 - 2 * r / (1 - r ** 2) ** 2 == F(5, 32), "p>=3 Euler envelope")
    require(F(10, 9) + F(8, 9) == 2, "lower Euler tail")
    return gap


def shifted_denominator_certificate(multiplier=F(8)):
    pair = [F(1, 8), F(7, 8)]
    b = sum(1 / rho for rho in pair)
    shifted = sum(1 / (1 - rho) ** 2 for rho in pair)
    require(shifted / b == F(50, 7), "reflected formal-pair ratio")
    require(shifted <= multiplier * b, "off-line reciprocal-square envelope")
    # GRH positive control: a formal central-line zero has ratio exactly 2.
    rho = F(1, 2)
    require((1 / (1 - rho) ** 2) / (1 / rho) == 2, "GRH kernel positive control")


def budget_certificate(l_min=32, c2=F(189, 125), additive=F(2)):
    require(c2 > 0 and 7 * c2 ** 2 >= 16, "pairing constant must dominate 4/sqrt(7)")
    elementary_constants()
    require(l_min >= 2 and ln_bounds(l_min)[0] > 1, "monotonicity range")
    require(8 * ln_bounds(l_min)[0] > 27, "t>27 at conductor threshold")
    require(8 * ln_bounds(l_min)[1] / l_min < F(7, 8), "t/L<7/8")
    l = F(l_min)
    c_l = c2 * (1 + 1 / l ** 3)
    require(c_l < F(303, 200), "paired c(x)L envelope")
    require(c2 * (1 / l + 1 / l ** 4) < F(6, 125), "paired c(x) envelope")
    d = F(119, 125)
    require(1 - c2 * (1 / l + 1 / l ** 4) > d, "positive real-B denominator")
    require((F(1, 2) + F(7, 8)) / d == F(1375, 952) < F(29, 20), "b/L envelope")
    require(F(29, 20) + F(1, 2) + F(7, 8) + 5 / l < 3, "small residual numerator")
    main = F(29, 20) * F(303, 200) + F(58, 135) + F(3, 125) + F(1, 216)
    require(main == F(286741, 108000), "main error sum")
    require(F(27, 4) / l ** 3 < F(1, 1000), "small error tail")
    total = main + F(1, 1000)
    require(total < F(8, 3), "common error budget K<8/3")
    bridge = F(5, 3) / (1 - F(5, 81))
    require(bridge == F(135, 76) < additive, "exponential additive envelope")
    return total, F(8, 3) - total


def failure_controls():
    for label, check in [
        ("insufficient pairing constant", lambda: budget_certificate(c2=F(3, 2))),
        ("negative pairing constant", lambda: budget_certificate(c2=-F(189, 125))),
        ("too small conductor threshold", lambda: budget_certificate(l_min=16)),
        ("retained GRH denominator constant", lambda: shifted_denominator_certificate(F(2))),
        ("uncharged p=2 envelope", lambda: euler_certificate(F(1, 500))),
        ("overstated additive constant", lambda: budget_certificate(additive=F(1))),
    ]:
        try:
            check()
        except ValueError:
            print(f"REJECT control: {label}")
        else:
            raise ValueError(f"bad control accepted: {label}")


def main():
    total, margin = budget_certificate()
    gap = euler_certificate()
    shifted_denominator_certificate()
    failure_controls()
    print(f"p=2 polynomial margin: {gap}")
    print(f"common error budget upper bound: {total} < 8/3")
    print(f"margin to 8/3: {margin}")
    print("exponential bridge: 135/76 < 2")
    print("range: primitive conductor q with log(q)>=32; x=(log q)^8")
    print("all constants and algebraic controls pass")


if __name__ == "__main__":
    main()
