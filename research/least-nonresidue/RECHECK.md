**Original idea: Geoffrey Irving.**

# Independent mathematical recheck: least nonresidues

Reviewed 2026-10-23 by a fresh-context Codex review agent, using the same
model family as the author. This is an independent AI recheck, not a human
review or a formal proof certificate. Requested author claim: `19141348`;
track: `corollaries` / `least-nonresidue`; original seed:
`f7e9c53c773500cea50225ca67a35d17`.

**Verdict: the stated conditional mathematical claims check out for the
snapshot below. No fatal issue or required theorem correction was found.**
There is one nonblocking parameter-guard issue in the checker, described
below; it does not affect its actual positive constants or default run.
The complete small-modulus argument works for every proper subgroup,
including composite moduli. It does not depend on enumerating prime moduli.

The review read `AGENTS.md`, `DISCOVERY.md`, the three new package files,
the accepted first-T1 and zero-pairing proofs, the two imported helper
implementations, and `discover/frontier.json`. It also consulted
[LLS arXiv:1309.3595v3](https://arxiv.org/pdf/1309.3595v3), Lemmas 2.1--2.3,
Lemma 3.1 and Section 3, including the residue identities preceding the
GRH estimates. No PR #11 theorem, review, or unmerged sibling result was
used as evidence for this package.

## Snapshot and scope

The worktree is `nonresidue/`, branch `session/20261023-nonresidue`.
Both its HEAD and the named upstream base were
`d2bd5167a42b8256f1362640dc149057920e5db9`. The package was uncommitted.
SHA-256 digests of the reviewed bytes were:

```text
dec8f433d1f4337bcd7f955810bdd305a93bcc8582ffdda31bf53455e6b5e5be  research/least-nonresidue/PROOF.md
ba7c8447b6a9818085f6e3036906f7b41c1d7c8141073fb450a3fd46b2cca8ce  research/least-nonresidue/README.md
bdd6d2cc5dc43cd2eab1f04c3ec840203d7a1f31e80edebe27ea06e7048e4982  research/least-nonresidue/constants.py
824af09db62887a04107e72f9aafb56345aef45c1ea3ccf6499956d6896e914c  research/zero-pairing/PROOF.md
abd066b2d27961e93ae007e5fb8897b5a841aff875b24af3eb0216d73bed8cbb  research/first-explicit-t1/PROOF.md
ace2b055b5279284d04d37b6c6dde77af86088245846700c502effb3e812e709  verify/check.py
ba252ae554ac3f4ca372b692ef6ed7966772716dfa57c5b65ed22ae84fe5a1f1  verify/mr.py
9ca629138c133ac8547efba9b47f4d862ae82e7079c4da0998961d8fa5c964a4  discover/frontier.json
```

The accepted proof/helper digests match the frontier record. Its accepted
status resolves the older draft labels still present in those proof files.
The three new-file digests were checked again before this report was written.

The precise mathematical domains confirmed are:

- Assuming H(7/8), for every integer `q >= 5` and every proper subgroup of
  `(Z/qZ)*`, the least prime coprime to `q` outside the subgroup is strictly
  below `(0.683 log q)^8`.
- The coefficient `0.678` works on that same domain with `q = 6` excluded.
  At `q = 6` the prime is exactly 5. At `q = 3,4` the exact primes are 2,3;
  neither logarithmic bound is being asserted there.
- For every prime `q >= 5`, the least positive quadratic nonresidue is a
  prime and is strictly below `(0.678 log q)^8`.
- For positive coefficients, `0.682` and smaller fail the first uniform
  domain at `q = 6`; `0.677` and smaller fail the prime quadratic domain at
  `q = 5`. These are obstructions, not proofs of optimality.

## Mathematical checks

**Subgroup reduction and complex characters.** A nontrivial character of
the nontrivial finite abelian quotient `G/H` pulls back to a nonprincipal
Dirichlet character trivial on `H`. Assuming all coprime primes up to `X`
lie in `H` gives `chi(n) = 1` for the units `n <= X`, and zero on nonunits.
Thus the imprimitive `S_chi` equals the principal sum and `T_chi >= 0`.
This does not assert that the inducing primitive character is 1 at primes
dividing `q`.

For a complex primitive character the functional equation and conjugation
give the same-character involution `rho -> 1-conjugate(rho)`.
Also `Re B(conjugate(chi*)) = Re B(chi*)`. Consequently all uses of the
paired bounds and `A = -Re B = sum Re(1/rho) >= 0` are legitimate.
Only real parts of the primitive sums are needed; no estimate for the full
complex value of `B` has been silently substituted.

**Both S corrections.** Write `a = log p`, `t = log X` and
`m = floor(t/a)`. The nonnegative prime-power weight is

```text
sum_{k=1}^m a(t-ka) = a*m*t - a^2*m*(m+1)/2 <= t^2/2,
t^2/2 - sum = ((t-m*a)^2 + m*a^2)/2 >= 0.
```

The principal correction therefore costs at most `omega(q)t^2/2`.
The primitive/imprimitive difference costs at most `omega(q/f)t^2/2`.
Since `omega(q/f) <= omega(q)`, (4) correctly charges their sum as
`omega(q)t^2`. There is no missing factor 2. The direct derivation also
covers `q/f = 1,2`, even though LLS states Lemma 3.1 for `m >= 3`.

**T correction and the conductor-3 case.** For each missing prime,
`1-p^k/X <= 1-1/X` on the supported terms, and the geometric series gives
the asserted `(1-1/X) log p/(p-1)` bound. Thus

```text
Re T_chi* >= -(1-1/X) U(r),                 r = q/f,
d*A <= (1/2)(1-1/X)[log(f/pi)+2U(r)].
```

Primes dividing both `r` and `f` do not contribute to the actual
difference; including them in `U(r)` only increases the upper bound.
Independently,

```text
log f + 2U(r) - log q
 = 2U(r) - log r
 <= sum_{p|r} (2/(p-1)-1) log p <= log 2.
```

Higher exponents in `r` strengthen this inequality. The terms for primes
2,3 and larger are respectively `log 2`, zero, and nonpositive. Since
`2 < pi`, the bracket is below `L = log q`. Multiplication by the positive
`1-1/X`, followed by `(1-1/X)L < L`, proves (5) without assuming the
bracket or `log(f/pi)` is positive. In particular `f = 3` is covered.

**Residue signs, gamma terms and the full criterion.** The primitive
S identity contributes `-Re B*t = A*t`; its constant zero sum costs
`8A`. The zeta constant zero sum costs `8b`. These are precisely the
`+8` inside `F`. In the T identity the real part of
`-B(conjugate(chi*)) - B(chi*)/X` is `(1+1/X)A`; subtracting the possible
zero error gives `d*A` on the left, with `-Re T` on the right.
These signs agree with the identities in LLS and the accepted replacements.

Dropping all four real gamma functions has the correct direction.
As a separate elementary check of their displayed formulas, for `X >= 64`,
use the classical bounds `pi < 22/7`, `gamma > 1/2` and `2/3 < log 2 < 1`.
Drop the negative series and use monotonicity of `(log X+1)/X`, `1/X`
and `1-1/X`. Upper bounds for `Etilde_0, Etilde_1, E_0, E_1` are then
respectively

```text
-2231/294,  -421/294,  -107/192,  -59/256,
```

all negative. Combining the two S estimates leaves exactly

```text
X <= F*[b+L/(2d)] + [L/(2d)+L/2+2]*t + 1 + omega(q)*t^2.
```

Here `log(f/pi) <= L` and `log(2pi) < 2` were used with positive `t`.
Division by `X` reproduces (6), including every logarithmic, constant and
missing-prime term. No LLS Lemma 2.4 estimate for the principal T sum is
needed or imported from GRH.

**Continuum envelope, strictness and dependence on C.** With `X=y^8`,
`C=339/500` and `y >= 7`, exact arithmetic gives

```text
1-c2*(1/7+1/7^4) = 33587/42875,
33587/42875 - 39/50 = 289/85750 > 0,
1+7/7^6+8/7^7 = 823600/823543 < 1001/1000,
7*(189/125)^2 - 16 = 47/15625 > 0.
```

The first bound drops the positive `1/X` and holds uniformly as `y`
increases. The second factor decreases as `y` increases. The cutoff
`q >= 65536` gives `y > 904/125 > 7`, and
`2^omega(q) <= q` gives `omega(q) < 2L`.

Every residual term is a positive multiple of `log(y)^m/y^a` with
`a >= 7` and `m <= 2`. Its derivative has the sign of
`m-a*log(y)`, which is negative on `y >= 7`. The leading `L/y=1/C`
term is constant and the remaining `b/y` decreases. Thus evaluating at
`y=7` and using `8 log 7 < 16` bounds the whole half-line, rather than
sampling it. Independent rational arithmetic reproduced

```text
error  = 241522181840005231/254054780070000000 < 1,
margin = 12532598229994769/254054780070000000 > 0.
```

For larger positive `C`, each C-dependent contribution to this fixed-y
certificate decreases, and the same cutoff still reaches `y >= 7`.
For `C=683/1000` the independently computed certificate is
`483056762993653607/511856680790000000 < 1`.

The conclusion is strictly `ell < X`: if an outside prime were exactly
`X`, both smoothing weights at that prime would be zero. The same
contradiction therefore works assuming only that no outside prime is
strictly below `X`.

**The all-subgroup small interval.** Every reduced representative
`1 <= a < q` has only prime factors coprime to `q`, all below `q`.
If all such primes belonged to `H`, every unit would belong to `H`.
Hence a proper subgroup misses some coprime prime strictly below `q`.
This argument applies to every integer modulus under discussion and
requires no prime distribution theorem.

For real `q > 1`, the derivative of `(C log q)^8/q` has the sign of
`8-log q`. It increases and then decreases, so its minimum on
`[7,65536]` is at an endpoint. Both endpoint inequalities are strict:
`(C log 7)^8 > 7`, and `C log 65536 > 7` with `7^8 > 65536`.
Thus `ell < q < (C log q)^8` on this entire interval, unconditionally.
The overlap with the analytic range at 65536 causes no gap.

At 5, the prime 2 generates all four units and is excluded from every
proper subgroup. At 6, the only proper subgroup is `{1}` and the least
coprime prime outside it is 5. The displayed powers in the checker
correctly verify these generators. The groups at 3 and 4 give 2 and 3.

**Least integer versus least prime, and the obstructions.** For odd prime
`q`, the nonzero squares form a proper subgroup of index 2. A least
positive nonresidue exists below `q`. If it were composite, its two
smaller positive factors would be nonzero squares by minimality, making
their product a square. Thus it is prime, and the outside-prime theorem
proves the stated least-integer corollary. Lower logarithm bounds were
used to prove sufficient coefficients; upper bounds were used to disprove
`0.677` at 5 and `0.682` at 6. All four comparison directions are correct.

## Independent computational evidence

All project executions used `python3 -B` inside the sandbox. The
independent calculations below imported no repository arithmetic or
primality helpers. They ran in memory; only this report was created.

The first command was `python3 -B - <<'PY' ... PY` from the session root,
using the following core calculation. It uses an exponential-series
enclosure instead of the author's atanh-series logarithm routine:

```python
from fractions import Fraction as R

def exp_bounds(x, N=64):
    term = lo = R(1)
    for j in range(1, N+1):
        term *= x/j
        lo += term
    nxt = term*x/(N+1)
    assert 0 < x < N+2
    return lo, lo+nxt/(1-x/(N+2))

brackets = {
    2: (6931471, 6931472),
    5: (16094379, 16094380),
    6: (17917594, 17917595),
    7: (19459101, 19459102),
}
logs = {n: (R(a, 10**7), R(b, 10**7))
        for n, (a, b) in brackets.items()}
for n, (lo, hi) in logs.items():
    assert exp_bounds(lo)[1] < n < exp_bounds(hi)[0]

C, D = R(339, 500), R(39, 50)
error = R(1001, 1000)*(R(231, 70000)+1/(2*C*D))
error += ((7/(2*C*D)+7/(2*C)+2)*16+1+14/C*256)/7**8
assert error == R(241522181840005231, 254054780070000000) < 1
assert C*16*logs[2][0] > 7
assert (C*logs[7][0])**8 > 7
assert (C*logs[5][0])**8 > 2
assert (R(683, 1000)*logs[6][0])**8 > 5
assert (R(677, 1000)*logs[5][1])**8 < 2
assert (R(682, 1000)*logs[6][1])**8 < 5
assert 7**8 > 65536
```

The omitted exponential terms have successive ratios at most `x/(N+2)`,
so the geometric tail above is a rigorous upper bound. All assertions use
exact Fractions. Illustrative, non-decision decimal enclosures were:

```text
(0.678 log 5)^8: between 2.01016331 and 2.01016433
(0.677 log 5)^8: between 1.98656665 and 1.98656766
(0.683 log 6)^8: between 5.03040743 and 5.03040969
(0.682 log 6)^8: between 4.97178717 and 4.97178940
(0.678 log 7)^8: between 9.17951484 and 9.17951863
```

The second independent command used an Eratosthenes sieve and the binary
Jacobi algorithm based on quadratic reciprocity, rather than trial
primality and Euler modular exponentiation. Its core is replayable from
the session root:

```python
from fractions import Fraction as R
from hashlib import sha256
from math import isqrt

limit = 65536
prime = bytearray(b'\x01')*limit
prime[0:2] = b'\x00\x00'
for p in range(2, isqrt(limit-1)+1):
    if prime[p]:
        for n in range(p*p, limit, p):
            prime[n] = 0

def jacobi(a, n):
    assert n > 0 and n % 2
    a, sign = a % n, 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5):
                sign = -sign
        if a % 4 == 3 and n % 4 == 3:
            sign = -sign
        a, n = n % a, a
    return sign if n == 1 else 0

moduli = [q for q in range(3, 258, 2) if prime[q]]+[31391]
for q in moduli:
    squares = {a*a % q for a in range(1, q)}
    for a in range(1, min(q, 128)):
        assert jacobi(a, q) == (1 if a in squares else -1)

C, pairs = R(339, 500), []
for q in range(5, limit, 2):
    if not prime[q]:
        continue
    a = 2
    while jacobi(a, q) != -1:
        a += 1
    assert prime[a]
    lower = {5: R(16094379, 10**7), 7: R(19459101, 10**7)}.get(
        q, R(2*(q.bit_length()-1), 3))
    assert a < (C*lower)**8
    pairs.append((q, a))

assert len(pairs) == 6540
assert max((a, q) for q, a in pairs) == (31, 31391)
assert [q for q, a in pairs if a == 31] == [31391]
data = ''.join(f'{q}:{a}\n' for q, a in pairs).encode('ascii')
assert sha256(data).hexdigest() == (
    '35c83133258b53504bd985dde46a3c7ffc6be75277f9d5be77120f85182de9fa')
```

For the nonexceptional moduli this uses the rigorous coarse lower bound
`log q >= floor(log_2 q)*log 2 > floor(log_2 q)*2/3`.
The first and last pairs were `(5,2)` and `(65521,17)`. Explicit square
sets validated the reciprocity routine on 55 prime moduli, including the
modulus attaining the maximum. Only after producing the independent
dataset, a `runpy.run_path` import compared every pair against the author's
`least_quadratic_nonresidue` and its `direct_prime_checks` aggregate:
all 6540 agreed. These are supplementary finite checks, not the proof of
the composite-modulus small interval or the unbounded analytic range.

Separately, the actual command
`python3 -B research/least-nonresidue/constants.py` in `nonresidue/`
exited 0. It printed the exact error and margin above, 6540 directly
checked primes, maximum 31 at 31391, all five advertised `REJECT control`
lines, and `all constants and direct checks pass`.

## Nonblocking checker issue

`constants.py:27` checks `7*c2**2 >= 16`, but does not check the sign of
`c2`. The concrete probe

```python
import runpy
from fractions import Fraction
m = runpy.run_path('nonresidue/research/least-nonresidue/constants.py',
                   run_name='review_import')
print(m['analytic_certificate'](c2=Fraction(-189, 125)))
```

returned the same successful certificate, although a negative number
cannot dominate the positive pairing coefficient `4/sqrt(7)`. A minimal
guard is `c2 > 0 and 7*c2**2 >= 16` in the existing `require`.
This is a fixable helper-input validation gap, not a counterexample to
the theorem or the default checker: the actual input is the accepted
positive `189/125`, and all five documented rejection controls pass.
No script, theorem or README changes were made during this review.

## Inputs taken on trust and limits

- H(7/8), including its application to zeta, remains an assumption. Its
  preprint, Lean proof and any kernel replay were not certified.
- The classical completed-L-function theory, zero identities, and analytic
  validity/convergence of the LLS contour shifts are accepted inputs.
  This review checked residue signs, gamma formulas and subsequent
  inequalities against LLS and the accepted local proofs; it supplies no
  new contour-convergence proof.
- The accepted paired zero-sum estimates and `b=231/10000`,
  `c2=189/125` are inputs, not new analytic estimates established by
  running this checker. Their applicable ranges and the rational
  comparison `c2 >= 4/sqrt(7)` were checked. The frontier and local proofs
  establish their predecessor provenance, irrespective of stale draft
  headers. Standard finite-group duality, character induction and
  quadratic reciprocity were used.
- The LLS versioned primary PDF was read through the web tool. Its byte
  hash quoted in `PROOF.md` was not independently recomputed: the native
  in-memory `urllib.request.urlopen` attempt failed with
  `URLError <urlopen error [Errno -3] Temporary failure in name resolution>`.
  No network-policy bypass was attempted. No repository material was
  sent to an external service.
- No exhaustive large-modulus character enumeration, optimal-coefficient
  proof, new H(theta) transfer, or generic validation of arbitrary checker
  parameter changes is claimed. Shared Miller--Rabin verifier/tests were
  not rerun as certification of this distinct theorem.
- Work stayed within the requested 45-minute bound. There were no further
  subagents, public actions, installations, or git mutations. The sole
  created artifact is this report, written with native `apply_patch`.

The verdict applies to the stated domains and the recorded file bytes;
maintainer acceptance remains a separate step.
