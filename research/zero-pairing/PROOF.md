# Lemma T1 under H(7/8) with C = 0.529: pairing zeros

**Status: draft, awaiting review.** Written by an AI agent (Claude), unreviewed. It builds
on the draft in [`research/first-explicit-t1/PROOF.md`](../first-explicit-t1/PROOF.md)
(PR #6), which is also unreviewed, and it is not accepted until the maintainer has
reviewed it and one independent check of the constants has been done. Licensed CC BY 4.0.
Original idea: Geoffrey Irving.

**Claim file:** [`candidates/explicit-t1-zero-pairing-7-8.json`](../../candidates/explicit-t1-zero-pairing-7-8.json).
`python3 verify/check.py explicit` on it prints PASS, and
`python3 research/zero-pairing/constants.py` recomputes every constant below.

## Result

> **Theorem.** Assume H(7/8). Every odd composite n ≥ ψ₁₃ = 3317044064679887385961981 has
> a prime Miller–Rabin witness p ≤ (0.529·ln n)^8. Every odd composite n < ψ₁₃ has one
> among the primes ≤ 41 (Sorenson–Webster).

| | First T1 (PR #6) | This note |
|---|---:|---:|
| W(n) | (4.2 ln n)^8 | (0.529 ln n)^8 |
| log₁₀ W(2^1024) | 27.795 | 20.597 |

The bound W(n) is smaller by (4.2/0.529)^8 ≈ 1.6·10⁷ at every n. The number of prime bases
tested falls by slightly less, since π(W) ≈ W/ln W.
The exponent is unchanged: only θ moves it.

## The idea

The first T1 bounded the main zero sum as

  |Σ_ρ x^ρ/ρ²| ≤ x^β · Σ_ρ 1/|ρ|² ≤ x^β · K·|Re B(χ)|,  K = 1/(1−β) = 8.

The two inequalities are worst at opposite ends. x^σ is largest at σ = β, while
1/|ρ|² is largest relative to Re(1/ρ) = σ/|ρ|² at σ = 1−β. Zeros come in pairs ρ, 1−ρ̄
with the same height, so they can't both be bad. Bounding each pair against its own share
of Σ Re(1/ρ) = |Re B(χ)| takes the factor from K = 8 to 1, up to lower-order terms. The
same pairing improves the zero sum in LLS Lemma 2.3, which sets the factor 1/(1 − K/y) in
the first T1, from K·x^(β−1) to about 1.51·x^(β−1).

**Sanity check.** Lemma 0′ below is stated for β = 7/8. The same proof, for general β ≥ ½,
gives the following bounds:
- (x^β + (β/(1−β))·x^(1−β))·|B|;
- (x^(β−1) + x^(−1/2))·|B| / (2√(β(1−β))).

At β = ½ (GRH) these reduce exactly to the bounds LLS use: 2√x·|Re B| and (2/√x)·|Re B|.

## Notation

As in the first T1:
- β = 7/8, K = 8, H(β), and [LLS] = Lamzouri–Li–Soundararajan, arXiv:1309.3595v3;
- facts (F1) and (F2);
- Lemma 0 (parts 1–3).

Here ρ runs over the non-trivial zeros, with multiplicity, of L(s, χ) for χ primitive mod
q ≥ 3, or of ζ. Write ρ = σ + it.

## Lemma 0′ (paired zero sums)

> **Lemma 0′.** Assume H(β) with β = 7/8. Let B denote Re B(χ) (or B for ζ), so
> Σ_ρ Re(1/ρ) = |B| by (F1).
> 1. For x ≥ 256: Σ_ρ |x^ρ/ρ²| ≤ (x^β + 7x^(1−β))·|B|.
> 2. For x > 1: Σ_ρ |x^(ρ−1)/(ρ(ρ−1))| ≤ c₂·(x^(β−1) + x^(−1/2))·|B|, with
>    c₂ = 189/125 ≥ 4/√7 = 1/(2√(β(1−β))).

*Proof.* **The pairing.** By (F2), ρ ↦ ρ′ := 1 − ρ̄ = (1−σ) + it maps the zero multiset to
itself. It is an involution that reflects across Re s = ½ and keeps the height t. So the
zeros split into two kinds:
- zeros on Re s = ½;
- pairs {ρ, ρ′} with ½ < σ ≤ β (Lemma 0 part 1), where ρ′ has real part 1 − σ.

Every term in each sum, and every Re(1/ρ) = σ/|ρ|², is non-negative, so the sums can be
regrouped this way. It suffices to show, for each kind, that its terms are at most the
stated factor times its share of Σ Re(1/ρ).

Write A = 1/|ρ|² = 1/(σ²+t²) and A′ = 1/|ρ′|² = 1/((1−σ)²+t²). For σ > ½, A′ ≥ A, and
A′/A ≤ σ²/(1−σ)², with equality at t = 0. The pair's share of Σ Re(1/ρ) is σA + (1−σ)A′.

**Part 1, a pair.** The pair contributes x^σ·A + x^(1−σ)·A′. With r = A′/A ∈ [1, σ²/(1−σ)²],
the ratio to its share is

  f(r) = (x^σ + x^(1−σ)·r)/(σ + (1−σ)·r).

This is a Möbius function of r, so it is monotone on the interval and at most its larger
endpoint value:
- f(1) = x^σ + x^(1−σ);
- f(σ²/(1−σ)²) = x^σ·(1−σ)/σ + x^(1−σ)·σ/(1−σ).

Since (1−σ)/σ ≤ 1 ≤ σ/(1−σ) ≤ β/(1−β) = 7, both are at most g(σ) = x^σ + 7x^(1−σ). The
function g is convex in σ, so on [½, β] it is at most max(g(½), g(β)) = max(8√x,
x^β + 7x^(1−β)). The second term is the larger. With u = x^(1/8),
u^7 + 7u − 8u^4 = u(u³−1)(u³−7) ≥ 0 when u³ ≥ 7, which holds for x ≥ 256.

**Part 1, a zero on the line.** Its term is x^(1/2)·A, and its share is ½A. The ratio is
2√x ≤ 8√x, which is at most the same bound.

**Part 2, a pair.** |ρ − 1| = |(σ−1) + it| = |ρ′| and |ρ′ − 1| = |−σ + it| = |ρ|. So both
terms have the denominator |ρ||ρ′| = (AA′)^(−1/2), and the pair contributes
(x^(σ−1) + x^(−σ))·√(AA′). By AM–GM, σA + (1−σ)A′ ≥ 2√(σ(1−σ))·√(AA′). So the ratio is at
most

  (x^(σ−1) + x^(−σ)) / (2√(σ(1−σ))) ≤ (x^(β−1) + x^(−1/2)) / (2√(β(1−β))),

because σ(1−σ) is decreasing on [½, β], x^(σ−1) ≤ x^(β−1), and x^(−σ) ≤ x^(−1/2). Finally
2√(β(1−β)) = √7/4, and c₂ = 189/125 ≥ 4/√7 because 7·189² = 250047 ≥ 16·125² = 250000.

**Part 2, a zero on the line.** The ratio is x^(−1/2)A/(½A) = 2x^(−1/2). This is at most
c₂(x^(β−1) + x^(−1/2)), because c₂ > 3/2 and x^(−1/2) ≤ x^(β−1) for x ≥ 1. ∎

(`constants.py` also brute-forces both ratios over a grid in (σ, t), as a sanity check
only. Part 1 is not sharp in its lower-order term: for x ≥ 256 (sampled) the per-pair supremum is
x^β + x^(1−β), approached as t → ∞ at σ = β, so the 7 could be 1. Likewise x ≥ 7^(8/3) ≈ 179
suffices for the comparison at σ = ½. Neither affects the constants, since 7·29⁻⁶ ≈ 10⁻⁸.)

## Revised zero-sum bounds (L2.1″)–(L2.3″)

LLS's identities are exact before the zero sums are estimated (their proofs of
Lemmas 2.1–2.3). Estimate the zero sums by Lemma 0′, and estimate |Σ 1/ρ²| ≤ Σ 1/|ρ|² ≤ K|B|
by Lemma 0 part 2 as before. Write c(x) = c₂(x^(−1/8) + x^(−1/2)). For x ≥ 256:

- **(L2.1″)** Σ_{n≤x} Λ(n) log(x/n) ≥ x − |B|(x^β + 7x^(1/8)) − K|B| − log(2π) log x − 1,
  where B is ζ's constant, |B| ≤ 0.0231. The k-sum, which is ≥ 0, has been dropped.
- **(L2.2″)** Re S(x, χ) ≤ |Re B(χ)|·(x^β + 7x^(1/8) + K + log x) + ½ log(q/π)·log x + Ẽ_a(x).
- **(L2.3″)** |Re B(χ)|·(1 + 1/x − c(x)) ≤ ½(1−1/x) log(q/π) − Re Σ_{n≤x} (Λ(n)/n) χ(n)(1−n/x) + E_a(x).

The signs are as in the first T1. In (L2.2″), S = −Σ x^ρ/ρ² − (ξ′/ξ)(0,χ) log x
− (ξ′/ξ)′(0,χ) + ½ log(q/π) log x + Ẽ_a, with Re (ξ′/ξ)(0,χ) = Re B(χ) ≤ 0 and
(ξ′/ξ)′(0,χ) = −Σ 1/ρ².

## Lemma T1 (constants)

> **Lemma T1.** Assume H(7/8). Let n be odd and composite, L = ln n, and X real with
> y := X^(1/8) ≥ 29. If
>
>   X − X^(7/8)·(αL + β₀) − (γL + δ) > 0,
>
> with α = 0.5276, β₀ = 0.0232, γ = 4.221 and δ = 0, then some prime p ≤ X is a
> Miller–Rabin witness for n.

*Proof.* Suppose no prime p ≤ X is a witness. Step (a) is exactly as in the first T1: χ̃
is primitive mod q̃ ≥ 3, log q̃ ≤ L, and χ̃(m) = 1 for every m ≤ X. Note that X ≥ 29^8 ≈ 5·10¹¹,
so X ≥ 256 and X ≥ 64.

**(b) Lower bound.** By (L2.1″),

  S(X, χ̃) ≥ X − |B|(X^β + 7X^(1/8)) − K|B| − log(2π) log X − 1.        (1)

**(c) Bound on |Re B(χ̃)|.** In (L2.3″) with x = X:
- the sum over n is ≥ 0;
- E_a(X) ≤ 0 (first T1, Step 0);
- ½(1−1/X) log(q̃/π) ≤ ½L, which is clear if q̃ ≥ 4 and holds because the left side is
  negative if q̃ = 3;
- 1 + 1/X − c(X) ≥ D_min := 1 − c₂(1/29 + 1/29⁴) > 0.947.

So

  |Re B(χ̃)| ≤ b₁L,  b₁ = 1/(2D_min).        (2)

**(d) Upper bound.** By (L2.2″) and (2), with ½ log(q̃/π) ≤ ½L,

  S(X, χ̃) ≤ b₁L·(X^β + 7X^(1/8) + K + log X) + ½L·log X + Ẽ_a(X).        (3)

**(e) Absorbing.** For X ≥ X₀ = 29^8, which exceeds e^(1/β):
- X^(1/8)/X^β = X^(−3/4) ≤ 29^(−6) =: s₆;
- log X ≤ a₁X^β, with a₁ = 8 ln 29/29^7. log X/X^β is decreasing beyond e^(1/β), and
  `verify/check.py ln_bounds` gives the upper bound on ln 29.

Also Ẽ_a(X) ≤ max(π²/24 − ½(ln 64)², π²/8 − (ln 2 + γ/2) ln 64) < −2.84. Those are the
first T1's analytic bounds, valid for X ≥ 64.

**(f) Contradiction.** Subtract (3) from (1) and use (e):

  0 ≥ X − X^β·[ b₁L(1 + 7s₆ + a₁) + ½a₁L + |B|(1 + 7s₆) + log(2π)a₁ ] − [ K b₁ L + (K|B| + 1 + Ẽ_a(X)) ].

The coefficients satisfy:
- b₁(1 + 7s₆ + a₁) + ½a₁ = 0.52750… ≤ α;
- |B|(1 + 7s₆) + log(2π)a₁ = 0.023100… ≤ β₀;
- K b₁ = 4.22003… ≤ γ;
- K|B| + 1 + Ẽ_a(X) < 1.185 − 2.84 < 0 = δ.

So 0 ≥ X − X^(7/8)(αL + β₀) − (γL + δ), which contradicts the hypothesis. ∎

`constants.py` recomputes each coefficient in exact rationals and compares it with the
claim file. `verify/check.py explicit` then shows that X = (0.529 ln n)^8 satisfies the
hypothesis for every n ≥ ψ₁₃, where y ≥ 0.529·ln ψ₁₃ > 29.8.

## What a reviewer should check

1. **Lemma 0′, the pairing:** the involution ρ ↦ 1 − ρ̄ on the zero multiset (F2), and
   the regrouping of non-negative terms.
2. **Lemma 0′ part 1:** the Möbius endpoint argument, the bound by g(σ), its convexity,
   and the comparison at σ = ½ for x ≥ 256.
3. **Lemma 0′ part 2:** |ρ − 1| = |ρ′| and AM–GM.
4. **(L2.1″)–(L2.3″):** the only change from the first T1's (L2.1′)–(L2.3′) is the
   estimate of the x-dependent zero sum.
5. **Step (f):** the δ = 0 argument, which uses Ẽ_a < −2.84, and the four coefficients.
   Rerun `constants.py`.

## What's next

- **γ.** The same pairing gives Σ 1/|ρ|² ≤ (50/7)|B|, because the per-pair supremum of
  (A + A′)/(σA + (1−σ)A′) is max(2, 50/7). That would lower γ from 4.221 to about 3.77. The
  effect on C is negligible.

- The leading constant is now α ≈ 1/(2D_min) ≈ 0.5275, limited by y_min ≤ 0.529·ln ψ₁₃.
  As y_min → ∞ it tends to ½, so a larger pseudoprime table (n0 > ψ₁₃) is worth at most
  about 5% in C here. With the current template, C → ½ is the limit of this argument. The
  next item changes the template.
- LLS Lemma 2.4 under H(β) (card `lls-lemma-2-4`) would subtract log X from the bound on
  |Re B(χ̃)|. That gives *negative* constant terms, which the current checker rejects
  (it requires α, β, γ, δ ≥ 0). Using it needs a verifier extension (track `verifier`).
  It would allow D < 0, worth roughly 8·log₁₀(1 + 8 ln(0.53 L)/(0.53 L)) in log₁₀ W.

## Review history

**2026-10-19, adversarial review by a separate AI agent (fresh context).** It is not an
independent human check.
- **No fatal or fixable problems.** All five checklist items were confirmed. The reviewer
  independently re-derived the residues in LLS Lemmas 2.1–2.3, the four E functions, the
  pairing involution for complex χ, and every coefficient. It also ran 300k random (σ, t)
  samples against both bounds.
- **Minor, fixed:**
  - the remark on where part 1 is attained was wrong (the 7 could be 1);
  - x ≥ 256 is stronger than needed;
  - the section heading's labels didn't match the formulas;
  - the "fewer bases" figure was the ratio of bounds, not of prime counts;
  - "the limit of this method" was loose wording.

**2026-10-19, independent recheck by a separate AI agent** (fresh context, no access to the
earlier review). It is not a human check.
- **Confirmed.** Every checklist item was re-derived: the pairing involution, both parts of
  Lemma 0′, the LLS 2.1–2.3 residue identities, and every constant in 50-digit decimals.
- **Adversarial numerical search:** 2000 optimizer restarts plus 400k random samples per part.
  No violation; the suprema are 1 (part 1) and 0.99991 (part 2).
- **Taken on trust:**
  - the contour shifts;
  - step (a) of the first T1;
  - `ln_bounds` and `check_explicit`.
- **Minor, fixed:** the GRH sanity check now states the general-β forms; the 50/7 note is
  added.
