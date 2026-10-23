**Original idea: Geoffrey Irving.**

# Independent mathematical review, round 2: coefficient 0.581

2026-10-23. Text: CC BY 4.0.

This is a fresh-context, independent **same-model AI review** by Codex
(gpt-6.1-sol). It is not human review. I did not author the refinement and
used no further agents. This report is the only file I wrote.

## Verdict and issues

**Confirmed within the stated conditional and classical-input scope.**
I found no fatal issue, no required mathematical fix, and no numerical
correction. Assuming H(7/8) and the classical analytic inputs below, the
refined application of criterion (13), together with the independently
recomputed finite fallback, proves

    P(a,q) < ((581/1000) phi(q) log q)^8
        for every integer q >= 3 and gcd(a,q) = 1.

The unchanged coset theorem remains

    P(aH,q) < max(80, h log q)^8
        for q >= 3 and h = [G:H] >= 2.

The cubic totient bound, threshold q = 2048, every factor of 1/C and
1/C^2, continuum monotonicity, rational total and margin, strictness,
finite coverage, and coefficient-0.58 obstruction all check out.

One optional documentation clarification: SOURCE-AUDIT.md still describes
the earlier fallback q < 512. Its header and README identify it as the
historical audit preceding the original proof, and RECHECK.md explicitly
pins round 1. Their old cutoffs do not invalidate the current argument.
If those historical documents are meant to describe the current result,
annotate that sentence as historical. PROOF.md, README.md, and constants.py
agree on the current q < 2048 fallback. Their statements that the refinement
is awaiting review accurately describe the frozen snapshot before this
report; the parent can now update that status separately.

## Reviewed snapshot

Repository HEAD was d1f29f2eab57bb0de12465e0e61385d6fea53075, the PR #11
head supplied in the brief. The proof's upstream base is
d2bd5167a42b8256f1362640dc149057920e5db9. The reviewed refinement was
uncommitted: only PROOF.md, README.md, and constants.py were modified at
entry. I read AGENTS.md, DISCOVERY.md, all five existing package files,
the relevant predecessor lemmas and gamma formulas, and ln_bounds.

Seed retained from the brief: f7e9c53c773500cea50225ca67a35d17.
The brief associates this refinement with handoff 19140169 and claim
19141097; I did not independently query those public coordination records.

SHA-256 values of the reviewed files:

| File | SHA-256 |
| --- | --- |
| PROOF.md | 8fc32454c30870a662462104a274a9c05342eea5afb49288affc7fde5529f765 |
| constants.py | e9866ceb4f180a6c7bb240d60baad52784554dae47bc1cf66849668214f19adc |
| README.md | 0f03d7e9c3dd4793c33cfe7d395f27a5faeafcd6da1e6b4b8374c5ae0154da13 |
| SOURCE-AUDIT.md | e138dcd568890957f3d16279700b48fa0b99edcf83733e7cab02eaa1d7190b5d |
| RECHECK.md | 7ba56b4b9fd9afd856c1b310969f018efddea8e6e9ebfdd6e07bc3f19caac098 |
| ../zero-pairing/PROOF.md | 824af09db62887a04107e72f9aafb56345aef45c1ea3ccf6499956d6896e914c |
| ../first-explicit-t1/PROOF.md | abd066b2d27961e93ae007e5fb8897b5a841aff875b24af3eb0216d73bed8cbb |
| ../../verify/check.py | ace2b055b5279284d04d37b6c6dde77af86088245846700c502effb3e812e709 |

I compared the working proof against HEAD using git show, without any git
mutation. Sections 1 through 6, including criterion (13), are byte-identical.
The SHA-256 of that text, from the Section 1 heading up to but excluding
the Section 7 heading, is
b65311fbb897e8b3e89be1428191b5edd8985df8a23cc51e79aba1ed1c316067.
The predecessor proof files and verify/check.py are unchanged from both
HEAD and the pinned upstream base. SOURCE-AUDIT.md and RECHECK.md are
unchanged from HEAD.

## Analytic context and reliance on round 1

I consulted the public [LLS v3 PDF](https://arxiv.org/pdf/1309.3595v3)
and [HTML rendering](https://arxiv.org/html/1309.3595v3), particularly
the residue calculations in Section 2 and the coset method in Section 4.
LLS's stated estimates assume GRH; the new application uses the local
replacements. I did not re-download and hash the source archives in this
round. The source hashes in SOURCE-AUDIT.md and RECHECK.md remain their
authors' recorded evidence.

I rely on round 1's completed detailed audit of the unchanged gamma
estimates, elementary pi/gamma/zeta constants, and residue/Euler-factor
calculations. I reread their use in the proof and checked the connection
to the new application. In particular:

- The two complex residue identities retain the full B_chi. The formal
  residues give -B_chi log X + sum 1/rho^2 in (1), and
  -conjugate(B_chi) - B_chi/X + Z_chi(X) in (2).
- Lemma 0' uses the same-character reflection rho -> 1-conjugate(rho).
  Its weights are A_chi = -Re B_chi, with c2 = 189/125. It applies here
  because X > 400^8 > 256. The fixed complex-B absorption at 2^16 is
  unaffected by the new C.
- The h-1 aggregation at the identity coset is applied before introducing
  the phases for a general coset. The principal zeta term supplies X.
  Euler-factor losses total h omega(q) t^2/2, not merely an unscaled
  omega(q) term.
- The elementary factorial inequality T_zeta(X) <= log X replaces the
  RH-dependent bound in LLS Lemma 2.4. Neither the GRH absorption at
  x = 100 nor LLS's GRH proper-power estimates is imported.
- All proper powers are bounded by sqrt(X) t^2/2. Thus criterion (13)
  includes the essential subtraction h t^2/(2 sqrt(X)).

These checks support reuse of criterion (13); the round-1 conclusion by
itself is not evidence for coefficient 0.581. The new substitutions and
finite cases were checked independently below.

## Cubic totient bound and analytic threshold

For any positive integer q, multiplicativity gives

    phi(q)^3/q^2 = product over p^a || q of p^(a-3) (p-1)^3.

For fixed p the factor increases by p when a increases. Its minimum at
a = 1 is 1/4 for p = 2 and 8/9 for p = 3. For p >= 5,

    (p-1)^3/p^2 = p(1-1/p)^3 >= p(4/5)^3 >= 64/25 > 1.

If 2 or 3 is absent, its contribution is 1, which increases the lower
bound. Hence the product is at least (1/4)(8/9) = 2/9, uniformly;
equality occurs at q = 6. There is no assumption on the number of prime
factors or their exponents.

For every q >= 2048,

    9*96^3 = 7962624 < 8388608 = 2*2048^2,
    phi(q)^3 >= 2*q^2/9 > 96^3.

Thus h = phi(q) > 96, including at q = 2048. Independently certified
log 2 > 2/3 gives L = log q >= 11 log 2 > 22/3. Therefore, with
C = 581/1000,

    y = C h L > C*96*(22/3) = 51128/125 = 400 + 1128/125 > 400.

The proof uses the deliberately weaker h >= 2 and L > 1 thereafter.
They imply

    h <= y/C,  L <= y/(2C),  omega(q) <= L/log 2 < 2L <= y/C.

These inequalities do not assume the old, now false relation hL <= y.
Here hL is exactly y/C.

## Every scaled term and the continuum envelope

Write ell = log y, t = 8 ell, X = y^8. The nonprincipal numerator obeys

    ((h-1)L/2 + t)/y
        <= 1/(2C) + 8 log y/y
        < 1/(2C) + 3/25,

because log y/y decreases for y >= 400 and log 400 < 6.
This is the factor of 1/C in the leading nonprincipal error.

Starting from the actual residual in (11),

    R = log(2pi)t + 1 + h omega(q)t^2/2
          + (h-1)((3L/2+26)t + t^2/2 + 3),

substitution gives exactly the stated upper envelope. Expanded after
division by X, it is

    16 ell/y^8 + 1/y^8
      + 32 ell^2/(C^2 y^6) + 6 ell/(C^2 y^6)
      + 208 ell/(C y^7) + 32 ell^2/(C y^7) + 3/(C y^7).

The two C^(-2) terms charge h omega(q) and hL, respectively.
The remaining nonprincipal residuals have C^(-1). The proper-power
error separately becomes

    h t^2/(2 sqrt(X)) <= 32 (log y)^2/(C y^3).

No factor of C is omitted in the script or the written proof.

For a term (log y)^b/y^a, its derivative has the sign of b-a log y
when b > 0, and it decreases directly when b = 0. Every residual term
has a >= 6, b <= 2; the proper-power term has a = 3, b = 2.
They decrease throughout y >= 400. Also log y/y decreases there, and
the positive reciprocal powers in the d and F envelopes decrease.
These are continuum bounds, not tests of finitely many real y.

At y = 400, replacing log y by 6 gives:

| Quantity | Independently derived exact value/envelope |
| --- | --- |
| Lower d endpoint, omitting positive y^(-8) | 3187903999811/3200000000000 > 249/250 |
| Excess of that lower endpoint over 249/250 | 703999811/3200000000000 |
| F multiplier 1+7/y^6+8/y^7 | 204800000000000351/204800000000000000 < 1001/1000 |
| Expanded residual endpoint | 190638489943417/221223976960000000000000000 < 1/10^9 |
| Zeta error | 231231/4000000000 |
| Nonprincipal error | 2036749/2066700 |
| Charged residual | 1/1000000000 |
| Proper-power error | 9/290500 |
| Sum of four charged errors | 114068220107243/115735200000000 < 1 |
| Positive normalized margin | 1666979892757/115735200000000 |

This proves (13) for q >= 2048. Strictness is sound: a prime exactly
at X has zero weight log(X/X). The strict excess of the coset count
over the proper-power envelope therefore forces a prime strictly below
X, as required by the claimed strict inequality.

This in-memory command reproduces the rational arithmetic without
importing the author script:

    python3 -B - <<'PY'
    from fractions import Fraction as F
    C,y,ell,k = F(581,1000),F(400),F(6),F(189,125)
    d = 1-k*(1/y+1/y**4)
    f = 1+7/y**6+8/y**7
    r = (16*ell/y**8 + 1/y**8
         + 32*ell**2/(C**2*y**6) + 6*ell/(C**2*y**6)
         + 208*ell/(C*y**7) + 32*ell**2/(C*y**7)
         + 3/(C*y**7))
    errors = [F(231,10000)*F(1001,1000)/y,
              F(1001,1000)*(1/(2*C)+F(3,25))/F(249,250),
              F(1,10**9),32*ell**2/(C*y**3)]
    assert d > F(249,250) and f < F(1001,1000)
    assert r == F(190638489943417,221223976960000000000000000)
    assert r < errors[2]
    assert sum(errors) == F(114068220107243,115735200000000) < 1
    assert 1-sum(errors) == F(1666979892757,115735200000000)
    assert C*96*F(22,3) == F(51128,125) > 400
    assert 9*96**3 < 2*2048**2
    print(d, r, sum(errors), 1-sum(errors))
    PY

## Independent finite enumeration and logarithm directions

I enumerated every reduced a in increasing order for each q = 3..2047.
For each class I tested a, a+q, a+2q, ... until prime, using division
by every odd integer through the integer square root, with 2 handled
separately. This uses neither an Eratosthenes sieve, a supplied prime
list, the totient sieve, nor the author's finite-certificate logic.
The totient in this enumeration is the direct gcd count.

I used a different rational logarithm algorithm from ln_bounds:

    -log(1-z) = sum from j=1 to N of z^j/j + positive tail,
    tail <= z^(N+1)/((N+1)(1-z)).

For q = 2^k m, 1 <= m < 2, use z = 1-1/m and add k times the
log 2 enclosure obtained at z = 1/2. All arguments lie in [0,1/2].
N = 80 suffices. The partial sum is a lower bound; adding the displayed
tail is an upper bound. All certificate decisions use exact Fractions.

Every class passed

    least prime < (C phi(q) independent_log_lower(q))^8.

Results:

- 2045 moduli and **1,274,560 reduced classes**.
- Largest least prime: **169937, class 722 modulo 1945**.
- All 87 earlier positive members of that progression are composite.
- The largest ratio of a least prime to its certified lower bound occurs
  at q = 3, a = 1, p = 7.
- SHA-256 of records q,a,p followed by a newline, ordered by q then a:
  d3cbf54f933da04873ff6482d18081a88ac75c626fc3310a64b521ced057c27c.
- The q < 512 prefix independently reproduces round 1: 79,594 classes,
  maximum (p,q,a) = (37363,461,22), record SHA-256
  4dc76edfbf66e13f2f4a17965db5cf67f5d459e5786360d6d2ea99b9c402badd.

A separate summatory calculation using trial-factorized Mobius values
gave sum(phi(q), q=1..2047) = 1274562. Subtracting phi(1)+phi(2) = 2
again gives 1274560.

For the obstruction the direction must reverse: an **upper** log bound
is required. The independent series verifies the rational enclosure

    1098612288668109/10^15 < log 3 < 109861228866811/10^14.

Using its upper endpoint gives the exact rational comparison

    ((29/25)*(109861228866811/10^14))^8
        < 6956960449139/10^12 < 7.

Using its lower endpoint for coefficient 0.581 instead gives

    ((581/500)*(1098612288668109/10^15))^8
        > 7053499582707/10^12 > 7.

Since P(1,3) = 7, coefficient 0.58, and every nonnegative smaller
coefficient, fails the same all-q theorem. The script correctly uses
ln_bounds(3)[1] for this impossibility proof and ln_bounds(q)[0] for
the positive finite certificate. The result makes no optimality claim.

The following command, run from the session root, reproduces the
independent enumeration and the elementary log checks; it writes no files:

    python3 -B - <<'PY'
    from fractions import Fraction as F
    from math import gcd,isqrt
    from hashlib import sha256
    def prime(n):
        if n < 2: return False
        if n % 2 == 0: return n == 2
        return all(n % d for d in range(3,isqrt(n)+1,2))
    def series(z,N=80):
        s,p = F(0),z
        for j in range(1,N+1):
            s += p/j
            p *= z
        return s,s+p/((N+1)*(1-z))
    l2,u2 = series(F(1,2))
    def logs(q):
        k = q.bit_length()-1
        lo,hi = series(1-F(1<<k,q))
        return k*l2+lo,k*u2+hi
    C = F(581,1000)
    assert l2 > F(2,3) and logs(400)[1] < 6
    assert logs(400)[0] > 1
    count,largest,hardest,worst = 0,(0,0,0),None,F(0)
    digest,old_digest = sha256(),sha256()
    old_count,old_largest = 0,(0,0,0)
    for q in range(3,2048):
        residues = [a for a in range(1,q) if gcd(a,q)==1]
        bound = (C*len(residues)*logs(q)[0])**8
        pq,aq = 0,0
        for a in residues:
            p = a
            while not prime(p): p += q
            assert p < bound,(q,a,p)
            count += 1
            if p > pq: pq,aq = p,a
            largest = max(largest,(p,q,a))
            record = (('%d,%d,%d' % (q,a,p))+chr(10)).encode()
            digest.update(record)
            if q < 512:
                old_count += 1
                old_largest = max(old_largest,(p,q,a))
                old_digest.update(record)
        ratio = F(pq)/bound
        if ratio > worst:
            worst,hardest = ratio,(pq,q,aq,len(residues))
    assert count == 1274560 and largest == (169937,1945,722)
    assert hardest == (7,3,1,2)
    assert old_count == 79594 and old_largest == (37363,461,22)
    assert digest.hexdigest() == 'd3cbf54f933da04873ff6482d18081a88ac75c626fc3310a64b521ced057c27c'
    assert old_digest.hexdigest() == '4dc76edfbf66e13f2f4a17965db5cf67f5d459e5786360d6d2ea99b9c402badd'
    lo,hi = F(1098612288668109,10**15),F(109861228866811,10**14)
    l3,u3 = logs(3)
    assert lo < l3 < u3 < hi
    assert (F(29,25)*hi)**8 < F(6956960449139,10**12) < 7
    assert (F(581,500)*lo)**8 > F(7053499582707,10**12) > 7
    assert prime(169937)
    assert all(not prime(722+k*1945) for k in range(87))
    print(count,largest,hardest,digest.hexdigest())
    PY

## Author checker and the five controls

I also ran from repo/:

    python3 -B research/least-prime-progression/constants.py

It exited 0. Both original and refined certificates passed; the printed
refined total and margin, class count, and maximal class match the
independent calculations above. All five controls printed REJECT control.
I called each control separately to inspect its actual rejection:

| Control | Actual ValueError |
| --- | --- |
| c2 = 3/2 | c2 must dominate 4/sqrt(7) |
| Original analytic y_min = 64 | d(X) > 49/50 |
| q = 3, prime list [2,3,5] | prime list does not cover every reduced class modulo 3 |
| q = 3, coefficient 1/2 | progression bound fails at q=3, a=1, p=7 |
| q = 3, coefficient 29/50 | progression bound fails at q=3, a=1, p=7 |

The first two reject failure of the chosen certificate, not impossibility
of some stronger analytic argument. The coefficient-0.58 control itself
tests rejection of a proposed positive certificate; the separate upper-log
comparison supplies the mathematical impossibility proof.

I checked the new coverage optimization directly. In the totient sieve,
values[p] = p detects primes because every composite already had a smaller
prime factor processed. Each update removes exactly one factor (1-1/p).
In increasing prime order, every p not dividing q lies in a reduced class.
Marking only unseen residues records their first primes. With the exact
phi(q), reaching remaining = 0 therefore covers precisely every reduced
class; the last marked prime is their maximum. It is sound to compare
that one maximum per modulus, since the proposed bound depends only on q.

The supplied list in the actual program is the increasing, complete list
from its standard Eratosthenes sieve. Its p*p slice start and slice length
are correct. I additionally trial-divided all 82,025 listed primes through
2^20 and verified membership against independent primality testing for
every integer through 169937, the actual largest coverage endpoint.
I compared every totient-sieve output through q = 2047 with direct gcd
counts, extending the author's check through 512.

The helper presumes an ascending list of genuine primes and an accurate
phi argument, as its internal caller provides. Its explicit incomplete-list
rejection covers failure to reach all classes. No claim is made that it
validates arbitrary unsorted, duplicate, or fabricated caller input.

## Domains, trust boundary, and limitations

The finite range 3 <= q < 2048 and analytic range q >= 2048 meet with no
gap or overlap requirement. H = {1} has h = phi(q) >= 2 throughout q >= 3.
No use is made of LLS's q >= 20000 cutoff, its finite computation, or its
upper restriction X <= (q log q)^2. The coset theorem retains its original
cutoff 80 and has no finite fallback. q = 2 remains excluded in all
current theorem statements. The retained q = 512 endpoint assertions
inside analytic_certificate are checks for the original coefficient-1
application; they do not replace the new q = 2048 certificate.

This review takes classical analytic continuation, functional equations,
Hadamard factorizations, standard gamma identities, and the cited contour
shifts and limiting operations on trust as published inputs. It checks
their stated algebraic use and the new inequalities, not a new proof of
contour convergence. H(7/8) is assumed, not proved. No Lean proof was
replayed or certified. This is neither an unconditional least-prime
theorem nor a new Miller--Rabin frontier, and it does not determine the
optimal progression coefficient.

The existing baseline verifier and unit-test suite were reported passing
in the brief. I did not rerun them: they do not certify this new theorem.
I ran the package checker and all independent computations described here.
No global installation, public write, git mutation, or additional agent
was used. Only public primary-source URLs were sent to web tools; no
unpublished repository contents were sent to an external service.
All local reads and computations used bounded native workspace tools;
the known misbound context-mode filesystem tools were neither widened
nor used to bypass a denial.
