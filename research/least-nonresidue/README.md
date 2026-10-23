**Original idea: Geoffrey Irving.**

# Explicit least nonresidues under H(7/8)

For every q >= 5 and every proper subgroup H of (Z/qZ)*, this package proves,
conditionally on H(7/8), that the least prime ell not dividing q and outside H
satisfies

    ell < (0.683 log q)^8.

If q != 6, coefficient 0.678 suffices. At q = 6 the outside prime is exactly
5. For every prime q >= 5, in particular, the least positive quadratic
nonresidue is a prime below (0.678 log q)^8. The cases q = 3 and 4 have exact
outside primes 2 and 3. All logarithms are natural.

- [PROOF.md](PROOF.md): the complete conditional argument, all ranges and errors.
- [constants.py](constants.py): exact new-constant recomputation, small-range
  endpoints, 6540 direct prime-modulus checks and seven rejection controls.
- [RECHECK.md](RECHECK.md): independent fresh-context same-model AI recheck of
  the complete conditional theorem and a separate direct computational route.
- [GUARD-RECHECK.md](GUARD-RECHECK.md): targeted follow-up confirming the positive
  coefficient guard, negative regression control and unchanged default results.

From the repository root (Python standard library only):

```sh
python3 research/zero-pairing/constants.py
python3 research/least-nonresidue/constants.py
python3 verify/check.py all
python3 -m unittest discover -s tests
```

The new checker certifies analytic error
`241522181840005231/254054780070000000 < 1`. It directly checks every prime
5 <= q < 65536. The mathematical small-range proof handles all proper
subgroups using the elementary p < q observation and two exact endpoints,
so these direct quadratic checks are supplementary evidence.

The constants face real small-modulus obstructions: 0.682 fails the general
theorem at q = 6, and 0.677 fails the quadratic theorem at q = 5. No claim
of optimality is made. H(7/8), its Lean proof and new contour-convergence
arguments are outside the checker's scope.

Section 5 also gives an author-checked and independently AI-rechecked extension
under H(8748867/10000000): replace exponent 8 by the exact
10000000/1251133, with the same coefficients, domains and small cases.
All fractional powers are bounded by safe integer-power comparisons.
Its separate fresh-context review, [RECHECK-THETA.md](RECHECK-THETA.md),
independently derives the transfer, arithmetic, endpoints and all 6540 direct
prime checks. The earlier H(7/8) reviews remain historical evidence for their
own snapshots.

## Scope, evidence and credit

Card: `corollaries` / `least-nonresidue`, catalog revision 5; original seed
`f7e9c53c773500cea50225ca67a35d17`. Upstream base:
`d2bd5167a42b8256f1362640dc149057920e5db9`. The preceding progression work
identified useful conductor bookkeeping; this is a standalone sibling
package against main, deriving its lemmas from accepted inputs. No unmerged
PR or accepted-record change is required.

Credit: Geoffrey Irving; Bach; Lamzouri--Li--Soundararajan,
[arXiv:1309.3595v3](https://arxiv.org/abs/1309.3595v3), Section 3 and Lemmas
2.1--2.3; Claude's accepted first-T1 and zero-pairing packages (PRs #6 and #8).
Codex drafted this contribution and ran its author checks. Separate fresh-context
same-model AI reviews confirmed the original mathematical claims, the small
input-guard fix, and the smaller-theta extension. The independent finite route
used a prime sieve and quadratic reciprocity,
rather than the author's trial primality and modular exponentiation. This is
AI review, not human review; maintainer review remains pending. Each report pins
its snapshot; subsequent edits record review status and links only.
Text/proofs: CC BY 4.0; code: Apache-2.0.

## Open next questions

- Narrow the gaps between the sufficient coefficients and their explicit
  small-modulus obstructions, while preserving the exact domains.
- Optimize the parameter-dependent constants while retaining exact directed
  bounds for noninteger powers and an explicitly checked complete domain.
