Original idea: **Geoffrey Irving**.

# Explicit witnesses for the smaller theta

Assuming H(8748867/10000000), including zeta, every odd composite
n>=3317044064679887385961981 has a prime Miller--Rabin witness

    p <= (0.528 log n)^(10000000/1251133).

The bit exponent in the repository's model is exactly
12502266/1251133<10, with gap9064/1251133. The same coefficient certificate
also improves the H(7/8) bound to (0.528 log n)^8. Smaller odd composites
retain the unconditional first-thirteen-prime-bases fallback, primes<=41.
The two half-plane assumptions are separate; neither is proved here.

- [PROOF.md](PROOF.md) proves the general pairing lemma with its X range,
  the parameter transfer, all four gamma signs, and the full T1 inequality.
- [constants.py](constants.py) certifies all constants with exact rationals,
  checks both new claim files, and runs ten deliberate rejection controls.
- The new JSON files in `candidates/` use the existing verifier format.
- [RECHECK.md](RECHECK.md) independently reconstructs the complete theorem,
  with integer fixed-point arithmetic, source-scope checks and exact hashes.

From the repository root, Python standard library only:

```sh
python3 research/zero-pairing/constants.py
python3 research/lower-theta/constants.py
python3 verify/check.py all
python3 -m unittest discover -s tests
```

Status: author-checked conditional draft, confirmed by a separate fresh-context
same-model AI theorem review with no required fixes. Source research and author
checks do not count as that review. Maintainer review remains pending. The
report pins its snapshot; later edits record review status and links only.
The shared verifier checks the substitution into T1, whose analytic proof
is supplied separately. No accepted frontier, ledger or contributor record
is changed. The smaller-theta claim assumes H(theta) directly: the scope of
Xu--Sang's versioned preprint was read, but its proof and analytic inputs,
H(7/8), Lean replay, classical contour foundations, pseudoprime minimality
search and the bit-cost model are not newly certified by this package.

Base: d2bd5167a42b8256f1362640dc149057920e5db9. Task: `explicit-lower-theta`,
catalog revision5. Original seed: f7e9c53c773500cea50225ca67a35d17; a concrete
priority follow-on after the drawn corollaries. Credit: Geoffrey Irving;
Bach; Lamzouri--Li--Soundararajan; Claude's accepted T1 and zero-pairing work
in PRs6 and8; Xu--Sang; Conrad; Sorenson--Webster. Codex supplied source
research, author checks and a separate theorem recheck. This is AI review,
not human or formal verification. Text/proofs CC BY4.0; code Apache-2.0.

A next question is to optimize the directed coefficient bounds while
retaining exact arithmetic and the complete n>=PSI_13 range. The controls
show why the old powers4,6,7 cannot simply be copied at the smaller theta.
