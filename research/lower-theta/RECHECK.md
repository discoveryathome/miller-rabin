Original idea: **Geoffrey Irving**. Text: CC BY 4.0.

# Independent recheck of the frozen lower-theta contribution

**Verdict: PASS for the stated conditional contribution; no blocking finding.**
I found no error requiring a change to the five frozen inputs. The derivation
supports C=66/125 under H(8748867/10000000), with witness exponent
10000000/1251133, and separately under H(7/8), with witness exponent 8.
Both statements cover n>=PSI_13; the cited small-n theorem completes the
all-odd-composite domain. This is evidence for maintainer review, not acceptance,
a human review, a formal proof, or verification of either hypothesis.

Review date: 2026-10-23. Reviewer: a separate Codex / gpt-6.1-sol context,
given the task brief without the parent's conversation history. This is a
same-model AI review. I read AGENTS.md, DISCOVERY.md and the accepted frontier
first. I did not read SOURCE-DRAFT.md, reuse an earlier theorem review, delegate
further, change a frozen input, change git state, install anything, or publish
anything. The only review artifact written is this file.

Worktree: `/root/.t3/scratch/2026-10-23-fetch-https-discoveryathome-org-v0-7d492a7d/theta`.
Branch: `session/20261023-lower-theta`. HEAD and accepted base were both
`d2bd5167a42b8256f1362640dc149057920e5db9`. The new package and candidates
were untracked at review time; that commit alone does not identify their bytes.
Their SHA-256 hashes below do. The shared verifier and tests were byte-for-byte
unchanged from the accepted base.

## Findings from the written argument

1. **The pairing transfer is valid, including its range restriction.**
   In PROOF.md lines 61–114, the functional equation first sends a zero of chi
   to 1-rho for conjugate(chi); conjugation then sends it to
   1-conjugate(rho) for chi itself. This preserves multiplicity and height,
   including for complex characters. For fixed X, the absolute summands and
   the weights Re(1/rho) are nonnegative and O(1/t^2) at large height;
   classical zero counting makes the sums convergent. Reflection pairs can
   therefore be regrouped without a conditional-convergence issue.

   Writing r=v/u, I independently obtain the two endpoint ratios
   X^sigma+X^(1-sigma) and
   ((1-sigma)/sigma)X^sigma+(sigma/(1-sigma))X^(1-sigma).
   The derivative in r has constant sign. Each endpoint is bounded by
   g(sigma)=X^sigma+R X^(1-sigma). Convexity and
   (g(b)-g(1/2))/sqrt(X)=(z-1)(z-R)/z, z=X^(b-1/2), give P1
   when z>=R. The proof explicitly imposes this condition. With R=7,
   b in [13/15,7/8] and X>=256, the integer comparison 256^11>7^30
   certifies it. Critical-line zeros are counted once per multiplicity:
   their ratios are 2sqrt(X) in P1 and 2/sqrt(X) in P2, both covered.

   For P2, |rho-1|=|rho'| and weighted AM–GM give exactly the displayed
   denominator 2sqrt(sigma(1-sigma)). The positive c2=189/125 works because
   7*189^2=250047>250000=16*125^2. P0 follows termwise from
   Re(rho)>=1-b. These are proofs at every height, not conclusions from a grid.

2. **The analytic identities are used before their GRH estimates.**
   I compared Section 2 with the primary
   [LLS v3 text, Section 2 and the proofs of Lemmas 2.1–2.3](https://arxiv.org/html/1309.3595v3#S2),
   also consulting the [versioned PDF](https://arxiv.org/pdf/1309.3595v3).
   The four E/Et functions, parity factors, series indices and signs agree.
   The three zero-sum replacements are P0 for the static sum, P1 for the
   X^rho/rho^2 sum, and P2 for the X^(rho-1)/(rho(rho-1)) sum.
   In particular, the real part of the latter identity has
   A(1+1/X)+Re(zero sum), so its lower bound is A*d(X), with the
   minus sign in d(X) as written. The upper S bound has +A log X.
   No critical-line identity is retained after replacing these estimates.

   I also checked that the real-B identity does not import GRH: Hadamard
   logarithmic differentiation at 1 gives
   Re(xi'/xi)(1)=Re B+2*sum Re(1/rho), using reflection; the functional
   equation gives Re(xi'/xi)(1)=-Re B. Thus Re B=-sum Re(1/rho).
   The general analytic foundations needed to justify these operations are
   declared trusted inputs, as distinguished below.

3. **The reduction to a primitive character covers prime powers.**
   [Conrad, Theorem 4.1, proof Cases 1–2, pages 7–8](https://kconrad.math.uconn.edu/blurbs/ugradnumthy/millerrabin.pdf)
   supplies the claimed proper subgroup for every odd composite. In the
   prime-power case its elements satisfy a^(p-1)=1 modulo p^e; an element
   of order p proves properness. In the other case Conrad constructs a
   proper subgroup by the maximal squaring level and CRT. A nontrivial
   character of the quotient then gives the required character. With no
   prime witness <=X, no such prime divides n; induction to the primitive
   character preserves all values at integers <=X. Its conductor q>=3
   divides n. Hence S agrees with the zeta sum and T>=0. The separate
   handling of log(q/pi)<0 at q=3 is valid.

4. **The elementary constant bounds and remainder signs are correct.**
   For A_j=H_j-log j-1/(2j), direct subtraction gives

       A_(j+1)-A_j = (1/j+1/(j+1))/2 - integral_j^(j+1) dt/t
                    = (1/2) integral_j^(j+1) (t-j)(j+1-t)(1/t)'' dt.

   This is positive. Since (t-j)(j+1-t)<=1/4 and (1/t)''=2/t^3,
   it is at most (1/8)(1/j^2-1/(j+1)^2). Telescoping to gamma_E
   proves A_N<gamma_E<A_N+1/(8N^2), with the signs used in the draft.
   The independent integer computation below uses N=512 and a different
   pi identity and logarithm expansion. It confirms all bounds in (3),
   including zeta_b<.0231 and log(2pi)<1.8379.

   Dropping the negative series and using monotonicity for X>=64 gives
   E_0<=-22947/25600, E_1<=-34963/128000,
   Et_0<=-4112241/500000 and Et_1<=-2841077/1000000.
   Thus E_a<0 and Et_a<-2.84 uniformly. Since K<=8,
   K*zeta_b+1+Et_a<-2069/1250<0. This justifies delta=0 for
   the entire required range; an endpoint sample alone would not suffice.

5. **The directed powers, coefficients and T1 subtraction check out.**
   For each of the two b values, 7<K<=8. Since y>=29>1,
   y^(-K/2)<=y^-3, y^(2-K)<=y^-5 and
   K log(y)/y^(K-1)<=8 log(y)/y^6. Also log(y)/y^6 decreases here.
   The extra +1/X in d(X) can safely be dropped in its lower bound.
   Independently clearing integer denominators gives

       Dmin      = 2889487/3048625 > 0,
       b1        = 3048625/5778974,
       alpha_need= 566685633068042594/1074208908328954375
                 = .5275376406527684... < 10551/20000,
       beta_need = 171755911431067/7435291512500000
                 = .0231000911184606... < 29/1250,
       gamma_need= 12194500/2889487
                 = 4.2202993126461548... < 4221/1000.

   Subtracting the upper character S bound from the lower zeta bound
   gives (6), including the sign of Et_a in its final bracket. Under the
   no-witness assumption, X is at most the stated majorant with the
   negative static charge. Dropping that charge and enlarging the three
   coefficients yields precisely T1, so its strict positive inequality
   contradicts the no-witness assumption. This checks the analytic step
   that the shared substitution verifier cannot prove.

6. **Both substitutions hold on the whole half-line.**
   I inspected verify/check.py, especially lines 103–156, rather than
   treating its PASS as proof of its algebra. Division by X^b gives

       g(L)=(9/20000)L-29/1250-(4221/1000)L/(C L)^(K-1).

   Its slope is positive. Its subtracted tail is a positive constant
   times L^(2-K), so it decreases for every L>0. The verifier's general
   derivative test and its use of an exact rational logarithm lower bound
   have the same direction. At the smaller theta, floor(K-1)=6; at 7/8
   it equals 7. Replacing K-1 by either appropriate floor enlarges the
   tail because C L>1. All deciding comparisons are rational; floats
   occur only in reports or rejection messages.

   My separate logarithm computation proves

       56.461116 < log(PSI_13) < 56.461117,
       C*56.461116 = 29.811469248 > 29,
       g_6(56.461116) = .0022071626806533... > 2207/1000000,

   where g_6 uses the larger tail exponent 6 for both claims. The decimal
   is display only: the command below certifies the strict comparison by
   integer cross multiplication. Monotonicity proves every n>=PSI_13,
   including equality at the threshold. Below it,
   [Sorenson–Webster, Theorem 1.1](https://arxiv.org/pdf/1509.00864)
   gives PSI_13=3317044064679887385961981 as the first composite passing
   the first thirteen prime bases, whose largest is 41. Thus there is no
   gap between the two domains. The published minimality computation is
   a cited input, not something the repository's small-n sanity run proves.

7. **The exponent and negative controls have the claimed meaning.**
   Exact integer arithmetic gives 2+K=12502266/1251133 and
   10-(2+K)=9064/1251133>0. Under H(7/8) the exponent is exactly 10.
   These costs use the repository's declared bit-cost model.
   All ten controls rejected for their intended reason:

   - C=.5279: endpoint inequality not established;
   - C=.5275: negative linear slope, hence large-n failure of this template;
   - y_min=30: the threshold substitution is below the template's range;
   - bit exponent 9.9927: below the exact exponent;
   - alpha=.52753: below the required coefficient;
   - c2=3/2: below the certified pairing threshold;
   - negative c2: violates the explicit positivity guard;
   - half-power 4, paired-power 6, and logarithmic-power 7: each violates
     its directed exponent inequality at the smaller theta.

   The controls include reason-string checks, not merely catching any error.
   The negative-c2 check rejects before any denominator or coefficient
   calculation. The independent command also proves
   K*(1+(8-K)*log29_lower)>8; exp(u)>=1+u then shows that the old
   logarithmic cap actually underestimates the term at y=29. A rejected
   certificate is not a counterexample to an L-function theorem or to the
   existence of some better witness bound.

## Source scope and analytic trust boundaries

The primary [Xu–Sang v2 theorem](https://arxiv.org/html/2610.15291v2#S1.SS2)
states the boundary 8748867/10000000 for every finite-order Hecke L-function
in its family and for every Dirichlet L-function, explicitly including zeta
and permitting principal poles at 1. Section 2 and Appendix G make imported
OpenAI analytic results hypotheses, in addition to the family-wide 7/8
half-plane. Sections 7–8 retain that dependency in the two-stage conclusion
and its Dirichlet transfer. I checked this scope and dependency, not the
validity of those analytic inputs or the new proof. Omitting or restoring
Euler factors introduces zeros only on Re(s)=0. The frozen contribution
correctly assumes H(theta) directly and does not claim that H(7/8) alone
establishes the smaller half-plane. The backport is a separate conditional
assertion under H(7/8).

The classical functional equations, analytic continuation, order-one
Hadamard products, zero counting, and the contour-shift and horizontal-limit
justifications are trusted analytic foundations. I checked their use and
the resulting residue signs, not new proofs of those foundations from
first principles. LLS's RH/GRH lemma statements themselves are not being
imported as unconditional estimates. The accepted first-T1 and zero-pairing
packages are the declared predecessors, and their historical draft banners
do not override discover/frontier.json.

Neither this review nor a passing arithmetic checker proves H(theta),
H(7/8), the imported OpenAI inputs, Xu–Sang's analytic proof, a Lean replay,
the pseudoprime search's exhaustive minimality, or the bit-cost model from
first principles. There was no calculation of actual L-function zeros,
optimization claim, or formal verification. A fresh AI context and a
different arithmetic route reduce some correlated mistakes but do not
remove same-model conceptual errors. Maintainer and human mathematical
review remain necessary for acceptance.

## Reproduce the observed checks

From the theta repository root, with Python standard library only:

```sh
export PYTHONDONTWRITEBYTECODE=1
python3 research/zero-pairing/constants.py
python3 research/lower-theta/constants.py
python3 verify/check.py all
python3 -m unittest discover -s tests
```

All four commands exited 0 under Python 3.13.5. The new checker passed both
new candidate files and all ten rejection controls. The shared checker's
displayed endpoint lower bounds were .00220716 and .00220749, respectively.
The unittest suite ran 16 tests, all passing. The shared small-n sanity run
checked odd inputs through 2000001 and the recorded PSI_12/PSI_13 examples;
it did not replay the cited exhaustive search. The accepted zero-pairing
script's floating grid is only a sanity check and was not used as proof.

### Independent calculation without either author checker

The following standalone command imports neither verify/check.py nor
constants.py and does not use Fraction or floating-point decisions. It uses
integer fixed-point intervals at scale 10^55. After reducing a/b to [1,2),
log(a/b) is computed from -log(1-z)=sum(z^j/j), z=(a-b)/a<=1/2.
The positive omitted tail is at most z^(M+1)/((M+1)(1-z)); every division
is rounded outward with integer floor/ceiling. This differs from the
author's atanh series. The pi calculation uses
pi=4*(atan(1/2)+atan(1/3)), rather than Machin's identity, with alternating
series errors. Gamma uses the independently checked trapezoid enclosure
at N=512. Coefficients and the endpoint are checked by integer cross products.

```sh
python3 - <<'PY'
from math import gcd

S = 10**55
M = 240

def ceildiv(a, b):
    return -(-a // b)

def unitlog(a, b):
    assert b <= a <= 2*b
    z = a-b
    pn, pd = z, a
    lo = hi = 0
    for j in range(1, M+1):
        lo += S*pn // (j*pd)
        hi += ceildiv(S*pn, j*pd)
        pn *= z
        pd *= a
    hi += ceildiv(S*pn*a, (M+1)*pd*b)
    return lo, hi

def logI(n, d=1):
    assert n > 0 and d > 0
    k, a, b = 0, n, d
    while a < b:
        a *= 2
        k -= 1
    while a >= 2*b:
        b *= 2
        k += 1
    u, v = unitlog(a, b)
    p, q = unitlog(2, 1)
    return (u+k*p, v+k*q) if k >= 0 else (u+k*q, v+k*p)

def atanI(q):
    lo = hi = 0
    for j in range(110):
        d = (2*j+1)*q**(2*j+1)
        l, h = S//d, ceildiv(S, d)
        if j % 2:
            lo -= h
            hi -= l
        else:
            lo += l
            hi += h
    e = ceildiv(S, 221*q**221)
    return lo-e, hi+e

a, b = atanI(2)
c, d = atanI(3)
piLo, piHi = 4*(a+c), 4*(b+d)
assert 31415926*S < 10**7*piLo < 10**7*piHi < 31415927*S
N = 512
hLo = sum(S//j for j in range(1, N+1))
hHi = sum(ceildiv(S, j) for j in range(1, N+1))
lN, hN = logI(N)
gLo = hLo-hN-ceildiv(S, 2*N)
gHi = hHi-lN-S//(2*N)+ceildiv(S, 8*N*N)
assert 1000*gLo > 577*S
log4piLo = logI(4*piLo, S)[0]
assert 10000*(2*S+gHi-log4piLo) < 462*S
assert 10000*logI(2*piHi, S)[1] < 18379*S
l29, h29 = logI(29)
assert h29*10000 < 33673*S and 6*l29 > S
assert 693*S < 1000*logI(2)[0] < 1000*logI(2)[1] < 694*S
assert 4158*S < 1000*logI(64)[0] < 1000*logI(64)[1] < 4160*S
assert 100*piHi*piHi < 42*24*S*S
assert 100*piHi*piHi < 124*8*S*S
assert -693*128-577*63+516*20 == -22947*5
assert -577*63+694*2 == -34963
assert 42*20000-4158**2 == -4112241*4
assert 124*20000-(2*693+577)*4158 == -2841077*2
assert 8*231+10000-28400 == -2069*8

Dnum = 125*29**3-189*(29**2+1)
Dden = 125*29**3
assert (Dnum, Dden) == (2889487, 3048625) and Dnum > 0
T = 10000*29**6
an = Dden*(T+70000*29+8*33673)+Dnum*8*33673
ad = 2*Dnum*T
bn = 231*(T+70000*29)+18379*8*33673
bd = 10000*T
gn, gd = 4*Dden, Dnum
assert an*20000 < 10551*ad
assert bn*1250 < 29*bd
assert gn*1000 < 4221*gd
assert 7*189**2 > 16*125**2
assert 256**11 > 7**30 and 29**7 > 256

psi = 3317044064679887385961981
lpsi, hpsi = logI(psi)
p, q = lpsi*10**6//S, 10**6
assert p == 56461116 and hpsi*10**6 < 56461117*S
assert p*S <= q*lpsi
Y, Z = 66*p, 125*q
assert Y*1000 > 29811*Z
Gnum = (9*p-464*q)*Y**6-84420*p*Z**6
Gden = 20000*q*Y**6
assert Gnum*10**6 > 2207*Gden
assert 10**7*(1251133*S+9064*l29) > 8*1251133**2*S
for tnum, tden in [(8748867, 10000000), (7, 8)]:
    assert 13*tden <= 15*tnum and 8*tnum <= 7*tden
    kn, kd = tden, tden-tnum
    assert 7*kd < kn <= 8*kd
    assert 2*3*kd <= kn and 5*kd <= kn-2*kd and 6*kd <= kn-kd
    assert tnum//kd in (6, 7)
assert 2*1251133+10000000 == 12502266
assert 10*1251133-12502266 == 9064
for label, n, d in [('alpha', an, ad), ('beta', bn, bd), ('gamma', gn, gd)]:
    g = gcd(n, d)
    print(label, str(n//g)+'/'+str(d//g))
print('coarse L lower:', str(p)+'/'+str(q))
print('g_6(coarse L) > 2207/1000000: PASS')
print('INDEPENDENT INTEGER FIXED-POINT CERTIFICATE: PASS')
PY
```

## Exact reviewed hashes

SHA-256, relative to the worktree root. The five new frozen inputs are first;
the remaining entries pin the protocol and principal supporting artifacts.
This review's conclusions apply to these bytes. A changed proof, checker,
coefficient, assumption or domain needs a corresponding recheck.

```text
f6b90d51399c723202543a4d8727a0b42a4c9f7c5d748754967c3a80fb2f0a9f  research/lower-theta/PROOF.md
5f1c91d03cd0452cffbcc840b1a5fe4610081f769cdd04b67061f965f6f0bd3f  research/lower-theta/constants.py
d57b986b9f8dde4da7a56431fa22306a96179d1653d2c73685cf540a94729ec1  research/lower-theta/README.md
7b98ca2e74e4b08d81ec9b70f2430f333544241a62ca3bb5444f912f2fce55d5  candidates/explicit-t1-lower-theta.json
6a735a697c472ff91e8c778f746c8c0961c0d3a316e31cd79cf2f775b8019b4f  candidates/explicit-t1-paired-refinement-7-8.json
e8f93ce38983d792791c3f9ad9b8b0a367668b3b7b945b071b6f360c45babd62  AGENTS.md
e603c2aaf4b9c692b315213f6c7dd5aebdfba5932e67155e53c76a6590ec4ddf  DISCOVERY.md
9ca629138c133ac8547efba9b47f4d862ae82e7079c4da0998961d8fa5c964a4  discover/frontier.json
ace2b055b5279284d04d37b6c6dde77af86088245846700c502effb3e812e709  verify/check.py
ba252ae554ac3f4ca372b692ef6ed7966772716dfa57c5b65ed22ae84fe5a1f1  verify/mr.py
1e5f766a3b3c39c9d03263056cf636a1b06c8f5e2ed9d3e1c8f1d1e2926b6082  tests/test_check.py
91343a3289cccfd69b022478412e44d53fe1354f7808da8e24c392b9e1be21f5  docs/template-T1.md
09b128dc0febdd15768b00c12fad6a4ec4ce4aa8cba774d6721b9f80675f2c8e  docs/verifier.md
824af09db62887a04107e72f9aafb56345aef45c1ea3ccf6499956d6896e914c  research/zero-pairing/PROOF.md
b71772dee37a2b068677c2800c2dce6d0737a94d03380f47b2f9d87ec6e610a7  research/zero-pairing/constants.py
abd066b2d27961e93ae007e5fb8897b5a841aff875b24af3eb0216d73bed8cbb  research/first-explicit-t1/PROOF.md
```

To check this manifest without creating another file, run from the worktree root:

```sh
python3 - <<'PY'
from pathlib import Path
import hashlib
text = Path('research/lower-theta/RECHECK.md').read_text()
manifest = text.split('```text\n', 1)[1].split('```', 1)[0]
for line in manifest.splitlines():
    expected, name = line.split(None, 1)
    actual = hashlib.sha256(Path(name).read_bytes()).hexdigest()
    assert actual == expected, name
print('reviewed manifest: PASS')
PY
```
