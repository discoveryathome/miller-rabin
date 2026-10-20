# Explicit deterministic Miller–Rabin under the quasi-Riemann hypothesis: contributing research effort

**Start here if you were told to contribute without a specific task.** Aim for one useful,
independently reviewable result in the time available (default 60 minutes). The generic
session procedure (refresh, orient, choose, bound, verify, hand off) comes from the
Discovery@Home playbooks (https://github.com/discoveryathome/discover/tree/main/playbooks).
This file holds only what is specific to this project.

**Original idea: Geoffrey Irving.** Maintainer of record: Douglas R. Colkitt.

## The problem

**Background.** The Miller–Rabin test declares n prime when no base a in a test set is a
witness to compositeness. Under GRH, Bach (1990) proved that testing every a ≤ 2(ln n)²
suffices. That gives a deterministic test running in (log n)^(4+o(1)) bit operations.
Without GRH, the best known bound on the least witness is a power of n, so a deterministic
Miller–Rabin in P was open. The only proven deterministic polynomial-time primality test
is AKS. Its best variant, Lenstra–Pomerance, runs in (log n)^(6+o(1)).

**The new input.** On 2026-09-30, OpenAI released an AI-generated, unreviewed preprint.
It claims that no Dirichlet L-function has a zero with Re s > 7/8. We call this
**H(7/8)**. If it holds, Bach's argument goes through with GRH replaced by H(θ). The
result is a witness below **W(n) = (C·ln n + D)^(1/(1−θ))** and a running time of
(log n)^(2 + 1/(1−θ) + o(1)).

| Zero-free line θ | Running-time exponent |
|---|---|
| 7/8 | 10 |
| 0.8748867 (Xu–Sang, best published) | ≈ 9.9928 |

**The goal of this project.** Nobody has written that argument out with explicit
constants. Without an explicit C, the corollary is an existence statement, not an
algorithm: the loop doesn't know where to stop. The goal is:

1. Make W(n) fully explicit and rigorous under H(θ).
2. Then make it as small as possible: smaller C first, then D and n0.

The precise statements are in [docs/template-T1.md](docs/template-T1.md).

## Current frontier

[`discover/frontier.json`](discover/frontier.json) records the accepted result. Assuming
H(7/8), every odd composite n has a prime witness p ≤ max(41, (0.529·ln n)^8), with
log₁₀ W(2^1024) = 20.597. Proof: [research/zero-pairing/PROOF.md](research/zero-pairing/PROOF.md).

What is *not* established:
- the preprint itself (assumption A1), which no one has refereed and whose Lean proof
  this project hasn't replayed;
- an explicit C for any θ < 7/8, such as Xu–Sang's;
- anything below C = ½, the limit of the current template.

## The bottleneck

Two drafts of Lemma T1 with explicit constants now exist under H(7/8):
- W(n) = (4.2 ln n)^8, in PR #6;
- W(n) = (0.529 ln n)^8, in PR #7. It pairs each zero ρ with 1 − ρ̄ and is stacked on #6.

The bottleneck is **an independent check of those drafts** (card `recheck-first-t1`).
Until one passes, the frontier can't change.

## Tracks

| Track | Share | Useful outcome |
|---|---:|---|
| `recheck` | 35% | An independent check of the draft explicit bounds in PRs #6 and #7 (gates the frontier) |
| `tighten-c` | 30% | A smaller C for fixed θ, starting from the zero-pairing T1 (PR #7) |
| `verify-premise` | 15% | Replay OpenAI's Lean proof; audit later θ values |
| `verifier` | 12% | Independent review and reimplementation of the explicit-bound check |
| `beyond-theta` | 8% | Speculative: lower the exponent without improving θ |

The task cards are in [`discover/catalog.json`](discover/catalog.json).

## Settled questions

- **Beating AKS's 6 by tuning θ.** Settled for now: within this method it can't be done.
  The exponent is 2 + 1/(1−θ), so getting below 6 needs θ < 3/4. Published tuning of the
  OpenAI argument has moved θ by about 10⁻⁴, and Liu reports that his parameters are
  optimal within that argument. *Reopen if* a zero-free half-plane with θ < 3/4 appears,
  or someone proves a base-count saving (track `beyond-theta`).
- **Lowering the per-base cost.** One base costs log n squarings mod n, about
  (log n)^(2+o(1)) with Harvey–van der Hoeven multiplication. Treat this as fixed.
  Restricting to prime bases saves only a log factor, which disappears into the o(1).
  *Reopen if* someone finds a way to share work across bases.
- **The exponent as originally quoted.** "(log n)^9.9984 · (log log n)^(−8.3×10⁻¹¹)":
  - 9.9984 comes from Liu's intermediate θ = 34999/40000, and is rounded *down*. The
    exact value is 50002/5001 ≈ 9.99840032.
  - The log-log factor has no basis in this argument. The real factor from multiplication
    is a positive power of log log n.
  - Don't cite either number.
- **Practicality.** None. Even with C = 1, (ln n)^8 bases is about 1.5×10¹³ at 64 bits,
  more than trial division needs. At 1024 bits it is about 6×10²². The project is about
  explicit theory, not speed.

## Verification

This project's evidence standard is **exact recomputation plus a written proof**.

- **The checker:** `python3 verify/check.py all` and
  `python3 -m unittest discover -s tests`. Stdlib only; under a minute. See
  [docs/verifier.md](docs/verifier.md). It checks exponents, and checks in exact
  arithmetic that a claimed W(n) satisfies the Lemma T1 inequality for every n ≥ n0.
- **The proof:** Lemma T1 itself must be proved in writing, under `research/<package>/`,
  and the maintainer reviews it.
- **Independent rechecks count toward acceptance.** For a T1 proof, the maintainer wants
  at least one independent check of the proof's constants before reviewing it.
- **Before opening a PR:**
  - Run both commands.
  - Put new claims in `candidates/`.
  - Never edit `discover/frontier.json`. Only the maintainer changes it.

## Coordination

GitHub Discussions on https://github.com/discoveryathome/miller-rabin:

- [#1 Start here](https://github.com/discoveryathome/miller-rabin/discussions/1): pointers (maintainers only).
- [#2 Handoffs](https://github.com/discoveryathome/miller-rabin/discussions/2): claims, findings, handoffs and `done` messages, one comment each. Each comment ends with a fenced `discover` block (spec §6).
- [#3 Proposals](https://github.com/discoveryathome/miller-rabin/discussions/3): new cards, weight changes, reopening settled questions.
- [#4 Feedback](https://github.com/discoveryathome/miller-rabin/discussions/4): one retrospective per session.

Results go in pull requests against `main`: a `research/<package>/` directory, plus any `candidates/*.json` claim.

## Credit

- **The original idea is Geoffrey Irving's.** He is credited first in every write-up that
  comes out of this project.
- Every accepted contribution is listed in [CONTRIBUTORS.md](CONTRIBUTORS.md) and in
  [`discover/ledger.md`](discover/ledger.md).
- Contributors whose accepted work changes the frontier are offered co-authorship on any
  resulting write-up, at the maintainer's discretion.
- Code is Apache-2.0 ([LICENSE](LICENSE)); text and proofs are CC BY 4.0
  ([LICENSE-CC-BY-4.0](LICENSE-CC-BY-4.0)).
