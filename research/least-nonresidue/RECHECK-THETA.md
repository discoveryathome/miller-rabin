**Original idea: Geoffrey Irving.**

# Independent recheck of the smaller-theta extension

Reviewed 2026-10-23 by a separate fresh-context Codex agent, using the same
model as the author. This is an independent AI mathematical review, not a
human review, maintainer acceptance, or a formal proof certificate.

**Verdict: PASS for the frozen snapshot below, conditional on H(theta),
theta = 8748867/10000000, including zeta, and the declared classical analytic
inputs. No blocking issue or new nonblocking issue was found in scope.**

Section 5 correctly gives exponent `r = 10000000/1251133` with coefficient
`683/1000` for every integer q >= 5 and every proper subgroup of (Z/qZ)*.
Coefficient `339/500` works when q != 6 and therefore for the quadratic
corollary for every prime q >= 5. At q = 6 the outside prime is exactly 5;
the exact outside primes at q = 3,4 remain 2,3. All logarithms are natural.
The earlier H(7/8) reviews remain historical evidence for their own snapshots.

## Frozen bytes and provenance

Working directory throughout:
`/root/.t3/scratch/2026-10-23-fetch-https-discoveryathome-org-v0-7d492a7d/nonresidue`.
The checked HEAD is `eade12def19c0b67f9d176d0c69eb47e8c07254a`, the supplied
published PR #12 head. The extension is the uncommitted delta, not a theorem
already contained in that commit. Accepted base
`d2bd5167a42b8256f1362640dc149057920e5db9` is an ancestor of HEAD.

SHA-256 hashes of the actual reviewed inputs, relative to the repository root:

```text
fa0829add0ce06d72eb41221e596dd33fdb5ebc2b7b050eef4d7cc530c0c4721  research/least-nonresidue/PROOF.md
60029eab65e1d27196b677a9cd1c64f3b0e2844d5f4cd2f2b3c1ddeaf253ec7d  research/least-nonresidue/constants.py
5d34f3bb7be645514ef43a4f2432013972daf226a708b81bb020da4954bd837a  research/least-nonresidue/README.md
```

I read AGENTS.md and DISCOVERY.md first, then the frozen files, historical
rechecks, frontier record, accepted pairing proof, first-T1 analytic inputs,
and the imported logarithm/primality implementations. The following four
dependencies are byte-identical to the accepted base, checked using `git show`:

```text
824af09db62887a04107e72f9aafb56345aef45c1ea3ccf6499956d6896e914c  research/zero-pairing/PROOF.md
abd066b2d27961e93ae007e5fb8897b5a841aff875b24af3eb0216d73bed8cbb  research/first-explicit-t1/PROOF.md
ace2b055b5279284d04d37b6c6dde77af86088245846700c502effb3e812e709  verify/check.py
ba252ae554ac3f4ca372b692ef6ed7966772716dfa57c5b65ed22ae84fe5a1f1  verify/mr.py
```

Acceptance of the pairing input is determined from `discover/frontier.json`,
as AGENTS.md directs, despite old draft-status text inside the accepted proof.
No unmerged sibling result was used. The only file written in this review is
this report; the three frozen inputs were not edited.

## Pairing and transfer of the residue identities

For a complex primitive character, the functional equation sends a zero rho
of chi to `1-rho` of conjugate(chi). Conjugating that relation gives
`1-conjugate(rho)` as a zero of the original chi, with multiplicity preserved.
Thus the involution used here stays within one character even when chi is
not real. H(theta) and this reflection put all its zeros in
`1-theta <= Re rho <= theta`. The same reasoning applies to zeta.

Here is a direct check of the parameter-dependent part of the accepted lemma.
For an off-line pair with sigma = Re rho >= 1/2, put
`v = 1/|rho|^2`, `w = 1/|1-conjugate(rho)|^2`. Then
`1 <= w/v <= sigma^2/(1-sigma)^2`, and the main-sum ratio to the pair's
contribution `sigma*v + (1-sigma)*w` to A is fractional-linear in w/v.
Its endpoint values are

```text
X^sigma + X^(1-sigma),
((1-sigma)/sigma) X^sigma + (sigma/(1-sigma)) X^(1-sigma).
```

Both are bounded by `g(sigma) = X^sigma + 7 X^(1-sigma)`, because
`sigma/(1-sigma) <= theta/(1-theta) = r-1 < 7`. Convexity of g reduces the
remaining comparison to sigma = 1/2 and theta. With `u=X^(theta-1/2)`,

```text
(g(theta)-g(1/2))/sqrt(X) = u + 7/u - 8 = (u-1)(u-7)/u.
theta - 1/2 - 11/30 = 246601/30000000 > 0,
256^11 = 309485009821345068724781056,
7^30   = 22539340290692258087863249.
```

Consequently u > 7 for X >= 256, so the required endpoint is g(theta).
A zero on the critical line has main-sum ratio `2 sqrt(X)`, also below this
envelope. Positive-term regrouping justifies pairing the absolutely bounded
sums; it does not require cancellation or pairing different characters.

For the second kernel, the two members have common absolute denominator
`|rho| |1-conjugate(rho)|`. AM-GM bounds their ratio to A by

```text
(X^(sigma-1) + X^(-sigma)) / (2 sqrt(sigma(1-sigma)))
 <= (X^(theta-1) + X^(-1/2)) / (2 sqrt(theta(1-theta))).
```

The exact arithmetic is

```text
theta(1-theta) - 7/64 = 8496216311/100000000000000 > 0,
7 (189/125)^2 - 16 = 47/15625 > 0.
```

Thus the same positive c2 = 189/125 dominates the required coefficient.
The on-line ratio `2 X^(-1/2)` is also covered. Finally,
`sum 1/|rho|^2 <= A/(1-theta) = r A < 8 A`, so the constant zero sum is
covered by the same additive 8. These statements cover zeta as well.

I inspected [LLS v3](https://arxiv.org/pdf/1309.3595v3), printed pp. 5--8:
the residues before its GRH estimates, the real-part identity for B, and the
gamma terms agree with the accepted inputs. The formulas preceding its GRH
invocations are the relevant identities; its GRH error bounds are replaced
by the estimates just derived. This is not an application of its final GRH
theorem with a changed exponent. Contour convergence and the inherited
zeta/gamma constants are classical declared inputs, not newly proved here.

## Criterion, integer envelopes, and independent error

The character reduction in Sections 1--2 still works for all proper
subgroups, including composite moduli. A nonprincipal character trivial on H
is 1 on every unit in the contradiction range. Its weighted T sum is
nonnegative. Both imprimitive S corrections together cost at most
`omega(q) (log X)^2`. The T correction costs at most
`(1-1/X) U(q/f)`. The conductor saving

```text
log f + 2 U(q/f) - log q <= log 2 < log pi
```

therefore gives `A <= (log q)/(2d(X))` whenever d(X) > 0, including conductor
f = 3. No positive-sign assumption on log(f/pi) or full complex-B bound is
needed. The gamma signs remain valid since this range has X > 256 > 64.
The derivation of criterion (6) therefore survives with the new F and d.

Put `y = X^(1-theta)` and `X = y^r`. Independently computed exact differences:

```text
r - 799/100 = 344733/125113300 > 0,
8 - r       = 9064/1251133 > 0.
```

For y >= 7, the directions of every power replacement are correct:
`X^(-1/2) <= y^(-3)`, `X^(-theta) = y^(-(r-1)) <= y^(-6)`,
`X^(-1) <= y^(-7)`, and `log X <= 8 log y`. Consequently,

```text
F(X)/X <= 1/y + 7/y^6 + 8/y^7,
1 + 7/7^5 + 8/7^6 = 117706/117649,
1001/1000 - 117706/117649 = 60649/117649000 > 0,
1 - (189/125)(1/7 + 1/7^3) = 191/245,
191/245 - 77/100 = 47/4900 > 0.
```

The right-hand envelopes improve as y increases. For q >= 65536,
`y = (339/500) log q > (339/500)(32/3) = 904/125 > 7`.
Also `omega(q) <= log(q)/log(2) < 2 log(q)`.

After dividing criterion (6) by X, the residual terms are positive multiples
of `(log y)^b/y^a` with a >= 6 and 0 <= b <= 2. Their derivatives have sign
`b-a log y`, which is negative for y >= 7. The zeta b/y term decreases and
the leading L/y term is constant. Thus evaluating the integer envelope at
y = 7 with `8 log 7 < 16` is valid. My separate Fraction calculation gives

```text
leading term = 3261198187/3390000000,
residual     = 20543057/3070991847,
total        = 29748536893681951/30709918470000000 < 1,
margin       = 961381576318049/30709918470000000 > 0.
```

This reproduces (9) without calling `theta_certificate`. Increasing C only
improves the estimate. The argument yields a prime strictly below X: if X
itself is prime, its contribution to both weighted sums is zero, so the
same contradiction holds under the assumption that every eligible prime
strictly below X lies in H.

## Complete small range and coefficient obstructions

The unconditional `p < q` argument is valid: if every prime below q coprime
to q lay in H, factoring each reduced representative from 1 through q-1
would put every unit in H. This contradicts properness without enumerating
subgroups.

For positive C, the derivative of `(C log q)^r/q` has sign `r-log q`.
There is only an interior maximum, so the minimum on [7,65536] is at an
endpoint. The upper endpoint follows from `C log 65536 > 7` and
`7^7 = 823543 > 65536`. The lower endpoint and q = 5,6 were checked with
my own rational logarithm enclosures, without importing `ln_bounds`:

| q | C | Downward logarithm enclosure l_q | Exact rational base C*l_q | Certified lower bound for (C*l_q)^799/p^100 |
|---|---|---|---|---|
| 5 | 339/500 | 1.60943791 | 54559945149/50000000000 | 1521363/1000000 > 1, p=2 |
| 6 | 683/1000 | 1.79175946 | 61188585559/50000000000 | 1498397/1000000 > 1, p=5 |
| 7 | 339/500 | 1.94591014 | 32983176873/25000000000 | 10^11 > 1, p=7 |

All bases exceed 1, and r > 799/100. These rational-power comparisons
therefore imply the required strict real-power bounds. At q = 5, 2
generates the units, so every proper subgroup excludes it. At q = 6 the
only proper subgroup is {1} and its first outside prime is 5. This proves
the complete stated domains. For prime q, the subgroup of nonzero squares
applies, and a least positive quadratic nonresidue must be prime by
factoring a hypothetical composite least nonresidue into smaller residues.

The old obstructions persist in the new exponent. My independent upper
logarithm bounds give

```text
(0.677 log 5)^8 < 1986566783/1000000000 < 2,
(0.682 log 6)^8 < 621473589/125000000 < 5.
```

Both bases exceed 1, so replacing 8 by r < 8 makes those powers smaller.
The claimed domains therefore still exclude these proposed smaller
coefficients. This does not establish optimality of 0.678 or 0.683.

The essential independent arithmetic can be reproduced with this standalone
standard-library code. No project checker or floating-point logarithm is used:

```python
from fractions import Fraction as F

theta = F(8748867, 10000000)
r = 1 / (1 - theta)
C, c2 = F(339, 500), F(189, 125)
assert F(799, 100) < r < 8
assert theta - F(1, 2) > F(11, 30)
assert 256**11 > 7**30
assert theta * (1 - theta) >= F(7, 64)
assert c2 > 0 and 7*c2*c2 > 16
y, d = F(7), F(77, 100)
assert 1-c2*(1/y+1/y**3) > d
assert 1+7/y**5+8/y**6 < F(1001, 1000)
leading = F(1001, 1000)*(F(231, 10000)/y+1/(2*C*d))
residual = ((y/(2*C*d)+y/(2*C)+2)*16+1+(2*y/C)*16**2)/y**7
error = leading + residual
assert error == F(29748536893681951, 30709918470000000) < 1

def own_log(q, terms=160):
    z = F(q-1, q+1)
    power, lower = z, F(0)
    for j in range(terms):
        lower += 2*power/(2*j+1)
        power *= z*z
    tail = 2*power/((2*terms+1)*(1-z*z))
    return lower, lower+tail

assert own_log(2)[0] > F(2, 3)
assert 1 < own_log(7)[0] and own_log(7)[1] < 2
assert C*F(32, 3) > 7 and 7**7 > 65536
for q, c, p in [(5, C, 2), (6, F(683, 1000), 5), (7, C, 7)]:
    lo, hi = own_log(q)
    n = lo.numerator*10**8//lo.denominator
    assert hi < F(n+1, 10**8)
    base = c*F(n, 10**8)
    assert base > 1 and base**799 > p**100
for q, c, p in [(5, F(677, 1000), 2), (6, F(341, 500), 5)]:
    lo, hi = own_log(q)
    assert c*lo > 1 and (c*hi)**8 < p
```

The logarithm enclosure integrates the geometric series:
`log q = 2 sum_{j>=0} z^(2j+1)/(2j+1)` with `z=(q-1)/(q+1)`.
The omitted tail is at most `2 z^(321)/(321(1-z^2))`. The eight-decimal
lower values also agree with the actual imported helper; I checked overlap
of independently obtained enclosures for q = 2,5,6,7,11,13.

## Fresh computations and controls

I independently generated all 6540 primes in `5 <= q < 65536` by an
Eratosthenes sieve and found each least nonresidue using quadratic
reciprocity, rather than trial primality and modular exponentiation.
Every resulting least nonresidue was prime. The maximum was 31, last at
q = 31391. Comparing every entry with the current helper gave zero mismatches.
For the ordered byte sequence `f"{q}:{ell}\n"` over increasing q, the
independent table SHA-256 is
`35c83133258b53504bd985dde46a3c7ffc6be75277f9d5be77120f85182de9fa`.

The new bound was independently checked for every entry: q = 5 uses the
799-versus-100 comparison above; q = 7,11 use direct lower-logarithm
seventh-power comparisons against 3,2. For q >= 13, monotonicity and
`(C*own_log(13)[0])^7 > 12025397/250000 > 31` cover every entry at once.
All bases exceed 1 and r > 7, so these also verify the new real-power
bounds and the older eighth-power bounds. This finite evidence supplements
the proof for all subgroups; it is not its replacement.

A fresh run of the frozen `constants.py` exited 0, reproduced both printed
analytic fractions, checked all 6540 primes, and printed all seven rejection
controls. I separately invoked each control and checked its actual failure:

| Probe | Rejection reason (ValueError) |
|---|---|
| c2 = 3/2 | pairing constant must dominate 4/sqrt(7) |
| c2 = -189/125 | pairing constant must dominate 4/sqrt(7) |
| y_min = 6 | d(X) > 39/50 |
| prime_c = 677/1000 | q=5 endpoint |
| general_c = 341/500 | q=6 endpoint |
| quadratic modulus 9 | modulus must be prime and at least 5 |
| theta = 9/10 | refined exponent interval |

The seventh rejection is appropriate: theta = 9/10 gives r = 10, outside
the proved fixed-R=7 parameter range. A stronger hypothesis with a smaller
theta can imply the assumed line, but a weaker line cannot simply be
substituted into these envelopes.

Additional in-memory mutations of the new helper were rejected: raising
the claimed d bound to 39/50 or lowering y to 5 failed `refined d envelope`;
setting the F multiplier to 1 failed `refined F envelope`; replacing either
coefficient by its bad value failed the corresponding refined q=5 or q=6
endpoint; raising Q0 to 823544 failed `refined upper interval endpoint`.
No frozen bytes were changed for these probes.

Fresh repository-root runs, with bytecode writes disabled, also passed:

```text
python3 -B research/zero-pairing/constants.py       exit 0
python3 -B research/least-nonresidue/constants.py   exit 0
python3 -B verify/check.py all                    exit 0
python3 -B -m unittest discover -s tests           16 tests, OK
```

The shared verifier certifies its recorded Miller--Rabin claims, not the
new least-nonresidue theorem. The pairing script's floating-point grids are
sanity checks; none was used as a certificate for this extension. Parent
run summaries were not counted as independent verification.

## Prior findings and limits

Historical reports read in this review have hashes:

```text
84ff33b94198b224425b50892c29c0cbe0eb9f0a243982bf78ede7f6eaeb5618  research/least-nonresidue/RECHECK.md
c75db68a3b80e6ebf38232a9298d0be16000898cd229a38045c68c485c28ca31  research/least-nonresidue/GUARD-RECHECK.md
```

Round 1's sole nonblocking objection was acceptance of a negative c2 by a
squared-only guard. Its response is accepted: the current least-nonresidue
helper checks positivity explicitly, and my fresh negative probe rejects
for that guard. GUARD-RECHECK.md separately records the earlier 15 probes
and the three-script fix; I did not repeat that whole cross-package guard
audit. The theta delta does not remove the guard. There are no unresolved
prior objections and no required new correction in this reviewed scope.

The [Xu--Sang v2 reference](https://arxiv.org/abs/2610.15291v2) explicitly
conditions its claimed boundary improvement on analytic inputs of the
earlier work. The local frontier likewise marks A1b open and not peer
reviewed. This review checked the reference's stated parameter and
conditional status; it did not audit that paper's proof or establish its
analytic inputs. H(theta), including zeta, remains an explicit assumption.

This review does not prove H(7/8), H(theta), or GRH; replay any Lean proof;
enumerate or numerically certify L-function zeros; re-prove contour
convergence; or certify optimal coefficients. The accepted Hadamard,
residue, gamma-sign, and zeta-constant inputs remain declared dependencies.
The primary LLS PDF was inspected through the browsing tool, but its remote
binary SHA-256 was not recomputed in this round. Exact input hashes above
pin the local sources actually reviewed. Same-model AI agreement and
finite exact arithmetic do not constitute human or kernel verification.
Maintainer review and acceptance of this extension remain separate.
