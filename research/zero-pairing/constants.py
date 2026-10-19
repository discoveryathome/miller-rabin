"""Recompute the Lemma T1 constants in research/zero-pairing/PROOF.md (exact rationals),
check the claim file against them, and brute-force the two pairing ratios as a sanity check.
Run: python3 research/zero-pairing/constants.py"""

import json
import math
import sys
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "verify"))
import check  # noqa: E402

beta = F(7, 8)
K = 1 / (1 - beta)                      # 8
y_min = 29
c2 = F(189, 125)                        # >= 4/sqrt(7) = 1/(2 sqrt(beta(1-beta)))
B_abs = F(231, 10000)                   # |B| for zeta = 0.0230957...
ln2pi = F(18379, 10000)                 # > log(2 pi)
EG = 0.5772156649015329
assert c2 ** 2 * 7 >= 16
assert B_abs > abs(0.5 * math.log(4 * math.pi) - 1 - EG / 2)
assert ln2pi > math.log(2 * math.pi)

X0 = F(y_min) ** 8
assert X0 >= 256 and X0 > math.exp(1 / float(beta))  # Lemma 0' range; log X / X^beta decreasing
_, ln_ymin_hi = check.ln_bounds(y_min)
a1 = K * ln_ymin_hi / F(y_min) ** 7     # >= log X / X^beta for X >= X0
s6 = F(1, y_min ** 6)                   # >= X^(1-2 beta) = X^(-3/4)
D_min = 1 - c2 * (F(1, y_min) + F(1, y_min ** 4))   # <= 1 + 1/X - c(X)
assert D_min > 0
b1 = 1 / (2 * D_min)                    # |Re B(chi~)| <= b1 L
Fmax = 1 + (K - 1) * s6 + a1            # (X^b + 7 X^(1-b) + log X) / X^b, K X^-b term kept separate

need = {
    "alpha": b1 * Fmax + a1 / 2,
    "beta": B_abs * (1 + (K - 1) * s6) + ln2pi * a1,
    "gamma": K * b1,
}
# delta: K|B| + 1 + Et_a(X) <= 0, using Et_a(X) <= max(Et0, Et1) bound at x = 64 below.
L64 = math.log(64)
Et_bound = max(math.pi ** 2 / 24 - 0.5 * L64 ** 2, math.pi ** 2 / 8 - (math.log(2) + EG / 2) * L64)
assert float(K * B_abs) + 1 + Et_bound < -1, "delta = 0 needs K|B| + 1 + Et_a <= 0"

claim = json.loads((ROOT / "candidates/explicit-t1-zero-pairing-7-8.json").read_text())
t = claim["template"]
assert F(claim["theta"]) == beta and F(t["y_min"]) == y_min and F(t["w1"]) == 1 and F(t["delta"]) == 0
for k in need:
    assert F(t[k]) >= need[k], k
    print(f"{k:6s} needed {float(need[k]):.12g}  claimed {t[k]}  ok")
print(f"delta  needed <= 0 (K|B| + 1 + Et_a <= {float(K * B_abs) + 1 + Et_bound:.3f})  claimed 0  ok")

# Sanity check only: brute-force the pair ratios of Lemma 0' over sigma in (1/2, 7/8], t >= 0.
b = float(beta)
for x in (256.0, 1e6, float(X0)):
    wa = wb = 0.0
    for i in range(1, 200):
        s = 0.5 + (b - 0.5) * i / 199
        for j in range(1200):
            tt = 10 ** (-4 + 8 * j / 1199) if j else 0.0
            A, Bq = 1 / (s * s + tt * tt), 1 / ((1 - s) ** 2 + tt * tt)
            den = s * A + (1 - s) * Bq
            wa = max(wa, (x ** s * A + x ** (1 - s) * Bq) / den / (x ** b + 7 * x ** (1 - b)))
            wb = max(wb, (x ** (s - 1) + x ** -s) * math.sqrt(A * Bq) / den / (float(c2) * (x ** (b - 1) + x ** -0.5)))
    assert wa <= 1 + 1e-12 and wb <= 1, (x, wa, wb)
    print(f"x = {x:.3g}: sampled sup / claimed bound: (a) {wa:.6f}, (b) {wb:.6f}")
print("all constants check out")
