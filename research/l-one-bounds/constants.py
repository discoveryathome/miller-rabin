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


def refined_certificate(l_min=15, additive=F(2)):
    """Certify the new pinned truncation x=((31/50)*log q)^8."""
    l, a, c2, bz = F(l_min), F(31, 50), F(189, 125), F(231, 10000)
    require(l > 0, "positive refined conductor threshold")
    y = a * l
    require(y > 2 and y ** 8 > 256, "refined kernel range")
    t_lo, t_hi = F(446, 25), F(17841, 1000)
    y_lo = ln_bounds(y.numerator)[0] - ln_bounds(y.denominator)[1]
    y_hi = ln_bounds(y.numerator)[1] - ln_bounds(y.denominator)[0]
    require(8 * y_lo > t_lo and 8 * y_hi < t_hi, "refined t endpoint enclosure")
    require(t_lo > F(19, 2), "refined b/L monotonicity")
    harmonic100 = sum((F(1, k) for k in range(1, 101)), F(0))
    require(harmonic100 - ln_bounds(101)[1] > F(57, 100), "gamma>0.57")
    require(F(3, 256) + c2 * (F(1, 2) + F(1, 16)) * bz < F(7, 100),
            "T_z(x)<log x-3/2 for x>=256")
    c = c2 * (1 / y + 1 / y ** 4)
    d, x = 1 - c, y ** 8
    require(d > 0, "refined positive denominator")
    b_over_l = (F(1, 2) + (t_hi - F(3, 2)) / l) / d
    k_bound = (b_over_l * l * c + 8 * b_over_l / (a * t_lo)
               + bz * c + 8 * bz / (y * t_lo)
               + (b_over_l * l + l / 2 + t_hi + 5) / x
               + 2 / (x * t_lo) + 1 / (3 * x ** 3 * t_lo)
               + 2 * t_hi / y ** 4)
    require(k_bound < F(603, 100), "refined K<603/100")
    k = F(503, 100)
    require(k / t_lo < 3, "exponential series tail range")
    bridge = k + k ** 2 / (2 * t_lo * (1 - k / (3 * t_lo)))
    require(bridge == F(5637121, 969800) < F(728, 125), "refined exponential bridge")
    log_inv_a_lo = ln_bounds(50)[0] - ln_bounds(31)[1]
    require(log_inv_a_lo > F(239, 500), "log(50/31)>239/500")
    require(bridge < additive + 8 * log_inv_a_lo, "refined additive envelope")
    return k_bound, F(603, 100) - k_bound, bridge


def parameter_certificate(beta=F(8748867, 10000000), l_min=20, additive=F(2)):
    """Uniform leading-r envelope for 13/15<=beta<=7/8 and log q>=20."""
    beta = F(beta)
    require(F(13, 15) <= beta <= F(7, 8), "parameter pairing strip range")
    r, l, a, c2, bz = 1/(1-beta), F(l_min), F(31, 50), F(189, 125), F(231, 10000)
    require(F(15, 2) <= r <= 8 and c2 > 0 and 7*c2*c2 >= 16,
            "parameter reciprocal and paired bounds")
    require(l > 0, "positive parameter conductor threshold")
    y = a*l
    require(y > 1 and y**7 > 256, "parameter kernel range")
    y_lo = ln_bounds(y.numerator)[0]-ln_bounds(y.denominator)[1]
    y_hi = ln_bounds(y.numerator)[1]-ln_bounds(y.denominator)[0]
    t_lo, t_hi = F(75, 4), F(81, 4)
    require(F(15, 2)*y_lo > t_lo and 8*y_hi < t_hi,
            "parameter t endpoint enclosure")
    require(t_lo > F(19, 2), "parameter uniform b/L monotonicity")
    harmonic100 = sum((F(1, k) for k in range(1, 101)), F(0))
    require(harmonic100-ln_bounds(101)[1] > F(57, 100) and
            F(3, 256)+c2*F(9, 16)*bz < F(7, 100),
            "parameter zeta constant saving")
    c, x_lower = c2*(1/y+1/y**3), y**7
    d = 1-c
    require(d > 0, "parameter positive denominator")
    b_over_l = (F(1, 2)+(t_hi-F(3, 2))/l)/d
    k_bound = (b_over_l*l*c+8*b_over_l/(a*t_lo)
               +bz*c+8*bz/(y*t_lo)
               +(b_over_l*l+l/2+t_hi+5)/x_lower
               +2/(x_lower*t_lo)+1/(3*x_lower**3*t_lo)
               +2*t_hi/y**3)
    require(k_bound < F(26, 5), "parameter common budget K<26/5")
    if l_min == 20:
        require(d == F(5226959, 5958200) and
                b_over_l == F(17129825, 10453918), "parameter D0 and B0 arithmetic")
    k = F(21, 5)
    require(0 < k/t_lo < 3, "parameter exponential series range")
    bridge = k+k*k/(2*t_lo*(1-k/(3*t_lo)))
    require(bridge == F(8169, 1735) < 5, "parameter exponential bridge")
    log_inv_a_lo = ln_bounds(50)[0]-ln_bounds(31)[1]
    require(log_inv_a_lo > F(239, 500), "parameter scale logarithm")
    require(bridge < additive+F(15, 2)*log_inv_a_lo,
            "parameter additive envelope")
    return k_bound, F(26, 5)-k_bound, bridge


def failure_controls():
    for label, check in [
        ("insufficient pairing constant", lambda: budget_certificate(c2=F(3, 2))),
        ("negative pairing constant", lambda: budget_certificate(c2=-F(189, 125))),
        ("too small refined conductor threshold", lambda: refined_certificate(l_min=14)),
        ("retained GRH denominator constant", lambda: shifted_denominator_certificate(F(2))),
        ("uncharged p=2 envelope", lambda: euler_certificate(F(1, 500))),
        ("overstated additive constant", lambda: refined_certificate(additive=F(1))),
        ("unsupported parameter strip", lambda: parameter_certificate(beta=F(9, 10))),
        ("too small parameter threshold", lambda: parameter_certificate(l_min=19)),
        ("overstated parameter additive constant", lambda: parameter_certificate(additive=F(1))),
    ]:
        try:
            check()
        except ValueError:
            print(f"REJECT control: {label}")
        else:
            raise ValueError(f"bad control accepted: {label}")


def main():
    total, margin = budget_certificate()
    refined, refined_margin, bridge = refined_certificate()
    parameter, parameter_margin, parameter_bridge = parameter_certificate()
    require(parameter_certificate(beta=F(13, 15)) ==
            parameter_certificate(beta=F(7, 8)) ==
            (parameter, parameter_margin, parameter_bridge),
            "closed parameter endpoint certificates")
    gap = euler_certificate()
    shifted_denominator_certificate()
    failure_controls()
    print(f"p=2 polynomial margin: {gap}")
    print(f"original log(q)>=32 budget: {total} < 8/3; margin {margin}")
    print(f"refined K upper bound: {refined} < 603/100")
    print(f"refined K margin: {refined_margin}")
    print(f"refined exponential bridge: {bridge} < 728/125")
    print("range: primitive conductor q with log(q)>=15; x=((31/50)*log q)^8")
    print(f"parameter K upper bound: {parameter} < 26/5; margin {parameter_margin}")
    print(f"parameter exponential bridge: {parameter_bridge} < 5")
    print("parameter range: 13/15<=beta<=7/8, log(q)>=20; leading r=1/(1-beta)")
    print("all constants and algebraic controls pass")


if __name__ == "__main__":
    main()
