# Lemma T1 under H(7/8) with explicit constants

**Status: draft, awaiting review.** Written by an AI agent (Claude), unreviewed. It is
not accepted until the maintainer has reviewed it and, per DISCOVERY.md, one independent
check of the constants has been done. Licensed CC BY 4.0. Original idea: Geoffrey Irving.

**Claim file:** [`candidates/explicit-t1-first-7-8.json`](../../candidates/explicit-t1-first-7-8.json).
`python3 verify/check.py explicit` on it prints PASS.

## Result

> **Theorem.** Assume H(7/8). Every odd composite n ≥ ψ₁₃ = 3317044064679887385961981 has
> a prime Miller–Rabin witness p ≤ (4.2·ln n)^8. Every odd composite n < ψ₁₃ has one
> among the primes ≤ 41 (Sorenson–Webster).

The deterministic test is: try every prime p ≤ max(41, (4.2 ln n)^8). Its cost is
(log n)^(10+o(1)) bit operations. At n ≈ 2^1024, W(n) ≈ 10^27.8.

The theorem follows from Lemma T1 (below) and `verify/check.py explicit`. The checker
shows that x = (4.2 ln n)^8 satisfies the inequality of Lemma T1 for every n ≥ ψ₁₃.

## Notation and inputs

- **The half-plane.** Write β = 7/8 for the half-plane parameter. (This note uses θ, as
  in Lamzouri–Li–Soundararajan [LLS], for "some complex number of modulus ≤ 1".) Set
  K = 1/(1−β) = 8.
- **Standing hypothesis H(β):** no Dirichlet L-function, for any modulus, has a zero
  with Re s > β. The pole at s = 1 does not count as a zero.
- **Reference.** [LLS] = Y. Lamzouri, X. Li, K. Soundararajan, *Conditional bounds for
  the least quadratic non-residue and related problems*, Math. Comp. 84 (2015);
  arXiv:1309.3595v3. Lemma numbers below are theirs. Their arguments refine Bach (1990).
- **Unconditional facts.**
  - (F1) For a primitive χ mod q ≥ 3, the zeros of ξ(s, χ) are the non-trivial zeros
    of L(s, χ). They lie in 0 < Re s < 1, and Re B(χ) = −Σ_ρ Re(1/ρ) ([LLS] (2.4);
    Davenport ch. 12). For ζ, B = −Σ_ρ Re(1/ρ) = ½ log 4π − 1 − γ/2 = −0.02309…;
    we use |B| ≤ 0.0231.
  - (F2) The functional equation ξ(s, χ) = ε_χ ξ(1−s, χ̄), together with
    L(s̄, χ̄) = conj L(s, χ), shows that the multiset {1−ρ} equals the multiset {ρ̄'}
    of conjugate zeros. Hence Σ_ρ 1/|1−ρ|² = Σ_ρ 1/|ρ|².

## Step 0: what H(β) gives in place of GRH

**Lemma 0.** Assume H(β). Let χ be primitive mod q ≥ 3, or let χ give ζ, with ρ
running over the non-trivial zeros. Then:

1. 1−β ≤ Re ρ ≤ β;
2. Σ_ρ 1/|ρ|² ≤ K·|Re B(χ)| (for ζ, ≤ K|B|);
3. Σ_ρ 1/(|ρ||ρ−1|) ≤ K·|Re B(χ)|.

*Proof.*
1. Re ρ ≤ β is H(β). By (F2), 1−ρ is the conjugate of another zero of the same χ, so
   Re(1−ρ) ≤ β too.
2. Re(1/ρ) = Re ρ/|ρ|² ≥ (1−β)/|ρ|². Sum this and use (F1); every term is
   non-negative, so Re B(χ) ≤ 0.
3. By AM–GM, 1/(|ρ||1−ρ|) ≤ ½(1/|ρ|² + 1/|1−ρ|²). Then use (F2) and part 2. ∎

Under GRH (β = 1/2) these become the identities [LLS] uses, with K = 2 and equality in
part 2. [LLS] Lemmas 2.1–2.3 use GRH or RH in exactly three places (see
`research/bach-transfer/NOTE.md`):

- |x^ρ| = √x;
- Σ 1/|ρ|² = 2|Re B|;
- |ρ−1| = |ρ|, in Lemma 2.3.

Lemma 0 replaces all three. The residue expansions come from shifting the contour to
Re s → −∞. That shift is unconditional:
- the kernels x^s/s² and x^(s−1)/(s(s−1)) decay like |s|^(−2);
- the bounds on ξ′/ξ along suitable horizontal and left-hand paths (Davenport,
  *Multiplicative Number Theory*, chs. 17 and 19) make the connecting integrals vanish.

These are [LLS]'s own proofs of Lemmas 2.1–2.3. Replacing the three uses:

- **(L2.1′)** For x > 1:
  Σ_{m≤x} Λ(m) log(x/m) = x − log(2π)·log x − 1 + Σ_{k≥1} (1−x^(−2k))/(4k²)
  + θ·K|B|(x^β + 1).
  (In [LLS], 2|B|(√x + 1) bounds |Σ_ρ x^ρ/ρ²| + |Σ_ρ 1/ρ²|. Lemma 0 bounds the same two
  sums by K|B|·x^β and K|B|.)
- **(L2.2′)** For primitive χ mod q ≥ 3 and x > 1:
  Re S(x, χ) ≤ |Re B(χ)|·(K x^β + K + log x) + ½ log(q/π)·log x + Ẽ_a(x),
  where S(x, χ) = Σ_{m≤x} Λ(m) χ(m) log(x/m).
- **(L2.3′)** For primitive χ mod q ≥ 3 and x > 1 with K x^(β−1) < 1:
  |Re B(χ)|·(1 + 1/x − K x^(β−1)) ≤ ½(1−1/x) log(q/π) − Re Σ_{m≤x} (Λ(m)/m) χ(m)(1 − m/x) + E_a(x).
  (In [LLS], the zero sum Σ_ρ x^(ρ−1)/(ρ(ρ−1)) is bounded by (2/√x)|Re B|. Lemma 0
  parts 1 and 3 bound it by K x^(β−1)|Re B|. Taking real parts, the left side is
  |Re B| + |Re B|/x + (that sum), since Re B(χ̄) = Re B(χ) ≤ 0.)

The functions E_a and Ẽ_a (a = 0, 1) are the explicit, hypothesis-free functions in
[LLS] Lemmas 2.2–2.3, with γ Euler's constant:

- Ẽ₀(x) = π²/24 − (γ/2) log x − ½(log x)² − Σ_{k≥1} x^(−2k)/(2k)²;
- Ẽ₁(x) = π²/8 − (log 2 + γ/2) log x − Σ_{k≥0} x^(−2k−1)/(2k+1)²;
- E₀(x) = −log 2 − (γ/2)(1 − 1/x) + (log x + 1)/x − Σ_{k≥1} x^(−2k−1)/(2k(2k+1));
- E₁(x) = −Σ_{k≥0} x^(−2k−2)/((2k+1)(2k+2)) − (γ/2)(1 − 1/x) + (log 2)/x.

We use only **E_a(x), Ẽ_a(x) < 0 for x ≥ 64**. In each formula,
every series term enters with a minus sign, so dropping the series gives an upper bound.
Also (1 − 1/x) is increasing, and (ln x + 1)/x and (ln 2)/x are decreasing. So for
x ≥ 64:

- Ẽ₀(x) ≤ π²/24 − ½(ln 64)² < 0.42 − 8.6 < 0;
- Ẽ₁(x) ≤ π²/8 − (ln 2 + γ/2)·ln 64 < 1.24 − 4.08 < 0;
- E₀(x) ≤ −ln 2 − (γ/2)(63/64) + (ln 64 + 1)/64 < −0.69 − 0.28 + 0.09 < 0;
- E₁(x) ≤ −(γ/2)(63/64) + (ln 2)/64 < −0.28 + 0.02 < 0.

[LLS] states sharper versions without proof: Ẽ_a ≤ −11/4 at its line "since
Ẽ_a(X) ≤ −11/4 for X ≥ 64", and E_a < −1/4 in §3.1. `constants.py` also samples all four
numerically, as a sanity check only.

## Lemma T1 (constants for β = 7/8)

> **Lemma T1.** Assume H(7/8). Let n be odd and composite, L = ln n, and X real with
> y := X^(1/8) ≥ 200. If
>
>   X − X^(7/8)·(αL + β₀) − (γL + δ) > 0,
>
> with α = 25/6 + 10⁻¹², β₀ = 37/200, γ = 25/6, δ = 237/200, then some prime p ≤ X is a
> Miller–Rabin witness for n.

(β₀ is the template's "beta". These are exactly the constants in the claim file, with
w1 = 1 and y_min = 200.)

*Proof.* Suppose no prime p ≤ X is a witness. We reach a contradiction.

**(a) Reduction to a character.** By Conrad, *The Miller–Rabin test*, proof of
Theorem 4.1 (Cases 1 and 2), the non-witnesses for n lie in a proper subgroup H of
G = (ℤ/nℤ)\*, and every base not coprime to n is a witness. So:
- no prime p ≤ X divides n;
- every prime p ≤ X lies in H, reduced mod n.

Since H is proper, some non-trivial character χ mod n is 1 on H. Then χ(p) = 1 for every
prime p ≤ X, so χ(m) = 1 for every m ≤ X (all such m are coprime to n).

Let χ̃ mod q̃ be the primitive character inducing χ. It is non-principal, so q̃ ≥ 3, and
q̃ | n gives log q̃ ≤ L. Every m ≤ X is coprime to n, so χ̃(m) = χ(m) = 1 for all m ≤ X.

**(b) Lower bound.** S(X, χ̃) = Σ_{m≤X} Λ(m) log(X/m). Apply (L2.1′) and drop the
non-negative k-sum:

  S(X, χ̃) ≥ X − K|B| X^β − K|B| − log(2π) log X − 1.        (1)

**(c) Bound on |Re B(χ̃)|.** In (L2.3′) with x = X: the sum
Σ (Λ(m)/m) χ̃(m)(1 − m/X) is non-negative, because χ̃(m) = 1. Also E_a(X) ≤ 0 since
X ≥ 200⁸ ≥ 64, and log(q̃/π) < log q̃ ≤ L. Finally,
1 + 1/X − K X^(β−1) ≥ 1 − K/y ≥ 1 − 8/200 = 24/25 > 0. So

  |Re B(χ̃)| ≤ (25/24)·½L.        (2)

(If the right side of (L2.3′) is negative, (L2.3′) contradicts |Re B| ≥ 0. Either way
(2) holds.)

**(d) Upper bound.** Apply (L2.2′) with Ẽ_a(X) ≤ 0, then (2):

  S(X, χ̃) ≤ (25/24)·½L·(K X^β + K + log X) + ½L·log X.        (3)

**(e) Absorbing log X.** Let X₀ = 200⁸. On X ≥ X₀, the function log X / X^β is
decreasing, since X₀ > e^(1/β). So log X ≤ a₁ X^β with
a₁ = 8·ln 200/200⁷ < 3.32·10⁻¹⁵. (`verify/check.py ln_bounds` gives the upper bound on
ln 200.)

**(f) Contradiction.** Subtract (3) from (1) and use (e) and K|B| ≤ 0.1848:

  0 ≥ X − X^β·[K|B| + log(2π)·a₁ + ½L·((K + a₁)·25/24 + a₁)] − [K|B| + 1 + ½L·K·25/24].

The bracketed coefficients are at most:
- αL + β₀, since ½((8 + a₁)·25/24 + a₁) = 25/6 + (49/48)a₁ ≤ 25/6 + 10⁻¹² and
  0.1848 + log(2π)·a₁ < 0.1848 + 6.1·10⁻¹⁵ ≤ 37/200;
- γL + δ, since ½·8·25/24 = 25/6 and 0.1848 + 1 ≤ 237/200.

So 0 ≥ X − X^(7/8)(αL + β₀) − (γL + δ). That contradicts the hypothesis. ∎

The constant arithmetic is reproduced in `research/first-explicit-t1/constants.py`
(exact rationals).

## What a reviewer should check

1. **(L2.1′)–(L2.3′).** In [LLS] Lemmas 2.1–2.3, the hypothesis is used *only* through
   the three uses listed in Step 0. Their explicit E_a, Ẽ_a, and the contour shifts, are
   unconditional.
2. **Lemma 0 part 3.** The AM–GM step and the multiset identity (F2).
3. **Step (a).** The reduction: the liar subgroup, and χ̃(m) = 1 for m ≤ X when no
   prime ≤ X divides n.
4. **Signs and the bounds on E_a and Ẽ_a for X ≥ 64.**
5. **The rational constants:** `constants.py`, and `verify/check.py` for the
   n ≥ n0 step.

## Review history

**2026-10-19, adversarial review by a separate AI agent (fresh context).** It is not an
independent human check.
- **No fatal problems.**
- **Fixed:**
  - the sign of E_a and Ẽ_a for all x ≥ 64 is now proved analytically, where before it
    was only sampled;
  - the contour-shift citation was added;
  - "two places" corrected to "three";
  - the log(2π)·a₁ figure corrected;
  - Lemma 0 part 1 simplified.
- **Suggested tightening, not applied:** use [LLS] Lemma 2.4, re-bounded under H(β), to
  lower γ and δ.

**2026-10-19, independent recheck by a separate AI agent** (fresh context, no access to the
earlier review). It is not a human check.
- **Verdict: confirmed.** No fatal or fixable issues.
- **Re-derived:**
  - all four Γ-factor residues, cross-checked against direct quadrature at x = 100 (to 20
    digits);
  - the ζ residue at 0, cross-checked with mpmath;
  - Lemma 0 and (F2);
  - (L2.1′)–(L2.3′);
  - step (a) against Conrad, including n a prime power and primes dividing n;
  - the step (c)–(f) algebra;
  - the soundness of `check_explicit`.
- **Taken on trust:**
  - convergence of the contour shifts;
  - Re B(χ) = −Σ Re(1/ρ);
  - minimality of ψ₁₃.
- **Minor, fixed:**
  - the summation variable is now m, so it no longer clashes with the composite n;
  - E_a and Ẽ_a are written out;
  - the contour-shift justification is stated.

## Where C = 4.2 comes from, and the obvious tightening

The leading behaviour is y ≈ ½K·L/(1 − K/y_min), so C → K/2 = 4 as y_min → ∞. Under
GRH, K/2 = 1, which recovers LLS's (log q)². Here y_min is capped near C·ln ψ₁₃ ≈ 237
because n0 ≤ ψ₁₃. That cap gives the factor 25/24 and the choice C = 4.2 over 4.17.
Three ways to tighten (card `optimize-weight`):
- larger pseudoprime tables;
- making the bound on y depend on n instead of using y_min;
- a smoother weight than log(x/n).

Quantitatively: for this exponent, going from C = 4.2 to C = 4 cuts the bound by a factor
of (4.2/4)⁸ ≈ 1.48.
