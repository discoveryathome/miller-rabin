**Original idea: Geoffrey Irving.**

# Explicit least primes under half-plane hypotheses

This AI-authored research package transfers the coset argument of
[Lamzouri--Li--Soundararajan, arXiv:1309.3595v3](https://arxiv.org/abs/1309.3595v3),
Section 4, using the project's accepted zero-pairing Lemma 0'. Under H(7/8),
for q >= 3 and a subgroup of index h >= 2, it proves

    P(aH,q) < max(80, h log q)^8,
    P(a,q)  < (0.581 phi(q) log q)^8.

The second statement covers every reduced residue class; q = 2 is excluded.
It has an exact finite fallback for 3 <= q < 2048. The theorem remains
conditional on H(7/8), which this package does not prove or replay in Lean.

Section 8 adds an independently AI-rechecked extension for 13/15<=b<=7/8 under
H(b), with r=1/(1-b). The coset cutoff 80 is retained, and the sharp all-q
progression coefficient is exactly c_b=7^(1-b)/(2 log3):

    P(a,q) <= [c_b phi(q) log q]^r.

Equality holds exactly at q=3,a=1. All q>=4 satisfy the stronger strict
bound with coefficient .58. For b=8748867/10000000, this gives exponent
10000000/1251133, and the conservative decimal .581 still works.
This extension passed its own fresh-context recheck in RECHECK-SHARP.md.

Section 9 adds an author-checked improvement P(aH,q)<max(64,h logq)^r,
throughout the same parameter interval, awaiting its own fresh-context review.
It keeps the negative constant in the principal T sum, the h-1 saving and
a sharper proper-power bound. The q<=20 step uses the sharp progression
theorem in this package; the q>=21 estimate is uniform and analytic.

- [PROOF.md](PROOF.md): theorem, complete transfer, constants, and limitations.
- [constants.py](constants.py): exact rational recomputation and exhaustive
  fallback, with ten deliberate rejection controls. Python standard library only.
- [SOURCE-AUDIT.md](SOURCE-AUDIT.md): primary-source audit preceding the proof;
  this is not the fresh-context recheck of the finished theorem.
- [RECHECK.md](RECHECK.md): separate fresh-context same-model AI recheck of the
  coset theorem and original coefficient-1 progression corollary.
- [RECHECK-REFINEMENT.md](RECHECK-REFINEMENT.md): separate fresh-context same-model
  AI recheck confirming coefficient 0.581 and independently enumerating all
  1274560 fallback classes.
- [RECHECK-SHARP.md](RECHECK-SHARP.md): separate fresh-context same-model AI
  recheck of the full parameter interval, exact sharp coefficient and all
  1274558 new fallback classes, using a distinct progression search.

From the repository root:

```sh
python3 research/zero-pairing/constants.py
python3 research/least-prime-progression/constants.py
python3 verify/check.py all
python3 -m unittest discover -s tests
```

Expected new-check result: `all constants and finite checks pass`, including
1274560 reduced classes modulo 3 through 2047. The original coset error bound
is `5385194673/5600000000 < 1`; the refined progression error bound is
`114068220107243/115735200000000 < 1`. The new parameter coset error is
5446184217/5600000000<1; the sharp progression subdomain error is
5705615549587/5776800000000<1. The new fallback checks 1274558 classes
modulo 4 through 2047 using the weaker integer exponent 7. The new cutoff 64
error is 675090454343806963541/675706247040000000000<1. All ten controls
must reject.
The shared verifier continues to check only its existing Miller--Rabin claims.
The exact counterexample P(1,3)=7 rules out coefficient 0.58 in the same all-q
form, so this refinement is close to a genuine small-modulus obstruction.

## Session scope and credit

Card: `corollaries` / `least-prime-in-progression`, catalog revision 5.
Seed: `f7e9c53c773500cea50225ca67a35d17` (draw supplied by the user and retained).
Base: `d2bd5167a42b8256f1362640dc149057920e5db9`.
No matching open handoff or claim was found; the only open PR, #10, concerned
the reference implementation. This package adds the sibling least-prime theorem
and does not alter the project's record of accepted results.

Predecessors: Geoffrey Irving's original project idea; Bach's conditional method;
LLS's orthogonality and residue formulas; Claude's accepted first-T1 and
zero-pairing packages (PRs #6 and #8). Codex drafted this package and performed
its author checks. A separate fresh-context Codex agent rederived the analytic
steps and reproduced the finite fallback by trial division. This is AI review,
not human review. Source audit and theorem recheck are separate evidence items.

The initial coefficient-1 result was separately AI-rechecked. The open
corollaries handoff requested coefficient at most 3/4; Section 7 now strengthens
it to 0.581 using a new elementary cubic totient bound and a fully charged
analytic cutoff. The refinement is author-checked and separately AI-rechecked;
maintainer review remains pending. Each recheck pins its own snapshot; later
edits record review status and links only. The parameter and sharp-coefficient
extension is a new result, checked in its own RECHECK-SHARP.md report rather
than inferred from those historical reviews. All reports pin their snapshots;
subsequent edits record review status and links only.

## Open next questions

- Improve the coset cutoff 80 using PROOF.md (13), preserving the full domain.
- Replace the elementary proper-prime-power envelope by a sharper proved one
  under H(7/8); keep the separate principal and complex-character errors.
- Maintainer review of the conditional theorem and the evidence in RECHECK.md.

Text and proofs: CC BY 4.0. Code: Apache-2.0.
