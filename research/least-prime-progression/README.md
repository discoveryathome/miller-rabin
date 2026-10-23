**Original idea: Geoffrey Irving.**

# Explicit least primes under H(7/8)

This AI-authored research package transfers the coset argument of
[Lamzouri--Li--Soundararajan, arXiv:1309.3595v3](https://arxiv.org/abs/1309.3595v3),
Section 4, using the project's accepted zero-pairing Lemma 0'. Under H(7/8),
for q >= 3 and a subgroup of index h >= 2, it proves

    P(aH,q) < max(80, h log q)^8,
    P(a,q)  < (phi(q) log q)^8.

The second statement covers every reduced residue class; q = 2 is excluded.
It has an exact finite fallback for 3 <= q < 512. The theorem remains
conditional on H(7/8), which this package does not prove or replay in Lean.

- [PROOF.md](PROOF.md): theorem, complete transfer, constants, and limitations.
- [constants.py](constants.py): exact rational recomputation and exhaustive
  fallback, with four deliberate rejection controls. Python standard library only.
- [SOURCE-AUDIT.md](SOURCE-AUDIT.md): primary-source audit preceding the proof;
  this is not the fresh-context recheck of the finished theorem.
- [RECHECK.md](RECHECK.md): separate fresh-context same-model AI recheck;
  the conditional proof and exact constants were confirmed with no required fixes.

From the repository root:

```sh
python3 research/zero-pairing/constants.py
python3 research/least-prime-progression/constants.py
python3 verify/check.py all
python3 -m unittest discover -s tests
```

Expected new-check result: `all constants and finite checks pass`, including
79594 reduced classes modulo 3 through 511. The rational analytic error bound
is `5385194673/5600000000 < 1`; the four rejection controls must reject.
The shared verifier continues to check only its existing Miller--Rabin claims.

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

The analytic target was unchanged. A conservative coefficient 1 was chosen to
leave a clear positive margin and avoid inheriting GRH-only constants. The
small finite fallback is part of the written progression proof. Status:
author-checked and independently checked by a separate same-model AI context;
maintainer review is pending. RECHECK.md pins the reviewed snapshot hashes;
later proof/README edits record the review status and links only.

## Open next questions

- Reduce the progression coefficient below 1, using PROOF.md (13), exact
  endpoints and an explicitly bounded finite fallback.
- Replace the elementary proper-prime-power envelope by a sharper proved one
  under H(7/8); keep the separate principal and complex-character errors.
- Maintainer review of the conditional theorem and the evidence in RECHECK.md.

Text and proofs: CC BY 4.0. Code: Apache-2.0.
