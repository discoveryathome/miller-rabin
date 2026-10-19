# The hypothesis, the lemma template, and what the checker proves

## Hypothesis H(θ)

> **H(θ).** For every integer q ≥ 1 and every Dirichlet character χ mod q, L(s, χ) has
> no zero with Re s > θ. (The pole of L(s, χ₀) at s = 1 is not a zero.)

- **GRH** is H(1/2).
- **The quasi-Riemann claim** (OpenAI, 2026-09-30) is H(7/8). It is unreviewed.
  Two follow-up papers, both assuming OpenAI's analytic inputs, push θ slightly lower:
  - Liu, arXiv:2610.12234: 34999/40000, and ≈ 0.874957.
  - Xu–Sang, arXiv:2610.15291: 0.8748867.
- **Imprimitive characters.** For an imprimitive χ, L(s, χ) differs from the primitive
  L-function only by finitely many Euler factors (1 − χ*(p)p^(−s)). Their zeros lie on
  Re s = 0, so H(θ) for primitive characters implies it for all characters. Checking
  that the preprint's statement covers what is needed here is assumption A2 in
  [`discover/frontier.json`](../discover/frontier.json).

H(θ) contains no constants. Every constant below comes from classical, explicit analytic
number theory, so **C can be made fully rigorous today; only θ is conditional.**

## Template T1 (the lemma a written proof must establish)

Fix θ ∈ [1/2, 1). A T1 proof supplies explicit rationals w1 > 0, α, β, γ, δ ≥ 0 and
y_min ≥ 1, and proves:

> **Lemma T1.** Assume H(θ). Let n be an odd composite, L = ln n, and x a real number
> with x^(1−θ) ≥ y_min. If
>
>   **w1·x − x^θ·(α·L + β) − (γ·L + δ) > 0,**
>
> then some prime p ≤ x is a Miller–Rabin (strong) witness for n.

### How such a proof goes (Bach's argument with GRH replaced by H(θ))

This is a sketch of the expected route, not a proof. Writing it out rigorously, with every
constant explicit, is the core task (track `explicit-bound`).

1. **Liars sit in a proper subgroup.** For odd composite n, the strong liars lie in a
   proper subgroup G of (ℤ/nℤ)\*. (Standard; see Bach 1990, or Conrad's notes on
   Miller–Rabin.) A prime p | n with p < n is always a witness.
2. **A character detects G.** Since G is proper, some non-trivial χ mod n is 1 on G.
   Suppose no prime p ≤ x is a witness. Then no prime ≤ x divides n, and χ(p) = 1 for
   every prime p ≤ x. So χ(m) = χ₀(m) for every m ≤ x.
3. **Explicit formula.** Pick a weight w supported on [0, 1] and set
   S(x) = Σ_m Λ(m)·(χ₀(m) − χ(m))·w(m/x). By step 2, S(x) = 0. The explicit formula
   writes S(x) as:
   - a main term: x times the Mellin transform of w at 1, which gives w1;
   - minus a sum over the non-trivial zeros of L(s, χ₀) and L(s, χ). Under H(θ) and
     explicit zero-counting bounds for conductor ≤ n, this is at most x^θ·(α·L + β).
   - minus trivial zeros, Euler factors at primes dividing n, and conductor bookkeeping.
     Together these are at most γ·L + δ.
4. **Contradiction.** If the T1 inequality holds, S(x) > 0. That contradicts S(x) = 0.

Under GRH, Bach (Math. Comp. 55 (1990) 355–380) runs this argument and gets a witness
below 2(ln n)². That paper is the template for the bookkeeping.

## What `verify/check.py explicit` proves

A claim gives θ, C, D, n0 and the T1 constants. The checker shows, in exact rational
arithmetic with rigorous bounds on ln n0, that x = W(n) := (C·ln n + D)^(1/(1−θ))
satisfies the T1 inequality for **every** n ≥ n0. The method:

1. Substitute y = C·L + D and divide by x^θ.
2. Show the resulting function of L is nondecreasing on [ln n0, ∞).
3. Show it is positive at ln n0.

It also requires n0 ≤ ψ₁₃ = 3317044064679887385961981. Below that, the first 13 primes
(up to 41) contain a witness (Sorenson–Webster 2017).

Combined with Lemma T1, this gives the theorem:

> Assume H(θ). Every odd composite n has a prime witness p ≤ max(41, W(n)).

So the deterministic algorithm tests every prime base p ≤ max(41, W(n)). Its cost is
O(W(n)/log W(n) · (log n)² · log log n) bit operations, which is
(log n)^(2 + 1/(1−θ) + o(1)).

**The checker does not check the proof of Lemma T1.** That is human review of the written
proof, the second half of this project's evidence standard.

## The measure of progress

In order of priority:

1. The exponent 1/(1−θ), which only θ moves.
2. C (smaller is better).
3. D, then n0, as tie-breakers.

The checker reports log₁₀ W(2^1024) as a single comparable number.
