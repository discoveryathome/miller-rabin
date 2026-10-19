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
