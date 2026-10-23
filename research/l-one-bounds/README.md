**Original idea: Geoffrey Irving.**

# Explicit L(1,chi) and class-number bounds under H(7/8)

For a primitive Dirichlet character of conductor q with log q >= 32, put
M(q) = exp(gamma)(8 log log q + 2). This package proves, conditionally on
H(7/8) including zeta,

    pi^2/(6 M(q)) <= |L(1,chi)| <= M(q).

Thus the dependence remains of order log log q in both directions; the
leading constant changes from the GRH value 2 exp(gamma) to 8 exp(gamma).
The catalog's tentative power-of-log-q shape is unnecessary in this range.
For a negative fundamental discriminant -q in the same range,

    pi sqrt(q)/(6 M(q)) <= h(-q) <= M(q) sqrt(q)/pi.

The threshold is on the **primitive conductor**, not an arbitrary large
imprimitive modulus. PROOF.md Section 8 gives the explicit Euler factors
needed for imprimitive characters. Smaller conductors, principal characters,
optimal constants and the truth of H(7/8) are outside the theorem.

- [PROOF.md](PROOF.md): complete derivation, GRH-use audit and ranges.
- [constants.py](constants.py): exact rational budget, polynomial identities
  for the complex-phase Euler minimum at p=2, and six rejection controls.
- [RECHECK.md](RECHECK.md): independent fresh-context same-model AI review,
  confirming the complete conditional proof with independently derived arithmetic.

From the repository root (Python standard library only):

```sh
python3 research/zero-pairing/constants.py
python3 research/l-one-bounds/constants.py
python3 verify/check.py all
python3 -m unittest discover -s tests
```

The new checker reports K <= 286849/108000 < 8/3, with margin1151/108000,
p=2 polynomial margin17/7200, and exponential bridge135/76<2. The formal
pair {1/8,7/8} rejects a naive retained-GRH reciprocal-square constant2;
it is a strip-bound control, not an assertion about actual L-function zeros.
The full proof supplies all-height and all-conductor bounds in its stated
range; finite arithmetic checks alone do not establish the analytic theorem.

## Scope, evidence and credit

Card: `corollaries` / `l-one-bounds`, catalog revision5, original seed
`f7e9c53c773500cea50225ca67a35d17`. Base:
`d2bd5167a42b8256f1362640dc149057920e5db9`. This is an independent sibling
package against main; no unmerged theorem or accepted-record change is needed.
An AI source-research context derived the argument, then the parent checked
the source identities and packaged the exact arithmetic. Status:
author-checked and independently AI-rechecked conditional draft, pending
maintainer review. The recheck independently reconstructed the integrated
kernels, zeta pole limit, Euler minimum and complete uniform budget.
Source research is not counted as independent theorem verification. The report
pins its reviewed snapshot; later edits record review status and links only.

Predecessor credit: Geoffrey Irving; Bach; Lamzouri--Li--Soundararajan,
[arXiv:1309.3595v3](https://arxiv.org/abs/1309.3595v3), Lemmas2.3--2.6 and
Section5; Claude's accepted first-T1 and zero-pairing packages (PRs6 and8).
Codex authored this package. Text/proofs: CC BY4.0; code: Apache-2.0.

## Open next questions

- Lower log q>=32 or additive constant2 using a fully charged new truncation
  and uniform range proof.
- Extend the useful range to smaller primitive conductors with a new exact
  truncation and fully charged uniform errors.
