**Original idea: Geoffrey Irving.**

# Least primes in cosets and progressions under H(7/8)

AI-authored conditional research draft (Codex), 2026-10-23. Text: CC BY 4.0;
code: Apache-2.0. Author checks and a separate fresh-context same-model AI
recheck pass; see [RECHECK.md](RECHECK.md). Maintainer review is pending.
The report pins the reviewed snapshot; later proof edits record review status only.

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
> P(a,q) < (phi(q) log q)^8.

There is no small-modulus computation in the coset theorem. The progression
corollary uses an exact finite check for 3 <= q < 512, described below.
The assertion excludes q = 2. No assertion about the truth of H(7/8), an
unconditional Linnik constant, optimal constants, or a Miller--Rabin improvement
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

Take H = {1}, so h = phi(q). The elementary bound phi(q) >= sqrt(q/2)
follows by multiplying the factors

    phi(q)^2/q = product_{p^a || q} p^(a-2)(p-1)^2:

every odd-prime factor is at least 1, and the 2-factor is at least 1/2.
For q >= 512, phi(q) >= 16 and log q >= 9 log 2 > 6. Thus h log q > 96 > 80,
and the coset theorem gives the stated corollary without a cutoff term.

For 3 <= q < 512, `constants.py` sieves all primes through 65536, records
the first prime in each reduced residue class, and requires that every class
was reached. Each recorded prime is compared to the **lower** rational bound
(phi(q) * ln_bounds(q)[0])^8. All 79594 reduced classes pass; the largest
least prime in this range is 37363, in class 22 modulo 461. The sieve is
cross-checked against trial division through 512; the script also rejects an
incomplete prime list and a false coefficient on the known q = 3 case.
This is finite exhaustive evidence for precisely the stated fallback, not a
finite substitute for the analytic proof at larger moduli.

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
finite fallback; its four failure controls must print `REJECT control`.
The existing `verify/check.py` verifies its recorded Miller--Rabin claims, not
this coset theorem. This proof has no new T1 claim or accepted-frontier change.

Not checked here: H(7/8) or its Lean proof; the classical contour shifts beyond
the cited LLS residue identities; minimality or optimality of the constants;
any finite search over all large q or all subgroups. An independent source
audit preceded this proof; the separate completed theorem recheck is recorded in
[RECHECK.md](RECHECK.md), with its exact scope and classical-input limitations.

Open next question: can one reduce the progression coefficient from 1 while
retaining all q >= 3? First keep (13), exploit h = phi(q) and its elementary
lower bound, and check a proposed rational coefficient with exact endpoints
and an explicitly bounded finite fallback. A prime-power-only positive coset
count does not pass the success test.
