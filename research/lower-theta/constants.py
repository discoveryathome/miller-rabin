"""Exact certificates for PROOF.md; Python standard library only.

Run from the repository root: python3 research/lower-theta/constants.py
Floating values appear only in the shared verifier's display-only report.
"""

import copy
import json
import sys
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "verify"))
import check  # noqa: E402

THETA = F(8748867, 10000000)
CLAIMS = (
    ("explicit-t1-lower-theta.json", THETA),
    ("explicit-t1-paired-refinement-7-8.json", F(7, 8)),
)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def log_bounds(value):
    """Directed logarithm enclosure for a positive rational."""
    value = F(value)
    require(value > 0, "positive logarithm argument")
    nlo, nhi = check.ln_bounds(value.numerator)
    dlo, dhi = check.ln_bounds(value.denominator)
    return nlo - dhi, nhi - dlo


def atan_bounds(value, terms):
    value = F(value)
    require(0 < value < 1 and terms > 0, "alternating arctangent range")
    total = sum(((-1)**j * value**(2*j+1) / (2*j+1)
                 for j in range(terms)), F(0))
    omitted = (-1)**terms * value**(2*terms+1) / (2*terms+1)
    return min(total, total + omitted), max(total, total + omitted)


def elementary_certificate():
    a_lo, a_hi = atan_bounds(F(1, 5), 16)
    b_lo, b_hi = atan_bounds(F(1, 239), 5)
    pi_lo, pi_hi = 16*a_lo - 4*b_hi, 16*a_hi - 4*b_lo
    require(F(31415926, 10**7) < pi_lo < pi_hi < F(31415927, 10**7),
            "Machin pi enclosure")
    n = 256
    harmonic = sum((F(1, j) for j in range(1, n+1)), F(0))
    logn_lo, logn_hi = log_bounds(n)
    gamma_lo = harmonic - logn_hi - F(1, 2*n)
    gamma_hi = harmonic - logn_lo - F(1, 2*n) + F(1, 8*n*n)
    require(gamma_lo > F(577, 1000), "Euler constant lower bound")
    bz_hi = 1 + gamma_hi/2 - log_bounds(4*pi_lo)[0]/2
    require(bz_hi < F(231, 10000), "zeta real-B upper bound")
    require(log_bounds(2*pi_hi)[1] < F(18379, 10000),
            "log(2pi) upper bound")
    log2_lo, log2_hi = log_bounds(2)
    log64_lo, log64_hi = log_bounds(64)
    require(F(693, 1000) < log2_lo < log2_hi < F(694, 1000),
            "log2 enclosure")
    require(F(4158, 1000) < log64_lo < log64_hi < F(416, 100),
            "log64 enclosure")
    require(pi_hi*pi_hi/24 < F(42, 100) and
            pi_hi*pi_hi/8 < F(124, 100), "pi-square upper bounds")
    e0 = -F(693, 1000) - F(577, 2000)*F(63, 64) + F(516, 100)/64
    e1 = -F(577, 2000)*F(63, 64) + F(694, 1000)/64
    et0 = F(42, 100) - F(4158, 1000)**2/2
    et1 = F(124, 100) - (F(693, 1000) + F(577, 2000))*F(4158, 1000)
    require(e0 == -F(22947, 25600) and e1 == -F(34963, 128000),
            "E arithmetic")
    require(et0 == -F(4112241, 500000) and
            et1 == -F(2841077, 1000000), "Et arithmetic")
    require(e0 < 0 and e1 < 0 and max(et0, et1) < -F(284, 100),
            "uniform E and Et signs")
    delta_hi = 8*F(231, 10000) + 1 - F(284, 100)
    require(delta_hi == -F(2069, 1250) < 0, "nonpositive static delta")
    return e0, e1, et0, et1, delta_hi


def coefficient_certificate(beta=THETA, c2=F(189, 125), half_power=3,
                            pair_power=5, log_power=6,
                            alpha=F(10551, 20000)):
    """Check the fixed proof's directed envelopes, not a numerical zero grid."""
    beta, c2, alpha = F(beta), F(c2), F(alpha)
    require(F(13, 15) <= beta <= F(7, 8), "fixed pairing strip range")
    k = 1/(1-beta)
    require(7 < k <= 8 and beta/(1-beta) <= 7, "pairing R and K")
    require(c2 > 0 and 7*c2*c2 >= 16, "positive pairing coefficient")
    require(beta-F(1, 2) >= F(11, 30) and 256**11 > 7**30,
            "pairing X>=256 endpoint condition")
    require(half_power <= k/2, "unsafe half-power envelope")
    require(pair_power <= k-2, "unsafe paired-power envelope")
    require(log_power <= k-1, "unsafe logarithmic-power envelope")
    require((half_power, pair_power, log_power) == (3, 5, 6),
            "this certificate uses powers 3,5,6")
    require(29**7 > 256, "T1 X range")
    ln29_lo, ln29_hi = log_bounds(29)
    require(ln29_hi < F(33673, 10000) and 6*ln29_lo > 1,
            "uniform decreasing logarithmic envelope")
    d_min = 1-c2*(F(1, 29)+F(1, 29**3))
    require(d_min > 0, "positive real-B denominator")
    b1, s = 1/(2*d_min), F(1, 29**5)
    a = 8*F(33673, 10000)/29**6
    need = {
        "alpha": b1*(1+7*s+a)+a/2,
        "beta": F(231, 10000)*(1+7*s)+F(18379, 10000)*a,
        "gamma": 8*b1,
    }
    require(alpha >= need["alpha"], "insufficient alpha coefficient")
    require(F(29, 1250) >= need["beta"], "insufficient beta coefficient")
    require(F(4221, 1000) >= need["gamma"], "insufficient gamma coefficient")
    if c2 == F(189, 125):
        require(d_min == F(2889487, 3048625), "Dmin arithmetic")
        require(need["alpha"] == F(566685633068042594, 1074208908328954375),
                "alpha arithmetic")
        require(need["beta"] == F(171755911431067, 7435291512500000),
                "beta arithmetic")
        require(need["gamma"] == F(12194500, 2889487), "gamma arithmetic")
    return need


def reject(label, callback, reason):
    try:
        callback()
    except (ValueError, check.Reject) as error:
        require(reason in str(error), f"wrong rejection for {label}: {error}")
        print(f"REJECT control: {label}: {error}")
    else:
        raise ValueError(f"control unexpectedly passed: {label}")


def main():
    elementary_certificate()
    for name, beta in CLAIMS:
        need = coefficient_certificate(beta)
        claim = json.loads((ROOT / "candidates" / name).read_text())
        require(F(claim["theta"]) == beta and F(claim["C"]) == F(66, 125)
                and F(claim["D"]) == 0 and claim["n0"] == check.mr.PSI_13,
                "claim domain and substitution")
        template = claim["template"]
        require(F(template["w1"]) == 1 and F(template["delta"]) == 0 and
                F(template["y_min"]) == 29, "claim template range")
        for key, value in need.items():
            require(F(template[key]) >= value, f"claim {key} coefficient")
        result = check.check_explicit(claim)
        l0 = log_bounds(check.mr.PSI_13)[0]
        y0 = F(66, 125)*l0
        g0 = F(9, 20000)*l0-F(29, 1250)-F(4221, 1000)*l0/y0**6
        require(y0 > F(29811, 1000) > 29 and g0 > F(2207, 10**6),
                "uniform endpoint lower bounds")
        print(f"PASS {name}: theta={beta}, witness exponent={1/(1-beta)}")
        print("  shared-verifier display:", result["g_at_n0_lower_bound"])
    print("needed coefficients:", {key: str(value) for key, value in need.items()})
    exponent = 2+1/(1-THETA)
    require(exponent == F(12502266, 1251133) and 10-exponent == F(9064, 1251133),
            "exact bit exponent")
    check.check_exponent({"theta": str(THETA), "claimed_exponent": str(exponent)})
    print("exact bit exponent:", exponent, "; gap below10:", 10-exponent)

    source = json.loads((ROOT / "candidates" / CLAIMS[0][0]).read_text())
    bad = copy.deepcopy(source)
    bad["C"] = "5279/10000"
    reject("C=.5279 endpoint", lambda: check.check_explicit(bad), "inequality not established")
    bad = copy.deepcopy(source)
    bad["C"] = "5275/10000"
    reject("C=.5275 slope", lambda: check.check_explicit(bad), "bound fails for large n")
    bad = copy.deepcopy(source)
    bad["template"]["y_min"] = "30"
    reject("y_min30", lambda: check.check_explicit(bad), "below y_min")
    reject("rounded-down bit exponent", lambda: check.check_exponent(
        {"theta": str(THETA), "claimed_exponent": "9.9927"}), "rounding down")
    reject("alpha=.52753", lambda: coefficient_certificate(alpha=F(52753, 100000)),
           "insufficient alpha")
    reject("c2=3/2", lambda: coefficient_certificate(c2=F(3, 2)),
           "positive pairing coefficient")
    reject("negative c2", lambda: coefficient_certificate(c2=-F(189, 125)),
           "positive pairing coefficient")
    reject("copied half-power4", lambda: coefficient_certificate(half_power=4),
           "unsafe half-power")
    reject("copied paired-power6", lambda: coefficient_certificate(pair_power=6),
           "unsafe paired-power")
    reject("copied logarithmic-power7", lambda: coefficient_certificate(log_power=7),
           "unsafe logarithmic-power")
    k = 1/(1-THETA)
    require(k*(1+(8-k)*log_bounds(29)[0]) > 8,
            "old logarithmic cap must underestimate the true value")
    print("old logarithmic cap disproved by a rational exponential lower bound")
    print("all constants, both claims and ten rejection controls pass")


if __name__ == "__main__":
    main()
