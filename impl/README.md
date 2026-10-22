# A reference implementation of the accepted test

**Original idea: Geoffrey Irving.** This implementation was developed by an AI
agent during a Discovery@Home donation. It implements the existing accepted
bound at base commit `d2bd5167a42b8256f1362640dc149057920e5db9`; it does not change
the theorem, verifier, frontier, or its assumptions.

For integers below `PSI_13 = 3317044064679887385961981`, testing the first 13 prime
bases is deterministic without H(7/8). At and above that cutoff, a complete scan
through the accepted witness bound gives a deterministic primality conclusion
**conditional on H(7/8)**. Finding a strong witness proves compositeness without
that hypothesis. The accepted result and the current status of its assumptions
are in [discover/frontier.json](../discover/frontier.json).

## Run

Python 3.9+; standard library only. From the repository root:

```sh
python3 -m impl.deterministic_mr 2305843009213693951
# prime
python3 -m impl.deterministic_mr 3317044064679887385961981
# composite (base 43 is a witness)
python3 -m impl.deterministic_mr 3317044064679887385961981 --max-bases 13
# inconclusive after 13 prime bases; no primality conclusion (exit status 2)
```

The CLI defaults to at most 10,000 tested bases. `--max-bases N` changes that work
limit; `--unlimited` requests the entire theoretical scan. A completed decision
exits with status 0, so read its output to distinguish prime from composite.
Zero, one and negative integers are reported as not prime. The CLI prints
`prime (conditional on H(7/8))` for a successful large-input scan.

The Python API is `impl.deterministic_mr.is_prime(n, max_bases=None)`: it returns a
boolean after a complete decision, or raises `BaseLimitExceeded` if a supplied
base limit prevents completion. Its uncapped default is the mathematical
reference algorithm and can take impractically long on large primes. The helper
`witness_bound(n)` reports an integer limit without scanning it.

## Why the limit cannot round down

The existing [verify/check.py](../verify/check.py) encloses `ln(n)` in exact
fractions `[L,U]`. It uses `n=2^k y`, `1<=y<2`, and the positive power series
for `atanh`, with a rational bound on its remaining tail. For `n>=PSI_13`,
`witness_bound` computes

`B = max(41, ceil(((529/1000) * U)^8))`.

All arithmetic is `fractions.Fraction` or integer arithmetic. Since `U>=ln(n)>=0`,
the positive multiplier and eighth power preserve the inequality; the integer
ceiling cannot decrease it. Thus every prime at most `(0.529 ln n)^8` is included.
No float, decimal logarithm, or float-to-int conversion enters this bound.

The shortcut uses **strictly** `n<PSI_13`. At equality the first 13 bases all pass,
so applying the shortcut there would be wrong. The [Sorenson–Webster primary
paper](https://arxiv.org/abs/1509.00864), Theorem 1.1, supplies `psi_12` and
`psi_13`; the project's accepted proof supplies the conditional large-input
bound. The implementation reuses [verify/mr.py](../verify/mr.py) for exact
modular witness tests rather than duplicating them.

## Prime generation and scale

The incremental segmented sieve yields every prime through `B`, including `B`
when it is prime. Its first segment is `[2,3]`. Subsequently a segment starting
at `low` ends no later than `2*low-1`, whose square root is below `low`. All primes
needed to strike that segment were therefore discovered earlier. Multiples are
struck from `max(p*p, ceil(low/p)*p)`. Every composite has a prime factor at most
the square root of the segment's end, so no composite survives; genuine primes
are never struck. Segments stop at `B` and have at most 32,768 bytes.

Sieving primes are retained only through `isqrt(B)` and discovered as iteration
advances. The generator does not preallocate a `B`-sized table or enumerate all
primes through `sqrt(B)` before trying the first witness. Its eventual prime
cache can still be enormous; segmentation does not make a full large scan
practical.

The following are budgets at `n=2^bits-1`, before an early witness. The reported
`B` is a safe cap for every input of that bit size; the count intervals describe
`pi(B)` at that largest-size budget, not a lower bound on work for every smaller
input. They are not elapsed-time claims or exact prime counts for the large cases.

| Bits | Inclusive prime-base limit B | Full base-count budget |
| ---: | ---: | ---: |
| 64 | 41 | 13 (exact) |
| 128 | 23,546,633,375,396 | 764,749,280,272 to 959,806,231,697 |
| 1024 | 395,046,954,211,813,343,884 | 8,329,836,307,735,353,089 to 10,454,444,356,386,332,247 |

The large intervals use the unconditional inequalities
`x/ln(x) < pi(x) < 1.25506*x/ln(x)` for `x>=17`, from Rosser–Schoenfeld,
[*Approximate formulas for some functions of prime numbers*](https://doi.org/10.1215/ijm/1255631807),
p. 69, Corollary 1, equations (3.5)–(3.6)
([full paper](https://denisevellachemla.eu/Rosser-Schoenfeld-1962.pdf)).
The report again encloses the logarithm rationally, uses the upper logarithm for
the lower count and the lower logarithm for the upper count, then rounds the
strict inequalities in the safe integer directions. Reproduce
[base-counts.json](base-counts.json) with `python3 -m impl.base_counts`.

These budgets make the accepted test a useful exact reference and a feasible
small-input test. This implementation makes no claim to achieve the theorem's
asymptotic bit-complexity model using Python's actual arithmetic implementation.

## Validation and open next questions

```sh
python3 -m unittest discover -s tests
python3 verify/check.py all
python3 research/zero-pairing/constants.py
```

Tests cover every integer `0<=n<1,000,000` against the project's independent
trial-division routine, strong pseudoprime regressions through `psi_13`, the
strict cutoff, exact/inexact ceiling cases, segment endpoints, an enormous lazy
sieve bound, limited scans, and CLI labels. The large branch is also exercised
to full exhaustion with a small controlled bound; all the real `psi_13` bases
through its first witness are tested. The optional base limit cannot be mistaken
for a passed primality test.

No complete scan of a real prime at or above `psi_13` was attempted. The finite
tests and code argument do not establish H(7/8), replay its Lean proof, or replace
the published small-input theorem. A [fresh-context AI recheck](recheck-round-1.md)
found no actionable defects in its stated scope, including the rounding direction,
sieve invariant and incomplete-scan behavior. Its source hashes and limitations
are recorded in the report; maintainer acceptance is separate.

A separate bounded diagnostic on `2^127-1` reached the default 10,000-base cap
and correctly returned inconclusive. On the author's Python 3.13.5 environment it
took about 7.15 seconds with `tracemalloc` enabled and peaked at 443,270 bytes of
Python-tracked allocations (not process RSS). This checks early-run allocation
behavior; it is not a controlled performance benchmark or a primality conclusion.

The next useful review is to check the upward-rounding argument and the sieve
invariant against the exact PR head, and rerun the tests. Any future faster
implementation must retain explicit inconclusive results for incomplete scans
and the hypothesis label for large-input primality conclusions.
