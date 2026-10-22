Original idea: **Geoffrey Irving**. Attribution added by the parent; the review below is the fresh-context reviewer's report.

# Reference implementation: fresh-context AI recheck, round 1

What this change does: it adds a standard-library Miller–Rabin implementation of the accepted witness bound, with an unconditional small-input branch and an H(7/8)-conditional large-input branch. A caller can impose a base budget, whose exhaustion produces an inconclusive result.

**Verdict: no actionable runtime or test defects found in the bounded scope below.** This is a same-model, fresh-context AI recheck, not an independent human check or maintainer acceptance. The reviewer was a separate review context using GPT-6 Astra, with the implementation brief and repository sources but no parent reasoning transcript. No further agents were spawned. The parent remains responsible for publication, the complete test/checker run, and acceptance claims.

## Scope and identity

- Review date: 2026-10-22 UTC.
- Repository: `/root/projects/discoveryathome/donation-20261022T173844Z/round-2/repo`.
- Base and observed HEAD: `d2bd5167a42b8256f1362640dc149057920e5db9`.
- Branch: `session/9be1ae01-miller-rabin`.
- Round seed: `9be1ae0151a3cb6841bc60daaa5bc4fb`.
- Task: `reference-implementation` in `discover/catalog.json`.
- Main review: `impl/deterministic_mr.py`, `impl/__init__.py`, and `tests/test_deterministic_mr.py`, including their existing `verify.check` and `verify.mr` dependencies.
- Read `AGENTS.md`, the task card, `DISCOVERY.md`, the accepted frontier statement, and the relevant statement/handoff in `research/zero-pairing/PROOF.md`. The analytic proof itself was not re-proved.
- Python: CPython 3.13.5. Checks used only the standard library, with `-B` or `sys.dont_write_bytecode = True` to avoid writing bytecode.

The test file changed during the review to import `impl.base_counts` and add a prime-count-interval test. I reviewed that updated source and reran all its non-exhaustive tests. The runtime sources stayed unchanged. I inspected the new helper for integration and ran its added test; the README, generated base-count report, and the external prime-count theorem are outside this runtime recheck's conclusion.

This reviewer made no repository edits, commits, posts, or changes to accepted records. The only authored file is this report, outside `repo`. The parent staged the new files during the review; that staging was not performed by this reviewer.

## Standards

No actionable violations found. Runtime imports use the standard library and existing verifier helpers. Existing verifier, frontier, catalog, research, `AGENTS.md`, and `DISCOVERY.md` files were unchanged against the stated base. The public function docstring states that a large-input `True` assumes H(7/8), that `False` does not need the hypothesis, and that large prime inputs are impractical. CLI success for a large prime explicitly prints the conditional label.

## Specification and correctness

No actionable deviations found in the reviewed runtime and tests.

1. **Strict cutoff.** `witness_bound` and `is_prime` use `n < PSI_13`, not `<=`. Below the cutoff, the sequence is exactly the existing first 13 primes, ending at 41. Bases at least `n` are skipped for very small inputs; this is safe because every composite has a proper prime divisor below `n`, which is a strong witness. Negative integers, zero, one, two, and even integers are handled before the witness loop.
2. **PSI_13 itself.** The actual input `3317044064679887385961981` passes the first 13 bases, raises `BaseLimitExceeded` at budget 13, and is rejected at base 43 with budget 14. The strict cutoff agrees with the definition and Theorem 1.1 of [Sorenson–Webster, arXiv:1509.00864v1](https://arxiv.org/pdf/1509.00864): PSI_12 and PSI_13 are the smallest strong pseudoprimes to the corresponding initial prime bases. The numerical constants match the theorem.
3. **Upward bound.** The existing `ln_bounds` writes `n = 2^k y`, where `1 <= y < 2`, and encloses the nonnegative atanh series using its positive geometric tail. Its returned upper rational `U` therefore satisfies `ln(n) <= U`. For large inputs, positive monotonicity gives `(529 ln(n)/1000)^8 <= (529 U/1000)^8 = A/B`. The expression `-(-A // B)` is exactly `ceil(A/B)`. There is no floating-point operation in this path. The extra maximum with 41 cannot lower the bound. Independent exact inequalities and 100-digit Decimal corroboration passed at the cutoff and 128-/1024-bit examples; Decimal was not used as the proof of safety.
4. **Sieve completeness.** The first segment is contained in `[2, 3]` and has no composite. Every subsequent segment starts at `low >= 4` and ends at `high <= 2*low - 1 < low^2`. A composite in that segment has a prime divisor at most `sqrt(high) < low`, already encountered and retained, since it is also at most `sqrt(limit)`. Marking starts at the first multiple in the segment, or `p*p` if larger. Thus every composite is marked and no prime is removed. `while low <= limit` and an inclusive `high` include a prime equal to the final limit. A short final segment can give zero multiples for a cached prime; the slice assignment then has length zero and is harmless.
5. **Budget and completion.** The budget is checked before each actual witness test. Exhaustion raises an exception; passing a prefix never becomes a prime answer. A witness on the last permitted base is still tested. A budget exactly equal to the number of necessary bases allows a completed scan to return. The generator can produce one additional candidate to discover that a budget is exhausted; it never applies that extra witness test.
6. **Coverage.** The test source includes `range(1_000_000)` compared directly with `is_prime_trial`, plus all 13 psi-table rows. I deliberately did not duplicate the million-input primality run assigned to the parent. I did run the remaining tests, including the psi table, and independent checks described below.
7. **Memory.** Each segment is at most 32,768 bytes. Cached primes grow with the consumed prefix, up to primes through `isqrt(limit)`; this is lazy, not constant total space. Full large-prime scans remain impractical. Consuming 10,000 primes from limits `633346037751` and `10**100` used approximately 442 KB of traced Python allocations in each case, rather than allocating to either final limit. The measurement excludes interpreter overhead and is not a full-scan memory guarantee.

## Commands and observed results

All commands and Python probes were run with the repository above explicitly selected. Python probes ran in the context-mode sandbox with this bootstrap; the listings below are reproducible as a `python3 -B -` heredoc with the same bootstrap:

```python
import os, sys
root = '/root/projects/discoveryathome/donation-20261022T173844Z/round-2/repo'
os.chdir(root)
sys.path.insert(0, root)
sys.dont_write_bytecode = True
```

Repository commands:

```sh
git rev-parse HEAD
git branch --show-current
GIT_OPTIONAL_LOCKS=0 git status --short
git diff --exit-code d2bd5167a42b8256f1362640dc149057920e5db9 -- verify discover research AGENTS.md DISCOVERY.md
```

The first two returned the base and branch above. The last command returned exit 0 with no diff. The final observed status contained only the parent's six staged additions: the runtime, package initializer, README, two base-count files, and test file.

### Focused authored tests

Executed after reviewing the updated test-file hash:

```python
import unittest
suite = unittest.defaultTestLoader.discover('tests', pattern='test_deterministic_mr.py')
def selected(tests):
    for test in tests:
        if isinstance(test, unittest.TestSuite):
            yield from selected(test)
        elif not test.id().endswith('test_exhaustive_below_one_million'):
            yield test
result = unittest.TextTestRunner(stream=sys.stdout, verbosity=1).run(
    unittest.TestSuite(selected(suite)))
assert result.wasSuccessful()
```

Result: **12 tests passed, 1.903 seconds**, including the added base-count-interval test. The complete current file contains 13 test methods; the one excluded method is the exhaustive million-input check.

### Independent sieve probe

```python
import bisect, math, random
from impl import deterministic_mr as impl
N = 1_100_000
flags = bytearray(b'\x01') * (N + 1)
flags[:2] = b'\x00\x00'
for p in range(2, math.isqrt(N) + 1):
    if flags[p]:
        flags[p*p::p] = b'\x00' * ((N - p*p) // p + 1)
expected = [n for n in range(N + 1) if flags[n]]
limits = {-9, -1, 0, 1, 2, 3}
limits.update(2**k + d for k in range(2, 18) for d in (-1, 0, 1))
limits.update(65536 + 32768*j + d
              for j in (1, 2, 3, 7, 15, 31) for d in (-1, 0, 1))
limits.update(p*p + d for p in (257, 263, 509, 997) for d in (-1, 0, 1))
rng = random.Random(int('9be1ae0151a3cb6841bc60daaa5bc4fb', 16))
limits.update(rng.sample(expected, 12))
limits.add(N)
for limit in sorted(limits):
    got = list(impl.primes_up_to(limit))
    assert got == expected[:bisect.bisect_right(expected, limit)], limit
    assert len(got) == len(set(got)), limit
```

Result: **93 limits passed, 2.347 seconds**. The independent dense sieve found 85,714 primes through 1,100,000, ending at 1,099,997. Cases covered growing-segment transitions, transitions after the segment-size cap, prime squares, zero-length marking slices, and prime-valued final limits.

### Exact-bound and last-base probes

```python
from decimal import Decimal, localcontext
from fractions import Fraction
from unittest.mock import patch
from verify.mr import PSI_13, FIRST_13_PRIMES, is_prime_trial
from impl import deterministic_mr as impl
import math
for n in (PSI_13 - 1, PSI_13, PSI_13 + 2, 2**128 - 1, 2**1024 - 1):
    bound = impl.witness_bound(n)
    if n < PSI_13:
        assert bound == 41
        continue
    lo, hi = impl.ln_bounds(n)
    exact = (Fraction(529, 1000) * hi)**8
    assert bound * exact.denominator >= exact.numerator > (bound - 1) * exact.denominator
    with localcontext() as ctx:
        ctx.prec = 100
        log = Decimal(n).ln()
        assert Decimal(lo.numerator)/lo.denominator < log < Decimal(hi.numerator)/hi.denominator
        assert Decimal(bound - 1) < (Decimal(529)/1000 * log)**8 < Decimal(bound)
for target in (Fraction(2000, 529), Fraction(2001, 529)):
    with patch.object(impl, 'ln_bounds', return_value=(Fraction(0), target)):
        assert impl.witness_bound(PSI_13) == math.ceil((Fraction(529, 1000) * target)**8)
for limit in (2, 3, 4, 41, 43, 65536, 65537, 98303, 98304, 98317):
    expected = [p for p in range(2, limit + 1) if is_prime_trial(p)]
    seen = []
    def witness(p, n):
        seen.append(p)
        return p == expected[-1]
    with patch.object(impl, 'witness_bound', return_value=limit), \
            patch.object(impl, 'is_witness', side_effect=witness):
        assert impl.is_prime(PSI_13, max_bases=len(expected)) is False
        assert seen == expected
        seen.clear()
        try:
            impl.is_prime(PSI_13, max_bases=len(expected) - 1)
        except impl.BaseLimitExceeded:
            pass
        else:
            raise AssertionError(('cap bypass', limit))
        assert seen == expected[:-1]
    with patch.object(impl, 'witness_bound', return_value=limit), \
            patch.object(impl, 'is_witness', return_value=False) as check:
        assert impl.is_prime(PSI_13, max_bases=len(expected)) is True
        assert check.call_count == len(expected)
seen = []
with patch.object(impl, 'primes_up_to', side_effect=AssertionError('cutoff entered sieve')), \
        patch.object(impl, 'is_witness', side_effect=lambda p, n: seen.append(p) or False):
    assert impl.is_prime(PSI_13 - 2, max_bases=13) is True
    assert seen == list(FIRST_13_PRIMES)
assert impl.is_prime(PSI_13, max_bases=14) is False
try:
    impl.is_prime(PSI_13, max_bases=13)
except impl.BaseLimitExceeded:
    pass
else:
    raise AssertionError('PSI_13 cap misclassified')
```

Result: **all passed, 4.838 seconds**. Observed bounds were 41 below the cutoff, `633346037751` at the cutoff and cutoff + 2, `23546633375396` at `2**128 - 1`, and `395046954211813343884` at `2**1024 - 1`. Ten synthetic limits each passed three completion/budget modes. The mocks test control flow only; mocked `True` results are not primality evidence.

### CLI subprocesses and lazy memory

The following argument lists were each passed to `[sys.executable, '-B', '-m', 'impl.deterministic_mr', *args]` using `subprocess.run(..., cwd=root, capture_output=True, text=True, timeout=10)`:

```text
0                                         => exit 0, not prime
-7                                        => exit 0, not prime
2 --max-bases 0                            => exit 0, prime
43 --max-bases 12                          => exit 2, inconclusive
43 --max-bases 13                          => exit 0, prime
3317044064679887385961981 --max-bases 13    => exit 2, inconclusive
3317044064679887385961981 --max-bases 14    => exit 0, composite
3317044064679887385961981 --unlimited      => exit 0, composite
170141183460469231731687303715884105727     => exit 2, inconclusive after 10000 prime bases
9 --max-bases 0                            => exit 2, inconclusive
43 --max-bases -1                          => exit 2, must be nonnegative
hello                                     => exit 2, invalid int value
```

All 12 subprocess return-code and message assertions passed. The authored mocked-prime CLI test also verifies the `conditional on H(7/8)` output label.

```python
import tracemalloc
from itertools import islice
from impl import deterministic_mr as impl
for limit in (633346037751, 10**100):
    tracemalloc.start()
    g = impl.primes_up_to(limit)
    for base in islice(g, 10000):
        pass
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    state = g.gi_frame.f_locals
    assert base == 104729 and len(state['primes']) == 10000
    assert len(state['segment']) <= 32768
    print(limit, peak, len(state['segment']))
    g.close()
```

Observed traced peaks: **442,204 bytes** and **442,228 bytes**, respectively; the active segment was 32,768 bytes in both cases. The measured prefixes took 0.345 and 0.310 seconds. Allocation counts and timings are environment-specific.

## Source hashes

SHA-256 of the reviewed local bytes, paths relative to `repo`:

```text
7ff09121134c8b70b04fc891ca3b27b92771e786604bce94788a0e3b7e6fcbe6  impl/deterministic_mr.py
7bb58865a298496e1504863f4021fd1fb49e06d95a15e98268e2065bc8b11383  impl/__init__.py
0f3dfd888f03efd19846e3abd1a561ca732b063daf01f05a54318eff3fdc9d00  tests/test_deterministic_mr.py
a5b856376ae7edd040110385a98379e116a3cc4b49b3ab77fcf3c9755c3b273d  impl/base_counts.py
e8f93ce38983d792791c3f9ad9b8b0a367668b3b7b945b071b6f360c45babd62  AGENTS.md
e603c2aaf4b9c692b315213f6c7dd5aebdfba5932e67155e53c76a6590ec4ddf  DISCOVERY.md
21215199c05c883d31f61d2969f086d7293377cdfa988944b62b8f140451b5a7  discover/catalog.json
9ca629138c133ac8547efba9b47f4d862ae82e7079c4da0998961d8fa5c964a4  discover/frontier.json
ace2b055b5279284d04d37b6c6dde77af86088245846700c502effb3e812e709  verify/check.py
ba252ae554ac3f4ca372b692ef6ed7966772716dfa57c5b65ed22ae84fe5a1f1  verify/mr.py
824af09db62887a04107e72f9aafb56345aef45c1ea3ccf6499956d6896e914c  research/zero-pairing/PROOF.md
```

The test file initially had hash `3d0324e8105a7f61e199b648f29129e7fa1e1dfcee0ad89c577d6e701841d66d`. The final tests result above applies to the updated hash in the manifest. Hashes were computed with `hashlib.sha256(Path(path).read_bytes()).hexdigest()`; the runtime hashes remained identical across the review.

## Limitations and handoff

- No exhaustive primality run over `[0, 10**6)` was performed by this reviewer; the test is present and the parent was assigned that run. The previous 16-test baseline passing is information supplied in the brief, not a fresh reviewer result.
- `python3 verify/check.py all` was not rerun here. The accepted verifier and frontier were confirmed unchanged; the parent must supply the full required verification evidence.
- No full scan of the accepted large-input bound for an actual large prime was attempted. Large-input completion was checked with controlled small bounds; actual PSI_13 rejection and budget exhaustion were checked without mocks.
- Memory measurements cover consumed prefixes and Python allocations, not total process RSS or completion at a 1024-bit witness limit. Full storage can reach the primes through `sqrt(limit)`.
- H(7/8), the analytic T1 proof, and the original exhaustive Sorenson–Webster computation were not re-established. The cited theorem's statement and constants were checked against its primary PDF.
- The auxiliary base-count helper was inspected and its small count-interval test passed, but this report does not certify the README, generated count report, or its external analytic estimates.
- Context-mode web fetching failed with `Cannot find module 'turndown'`; the cited arXiv abstract and PDF were successfully read with the web tool instead. This did not limit the runtime checks.

Standards: zero actionable findings. Specification/runtime: zero actionable findings within the stated scope. This evidence is suitable for the parent to attach as a fresh-context AI recheck; it does not confer maintainer acceptance.
