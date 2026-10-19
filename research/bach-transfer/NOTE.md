# Does Bach's argument use GRH only through where the zeros are? (card `bach-uses-only-zero-location`)

**Evidence level:** author-checked (one reader).

**Source.** Bach 1990 (Math. Comp. 55) returned 403 from ams.org, so I read the
refinement of Bach's method instead:

> Lamzouri, Li, Soundararajan, *Conditional bounds for the least quadratic non-residue
> and related problems*, arXiv:1309.3595v3 [LLS].

Its Theorem 1.1 (the least prime ℓ ∤ q outside a proper subgroup is < (log q + B(q))²,
and < (log q)² when q has no prime factor below (log q)²) is Bach's result with better
constants. Annotating Bach 1990 itself is still open, and is worth doing if a reviewer
wants the original.

## Where [LLS] uses GRH or RH

| Place | Use | Replacement under H(θ), with K = 1/(1−θ) |
|---|---|---|
| Lemma 2.1 (ζ), Lemma 2.2: Σ_ρ x^ρ/ρ² | \|x^ρ\| = √x and Σ 1/\|ρ\|² = 2\|Re B\| | ≤ x^θ · K\|Re B\| |
| Lemma 2.2: (ξ'/ξ)'(0, χ) = −Σ 1/ρ² | Σ 1/\|ρ\|² = 2\|Re B\| | ≤ K\|Re B\| |
| Lemma 2.3: Σ_ρ x^(ρ−1)/(ρ(ρ−1)) | \|x^(ρ−1)\| = x^(−1/2), \|ρ−1\| = \|ρ\| | ≤ x^(θ−1) · K\|Re B\|, via AM–GM and {1−ρ} = {ρ̄'} |
| Hadamard product, Re B(χ) = −Σ Re(1/ρ) | none (unconditional) | unchanged |
| E_a, Ẽ_a, Lemma 3.1, §3 bookkeeping | none | unchanged |

The key inequality: Re(1/ρ) = Re ρ/|ρ|² ≥ (1−θ)/|ρ|². This holds because H(θ), together
with the functional equation, puts every non-trivial zero in 1−θ ≤ Re ρ ≤ θ.

**Verdict: yes.** With these three replacements the argument goes through. It gives a
witness bound X ≈ ((K/2)·ln n)^K, so the exponent is K = 1/(1−θ), as the project assumed.
For θ = 1/2 this recovers the GRH bound, (log q)².

## A simplification for Miller–Rabin

A prime p | n is itself a witness. So when we suppose there is no witness ≤ X, we may also
assume no prime ≤ X divides n. That puts us in [LLS] Part 2's setting: all the ω(q) and
(n, q) > 1 corrections vanish, and χ̃(m) = 1 for every m ≤ X. See
`research/first-explicit-t1/PROOF.md`, step (a).

```discover
{"v": 0, "kind": "done", "task": "bach-uses-only-zero-location", "scope": "LLS (refining Bach) uses GRH only via |x^rho| = sqrt(x) and sum 1/|rho|^2 = 2|Re B|; both have H(theta) analogues with factor K = 1/(1-theta); exponent 1/(1-theta) confirmed", "base": "6f85127", "posted_at": "2026-10-19T10:30:00Z", "evidence_level": "author-checked", "artifact": "research/bach-transfer/NOTE.md"}
```
