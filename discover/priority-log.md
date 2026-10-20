# Priority log

## Revision 1 · 2026-10-19

This is the initial allocation. It is a hypothesis, not a mandate.

| Track | Weight | Why |
|---|---:|---|
| `explicit-bound` | 40 | It's the bottleneck. No explicit constant exists, so the corollary isn't yet an algorithm. A loose but rigorous first T1 unblocks everything else. |
| `verify-premise` | 25 | Everything rests on an unreviewed preprint (A1) and on a scope question (A2). Cheap reading tasks catch problems early. |
| `verifier` | 15 | The explicit-bound check is new code, written by an agent. Donors and the frontier depend on it. |
| `tighten-c` | 12 | Valuable, but blocked until the first T1 lands. The weight stays low until then. |
| `beyond-theta` | 8 | Speculative. No literature supports it, so it gets a small weight. It is the only route to beating AKS's 6 short of θ < 3/4. |

**Next review:**
- after the first accepted T1 proof (then move weight from `explicit-bound` to
  `tighten-c`);
- if A1 or A2 is refuted;
- otherwise, after 20 contributions.

## Revision 2 · 2026-10-19

This revision follows the first hub assessment and the draft results in PRs #5 and #6.

**Covered cards replaced by their remaining work.** The picker doesn't weight by
`existing_checks`, so covered cards kept getting about 37% of draws.

| Old card | Replaced by |
|---|---|
| `preprint-scope` | `replay-lean-proof` |
| `bach-uses-only-zero-location` | `bach-original-annotation` |
| `first-explicit-t1` | `recheck-first-t1` |

**Changes:**
- New track `recheck` (35): the open task that now gates the frontier is the independent
  check of PR #6.
- `tighten-c` raised from 12 to 30 and unblocked, now that a draft T1 exists. It adds the
  reviewer-suggested card `lls-lemma-2-4`, and `zero-sum-inputs` moves here.
- `verify-premise` lowered from 25 to 15; `verifier` from 15 to 12. `explicit-bound` is
  removed: its remaining card moved into `tighten-c`.

**Next review:** when PR #6 is accepted or rejected, or after 20 contributions.

## Revision 3 (2026-10-19)

**Weights unchanged.** A second draft T1 (PR #7, zero pairing, C = 0.529) now exists.
- `recheck-first-t1` now covers both PR #6 and PR #7.
- `lls-lemma-2-4` is re-aimed at the PR #7 proof. It notes that it needs a verifier
  extension for negative template constants.

**Next review:** when PR #6 or #7 is accepted or rejected, or after 20 contributions.

## Revision 4 (2026-10-19)

- PRs #5 and #6 are merged. The zero-pairing draft moved from the auto-closed #7 to #8.
- Each of #5, #6 and #8 was independently rechecked, and all three were confirmed. The
  maintainer counts same-model, fresh-context rechecks as independent. The minor fixes are
  in this PR (#9).
- The maintainer directed that #8 moves the frontier on merge.

**Weights:**
- `recheck` lowered from 35 to 15: its gate is cleared, and `recheck-first-t1` is retired.
- `tighten-c` raised from 30 to 40.
- `verify-premise` raised from 15 to 20: A1 (the unrefereed preprint) is now the main open
  assumption.
- `verifier` raised from 12 to 17: new card `negative-template-constants`, which unblocks
  `lls-lemma-2-4`.

**Next review:** when #8 merges, or after 20 contributions.

## Revision 5 (2026-10-20)

**Pre-launch, by the maintainer's decision.** First contributors should land on reachable,
visible results.
- **New track `quick-wins` (35):**
  - `explicit-lower-theta`: the zero-pairing proof at Xu–Sang's θ, giving an exponent
    below 10. A float probe suggests C ≈ 0.528.
  - `reference-implementation`.
- **New track `corollaries` (20):** the maintainer widened the scope to LLS's sibling
  theorems under H(7/8). Cards `least-nonresidue`, `least-prime-in-progression` and
  `l-one-bounds`.
- **Weights:** `tighten-c` 40 → 20, `verifier` 17 → 10, `verify-premise` 20 → 8,
  `recheck` 15 → 4, `beyond-theta` 8 → 3.
- **DISCOVERY.md** now states the ceilings: C ≥ ½ in this argument, the exponent is tied
  to θ, and A1 is the main open assumption.

**Next review:** after the first 10 contributions, or when `quick-wins` empties.

