**Original idea: Geoffrey Irving.**

# Round 2: pairing-coefficient guard recheck

Reviewed 2026-10-23 by a fresh-context, same-model AI review agent:
Codex, `gpt-6.1-sol`, max reasoning effort. This is an AI follow-up review,
not a human review, a review by a different model, or a formal certificate.

**Verdict: the round-one input-guard issue is fixed in all three checked
scripts. No required correction was found within this review's scope.**
The requested five inputs behaved correctly in each script, the new
negative-input controls detect removal of the sign check, and all three
current default command-line replays exited 0 with six rejection controls
each. The nonresidue default values and 6540-prime replay are unchanged.

## Scope and exact snapshot

This is the requested short follow-up to `RECHECK.md`. Its scope is the
`c2` guard, regression controls, actual positive default certificate
values, and nonresidue proof/code/documentation count consistency.
The complete theorems in these three packages were **not** re-reviewed.
The progression and L1 paths below are related script copies inspected
for the same guard issue; their unmerged theorems are not dependencies
of the nonresidue result. Only `constants.py` was read in the L1 research
package; its concurrently edited proof and README were not read.

Paths below are relative to the session root
`/root/.t3/scratch/2026-10-23-fetch-https-discoveryathome-org-v0-7d492a7d`.
SHA-256 hashes were computed natively and checked again after the probes:

```text
6452bd48f55645c8873166f76e2e29f437c9e03e4a85e3652bb75838368054a6  nonresidue/research/least-nonresidue/constants.py
9b7a73d98c1aab548a01b15c74d1bab747adc2f6a82275e37008022c45b53c94  repo/research/least-prime-progression/constants.py
8eeedd8a215ae689169955de1b49e3c3499ca9adfe80b24c2b07d86db888ef5c  lone/research/l-one-bounds/constants.py
84ff33b94198b224425b50892c29c0cbe0eb9f0a243982bf78ede7f6eaeb5618  nonresidue/research/least-nonresidue/RECHECK.md
d38e4d83f409b887bde410ef8037cc58397218b4f777603b041525aa645ddddd  nonresidue/research/least-nonresidue/PROOF.md
1755cd4702e3fcface0273463c004ce95f9239e1a8b396e1d8deeea48558f192  nonresidue/research/least-nonresidue/README.md
```

The executed scripts use `verify/check.py` from their own checkout. All
three copies have SHA-256
`ace2b055b5279284d04d37b6c6dde77af86088245846700c502effb3e812e709`.
The nonresidue script also uses `nonresidue/verify/mr.py`, SHA-256
`ba252ae554ac3f4ca372b692ef6ed7966772716dfa57c5b65ed22ae84fe5a1f1`.
These helper hashes identify execution inputs; this follow-up does not
claim a new review of their implementations.

## Guard and coefficient uses

The three parameterized entry points now require exactly

```python
c2 > 0 and 7 * c2 ** 2 >= 16
```

before using `c2` in a denominator envelope:

- Nonresidue: `analytic_certificate`, lines 23–39; guard at 27, subsequent
  coefficient use at 30 in `1-c2*(1/y+1/y**4) > 39/50`.
- Progression: `analytic_certificate`, lines 69–101; guard at 71,
  coefficient uses at 74 in the complex absorption denominator and at
  82 in `d_lo`. The separate `progression_certificate` fixes its own
  positive `c2=189/125` at 107 and uses it at 109; it exposes no `c2`
  argument.
- L1: `budget_certificate`, lines 73–94; guard at 74, coefficient uses
  at 80, 82 and 84 in the paired envelopes and real-B denominator.

For a real rational coefficient the conjunction is the correct test for
`c2 >= 4/sqrt(7)`: positivity selects the positive square-root branch.
The actual default is positive `189/125`, and exact arithmetic gives
`7*(189/125)**2-16 = 47/15625 > 0`. In contrast,
`7*(3/2)**2-16 = -1/4`, and zero also fails. The previously accepted
`-189/125` passes the square test but now fails positivity.

Independent calls used standard-library `Fraction`, not floating-point
comparisons. All 15 requested probes passed:

```text
c2          nonresidue analytic   progression analytic   L1 budget
189/125     accept                accept                  accept
-189/125    reject ValueError     reject ValueError       reject ValueError
0           reject ValueError     reject ValueError       reject ValueError
3/2         reject ValueError     reject ValueError       reject ValueError
1513/1000   accept                accept                  accept
```

Every rejection reported the pairing-constant guard message containing
`4/sqrt(7)`, rather than failing at an unrelated downstream check.
The larger positive value was chosen to satisfy the remaining fixed
envelopes; this does not assert that every larger positive value passes.
For it, nonresidue and L1 return the same fixed error bounds as their
defaults. Progression returns complex denominator `1008967/1638400`,
still greater than `3/5`, and the same total error bound as its default.
That denominator is expected to change with `c2`.

The first probe harness incorrectly asserted that this progression
denominator would also stay unchanged, and stopped at that assertion.
The corrected harness checked its exact expected value and completed all
15 probes and the three regression mutations successfully. This was a
review-harness expectation error, not a failure of the checked scripts.

## Regression controls and default replay evidence

Each script contains exactly six rejection controls, including one
`negative pairing constant` control with argument `-189/125`:
nonresidue lines 82–88, progression 183–190, and L1 98–105.
Direct calls to each `failure_controls()` produced exactly six
`REJECT control:` lines and no accepted bad control. Thus there are six
per script, eighteen across the three separate replays.

As a regression sensitivity check, I compiled each script into a separate
in-memory namespace after replacing only the new guard conjunction by
the former square-only condition. No file was changed. In each such
mutant, the certificate accepted `-189/125`, and the current
`failure_controls()` then raised its explicit accepted-control error
naming `negative pairing constant`. The added control therefore detects
the original bug in each copy.

The actual commands, from the session root, were:

```sh
python3 -B nonresidue/research/least-nonresidue/constants.py
python3 -B repo/research/least-prime-progression/constants.py
python3 -B lone/research/l-one-bounds/constants.py
```

All exited 0. Exact outputs relevant to this scope were:

```text
Nonresidue:
  analytic normalized error: 241522181840005231/254054780070000000
  analytic normalized margin: 12532598229994769/254054780070000000
  general coefficient: 683/1000; prime coefficient: 339/500
  direct checks: 6540 primes with 5 <= q < 65536
  largest least quadratic nonresidue: 31, last at q=31391
  six REJECT control lines
  all constants and direct checks pass

Progression (related script replay):
  complex B denominator: 1009383/1638400 > 3/5
  normalized total error: 5385194673/5600000000 < 1
  normalized margin: 214805327/5600000000
  progression coefficient: 581/1000
  refined normalized error: 114068220107243/115735200000000 < 1
  refined margin: 1666979892757/115735200000000
  finite fallback: q=3..2047; 1274560 reduced classes
  largest least prime: p=169937, q=1945, a=722
  six REJECT control lines
  all constants and finite checks pass

L1 (related script replay):
  p=2 polynomial margin: 17/7200
  common error budget: 286849/108000 < 8/3
  margin to 8/3: 1151/108000
  exponential bridge: 135/76 < 2
  six REJECT control lines
  all constants and algebraic controls pass
```

I also separately evaluated the nonresidue fixed-envelope formula using
`Fraction` with `C=339/500`, `d=39/50`, `y=7`, `t=16`,
`factor=1001/1000` and `b=231/10000`. It equals the exact default error
above and the round-one result. Calling the general coefficient
`C=683/1000` gives
`483056762993653607/511856680790000000 < 1`, also the round-one value.
These checks concern the arithmetic returned by the certificates, not
new proofs that their analytic inputs hold.

The targeted probe and mutation checks can be reproduced from the
session root without writing any file:

```python
from contextlib import redirect_stdout
from fractions import Fraction as F
from io import StringIO
from pathlib import Path
import runpy
import sys

scripts = [
    ('nonresidue/research/least-nonresidue/constants.py', 'analytic_certificate'),
    ('repo/research/least-prime-progression/constants.py', 'analytic_certificate'),
    ('lone/research/l-one-bounds/constants.py', 'budget_certificate'),
]
for path, name in scripts:
    for helper in ('check', 'mr'):
        sys.modules.pop(helper, None)  # use this checkout's helper imports
    m = runpy.run_path(path, run_name='guard_review')
    default = m[name]()
    for c2 in (F(189, 125), F(1513, 1000)):
        actual = m[name](c2=c2)
        if path.startswith('repo/') and c2 == F(1513, 1000):
            assert actual == (F(1008967, 1638400), default[1])
            assert actual[0] > F(3, 5)
        else:
            assert actual == default
    for c2 in (-F(189, 125), F(0), F(3, 2)):
        try:
            m[name](c2=c2)
        except ValueError as error:
            assert '4/sqrt(7)' in str(error)
        else:
            raise AssertionError(('bad c2 accepted', path, c2))
    output = StringIO()
    with redirect_stdout(output):
        m['failure_controls']()
    lines = output.getvalue().splitlines()
    assert len(lines) == 6
    assert all(line.startswith('REJECT control: ') for line in lines)
    assert sum('negative pairing constant' in line for line in lines) == 1
    old = Path(path).read_text().replace(
        'c2 > 0 and 7 * c2 ** 2 >= 16', '7 * c2 ** 2 >= 16')
    mutant = {'__file__': str(Path(path).resolve()), '__name__': 'guard_mutant'}
    exec(compile(old, path, 'exec'), mutant)
    mutant[name](c2=-F(189, 125))  # old guard incorrectly accepts this
    with redirect_stdout(StringIO()):
        try:
            mutant['failure_controls']()
        except ValueError as error:
            assert 'negative pairing constant' in str(error)
        else:
            raise AssertionError(('regression undetected', path))
print('all 15 probes and 3 regression mutations pass')
```

## Round-one byte comparison and documentation consistency

The previous report records a SHA-256 for the original nonresidue script.
In memory, removing only `c2 > 0 and ` from the new guard and deleting
the single new negative-control list entry restores exactly
`bdd6d2cc5dc43cd2eab1f04c3ec840203d7a1f31e80edebe27ea06e7048e4982`,
the round-one hash. This confirms that no positive formula, theorem
constant, or other checker code changed in that script.

Changing `six` back to `five` in the current nonresidue README restores
exactly its recorded round-one hash
`ba7c8447b6a9818085f6e3036906f7b41c1d7c8141073fb450a3fd46b2cca8ce`.
For `PROOF.md`, the complete byte delta additionally clarifies the
guard's positivity: changing `six` to `five` and
`also test positivity of the pairing` to `also test the pairing` restores
exactly its round-one hash
`dec8f433d1f4337bcd7f955810bdd305a93bcc8582ffdda31bf53455e6b5e5be`.
Thus the proof change includes that explanatory wording as well as the
count, with no change to its mathematical inequalities or constants.

Current `PROOF.md` lines 213–215 and 228–229 and `README.md` line 18
all say six rejection controls, agreeing with code and execution.
The current proof's `c2=189/125` and its 6540-prime count also agree
with the default replay. The five-control statements in `RECHECK.md`
describe its explicitly hashed earlier snapshot and remain historical
evidence; that report was not edited. No historical byte comparison of
the two related scripts is claimed because this brief supplies no
round-one hashes for them.

## Limits and actions

The round-one mathematical review is prior evidence, not work repeated
here. In particular this follow-up does not independently certify the
three full theorems, H(7/8), Lean/kernel inputs, L-function theory,
contour inputs, accepted pairing estimates, or source provenance.
It does not establish correctness for arbitrary parameter types or
every possible change of a positive coefficient. The finite default
replays are execution regressions, not independent proofs of their
unbounded mathematical claims.

Work stayed within the requested ten-minute bound. Execution used
sandboxed native `python3 -B` with no bytecode writes. No network calls,
further agents, git mutations, public writes, script edits, or edits to
existing reports were made. The only created file is this report.
