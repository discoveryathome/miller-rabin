"""Recompute the Lemma T1 constants in PROOF.md (exact rationals) and sanity-check the
sign facts it uses. Run: python3 research/first-explicit-t1/constants.py"""

import math
import sys
from fractions import Fraction as F
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "verify"))
import check  # noqa: E402

beta = F(7, 8)
K = 1 / (1 - beta)                      # 8
y_min = F(200)
B_abs = F(231, 10000)                   # |B| = |1/2 log 4pi - 1 - gamma/2| = 0.0230957...
ln2pi = F(18379, 10000)                 # > log(2 pi) = 1.8378770...
assert B_abs > abs(0.5 * math.log(4 * math.pi) - 1 - 0.5772156649015329 / 2)
assert ln2pi > math.log(2 * math.pi)

_, ln200_hi = check.ln_bounds(200)
a1 = K * ln200_hi / y_min ** 7          # log X / X^beta at X = y_min^K (= 200^8)
assert 200 ** 8 > math.exp(1 / float(beta))  # log X / X^beta decreasing beyond e^(1/beta)
fac = 1 / (1 - K / y_min)               # 25/24

need = {
    "alpha": F(1, 2) * ((K + a1) * fac + a1),
    "beta": K * B_abs + ln2pi * a1,
    "gamma": F(1, 2) * K * fac,
    "delta": K * B_abs + 1,
}
claimed = {"alpha": F(25, 6) + F(1, 10**12), "beta": F(37, 200), "gamma": F(25, 6), "delta": F(237, 200)}
for k in need:
    assert claimed[k] >= need[k], k
    print(f"{k:6s} needed {float(need[k]):.15g}  claimed {claimed[k]}  ok")


EG = 0.5772156649015329

# Analytic sign bounds for all x >= 64 (PROOF.md, Step 0): drop the nonpositive series,
# use monotonicity, evaluate at x = 64. Each must be < 0.
L64 = math.log(64)
for name, val in (
    ("Et0", math.pi**2 / 24 - 0.5 * L64**2),
    ("Et1", math.pi**2 / 8 - (math.log(2) + EG / 2) * L64),
    ("E0", -math.log(2) - EG / 2 * (63 / 64) + (L64 + 1) / 64),
    ("E1", -EG / 2 * (63 / 64) + math.log(2) / 64),
):
    assert val < -0.2, name
    print(f"{name:4s} analytic bound for x >= 64: {val:.4f} (< 0)")

# Numerical sampling of the exact functions: a sanity check only.


def E0(x):
    return -math.log(2) - EG / 2 * (1 - 1 / x) + (math.log(x) + 1) / x - sum(x ** (-2 * k - 1) / (2 * k * (2 * k + 1)) for k in range(1, 50))


def E1(x):
    return -sum(x ** (-2 * k - 2) / ((2 * k + 1) * (2 * k + 2)) for k in range(50)) - EG / 2 * (1 - 1 / x) + math.log(2) / x


def Et0(x):
    return math.pi**2 / 24 - EG / 2 * math.log(x) - 0.5 * math.log(x) ** 2 - sum(x ** (-2 * k) / (2 * k) ** 2 for k in range(1, 50))


def Et1(x):
    return math.pi**2 / 8 - (math.log(2) + EG / 2) * math.log(x) - sum(x ** (-2 * k - 1) / (2 * k + 1) ** 2 for k in range(50))


xs = [64 * 1.01**i for i in range(5000)]
for f in (E0, E1, Et0, Et1):
    worst = max(f(x) for x in xs)
    assert worst < 0, f.__name__
    print(f"{f.__name__:4s} max over sampled x in [64, {xs[-1]:.3g}]: {worst:.4f} (< 0)")
print("all constants check out")
