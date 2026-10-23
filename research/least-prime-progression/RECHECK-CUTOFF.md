**Original idea: Geoffrey Irving.**

# Independent mathematical recheck: coset cutoff 64

Reviewed 2026-10-23 by a fresh-context Codex review agent, `gpt-6.1-sol`,
max reasoning effort. This is a separate, same-model AI review, not human,
formal, or maintainer acceptance. Text: CC BY 4.0; executable checks:
Apache-2.0.

## Verdict and issues

**Confirmed within the stated conditional and classical-input scope.**
No blocking issue, required mathematical correction, or arithmetic error
was found in the frozen change. Section 9 proves, for every fixed
`13/15 <= b <= 7/8`, assuming H(b), including zeta, and with
`r = 1/(1-b)`,

    P(aH,q) < max(64,h log q)^r

for every integer `q >= 3`, subgroup `H` of `(Z/qZ)*` of index `h >= 2`,
and coset representative `a` in that group. The proof covers both closed
parameter endpoints and all real cutoffs arising from these parameters.
Its strict inequality does not discard the possibility that the real
cutoff is a prime.

The new small-modulus dependency is substantive and correctly disclosed:
`3 <= q <= 20` uses this package's previously reviewed sharp progression
theorem. The old cutoff-80 proof remains fully analytic. Neither the sharp
progression coefficient nor its unique equality case is changed.

## Reviewed snapshot and dependency hashes

Working directory:
`/root/.t3/scratch/2026-10-23-fetch-https-discoveryathome-org-v0-7d492a7d/repo`.

- Branch: `session/20261023T0602-corollaries`.
- Local HEAD, also the published PR #11 head supplied in the brief:
  `1606bf12a21ae37707befab1a5caa3c32bdd8770`.
- Accepted base: `d2bd5167a42b8256f1362640dc149057920e5db9`.
- New frozen inputs are the **uncommitted** PROOF.md, constants.py and
  README.md below. A HEAD-only review would omit the new theorem.

SHA-256 of the frozen inputs:

```text
6644756e47adc7ead5f65fa6a40dcc4c1cc03054d6b03705e45fa5555b7c71f0  research/least-prime-progression/PROOF.md
2bcbe0ee8f7e4b0fd51eab519fe4bfb6db992bd1f4ab4475ea0adfe0f586ee82  research/least-prime-progression/constants.py
7dddbf5156bdd7f1d19d5624488fdbb02ea478cafcbda4563f5bfaceee4ac94a  research/least-prime-progression/README.md
```

The following instructions and accepted dependencies were read or checked
in their relevant uses. Each was byte-compared with the same path at the
accepted base and is identical:

```text
e8f93ce38983d792791c3f9ad9b8b0a367668b3b7b945b071b6f360c45babd62  AGENTS.md
e603c2aaf4b9c692b315213f6c7dd5aebdfba5932e67155e53c76a6590ec4ddf  DISCOVERY.md
9ca629138c133ac8547efba9b47f4d862ae82e7079c4da0998961d8fa5c964a4  discover/frontier.json
824af09db62887a04107e72f9aafb56345aef45c1ea3ccf6499956d6896e914c  research/zero-pairing/PROOF.md
b71772dee37a2b068677c2800c2dce6d0737a94d03380f47b2f9d87ec6e610a7  research/zero-pairing/constants.py
abd066b2d27961e93ae007e5fb8897b5a841aff875b24af3eb0216d73bed8cbb  research/first-explicit-t1/PROOF.md
ace2b055b5279284d04d37b6c6dde77af86088245846700c502effb3e812e709  verify/check.py
```

The frontier still records the accepted PR #8 zero-pairing result, building
on PR #6. This review does not promote the corollary to that frontier.

For the same-package predecessor, HEAD's constants.py has SHA-256
`b28e47ef7df20c6ca731525ce2108ed5c92380526f24e7a2dbb8bd19eb92c14a`,
exactly the constants.py input pinned by RECHECK-SHARP.md. HEAD's PROOF.md
has SHA-256
`1979aacd1963a712e787ee841aa72abbb51b2c19cb974e91a87697cad3c6ec68`;
it includes the subsequent review-status wording. RECHECK-SHARP.md pins
its earlier frozen PROOF.md as
`725cff10144eacee1819140c4ec9fec2cf3a8938ed19cf017321e6c2fa71314e`.
These whole-file hashes should not be conflated.

I independently byte-compared the Section 8 theorem/proof span, starting
at `## 8. Parameter transfer` and ending immediately before its review-status
paragraph, with HEAD. It is unchanged, with SHA-256
`ae8b721bff26643ff4f1411245e0b375bd6d7174d197445012bc8cb9d8fe7bcf`.
An AST comparison also found every old helper unchanged except
`failure_controls` and `main`, which add the three controls and the new
certificate's call/output. In particular, the progression, parameter,
sieve, totient and finite-certificate implementations are unchanged.

## Primary source and residue signs

I checked the proof of [LLS, arXiv:1309.3595v3, Lemma 2.4, printed
page 8](https://arxiv.org/html/1309.3595v3#S2.Lem4), also inspected in the
[versioned PDF](https://arxiv.org/pdf/1309.3595v3). The identity before its
RH estimate is exactly Section 9's (23). No unmerged L-value theorem was
used. The independently fetched HTML response was 685354 bytes, SHA-256
`a9560eb9b5b15592df481488765aea74d7a199c3c74553cdd4464ddbf09b7b4f`.
The context-mode HTML converter failed because `turndown` was missing;
standard-library HTTPS fetching and the web tool supplied the source check.
Nothing was installed.

Independently reconstruct the residues of

    -(zeta'/zeta)(s) X^(s-1) / [s(s-1)].

At `s=1`, the expansions `-zeta'/zeta = 1/(s-1)-gamma+...` and
`X^(s-1)/s = 1+(t-1)(s-1)+...` give `t-1-gamma`.
At `s=0`, `zeta'/zeta(0)=log(2pi)` and the residue of `1/[s(s-1)]`
is `-1`, giving `+log(2pi)/X`. A nontrivial zero contributes
`-X^(rho-1)/[rho(rho-1)]`, with multiplicity. A trivial zero `-2k`
contributes `-X^(-2k-1)/[2k(2k+1)]`. Thus

    T_zeta(X) = t-(1+gamma)+log(2pi)/X-Z_zeta(X)
                -sum_(k>=1) X^(-2k-1)/[2k(2k+1)].

In particular, the trivial-zero series is negative and the nontrivial
sum has a minus sign. The classical contour justification remains an
input; these residue signs do not require RH.

Write `b_zeta=231/10000` to distinguish it from the parameter b. The
previously reviewed uniform paired-zero estimate gives

    |Z_zeta(X)| <= c(X;b)|B_zeta|,
    c(X;b) = (189/125)[X^(b-1)+X^(-1/2)].

For `X>1`, this correction increases with b and decreases with X for
every b in the stated interval. For `X>=256` its contribution, together
with the positive residue at zero, is strictly less than

    3/256 + (189/125)(9/16)(231/10000)
      = 313653/10000000 < 7/100.

The exact lower bound on the saving is

    1+57/100-313653/10000000 = 15386347/10000000 > 3/2.

Dropping the negative trivial-zero series therefore proves
`T_zeta(X)<t-3/2`. An independent rational computation below checks
`gamma>.57`, `0<|B_zeta|<.0231`, and `log(2pi)<2<3`; it does not import
the package's elementary-constant or logarithm helper.

## Aggregate, complex constants, and every residual loss

The real part of the primitive-character identity (2) gives

    d(X;b) A_chi* <= L/2-Re T(X,chi)

after precisely the Euler correction in (7), the conductor inequality
(8), and `E_a<=0`. This uses the denominator `1+1/X-c(X;b)`. The bound
on the full complex `B_chi*`, used separately for the phased coset sum,
still uses its distinct absorption denominator `1-1/u-c(u;b)` at
`u=65536`. Since `b<=7/8`, that denominator is at least its old value
`1009383/1638400>3/5`. No imaginary component was replaced by a real-part
bound in this change.

Orthogonality at H, with nonnegative weights, gives

    -Re sum_(chi!=chi0) T(X,chi) <= T(X,chi0) <= T_zeta(X).

There are exactly `h-1` nonprincipal characters. Therefore the new
numerator is

    N = (h-1)L/2+t-3/2,
    sum_(chi!=chi0) A_chi* <= N/d(X;b).

The principal character's missing Euler factors can only decrease its
T sum, so this improvement incurs no new positive correction there.
The complex phases in the S sum are still bounded in absolute value.
All other charges in the lower bound on `h C(X;aH)` remain

    b_zeta F_b(X),
    R = log(2pi)t+1+h omega(q)t^2/2
          +(h-1)[(3L/2+26)t+t^2/2+3].

The factor `h omega(q)/2` retains the principal Euler loss and all
`h-1` nonprincipal Euler losses from (6). The coefficient `3L/2+26`
retains the full complex B bound, conductor logarithm and gamma
residual. None is absorbed into the new zeta saving.

The proper-power argument still charges every exponent `k>=2`. For
each prime `p<=sqrt(X)`, with `v=t/log p`, its contribution is at most

    (log p)^2 sum_(k=2)^floor(v) (v-k)
      <= (log p)^2 integral_1^v (v-w) dw <= t^2/2.

Counting at most `sqrt(X)` such primes yields `Q(X)<=sqrt(X)t^2/2`.
This includes even powers, odd powers, and powers whose residues leave
and return to the coset. Bounding by all powers also safely includes
primes dividing q. The strengthened sufficient condition is consequently

    b_zeta F_b(X)/X + F_b(X) N/[X d(X;b)]
      + R/X + h t^2/[2 sqrt(X)] < 1.

## Complete analytic domain and directed envelopes

For every integer `q>=21`, exact logarithm bounds give `L>3`. With
`y=max(64,hL)` and `X=y^r`, the whole parameter interval gives

    y>=64,   15/2<=r<=8,   h<=y/3,   L<=y/2,
    omega(q)<=L/log2<2L<=y,   t<=8 log y.

In particular X exceeds 256, so every source estimate is in range.
Retaining `-L/2` in `(h-1)L/2`, in addition to the new zeta saving,
gives

    N/y <= 1/2+(8 log y-3)/y =: A(y).

Here N is positive: for `h>=2` and `L>3`, `N>=L/2+t-3/2>t>0`.
Thus replacing the positive denominator by a lower bound, and replacing
`F_b/X` by an upper bound, have the asserted directions. Also A(y) is
positive and its derivative has sign `11-8 log y<0` throughout `y>=64`.
Both subtractions of `3/2` are justified separately.

The two weaker integer-power substitutions are

    F_b(X)/X = 1/y+7/y^(r-1)+8/y^r
      <= (1+7/y^5+8/y^6)/y < (1000001/1000000)/y,
    d(X;b) >= 1-(189/125)(1/y+1/y^3)
      >= 31993667/32768000 =: d0 > 0.

Their validity is uniform in r; they are not extrapolated from `r=8`.
The positive `1/X` in d was discarded in the safe direction. Its lower
envelope increases with y, while both correction monomials for F decrease.

Furthermore,

    sqrt(X)>=y^(15/4)>22y^3,

because `y^3>=64^3=262144>234256=22^4`. The charged power loss is hence

    h t^2/[2 sqrt(X)] <= (16/33)(log y)^2/y^2.

This function decreases for `log y>1`. The residual is bounded by

    [2t+1+y^2t^2/6+(y/3)((3y/4+26)t+t^2/2+3)]/y^7.

Expanding after substituting `t<=8 log y`, with `ell=log y`, gives
exactly seven nonnegative summands:

    16ell/y^7 + 1/y^7 + (32/3)ell^2/y^5 + 2ell/y^5
      +(208/3)ell/y^6+(32/3)ell^2/y^6+1/y^6.

For `ell^j/y^k`, the derivative has sign `j-k log y` when `j>0`;
the `j=0` terms decrease directly. Here `k>=5`, `j<=2`, and
`log64>2`. This proves decrease on the entire ray, term by term.
At `y=64`, using `log64<104/25`, their sum is
`102572093/549755813888000<1/1000000`.

At the same endpoint, `A(y)<1557/1600`. With
`f=1000001/1000000`, the four fully charged budgets are:

| Charge | Exact upper budget |
| --- | --- |
| Principal zero sum, `b_zeta f/64` | `231000231/640000000000` |
| Nonprincipal aggregate, `f(1557/1600)/d0` | `99648099648/99980209375` |
| Residual R/X | `1/1000000` |
| Every proper prime power | `169/82500` |

Their sum is exactly

    675090454343806963541/675706247040000000000 < 1,

with margin

    615792696193036459/675706247040000000000 > 0.

The derivative arguments, exponent directions, positivity and endpoint
arithmetic establish the continuum statement. Checking a list of b or y
values would not establish it.

## Small moduli, dependency direction, and strictness

For `3<=q<=20`, `phi(q)<=q-1<=19` and `log q<3`. Uniformly in b,

    1-b<=2/15<1/6,   7^(1/6)<2,   log3>1,

so `c_b=7^(1-b)/(2log3)<1`. For a reduced representative a in the
specified coset, Section 8 gives

    P(aH,q)<=P(a,q)<57^r<64^r.

Although the progression theorem uses a non-strict inequality, its base
is strictly below 57. This also handles its exceptional equality
`q=3,a=1`, where its right side is exactly 7. In this range `h<=phi(q)`
also gives `h log q<57<64`, so y is indeed 64.

This is a noncircular dependency. Section 8's large-q progression proof
uses criterion (13), its own q>=2048 envelope, and its finite remainder;
it does not use Section 9 or the new zeta saving. The earlier independent
review covers that complete predecessor. As an additional local check,
I independently searched each reduced progression for `q=3..20`, using
trial-division primality rather than the package's prime-list marking.
All 126 classes passed; the largest least prime was `191` at `q=19,a=1`.
For q>=4 I checked the stronger `.58` base to the integer power 7, which
implies the required bound for `r>=15/2`. At q=3 I checked the least
primes 7 and 2 directly.

For large q, assume that there is no prime **strictly below** X in the
coset. Any prime equal to X contributes zero to the logarithmic count.
Thus `C(X;aH)<=Q(X)` still holds under that assumption, whereas the exact
budget below 1 contradicts it. This proves `P(aH,q)<X`, also when X is
an integer or a prime. Both parameter endpoints are included by weak
exponent bounds and a strictly positive rational final margin.

## Helper guards, controls, and replays

I replayed `analytic_certificate`, `progression_certificate`,
`theta_certificate` and `coset_cutoff_certificate` separately, with
bytecode writes disabled. Their outputs were respectively:

```text
complex absorption denominator: 1009383/1638400
original analytic total:        5385194673/5600000000
refined progression total:      114068220107243/115735200000000
parameter coset total:          5446184217/5600000000
sharp progression total:        5705615549587/5776800000000
cutoff64 total:                 675090454343806963541/675706247040000000000
```

The parameter helper also returned its unchanged pair of totals at
`b=13/15`, `b=7/8` and `b=8748867/10000000`. These are regression
checks; the proof of uniformity is the preceding inequalities.

I ran all ten controls and separately captured their actual reasons:

| Control | Actual rejecting condition |
| --- | --- |
| Pairing constant `3/2` | `c2 must dominate 4/sqrt(7)` |
| Pairing constant `-189/125` | `c2 must dominate 4/sqrt(7)` |
| Old analytic cutoff 64 | `d(X) > 49/50` |
| Missing reduced class | Prime list does not cover every reduced class modulo 3 |
| All-q progression coefficient `1/2` | Bound fails at `q=3,a=1,p=7` |
| All-q progression coefficient `.58` | Bound fails at `q=3,a=1,p=7` |
| Parameter `b=9/10` | `unsupported pairing strip` |
| New cutoff 63 | `cutoff positive full margin` |
| New saving `tau=0` | `cutoff positive full margin` |
| New saving `tau=2` | `justified zeta constant subtraction` |

The new cutoff-63 raw budget is
`42586705492668352969/42280685370000000000>1`. Removing only the zeta
saving gives
`691310630563966963541/675706247040000000000>1`. A saving of 2 would
give a budget below 1 but exceeds the justified saving
`15386347/10000000`; it must be rejected before using that budget.
These controls reject the fixed certificate, not every possible proof
with cutoff 63 or a stronger zeta estimate.

The new helper checks the positive pairing coefficient, justification
of tau, modulus split, small-q base, square-root range, logarithmic
range, positive denominator, F envelope, residual and full margin.
For every tau it accepts, `0<=tau<15386347/10000000`; its generalized
aggregate has derivative sign `19/2+tau-8log y<0` when `log y>2`.
Thus the auxiliary tau parameter does not introduce an unproved
monotonicity case. No claim that arbitrary larger cutoffs pass this
helper is made; its logarithm cap is fixed.

Additional inherited-guard probes rejected `c2=-189/125,0,3/2` at the
pairing guard and accepted `189/125` and `1513/1000`. In two separate
**in-memory** source mutations, removing the inherited sign check and
removing the new upper bound on tau caused `failure_controls()` to fail
at `negative pairing constant` and `unjustified zeta constant saving`,
respectively. The actual files were never mutated.

The following baseline commands were rerun and passed:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 research/zero-pairing/constants.py
PYTHONDONTWRITEBYTECODE=1 python3 verify/check.py all
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests
```

The unit suite ran 16 tests. The shared verifier checks the recorded
Miller--Rabin claims; it does not verify this new analytic theorem. The
accepted zero-pairing replay includes numerical samples; those samples
are not the independent exact certificate above.

I did **not** rerun the whole least-prime-progression `main()` or repeat
the unchanged q<2048 searches over 1274560/1274558 classes. Their prior
complete independent check is recorded in RECHECK-SHARP.md. The new
arithmetic, all ten controls, old analytic positive controls and the
126-class small domain were checked in this review. The author's full
replay was not counted as an independent check of the new theorem.

## Independent reproducible arithmetic

Run from the repository root. This first command uses no local imports
and does not call the author's certificate. Its logarithm enclosure is
an independently implemented positive atanh series with an explicit
tail; the pi and gamma enclosures use 25 terms and N=512 respectively.
The residual is summed in its independently expanded seven-term form.

```sh
PYTHONDONTWRITEBYTECODE=1 python3 - <<'PY'
from fractions import Fraction as F
from math import gcd, isqrt

def log_box(x, n=80):
    x, k = F(x), 0
    while x >= 2:
        x /= 2
        k += 1
    while x < 1:
        x *= 2
        k -= 1
    def series(u):
        z = (u-1)/(u+1)
        term, total = z, F(0)
        for j in range(n):
            total += term/(2*j+1)
            term *= z*z
        lo = 2*total
        return lo, lo+2*term/((2*n+1)*(1-z*z))
    a, b = series(x)
    c, d = series(F(2))
    return (a+k*c, b+k*d) if k >= 0 else (a+k*d, b+k*c)

def atan_box(x, n=25):
    s = sum(((-1)**j*x**(2*j+1)/(2*j+1) for j in range(n)), F(0))
    nxt = (-1)**n*x**(2*n+1)/(2*n+1)
    return min(s, s+nxt), max(s, s+nxt)

a, b = atan_box(F(1, 5))
c, d = atan_box(F(1, 239))
pi_lo, pi_hi = 16*a-4*d, 16*b-4*c
n = 512
harmonic = sum((F(1, j) for j in range(1, n+1)), F(0))
lo, hi = log_box(n)
gamma_lo = harmonic-hi-F(1, 2*n)
gamma_hi = harmonic-lo-F(1, 2*n)+F(1, 8*n*n)
assert F(57, 100) < gamma_lo < gamma_hi < F(58, 100)
b_lo = 1+gamma_lo/2-log_box(4*pi_hi)[1]/2
b_hi = 1+gamma_hi/2-log_box(4*pi_lo)[0]/2
assert 0 < b_lo < b_hi < F(231, 10000)
assert log_box(2*pi_hi)[1] < 2 < 3
assert log_box(20)[1] < 3 < log_box(21)[0]
assert log_box(3)[0] > 1 and F(2, 15) < F(1, 6) and 7 < 2**6
assert 1/(1-F(13, 15)) == F(15, 2)
assert 1/(1-F(7, 8)) == 8

y, ell, bz, c2, f = F(64), F(104, 25), F(231, 10000), F(189, 125), F(1000001, 1000000)
assert 2 < log_box(64)[0] < log_box(64)[1] < ell
assert 64**3 > 22**4 and y**7 > 256
assert 1+7/y**5+8/y**6 < f
charge = F(3, 256)+c2*F(9, 16)*bz
assert charge == F(313653, 10000000) < F(7, 100)
assert 1+F(57, 100)-charge == F(15386347, 10000000) > F(3, 2)
d0 = 1-c2*(1/y+1/y**3)
assert d0 == F(31993667, 32768000) > 0
aggregate = F(1, 2)+(8*ell-3)/y
assert aggregate == F(1557, 1600)
residual = (16*ell/y**7+1/y**7+F(32, 3)*ell**2/y**5+2*ell/y**5
            +F(208, 3)*ell/y**6+F(32, 3)*ell**2/y**6+1/y**6)
assert residual == F(102572093, 549755813888000) < F(1, 10**6)
parts = [bz*f/y, f*aggregate/d0, F(1, 10**6), F(16, 33)*ell**2/y**2]
assert parts == [F(231000231, 640000000000), F(99648099648, 99980209375),
                 F(1, 1000000), F(169, 82500)]
total = sum(parts, F(0))
assert total == F(675090454343806963541, 675706247040000000000) < 1
assert 1-total == F(615792696193036459, 675706247040000000000) > 0
assert 11-8*2 < 0 and 2-2*2 < 0
assert all(j-2*k < 0 for k, j in [(7, 1), (7, 0), (5, 2), (5, 1),
                                  (6, 1), (6, 2), (6, 0)])

def raw_budget(y, tau):
    y = F(y)
    d = 1-c2*(1/y+1/y**3)
    return (bz*f/y+f*(F(1, 2)+(8*ell-F(3, 2)-tau)/y)/d
            +F(1, 10**6)+F(16, 33)*ell**2/y**2)
assert raw_budget(63, F(3, 2)) == F(42586705492668352969, 42280685370000000000) > 1
assert raw_budget(64, 0) == F(691310630563966963541, 675706247040000000000) > 1
assert raw_budget(64, 2) < 1 and 2 > 1+F(57, 100)-charge

classes, largest = 0, (0, 0, 0)
for q in range(3, 21):
    phi = sum(gcd(a, q) == 1 for a in range(1, q))
    assert phi <= 19
    for a in range(1, q):
        if gcd(a, q) != 1:
            continue
        p = a if a >= 2 else a+q
        while not (p >= 2 and all(p % d for d in range(2, isqrt(p)+1))):
            p += q
        classes += 1
        largest = max(largest, (p, q, a))
        if q >= 4:
            base = F(29, 50)*phi*log_box(q)[0]
            assert base > 1 and p < base**7
        else:
            assert (a, p) in [(1, 7), (2, 2)]
assert classes == 126 and largest == (191, 19, 1)
print('independent cutoff64 arithmetic PASS; total', total, 'margin', 1-total)
print('independent small domain PASS;', classes, 'classes; largest', largest)
PY
```

The following shorter replay exercises the actual helpers and checks
specific rejection reasons. It omits the unchanged long finite fallback.

```sh
PYTHONDONTWRITEBYTECODE=1 python3 - <<'PY'
import runpy
from fractions import Fraction as F

m = runpy.run_path('research/least-prime-progression/constants.py')
assert m['analytic_certificate']() == (F(1009383, 1638400), F(5385194673, 5600000000))
assert m['progression_certificate']() == F(114068220107243, 115735200000000)
for b in [F(13, 15), F(7, 8), m['SMALLER_THETA']]:
    assert m['theta_certificate'](beta=b) == (F(5446184217, 5600000000),
                                             F(5705615549587, 5776800000000))
assert m['coset_cutoff_certificate']() == F(675090454343806963541, 675706247040000000000)
for kwargs, reason in [({'y_min': 63}, 'cutoff positive full margin'),
                       ({'tau': 0}, 'cutoff positive full margin'),
                       ({'tau': 2}, 'justified zeta constant subtraction')]:
    try:
        m['coset_cutoff_certificate'](**kwargs)
    except ValueError as e:
        assert str(e) == reason
    else:
        raise AssertionError(kwargs)
for c2 in [-F(189, 125), F(0), F(3, 2)]:
    try:
        m['analytic_certificate'](c2=c2)
    except ValueError as e:
        assert str(e) == 'c2 must dominate 4/sqrt(7)'
    else:
        raise AssertionError(c2)
for c2 in [F(189, 125), F(1513, 1000)]:
    m['analytic_certificate'](c2=c2)
m['failure_controls']()
print('helper replay PASS')
PY
```

To reproduce the important snapshot/dependency comparisons without
writing git objects:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 - <<'PY'
import hashlib
import subprocess
from pathlib import Path

base = 'd2bd5167a42b8256f1362640dc149057920e5db9'
assert subprocess.check_output(['git', 'rev-parse', 'HEAD'], text=True).strip() == '1606bf12a21ae37707befab1a5caa3c32bdd8770'
expected = {
    'PROOF.md': '6644756e47adc7ead5f65fa6a40dcc4c1cc03054d6b03705e45fa5555b7c71f0',
    'constants.py': '2bcbe0ee8f7e4b0fd51eab519fe4bfb6db992bd1f4ab4475ea0adfe0f586ee82',
    'README.md': '7dddbf5156bdd7f1d19d5624488fdbb02ea478cafcbda4563f5bfaceee4ac94a',
}
for name, digest in expected.items():
    p = Path('research/least-prime-progression')/name
    assert hashlib.sha256(p.read_bytes()).hexdigest() == digest
for name in ['AGENTS.md', 'DISCOVERY.md', 'discover/frontier.json',
             'research/zero-pairing/PROOF.md', 'research/zero-pairing/constants.py',
             'research/first-explicit-t1/PROOF.md', 'verify/check.py']:
    assert Path(name).read_bytes() == subprocess.check_output(['git', 'show', base+':'+name])
name = 'research/least-prime-progression/constants.py'
head = subprocess.check_output(['git', 'show', 'HEAD:'+name])
assert hashlib.sha256(head).hexdigest() == 'b28e47ef7df20c6ca731525ce2108ed5c92380526f24e7a2dbb8bd19eb92c14a'
name = 'research/least-prime-progression/PROOF.md'
head = subprocess.check_output(['git', 'show', 'HEAD:'+name], text=True)
cur = Path(name).read_text()
old_span = head[head.index('## 8. Parameter transfer'):head.index('The new checker runs seven rejection controls')]
new_span = cur[cur.index('## 8. Parameter transfer'):cur.index('The first seven rejection controls')]
assert old_span == new_span
assert hashlib.sha256(new_span.encode()).hexdigest() == 'ae8b721bff26643ff4f1411245e0b375bd6d7174d197445012bc8cb9d8fe7bcf'
print('frozen inputs and dependency comparisons PASS')
PY
```

## Prior findings and their disposition

- [RECHECK.md](RECHECK.md), SHA-256
  `7ba56b4b9fd9afd856c1b310969f018efddea8e6e9ebfdd6e07bc3f19caac098`,
  passed the original cutoff 80 and coefficient 1. Its full complex
  constants, h-1 factor, Euler corrections and all-power loss remain
  intact. No old objection is reopened by the change.
- [RECHECK-REFINEMENT.md](RECHECK-REFINEMENT.md), SHA-256
  `04c1d72040b7497269fc8d6155337d61973d4665c2fa570b490fb6d00befc877`,
  passed `.581` and the enlarged finite fallback. Its optional historical
  cutoff clarification is already reflected in SOURCE-AUDIT.md, SHA-256
  `187e7f639fdee81410d58102aaf042de00a5b5cae6cb715e83e73314a34ad429`.
- The separate guard report at
  `../nonresidue/research/least-nonresidue/GUARD-RECHECK.md`, SHA-256
  `c75db68a3b80e6ebf38232a9298d0be16000898cd229a38045c68c485c28ca31`,
  passed the negative-c2 repair. Its relevant report was read; the
  current guard, five probes and in-memory regression test above confirm
  that this issue remains resolved. No sibling theorem was imported.
- [RECHECK-SHARP.md](RECHECK-SHARP.md), SHA-256
  `a0022a09548046031d05e600d88342c3c544c60e742beb35010f54054e93260e`,
  passed the complete parameter theorem, cutoff 80, sharp coefficient,
  q>=4 strict `.58` subdomain, unique q=3 equality, and all 1274558 new
  finite classes. That is the permitted same-package predecessor for
  the small-q step. It is not an independent review of the changed
  zeta saving, aggregate, power bound or cutoff64 total.

There were no unresolved inherited objections. The frozen inputs correctly
describe Section 9 as awaiting this review. Updating that status belongs
to the parent's subsequent edits, not to this report-only review.

## Limits

H(b), the proofs and analytic inputs of its source papers, classical
completed L-function and Hadamard identities, functional equations,
contour shifts, gamma formulas and convergence facts remain assumptions
at the same boundary as in the predecessor. Their relevant uses and the
new residue algebra were checked; their entire foundations were not
reproved. No OpenAI/Xu--Sang proof or Lean development was replayed.

The independent exact computations use Python integers and rational
arithmetic, with the usual trust in that runtime. Finite checking in this
review covers exactly q=3..20, not every subgroup or the whole earlier
fallback. The large-q proof and uniform parameter proof are analytic.
No optimality of cutoff 64, impossibility of cutoff 63, new T1 claim,
unconditional least-prime result or accepted-frontier improvement is
asserted.

Only this report was written. The frozen inputs were left unchanged;
there were no git mutations, installations, public posts or further
delegation. Unrelated untracked drafts were ignored.
