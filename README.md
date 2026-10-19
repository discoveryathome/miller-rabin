# Explicit deterministic Miller–Rabin under the quasi-Riemann hypothesis

**Original idea: Geoffrey Irving.** Maintainer of record: Douglas R. Colkitt.

## The question

OpenAI's unreviewed quasi-Riemann preprint (2026-09-30) claims that no Dirichlet
L-function has a zero with Re s > 7/8. If that holds, Miller–Rabin becomes deterministic
and polynomial-time: some prime base below

  **W(n) = (C·ln n + D)^(1/(1−θ))**

is always a witness, with θ = 7/8 or slightly less. The running time is
(log n)^(2 + 1/(1−θ) + o(1)).

| Zero-free line θ | Running-time exponent |
|---|---|
| 7/8 | 10 |
| 0.8748867 (Xu–Sang, best published) | ≈ 9.9928 |

**Nobody has written down an explicit C**, so the algorithm doesn't know where to stop.
This project makes C explicit and rigorous, then makes it as small as possible.

## What's known

- **Accepted result:** assuming H(7/8), every odd composite n has a prime Miller–Rabin
  witness p ≤ max(41, (0.529·ln n)^8). The proof is
  [research/zero-pairing/PROOF.md](research/zero-pairing/PROOF.md), and the claim is
  [`discover/frontier.json`](discover/frontier.json).
- **The exponent depends only on θ.** Getting below the 6 of Lenstra–Pomerance AKS would
  need θ < 3/4, which would be new mathematics, not tuning. Under GRH (θ = 1/2), Bach's
  bound 2(ln n)² gives an exponent of 4.

## Sources

- OpenAI, *The Quasi-Riemann Hypothesis: A Zero-Free Half-Plane Re(s) > 7/8* (2026),
  https://github.com/openai/math. Not refereed.
- B. Liu, arXiv:2610.12234.
- Y. Xu and H. Sang, arXiv:2610.15291.
- E. Bach, *Explicit bounds for primality testing and related problems*, Math. Comp. 55
  (1990) 355–380.
- J. Sorenson and J. Webster, *Strong pseudoprimes to twelve prime bases*, Math. Comp. 86
  (2017) 985–1003.

## Run the check

You need Python 3.9 or later; it uses only the standard library and takes under a minute.

```sh
python3 verify/check.py all
python3 -m unittest discover -s tests
```

[docs/verifier.md](docs/verifier.md) describes the claim formats.
[docs/template-T1.md](docs/template-T1.md) states the hypothesis, the lemma to prove, and
exactly what the checker establishes.

## Contributing

Agents start at [AGENTS.md](AGENTS.md); humans start at [DISCOVERY.md](DISCOVERY.md).

## License

Code is Apache-2.0 ([LICENSE](LICENSE)). Text and proofs are CC BY 4.0
([LICENSE-CC-BY-4.0](LICENSE-CC-BY-4.0)).
