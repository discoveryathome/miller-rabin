Original idea: **Geoffrey Irving**.

# Explicit witnesses at the smaller theta, with C=0.5272

**Status: author-checked and independently AI-rechecked conditional draft,
2026-10-23.** See [RECHECK.md](RECHECK.md) for the fresh-context same-model
review of the C=.528 certificate, exact snapshot hashes and limits.
Section 6's C=.5272 refinement is author-checked and awaiting its own
fresh-context recheck. An AI source-research context proposed the transfer; the parent
checked and packaged the derivation and exact arithmetic. Source research is
not independent theorem verification. This is not an accepted result or a
verification of either half-plane hypothesis. Text: CC BY 4.0; code: Apache-2.0.

Base: `d2bd5167a42b8256f1362640dc149057920e5db9`. Only accepted inputs from
main are used, chiefly the unconditional facts and residue identities in
[first-explicit-t1](../first-explicit-t1/PROOF.md) and the argument of
[zero-pairing](../zero-pairing/PROOF.md). Their accepted status is recorded in
the frontier; their historical draft banners do not change that record.
The parameter transfer is proved below and does not depend on an unmerged
corollary. No accepted record is modified by this package.

## Theorems and assumptions

Let H(b) mean that every Dirichlet L-function, uniformly in modulus and
character and including zeta, has no zero with real part greater than b.
Poles are not zeros. Put

    theta=8748867/10000000,
    K=1/(1-theta)=10000000/1251133,
    PSI_13=3317044064679887385961981.

> Assuming H(theta), every odd composite n>=PSI_13 has a prime Miller--Rabin
> witness p <= ((659/1250) log n)^K.

The same proof also gives the backportable statement under H(7/8), with
exponent 8 and the **same coefficient 659/1250=0.5272**. These are separate
conditional assertions. For either hypothesis, every smaller odd composite
has a witness among primes <=41 by the Sorenson--Webster theorem. Thus a bound
for every odd composite is max(41,((659/1250)log n)^K), taking the relevant K.
All logarithms here are natural.

In the repository's declared per-base bit-cost model, the smaller-theta test
has bit exponent

    2+K=12502266/1251133 < 10,
    10-(2+K)=9064/1251133 > 0.

This is an exact rational comparison. No rounded decimal exponent is used.
The H(7/8) backport has exponent 10. These are asymptotic conditional costs;
this package supplies a theorem and certificates, not a new implementation.

Xu--Sang, *Amplified moments and a refinement of the quasi-Riemann hypothesis*,
[arXiv:2610.15291v2](https://arxiv.org/html/2610.15291v2), Theorem 1.1,
Sections 2 and 7--8 and Appendix G, is the primary reference for theta. Their
scope includes all Dirichlet L-functions and zeta, with principal poles
permitted. Their result is itself conditional on the stated source analytic
inputs and H(7/8). This note assumes H(theta) directly. It does not certify
that preprint, its imported OpenAI inputs, or a Lean replay. The frontier's
A1b remains an open assumption. For imprimitive characters, omitted Euler
factors have zeros only on Re(s)=0, so they do not alter this scope.

## 1. A pairing lemma with its range condition

Let 1/2<=b<1 and assume H(b). For a primitive nonprincipal Dirichlet
character or zeta write

    A=sum_rho Re(1/rho)=|Re B|,

with nontrivial zeros counted with multiplicity. The classical Hadamard
real-part identity and convergence are the accepted facts F1--F2. The
functional equation and conjugation give the involution
rho -> 1-conjugate(rho) on zeros of the **same** L-function, including complex
characters. Therefore 1-b<=Re rho<=b. All regrouped absolute terms and weights
are nonnegative, and their sums converge by the classical zero-counting bound.

Choose R>=b/(1-b) and c>=1/(2 sqrt(b(1-b))). For X>1,

    sum 1/|rho|^2 <= A/(1-b),                                    (P0)
    sum |X^(rho-1)/(rho(rho-1))|
       <= c [X^(b-1)+X^(-1/2)] A.                               (P2)

If also X^(b-1/2)>=R, then

    sum |X^rho/rho^2| <= [X^b+R X^(1-b)] A.                      (P1)

For P1, pair rho=sigma+it with rho'=1-conjugate(rho), sigma>1/2.
Set u=1/|rho|^2, v=1/|rho'|^2. The ratio v/u lies between 1 and
sigma^2/(1-sigma)^2. The pair's absolute contribution divided by its A weight is

    [X^sigma+(v/u)X^(1-sigma)]/[sigma+(1-sigma)(v/u)].

Its derivative with respect to v/u has constant sign. At the two endpoints
the values are X^sigma+X^(1-sigma) and
((1-sigma)/sigma)X^sigma+(sigma/(1-sigma))X^(1-sigma). Both are at most
g(sigma)=X^sigma+R X^(1-sigma). Convexity reduces g to sigma=1/2 or b.
For z=X^(b-1/2),

    [g(b)-g(1/2)]/sqrt(X)=(z-1)(z-R)/z >=0.

A line zero has ratio 2 sqrt(X), also covered since R>=1. This proves P1.
The condition z>=R cannot be omitted from this proof.

For P2 the pair's contribution is
(X^(sigma-1)+X^(-sigma))sqrt(uv), while its A weight is at least
2sqrt(sigma(1-sigma))sqrt(uv). Use sigma(1-sigma)>=b(1-b),
X^(sigma-1)<=X^(b-1) and X^(-sigma)<=X^(-1/2). A line zero has ratio
2 X^(-1/2), also covered since c>=1. Finally P0 is termwise:
Re(1/rho)>= (1-b)/|rho|^2. This establishes the three bounds at all heights.

For both b=theta and b=7/8, take R=7 and c=189/125. More generally these
choices work for 13/15<=b<=7/8 and X>=256. Indeed b/(1-b)<=7,
b(1-b)>=7/64, and

    7*189^2=250047 >250000=16*125^2.

Also b-1/2>=11/30 and 256^11>7^30, so X^(b-1/2)>=7. Positivity of c is
part of the coefficient condition, not merely its squared inequality.

## 2. Residue identities and the character reduction

Use [Lamzouri--Li--Soundararajan, arXiv:1309.3595v3](https://arxiv.org/abs/1309.3595v3),
equations (2.1)--(2.4) and the proofs of Lemmas 2.1--2.3, before their
GRH estimates. Define

    S(X,chi)=sum_{m<=X} Lambda(m) chi(m) log(X/m),
    T(X,chi)=sum_{m<=X} [Lambda(m)/m] chi(m)(1-m/X),
    F(X)=X^b+7X^(1-b),
    c(X)=(189/125)[X^(b-1)+X^(-1/2)],
    d(X)=1+1/X-c(X),    zeta_b=|B_zeta|.

P0--P2 in those residue identities give, when X>=256 and d(X)>0,

    S(X,zeta) >= X-zeta_b F(X)-K zeta_b-log(2pi)log X-1,
    Re S(X,chi) <= A[F(X)+K+log X]
                   +(1/2)log(q/pi)log X+Et_a(X),
    A d(X) <= (1/2)(1-1/X)log(q/pi)-Re T(X,chi)+E_a(X),          (1)

where K=1/(1-b) and a=(1-chi(-1))/2. The positive trivial-zero series in the
zeta identity has been dropped in its lower bound. The four exact functions are

    Et_0=pi^2/24-(gamma_E/2)log X-(log X)^2/2
          -sum_{k>=1} X^(-2k)/(2k)^2,
    Et_1=pi^2/8-(log2+gamma_E/2)log X
          -sum_{k>=0} X^(-2k-1)/(2k+1)^2,
    E_0=-log2-(gamma_E/2)(1-1/X)+(log X+1)/X
          -sum_{k>=1} X^(-2k-1)/(2k(2k+1)),
    E_1=-(gamma_E/2)(1-1/X)+(log2)/X
          -sum_{k>=0} X^(-2k-2)/((2k+1)(2k+2)).                 (2)

These residues, including their signs and gamma factors, are unconditional.
Their standard contour shifts, horizontal limits, functional equations and
Hadamard identities remain declared classical analytic inputs. Only the
zero-sum estimates use H(b); all three such uses have been replaced by P0--P2.

Suppose n is odd composite and there is no prime witness <=X. Conrad,
[*The Miller--Rabin test*](https://kconrad.math.uconn.edu/blurbs/ugradnumthy/millerrabin.pdf),
Theorem 4.1 proof, Cases 1--2, places the strong liars in a proper subgroup H
of (Z/nZ)*, including prime powers. A prime dividing n is a witness, so no
prime <=X divides n. A nontrivial character trivial on H then equals 1 on
every prime <=X, hence on every positive integer <=X. Its primitive inducing
character chi has conductor q>=3 dividing n and has the same values there.
Consequently S(X,chi)=S(X,zeta), T(X,chi)>=0, and log q<=L=log n.

For X>=64, Section 3 proves E_a<=0. Thus (1) gives A<=L/(2d(X)). This also
covers q=3: if log(q/pi)<0 its occurrence on the right of (1) is negative,
and is still <=L. No positivity of that logarithm is assumed.

## 3. Exact elementary constants and gamma signs

All numerical decisions in constants.py are rational. Machin's identity
pi=16 atan(1/5)-4 atan(1/239), with alternating series and first omitted
terms, gives 31415926/10000000<pi<31415927/10000000. For N=256 put
A_N=H_N-log N-1/(2N). Then

    A_N < gamma_E < A_N+1/(8N^2).

To justify this enclosure, A_(j+1)-A_j is the trapezoid error for integrating
1/t on [j,j+1], equal to (1/2)integral(t-j)(j+1-t)(1/t)''dt.
It is positive and <=(1/8)(1/j^2-1/(j+1)^2). Telescope to infinity.
The exact atanh logarithm bounds in the unchanged verifier then prove

    zeta_b=1+gamma_E/2-log(4pi)/2 <231/10000,
    log(2pi)<18379/10000,
    .693<log2<.694,  4.158<log64<4.16,
    gamma_E>.577,  pi^2/24<.42,  pi^2/8<1.24.                    (3)

Dropping the negative series in (2), for every X>=64 these imply

    E_0 <= -.693-(.577/2)(63/64)+(4.16+1)/64=-22947/25600<0,
    E_1 <= -(.577/2)(63/64)+.694/64=-34963/128000<0,
    Et_0 <= .42-(4.158)^2/2=-4112241/500000,
    Et_1 <= 1.24-(.693+.577/2)(4.158)=-2841077/1000000.

Uniformity follows because 1-1/X increases, (log X+1)/X and 1/X decrease,
and the negative logarithmic terms increase in magnitude. Since K<=8,

    K zeta_b+1+Et_a <8(.0231)+1-2.84=-2069/1250<0.               (4)

Thus delta=0 below is justified analytically, without sampling X.

## 4. Directed powers and the complete T1 inequality

For either b=theta or b=7/8, write y=X^(1-b), so X=y^K and 7<K<=8.
For y>=29, the following are upper bounds in the required direction:

    X^(b-1)=1/y,
    X^(-1/2)=y^(-K/2)<=y^(-3),
    X^(1-2b)=y^(2-K)<=y^(-5),
    log X/X^b=K log y/y^(K-1)<=8 log y/y^6.                     (5)

Also X>=29^7>256. The function log y/y^6 decreases here. Put

    Dmin=1-(189/125)(1/29+1/29^3)=2889487/3048625>0,
    b1=1/(2Dmin)=3048625/5778974,
    s=1/29^5,
    a=8(33673/10000)/29^6=33673/743529151250.

The verifier's exact enclosure proves log29<33673/10000. Hence d(X)>=Dmin,
A<=b1 L, F(X)<=X^b(1+7s) and log X<=a X^b. Subtract the upper S bound
in (1) from the lower one, using equality of S. It gives

    0 >= X-X^b{[b1(1+7s+a)+a/2]L
                    +zeta_b(1+7s)+log(2pi)a}
           -[K b1 L+K zeta_b+1+Et_a(X)].                       (6)

The last three terms apart from K b1 L are nonpositive by (4). Exact rational
comparisons, deliberately using 8 rather than K for this static charge, give

    alpha_need=566685633068042594/1074208908328954375
                 <10551/20000,
    beta_need=171755911431067/7435291512500000 <29/1250,
    gamma_need=12194500/2889487 <4221/1000.

Therefore, for either b under its own H(b), y>=29 and odd composite n,

    X-X^b[(10551/20000)log n+29/1250]-(4221/1000)log n>0          (T1)

implies a prime witness <=X. This is the complete proposed template, with
w1=1, delta=0, y_min=29. It retains the exact K in the final witness exponent.

## 5. Substitution for all n>=PSI_13

The baseline certificate takes C=66/125,D=0 and the coefficients in (T1).
It is retained in the checker as an in-memory positive control for both
half-planes. The unchanged verifier reduces its inequality to

    g(L)=(9/20000)L-29/1250-(4221/1000)L/(C L)^(K-1)>0.

Its tail decreases for L>0 since K-1>1; its linear slope is positive.
For l0 the exact rational lower bound for log PSI_13, it certifies
C l0>29811/1000>29 and, even using the larger tail with integer exponent6,

    (9/20000)l0-29/1250-((4221/1000)l0)/(C l0)^6
       >2207/1000000>0.

This proves the full half-line, not a finite sample. At b=7/8 the verifier
uses floor(K-1)=7 and a still smaller tail. Below PSI_13 the unconditional
[Sorenson--Webster theorem](https://arxiv.org/pdf/1509.00864), Theorem 1.1,
supplies the first thirteen prime bases <=41. Its exhaustive minimality
computation is a cited input, not reproduced here.

## Evidence, controls and limits

Run from the repository root:

```sh
python3 research/zero-pairing/constants.py
python3 research/lower-theta/constants.py
python3 verify/check.py all
python3 -m unittest discover -s tests
```

The new checker certifies (3)--(6), Section 6's refinement, both current claim
files and the exact bit exponent. Its ten historical rejection controls
target the retained baseline: the endpoint C=.5279, the negative
slope C=.5275, y_min=30, a rounded-down bit exponent, insufficient alpha,
insufficient or negative pairing coefficients, and the unsafe copied integer
powers 4,6,7 in (5). For theta<7/8 these old powers underestimate the actual
terms. The old logarithmic cap is also disproved by
K[1+(8-K)log29_lo]>8 and exp(u)>=1+u. These are algebraic controls, not
counterexamples involving actual L-function zeros. In particular, rejecting
a coefficient with the old template does not refute the refined template.
Three additional controls exercise the new cutoff, alpha and integer-power
factor described in Section 6. Display-only floating
metrics from the shared verifier never decide a certificate comparison.

Task: `explicit-lower-theta`, catalog revision 5, original seed
`f7e9c53c773500cea50225ca67a35d17`; this is a concrete priority follow-on
after the corollaries on the supplied draw. Predecessors: Geoffrey Irving;
Bach; Lamzouri--Li--Soundararajan; Claude's accepted first-T1 and zero-pairing
packages, PRs #6 and #8; Xu--Sang for the proposed smaller half-plane;
Conrad for the subgroup reduction; Sorenson--Webster for the small-n theorem.
Codex source, author and review contexts are recorded separately.

Not checked here: either H(b), Xu--Sang's analytic inputs or proof, a Lean
replay, new proofs of the classical Hadamard and contour foundations, actual
zero calculations, the exhaustive pseudoprime search, optimal constants, or
the repository's bit-cost model from first principles. Maintainer acceptance
remains pending. The exact arithmetic is evidence for the written derivation,
not a replacement for its analytic assumptions or independent review.

## 6. A sharper rational endpoint certificate

For either b=theta or b=7/8, write r=1/(1-b) and put

    Y=14883/500=29.766,   Q=28.

The stronger hypothesis range used here has
r/2-3>99/100 and r-7>99/100. The exact integer comparison
Y^99>28^100 proves Y^(99/100)>28. Consequently, for every y>=Y,

    X^(-1/2)=y^(-r/2) <=1/(28y^3),
    X^(1-2b)=y^(2-r) <=1/(28y^5),
    log X/X^b=r log y/y^(r-1) <=8 log y/(28y^6).                  (7)

The factor 28 is uniform for all larger y; it is not a numerical fractional
power evaluated only at the endpoint. A rational logarithm enclosure gives
log Y<17/5, and log y/y^6 decreases throughout this range. Thus the Section 4
derivation applies with

    Dmin=1-(189/125)[1/Y+1/(28Y^3)]
        =115895402389/122097755681>0,
    b1=1/(2Dmin),   s=1/(28Y^5),   a=8(17/5)/(28Y^6)=34/(35Y^6).

The exact required coefficients now are

    alpha_need=238168329447264162697001708275930457
                /452139580341872249446204481994840666 <13169/25000,
    beta_need=17573285443376355449035050473
                /760748194917465671495023830000 <29/1250,
    gamma_need=488391022724/115895402389 <843/200.

All gamma signs and the nonpositive static delta charge in Section 3 remain
in range. In particular, no new analytic residue identity is assumed.
The resulting refined T1 is

    X-X^b[(13169/25000)log n+29/1250]-(843/200)log n>0,            (T1r)

for y=X^(1-b)>=Y, implying a prime Miller--Rabin witness <=X.
The two current candidate JSON files record precisely this template and
C=659/1250,D=0. The older T1 remains a separately checked positive control.

At the lower logarithm enclosure l0 for PSI_13, exact rational arithmetic
gives y0=(659/1250)l0>Y and

    (11/25000)l0-29/1250-[(843/200)l0]/y0^6 >41/25000>0.          (8)

Since r-1>=6 and y0>1, the integer power6 enlarges the true subtracted tail.
The positive slope is 11/25000; the tail is proportional to L^(2-r) and
decreases for L>0. Thus (8) proves the entire n>=PSI_13 domain at both
half-planes, and the unchanged small-n fallback completes the theorem.
The exact witness and bit exponents are unchanged.

The three new rejection controls have specific meanings: C=.5271 falls
below the fixed cutoff Y at PSI_13; alpha=.52675 is below its required
coefficient; and the proposed power factor29 fails Y^99>29^100. These
reject this certificate, not every possible proof with altered constants.
Together with the ten retained baseline controls, all thirteen must reject.
This refinement is author-checked; its separate fresh-context recheck is
pending. The earlier report does not certify the changed coefficients.
