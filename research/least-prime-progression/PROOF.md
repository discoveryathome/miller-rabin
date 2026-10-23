**Original idea: Geoffrey Irving.**

# Least primes in cosets and progressions under half-plane hypotheses

AI-authored conditional research draft (Codex), 2026-10-23. Text: CC BY 4.0;
code: Apache-2.0. The coset theorem and original coefficient-1 corollary passed
a separate fresh-context same-model AI recheck; see [RECHECK.md](RECHECK.md).
The coefficient-0.581 refinement also passed a separate fresh-context same-model
AI recheck; see [RECHECK-REFINEMENT.md](RECHECK-REFINEMENT.md). Both reports pin
their reviewed snapshots. The parameter transfer and sharp coefficient in
Section 8 passed their own fresh-context same-model AI recheck; see
[RECHECK-SHARP.md](RECHECK-SHARP.md).
The cutoff-64 improvement in Section 9 passed its own fresh-context same-model
AI recheck; see [RECHECK-CUTOFF.md](RECHECK-CUTOFF.md). Its exact reviewed
inputs are preserved in commit 0dabf63ca292550e4705e8cc3f847b3a28bd6a7a;
subsequent edits record status, links and the updated next question only.
Maintainer review is pending.

This builds on Bach's conditional least-prime method, Lamzouri--Li--Soundararajan
(LLS), and the accepted AI-authored first-T1 and zero-pairing packages by Claude
(PRs [#6](https://github.com/discoveryathome/miller-rabin/pull/6) and
[#8](https://github.com/discoveryathome/miller-rabin/pull/8)).
Their accepted status is recorded by `discover/frontier.json`; historical draft
labels in the proof files are not the record of acceptance.

## Result and scope

Assume **H(7/8)**: no Dirichlet L-function, including the zeta case, has a
nontrivial zero with real part greater than 7/8. All logarithms are natural.
Let q >= 3, G = (Z/qZ)*, and let H be a subgroup of index h = [G:H] >= 2.
For any a in G, let P(aH,q) be the least prime whose residue lies in aH.

> **Theorem.** Under H(7/8),
>
> P(aH,q) < max(80, h log q)^8.
>
> **Arithmetic-progression corollary.** For every q >= 3 and gcd(a,q) = 1,
>
> P(a,q) < (0.581 phi(q) log q)^8.

Section 8 strengthens this to the **sharp all-q coefficient**
`c_b=7^(1-b)/(2 log3)` for every b in [13/15,7/8], under H(b), with exponent
`r=1/(1-b)` and a non-strict inequality. Equality occurs exactly for
q=3,a=1. It also preserves the coset cutoff 80 with exponent r. In particular,
the two original strict inequalities remain true with exponent
10000000/1251133 under the separate assumption H(8748867/10000000).
Section 9 further lowers the coset cutoff to 64 throughout the same b interval;
the cutoff-80 certificate remains a positive control.

There is no small-modulus computation in the original cutoff-80 coset theorem.
The cutoff-64 improvement uses the progression theorem for q<=20. That
progression theorem has an exact finite check for 3 <= q < 2048, described below.
The assertion excludes q = 2. No assertion about the truth of H(7/8), an
unconditional Linnik constant, optimal coset cutoff, or a Miller--Rabin improvement
is made.

## Pinned inputs

- [LLS, arXiv:1309.3595v3](https://arxiv.org/abs/1309.3595v3),
  Theorem 1.4, Corollary 1.2, the residue calculations in Lemmas 2.1--2.3,
  Lemma 3.1 and Section 4. The PDF's printed pages 13--16 contain Section 4.
  [SOURCE-AUDIT.md](SOURCE-AUDIT.md) records the GRH dependencies being replaced.
- [`../zero-pairing/PROOF.md`](../zero-pairing/PROOF.md), Lemma 0', and
  [`../first-explicit-t1/PROOF.md`](../first-explicit-t1/PROOF.md), facts F1--F2
  and Lemma 0. Base commit: `d2bd5167a42b8256f1362640dc149057920e5db9`.
- [`../../verify/check.py`](../../verify/check.py), `ln_bounds`, supplies exact
  rational logarithm enclosures for the arithmetic check. No floating-point
  comparison is used by this package's certificate.

For a fixed q, only zeta and the primitive characters inducing the h characters
trivial on H need the zero hypothesis, uniformly at all heights. The primitive
conductors divide q. Imprimitive Euler-factor zeros are not put into Lemma 0'.

## 1. Exact formulas and paired zero bounds

For a primitive nonprincipal character chi of conductor f >= 3, write

    B_chi = (xi'/xi)(0,chi),  A_chi = -Re B_chi = sum_rho Re(1/rho),
    S(X,chi) = sum_{n<=X} Lambda(n) chi(n) log(X/n),
    T(X,chi) = sum_{n<=X} (Lambda(n)/n) chi(n) (1-n/X).

Zeros include multiplicities. Functional equation and conjugation give the
same-character involution rho -> 1-conjugate(rho). Thus H(7/8) puts every
nontrivial zero in 1/8 <= Re rho <= 7/8. A_chi is nonnegative.

The unconditional residue identities in the proofs of LLS Lemmas 2.2--2.3 are

    S(X,chi) = -sum_rho X^rho/rho^2 - B_chi log X
               + sum_rho 1/rho^2 + (1/2) log(f/pi) log X + Etilde_a(X),       (1)

    -conjugate(B_chi) - B_chi/X + Z_chi(X)
       = (1/2)(1-1/X) log(f/pi) - T(X,chi) + E_a(X),                       (2)

where Z_chi(X) = sum_rho X^(rho-1)/(rho(rho-1)), a = (1-chi(-1))/2,
and E_a, Etilde_a are LLS's real gamma-factor functions. These formulas retain
the complex constants; taking real parts alone would not suffice for a coset.

Put c2 = 189/125, b = 231/10000, and

    F(X) = X^(7/8) + 7 X^(1/8) + 8,
    c(X) = c2 (X^(-1/8) + X^(-1/2)),   d(X) = 1 + 1/X - c(X).

Lemma 0' gives, for X >= 256,

    sum_rho |X^rho/rho^2| <= (X^(7/8) + 7 X^(1/8)) A_chi,
    |Z_chi(X)| <= c(X) A_chi.

Lemma 0 gives sum_rho |1/rho^2| <= 8 A_chi. The same bounds hold for
zeta, replacing A_chi by |B_zeta| < b. The extra constant 8 is included in F.
For X >= 256, d(X) >= 1-c(256) = 299/2000 > 0.

The explicit gamma formulas also give, for X >= 64,

    E_a(X) <= 0,   |E_a(X)| < 1,
    |Etilde_a(X)| <= (log X)^2/2 + log X + 3.                              (3)

The Appendix proves the numerical bounds used here without sampling.

## 2. The full complex B_chi term

We first replace LLS's x = 100 application of Lemma 2.3, which cannot retain
its GRH denominator under the quoted pairing estimate. For every real x > 1,
the elementary bound

    x T_zeta(x) = sum_{n<=x} Lambda(n)(x/n-1)
      <= sum_{n<=x} Lambda(n) floor(x/n)
       = log(floor(x)!) <= x log x                                      (4)

shows T_zeta(x) <= log x. This bound is unconditional; in particular it does
not use the RH-dependent statement of LLS Lemma 2.4.

Use (2) at u = 65536 = 2^16. The triangle inequality, |T(u,chi)| <= T_zeta(u),
and A_chi <= |B_chi| give

    (1-1/u-c(u)) |B_chi|
       <= |(1/2)(1-1/u) log(f/pi) + E_a(u)| + T_zeta(u).

Here

    1-1/u-c(u) = 1009383/1638400 > 3/5.

Since log u < 12, log pi < 2, and |E_a(u)| < 1, the right side is less than
(1/2) log f + 14. Consequently, for every inducing conductor f dividing q,

    |B_chi| < (5/6) log f + 70/3 < log q + 24.                            (5)

This bounds imaginary as well as real parts, including complex characters.
Coset phases conjugate(chi(a)) can therefore be handled by absolute values.

## 3. Aggregate A_chi with the h - 1 factor

Let Hdual be the group of the h characters modulo q trivial on H, and chi0
its principal character. For chi != chi0, write chi* for its inducing primitive
character, f for its conductor and r = q/f. Elementary Euler-factor estimates
(LLS Lemma 3.1 and (3.2), or direct sums over prime powers) give

    |S(X,chi)-S(X,chi*)| <= (omega(r)/2)(log X)^2,                         (6)
    |T(X,chi)-T(X,chi*)|
       <= (1-1/X) sum_{p|r} log p/(p-1).                                 (7)

Only p dividing q but not f actually contribute; including all p dividing r
is an upper bound, also when a prime divides both f and r. Taking real parts
of (2), using E_a <= 0 and (7), yields

    d(X) A_chi* <= (1/2)(1-1/X)
                     [log(f/pi) + 2 sum_{p|r} log p/(p-1)] - Re T(X,chi).

Since log r >= sum_{p|r} log p,

    log f + 2 sum_{p|r} log p/(p-1) <= log q + log 2.

Indeed the possible positive prime contribution is log 2 at p = 2; it is
zero at p = 3 and negative for larger p. Since 2 < pi and log q > 0,

    d(X) A_chi* <= (1/2) log q - Re T(X,chi).                             (8)

This handles f = 3 too; no positive lower bound for log(f/pi) was assumed.
Orthogonality at the identity coset H, without phases, gives

    -Re sum_{chi in Hdual, chi!=chi0} T(X,chi)
       <= T(X,chi0) <= T_zeta(X) <= log X.

Thus the aggregate bound, with exactly h - 1 nonprincipal characters, is

    sum_{chi!=chi0} A_chi* <= [(h-1) log q/2 + log X] / d(X).              (9)

## 4. Lower bound for the coset count

Let C(X;aH) = sum_{n<=X, n mod q in aH} Lambda(n) log(X/n), and write
L = log q, t = log X. The exact orthogonality identity is

    h C(X;aH) = S(X,chi0) + sum_{chi!=chi0} conjugate(chi(a)) S(X,chi).     (10)

From (1), (3), (5), and |log(f/pi)| <= L + 2,

    |S(X,chi*)| <= F(X) A_chi* + (3L/2+26)t + t^2/2 + 3.

For the principal term, the zeta residue formula in LLS Lemma 2.1, before
estimating zeros, gives

    S_zeta(X) = X - log(2pi)t - 1
       + sum_{k>=1}(1-X^(-2k))/(4k^2) - sum_rho (X^rho-1)/rho^2.

Drop the nonnegative k-sum and remove primes dividing q to obtain

    S(X,chi0) >= X - b F(X) - log(2pi)t - 1 - omega(q)t^2/2.

Combine (6), (9), and (10). Since omega(q/f) <= omega(q), for X >= 256,

    h C(X;aH) >= X - b F(X)
        - F(X)[(h-1)L/2+t]/d(X) - R(q,h,X),                              (11)

where all principal and nonprincipal Euler-factor errors are charged in

    R(q,h,X) = log(2pi)t + 1 + h omega(q)t^2/2
                 + (h-1)[(3L/2+26)t+t^2/2+3].

## 5. Remove proper prime powers

If there is no prime p <= X in aH, its count consists only of proper prime
powers. For each p <= sqrt(X), put tau = log X/log p. Its total contribution
with exponents k >= 2 is

    (log p)^2 sum_{k=2}^{floor(tau)} (tau-k)
       <= (log p)^2 integral_1^tau (tau-v) dv <= (log X)^2/2.

There are at most sqrt(X) such primes. Therefore, unconditionally,

    C(X;aH) <= Q(X) <= sqrt(X) (log X)^2/2.                              (12)

This replaces both GRH-dependent prime-power estimates from LLS Section 4.
It follows from (11)--(12) that a prime exists if

    b F(X)/X + F(X)[(h-1)L/2+t]/(X d(X))
       + R(q,h,X)/X + h t^2/(2 sqrt(X)) < 1.                             (13)

## 6. Uniform analytic certificate

Set y = max(80,hL), X = y^8. Then y >= 80, hL <= y, h <= y, L <= y/2,
and omega(q) <= L/log 2 < 2L <= y. All uses of (1)--(13) are in range.
The following uniform envelopes suffice:

    d(X) > 49/50,
    F(X)/X = (1+7/y^6+8/y^7)/y < 1001/(1000y),
    [(h-1)L/2+t]/y <= 1/2 + 8 log y/y < 47/50.

For the last bound use monotonicity of log y/y for y >= 80 and
log 80 < 22/5. The four terms on the left of (13) are at most

    zeta:         231231/800000000,
    nonprincipal: 47047/49000,
    residual:     1/100000000,
    prime powers: 32 (log y)^2/y^3 < 121/100000.

For completeness the residual bound follows by substituting h <= y,
L <= y/2 and omega(q) <= y:

    R/X < [2t+1+y^2 t^2/2+y((3y/4+26)t+t^2/2+3)] / y^8.

Each summand is a positive constant times (log y)^b/y^a, with a >= 6
and 0 <= b <= 2, hence decreases for y >= 80. At y = 80, t < 176/5;
exact rational substitution is less than 1/100000000.
The four error bounds add to

    5385194673/5600000000 < 1,

leaving a normalized margin of at least 214805327/5600000000 > 0.
This contradicts (12), proves a prime lies strictly below X, and establishes
the coset theorem for every q >= 3 and h >= 2.

## 7. The progression corollary and its finite fallback

Take H = {1}, h = phi(q), and C = 581/1000. We use the full criterion (13)
with y = C h L, X = y^8. The uniform coset theorem remains unchanged.

First, the elementary bound

    phi(q)^3 >= 2q^2/9                                                  (14)

follows from phi(q)^3/q^2 = product_{p^a || q} p^(a-3)(p-1)^3.
The least 2-factor is 1/4 and the least 3-factor is 8/9. For p >= 5,
(p-1)^3/p^2 >= (4/5)^3 p >= 64/25 > 1; increasing a only increases a factor.
Omitting the 2- or 3-factor also increases this lower bound.

For q >= 2048 = 2^11, (14) gives h > 96, since
9*96^3 < 2*2048^2. Also L >= 11 log 2 > 22/3. Consequently

    y = C h L > C*96*(22/3) = 51128/125 > 400.

For every y >= 400 the bounds used in (13) can be charged with

    h <= y/C,  L <= y/(2C),  omega(q) < 2L <= y/C,
    d(X) > 249/250,   F(X)/X < 1001/(1000y),
    [(h-1)L/2+t]/y <= 1/(2C) + 8 log y/y < 1/(2C) + 3/25,

where t = 8 log y, log 400 < 6, and log y/y decreases in this range.
In particular, the factors of 1/C also enter the residual and prime-power
errors. The replacements for the last two terms of (13) are

    R/X <= [2t+1+y^2 t^2/(2C^2)
             +(y/C)((3y/(4C)+26)t+t^2/2+3)]/y^8,
    h t^2/(2 sqrt(X)) <= 32(log y)^2/(C y^3).

Every residual summand decreases for y >= 400 by the same derivative argument
as in Section 6. Substituting y = 400 and t < 48 gives R/X < 1/10^9.
Thus the four errors in (13) have sum less than or equal to

    (231/10000)(1001/1000)/400
      + (1001/1000)(1/(2C)+3/25)/(249/250)
      + 1/10^9 + 32*6^2/(C*400^3)
      = 114068220107243/115735200000000 < 1.                             (15)

The positive normalized margin is 1666979892757/115735200000000. This proves
the progression corollary for every q >= 2048.

For 3 <= q < 2048, `constants.py` sieves primes through 2^20 and computes
phi(q) by the integer totient sieve. In increasing prime order it marks each
new reduced residue class, skipping primes dividing q, until exactly phi(q)
classes have been reached. The last marked prime is the largest least prime
for that q. Comparing it to the **lower** rational bound
(C*phi(q)*ln_bounds(q)[0])^8 certifies every class at once; an incomplete prime
list is rejected. All 1274560 reduced classes pass. The largest least prime
is 169937, in class 722 modulo 1945. The prime sieve is cross-checked by trial
division and the totient sieve by direct gcd counts through 512.
These finite checks cover precisely the stated fallback; large moduli are
proved analytically by (15).

There is a concrete obstruction to lowering this all-q coefficient much
further: P(1,3) = 7, while exact upper logarithm bounds give

    ((29/50)*phi(3)*log 3)^8 < 7.

Thus coefficient 0.58, or any smaller coefficient in this same statement,
is impossible. Coefficient 0.581 is sufficient; no optimality is asserted.

## Appendix: exact elementary constants and gamma bounds

The exact script encloses pi using Machin's identity
pi = 16 arctan(1/5) - 4 arctan(1/239), with alternating-series remainders.
For Euler's constant put d_N = H_N - log N - 1/(2N). The trapezoid error for
1/x on [k,k+1] is

    d_(k+1)-d_k = integral_k^(k+1) (x-k)(k+1-x)/x^3 dx.

It is positive and at most (1/4) integral_k^(k+1) x^(-3) dx.
Since d_N tends to gamma, 0 < gamma-d_N < 1/(8N^2). At N = 256 these
exact rational enclosures certify 0.57 < gamma < 0.58, 2/3 < log 2 < 0.7,
log(2pi) < 2, and

    |B_zeta| = 1 + gamma/2 - log(4pi)/2 < 231/10000.

The four E functions are written explicitly in the first-T1 proof, Step 0,
and in LLS Lemmas 2.2--2.3. Dropping their negative tails proves E_a < 0
for x >= 64: use (log x+1)/x <= (log 64+1)/64 for E_0 and
-(0.57/2)(63/64)+0.7/64 < 0 for E_1. Once negative, their absolute values
are bounded above respectively by

    0.7 + 0.29 + x^(-3)/(1-x^(-2)) < 1,
    0.29 + x^(-2)/(1-x^(-2)) < 1.

The triangle inequality in their Etilde formulas, pi^2 < 10 and
log 2 + gamma/2 < 0.99 similarly gives (3); the two tails are bounded by
x^(-2)/(1-x^(-2)) and x^(-1)/(1-x^(-2)). No signs or finite samples of
an L-value or zero are used for these estimates.

## Verification limits and open next questions

Replay: `python3 research/least-prime-progression/constants.py` from the repository
root. It checks the rational envelopes, elementary constants, and precisely the
finite fallback; its ten failure controls must print `REJECT control`.
The existing `verify/check.py` verifies its recorded Miller--Rabin claims, not
this coset theorem. This proof has no new T1 claim or accepted-frontier change.

Not checked here: H(7/8) or its Lean proof; the classical contour shifts beyond
the cited LLS residue identities; optimality of the coset cutoff;
any finite search over all large q or all subgroups. An independent source
audit preceded this proof; the separate completed theorem recheck is recorded in
[RECHECK.md](RECHECK.md), with its exact scope and classical-input limitations.

Open next question: improve the coset cutoff 64 without weakening its all-q
domain. Keep (13), the full complex-character estimate, and proper-prime-power
subtraction; positivity of the smoothed coset count alone is insufficient.
Section 8 resolves the sharp-coefficient question while retaining a non-strict
inequality at its necessary equality case.

## 8. Parameter transfer and the sharp progression coefficient

Assume H(b) for 13/15<=b<=7/8, including zeta, and set

    r=1/(1-b),    c_b=7^(1-b)/(2 log3).

Then the following complete statements hold, with the same definitions and
q>=3 as above:

    P(aH,q) < max(80,h log q)^r,
    P(a,q) <= [c_b phi(q) log q]^r.                                 (16)

The second coefficient is sharp: equality holds exactly at q=3,a=1,
where P(1,3)=7. Every q>=4 satisfies the strictly stronger subdomain bound

    P(a,q) < [.58 phi(q) log q]^r.                                  (17)

This is a conditional parameter theorem, not a certification of H(b).
For b=8748867/10000000 it uses the half-plane from the frontier's A1b
reference, [Xu--Sang, arXiv:2610.15291v2](https://arxiv.org/html/2610.15291v2),
Theorem 1.1. That version covers all Dirichlet L-functions, including zeta,
but is itself conditional on its stated analytic inputs and H(7/8).
Its proof, imported analytic inputs and any Lean replay are not verified here.
The theorem assumes H(b) directly, and uses no unmerged sibling theorem.

First extend the accepted pairing argument, retaining its range condition.
The functional-equation involution within one character is still
rho ->1-conjugate(rho), and 1-b<=Re rho<=b. For an off-line pair with
sigma>=1/2, put v=1/|rho|^2,w=1/|1-conjugate(rho)|^2. The main-sum ratio
to its A weight is fractional-linear in w/v, whose endpoints give

    X^sigma+X^(1-sigma),
    ((1-sigma)/sigma)X^sigma+(sigma/(1-sigma))X^(1-sigma).

Since sigma/(1-sigma)<=7, both are bounded by
g(sigma)=X^sigma+7X^(1-sigma). Convexity reduces to sigma=1/2 or b.
For z=X^(b-1/2), [g(b)-g(1/2)]/sqrt(X)=(z-1)(z-7)/z>=0 whenever
z>=7. This holds for X>=256, because b-1/2>=11/30 and 256^11>7^30.
Line zeros have ratio 2 sqrt(X), also covered. For the second kernel,
AM--GM gives the paired ratio at most

    [X^(sigma-1)+X^(-sigma)]/[2sqrt(sigma(1-sigma))]
       <=(189/125)[X^(b-1)+X^(-1/2)],

because b(1-b)>=7/64 and 7*189^2>16*125^2. The constant zero sum is
bounded by rA<=8A. All terms and weights are nonnegative and convergent,
so the same-character regrouping applies equally to complex chi and zeta.
Thus Sections 1--5 and criterion (13) hold with

    F_b(X)=X^b+7X^(1-b)+8,
    c(X;b)=(189/125)[X^(b-1)+X^(-1/2)],
    d(X;b)=1+1/X-c(X;b).                                           (18)

The correction c(X;b) is distinct from the sharp coefficient c_b. The
full-complex B estimate (5) remains valid: at the fixed u=2^16,
b<=7/8 makes c(u;b) no larger than the old c(u), so its absorption
denominator is still >3/5. The h-1 aggregation, all Euler corrections and
the prime-power subtraction are unchanged. The gamma bounds are independent
of b. No real-part estimate has replaced the full complex constant.

Put y=X^(1-b), so X=y^r, with 7<r<=8. For y>=80,

    F_b(X)/X <=1/y+7/y^6+8/y^7 <1001/(1000y),
    d(X;b)>=1-(189/125)(1/y+1/y^3),
    X>=y^7,   log X<=8 log y,
    sqrt(X)>=y^(7/2)>8y^3.                                        (19)

These bounds use weaker integer powers in the safe direction. In particular,
copying the old y^-4 bound for X^-1/2 would be invalid when b<7/8.
For y=max(80,hL), the denominator in (19) is >49/50. The residual R/X
is at most the Section 6 numerator divided by y^7 instead of y^8, and is
<1/10^6 at y=80,t<176/5. Its summands have the form (log y)^j/y^k,
k>=5,j<=2, so they decrease throughout the range. Proper prime powers
now cost at most 4(log y)^2/y^2. The four errors in (13) are bounded by

    (231/10000)(1001/1000)/80
      +(1001/1000)(47/50)/(49/50)+1/10^6+4(22/5)^2/80^2
      =5446184217/5600000000 <1,                                 (20)

with margin 153815783/5600000000. This proves the first part of (16).
As before, a prime at X has zero logarithmic weight, so the criterion
actually gives a prime strictly below X.

For q>=2048 take C0=29/50=.58 and y=C0 phi(q)L. The cubic totient bound
(14) still gives y>400. We have d(X;b)>249/250 and
sqrt(X)>=y^(7/2)>=20y^3. The Section 7 residual numerator divided by
y^7 is <1/10^9; all its summands again decrease for y>=400. Therefore
the four errors in (13) have total at most

    (231/10000)(1001/1000)/400
      +(1001/1000)(1/(2C0)+3/25)/(249/250)
      +1/10^9+8*6^2/(5C0*400^2)
      =5705615549587/5776800000000 <1,                            (21)

with margin 71184450413/5776800000000. This proves (17) for large q.
For 4<=q<2048 the same exhaustive marking of least primes now checks

    largest_a P(a,q) <[.58 phi(q) ln_bounds(q)[0]]^7.

All 1274558 reduced classes pass, and every base exceeds 1. Since r>7,
this implies (17) on the complete finite remainder. The largest least prime
is still 169937 at q=1945,a=722. The old coefficient-.581 fallback is
retained as a positive control, rather than counted as evidence for this
new exponent check.

Finally the existing exact upper-log comparison
(.58*2log3)^8<7, together with .58*2log3>1 and r<=8, proves c_b>.58.
Thus (17) is strictly smaller than the second bound in (16) for every q>=4.
At q=3, the least primes in the two reduced classes are 2 and 7; the right
side of (16) is exactly 7. This proves (16), its only equality case, and
sharpness: any smaller coefficient fails at that same class.

For b=theta or 7/8, the old decimal coefficient .581 exceeds c_b. To certify
this without fractional powers, use r>=10000000/1251133>799/100 and a
downward eight-decimal rational enclosure l3 for log3. The checker proves

    (.581*2*l3)^799>7^100,   .581*2*l3>1.

Consequently the original strict coefficient-.581 corollary is also true
at the smaller-theta exponent. The exact expression c_b in (16), rather
than a rounded decimal, is the sharp coefficient.

The first seven rejection controls cover this parameter transfer and its
predecessors; Section 9 adds three more, for a current total of ten.
This extension and its complete finite domain are author-checked and passed
their own separate fresh-context AI review in RECHECK-SHARP.md. Neither the
original two reviews nor the source audit is counted as verification of this
new theorem. The report pins its snapshot; later edits record status and
links only. Maintainer review remains pending.

## 9. A smaller all-q coset cutoff

For every b in [13/15,7/8], assume H(b) including zeta and put r=1/(1-b).
The coset bound can be improved to

    P(aH,q) <max(64,h log q)^r       (q>=3, h>=2).                 (22)

The sharp progression theorem and all its equality cases remain unchanged.
This section uses its already proved small-q consequence, but no theorem
from a separate unmerged package. The older cutoff80 remains a fully
analytic positive control; (22) uses the progression theorem for q<=20.

First sharpen the principal T sum. Before the RH estimation in the proof
of LLS Lemma2.4, the residue identity is

    T_zeta(X)=log X-(1+gamma)+log(2pi)/X-Z_zeta(X)
              -sum_{k>=1} X^(-2k-1)/[2k(2k+1)].                 (23)

All terms and signs here are unconditional; its RH estimate is replaced.
Section8's paired bound and b<=7/8 give
|Z_zeta(X)|<=c(X;b)|B_zeta|<=c(X;7/8)|B_zeta|. For X>=256, use the
decreasing correction, gamma>.57, log(2pi)<3 and |B_zeta|<.0231:

    log(2pi)/X+c(X;b)|B_zeta|
      <3/256+(189/125)(1/2+1/16)(231/10000)
      =313653/10000000 <7/100.

Dropping the negative trivial-zero series in (23) proves

    T_zeta(X)<log X-3/2.                                         (24)

Accordingly, the orthogonality step in Section3 now yields
sum_(chi!=chi0) A_chi* <=[(h-1)L/2+t-3/2]/d(X;b). The h-1 factor,
complex B estimate, Euler corrections, gamma residual R and proper-power
subtraction remain as before. In criterion (13), only the aggregate
numerator changes from (h-1)L/2+t to (h-1)L/2+t-3/2.

For q>=21, L=log q>3. Choose y=max(64,hL), X=y^r and t=log X.
Then h<=y/3, L<=y/2, omega(q)<2L<=y, and

    [(h-1)L/2+t-3/2]/y <=1/2+(8log y-3)/y.                    (25)

The additional subtraction3/2 comes from the retained -L/2. The right
side decreases for y>=64: the derivative of its variable part has sign
11-8log y<0. Throughout the parameter interval, r>=15/2, so

    sqrt(X)>=y^(15/4)>22y^3,

because y>=64 and 64^3>22^4. Consequently the proper-power term is at most

    h t^2/(2sqrt(X)) <=(16/33)(log y)^2/y^2.                    (26)

Let f=1000001/1000000. The directed envelopes (19) and monotonicity give
F_b(X)/X<f/y for y>=64. The denominator has the uniform lower bound

    d(X;b)>=1-(189/125)(1/y+1/y^3)
            >=31993667/32768000=:d0>0.

The fully charged residual has the uniform bound

    R/X <=[2t+1+y^2t^2/6
              +(y/3)((3y/4+26)t+t^2/2+3)]/y^7.

Every summand is a nonnegative multiple of (log y)^j/y^k with k>=5,j<=2,
and decreases on this range. Since log64<104/25, its endpoint is
102572093/549755813888000<1/10^6. The zeta error, (25) divided by d0,
this residual and (26) therefore sum to at most

    (231/10000)f/64+f[1/2+(8*(104/25)-3)/64]/d0
       +1/10^6+(16/33)(104/25)^2/64^2
       =675090454343806963541/675706247040000000000 <1,            (27)

with positive margin 615792696193036459/675706247040000000000.
Thus the strengthened criterion proves (22) for every q>=21.

For 3<=q<=20, the sharp coefficient from Section8 obeys c_b<1:
1-b<=2/15<1/6, 7^(1/6)<2 and log3>1. Also phi(q)<=19 and logq<3.
For any coset choose one reduced class a in it. The already proved bound
gives P(aH,q)<=P(a,q)<57^r<64^r. A prime at the real cutoff has zero
logarithmic weight, so the large-q contradiction likewise supplies a prime
strictly below its cutoff. This completes the exact all-q statement.

The three additional controls reject cutoff63 with these fixed envelopes,
removal of the zeta constant saving, and an unjustified saving2 in (24).
They test this certificate and do not prove cutoff63 impossible. All ten
controls and old positive certificates are retained. This improvement passed
its own fresh-context independent AI recheck in RECHECK-CUTOFF.md; earlier
reviews do not certify its changed aggregate and prime-power bounds.
Maintainer acceptance remains separate.
