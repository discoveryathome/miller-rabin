Original idea: Geoffrey Irving.

# Explicit bounds for L(1, chi) under half-plane hypotheses

**Status: author-checked conditional draft, 2026-10-23.** A separate Codex
source-research context derived this argument; the parent checked the derivation
and packaged its exact arithmetic. A separate fresh-context same-model AI
recheck confirmed the log q>=32 certificate; see [RECHECK.md](RECHECK.md).
The extension to log q>=15 in Section 10 passed its own fresh-context
same-model AI recheck; see [RECHECK-REFINEMENT.md](RECHECK-REFINEMENT.md).
The leading-r parameter theorem in Section 11 is new author-checked work
awaiting its own fresh-context recheck.
Source research, author checks and that independent recheck are separate
evidence items. This is not an accepted result or a proof of H(7/8).
Maintainer review remains pending. Text: CC BY 4.0; code: Apache-2.0.

The intended independent base is upstream
`d2bd5167a42b8256f1362640dc149057920e5db9`. Acceptance is determined by
[`discover/frontier.json`](../../discover/frontier.json), not historical draft
banners. Draft PR #11, head `d1f29f2eab57bb0de12465e0e61385d6fea53075`, was
background context only. This derivation does not depend on that PR's theorem or
its full-complex B bound.

## Theorem and domain

The catalog's suggested power of log q is unnecessary for primitive characters.
The LLS equations retain **order log log q in both directions**. The loss from
GRH is a larger leading constant and a larger truncation parameter, rather than
a power of log q in the final answer.

The complete error budget for the following conservative result is given below.
All logarithms are natural.

> **Theorem.** Assume H(7/8), including its application to zeta. Let
> chi be a primitive Dirichlet character of conductor q, with log q >= 15. Then
>
>     pi^2 / [6 exp(gamma) (8 log log q + 2)]
>       <= |L(1,chi)| <= exp(gamma) (8 log log q + 2).                 (T)
>
> Equivalently, the reciprocal is at most
> `(6 exp(gamma)/pi^2) (8 log log q + 2)`.

The exact conductor threshold is q >= exp(15). There is no assertion here for
smaller primitive conductors. Section 5 supplies a simple certificate for
log q>=32 using

    L = log q,  x = L^8,  t = log x = 8 log L,  y = x^(1/8) = L.

Section 10 covers the full stated range using x=((31/50)log q)^8. Both
certificates retain the same leading constants in (T): 8 exp(gamma)
for |L(1,chi)| and 48 exp(gamma)/pi^2 for its reciprocal. These replace LLS's
GRH leading constants 2 exp(gamma) and 12 exp(gamma)/pi^2.

For a negative fundamental discriminant -q in the same range, Dirichlet's class
number formula gives the corollary

    pi sqrt(q) / [6 exp(gamma) (8 log log q + 2)]
      <= h(-q) <= exp(gamma) sqrt(q) (8 log log q + 2) / pi.           (CN)

This is a proposed sibling package against accepted main. It is not necessary
to merge the least-prime-progression package first.

## Exact sources and scope of their use

1. Y. Lamzouri, X. Li, K. Soundararajan, *Conditional bounds for the least
   quadratic non-residue and related problems*, **arXiv:1309.3595v3**:
   [versioned PDF](https://arxiv.org/pdf/1309.3595v3) and
   [versioned TeX source](https://arxiv.org/src/1309.3595v3). Both were read.
   The PDF is the 23-page version stamped 8 December 2016. Relevant locations:
   equations (2.1)-(2.4), PDF pp. 4-5; Lemma 2.3 and its proof, pp. 7-8;
   Lemmas 2.4-2.6 and their proofs, pp. 8-10; Section 5, including Lemma 5.1
   and equation (5.3), pp. 17-19; equation (1.3), PDF p. 4, for (CN).
   Decompressed TeX SHA-256:
   `2b5a85717f193b950ae522ad5c07f8f8bb1dc2213c073d54b4d4fa8cba6d98f8`.
2. The accepted local
   [zero-pairing proof, Lemma 0'](../zero-pairing/PROOF.md#lemma-0-paired-zero-sums),
   especially part 2, together with the unconditional facts (F1)-(F2) and
   strip argument in the
   [first-explicit-T1 proof](../first-explicit-t1/PROOF.md#step-0-what-hβ-gives-in-place-of-grh).
   Only these analytic lemmas are needed, not the witness theorem's numerical
   coefficients. The frontier records their accepted status.
3. The elementary factorial, Chebyshev, and finite Euler-product estimates
   used below are proved here. No additional published numerical prime estimate
   is assumed.

External requests contained only the public arXiv PDF/source URLs. Unpublished
repository material was not submitted to search engines or external websites.

## 1. Notation and accepted zero bounds

Let q >= 3 be a primitive conductor, a = (1-chi(-1))/2, and put

    Q = log(q/pi),
    g_a = (1/2) psi_0((1+a)/2),
    b = -Re B(chi) = sum_rho Re(1/rho) >= 0.

Thus g_0 = -log 2 - gamma/2 and g_1 = -gamma/2. The symbol b denotes the
nonnegative **real-part quantity**. It is not |B(chi)| for a complex character.

For zeta write

    b_z = -B_z = 1 + gamma/2 - (1/2) log(4 pi).

The exact formula for b_z is unconditional, LLS (2.2). For the final rational
budget even the very loose unconditional bound 0 <= b_z < 1/2 suffices:
gamma < 1 and log(4 pi) > 2 imply it. The familiar 0.02309... value is not
needed.

Under H(7/8), every nontrivial zero rho = alpha + i v lies in
1/8 <= alpha <= 7/8. This uses the functional equation as well as H. The same
zero multiset, even for complex chi, is preserved by rho -> 1-conjugate(rho).
Consequently

    sum_rho 1/|1-rho|^2 = sum_rho 1/|rho|^2 <= 8 b.                   (1.1)

The accepted paired bound gives, for x > 1,

    Z_chi(x) = sum_rho x^(rho-1) / [rho(rho-1)],
    |Z_chi(x)| <= c(x) b,
    c(x) = (189/125) (x^(-1/8) + x^(-1/2)).                         (1.2)

The identical statements hold for zeta with b_z. The rational coefficient
189/125 is an upper bound for 4/sqrt(7). No GRH identity
`sum 1/|rho|^2 = 2b` is used.

## 2. Exact identities, before estimating their zero terms

For x >= 2, set t = log x and define

    A_chi(x) = Re sum_{2<=n<=x} [Lambda(n) chi(n)/(n log n)]
                                  log(x/n)/t,
    T_chi(x) = Re sum_{n<=x} [Lambda(n) chi(n)/n] (1-n/x),
    F_chi(x) = A_chi(x) + T_chi(x)/t
             = Re sum_{2<=n<=x} Lambda(n) chi(n)
                         [1/(n log n) - 1/(x t)].                 (2.1)

Use subscripts z for the same finite sums with chi(n) replaced by 1. Endpoints
cause no half-weight issue because the displayed weights vanish at n=x.

The residue calculation in the proof of LLS Lemma 2.3, **before its GRH
estimate**, gives the exact real identity

    (1+1/x)b + Re Z_chi(x)
      = (1/2)(1-1/x)Q - T_chi(x) + E_a(x),                         (2.2)

where the exact gamma contributions are

    E_0(x) = -log 2 - (gamma/2)(1-1/x) + (t+1)/x
                - sum_{k>=1} x^(-2k-1)/[2k(2k+1)],
    E_1(x) = -(gamma/2)(1-1/x) + (log 2)/x
                - sum_{k>=0} x^(-2k-2)/[(2k+1)(2k+2)].            (2.3)

Define d(x) = 1+1/x-c(x). In particular, if d(x)>0 and E_a(x)<=0,

    b <= [(1/2)(1-1/x)Q + T_z(x)] / d(x).                         (2.4)

For q in (T), Q is positive and at most L. A proof of T_z(x)<=t appears in
Section 4 below, so (2.4) implies

    b <= (L/2+t)/d(x).                                            (2.5)

These are estimates derived from (2.2), not exact formulas for b.

The proof of LLS Lemma 2.5 also supplies an exact identity. With u the real
integration variable,

    log |L(1,chi)| = A_chi(x) + [Q/2+g_a-b]/t + R_chi(x) + H_a(x), (2.6)

    R_chi(x) = (1/t) Re sum_rho integral_{1}^{infinity}
                              x^(rho-u)/(rho-u)^2 du,
    H_a(x) = (1/t) integral_{1}^{infinity} sum_{n>=0}
                       x^(-2n-a-u)/(2n+a+u)^2 du.                 (2.7)

Here H_a is real and nonnegative. The contour residues and
`-Re L'/L(1,chi) = -b+Q/2+g_a` are exact and do not require GRH.
The zero-free gap under H justifies evaluating at u=1; the absolute bounds
below justify interchange and limiting operations for the integrated zero
terms. The underlying contour arguments are those in the cited LLS proofs.

### The shifted denominator in Lemma 2.5

For every u>=1,

    |rho-u| >= |rho-1|,
    |x^(rho-u)| <= x^(7/8-u).

One cannot replace |rho-1| by |rho| termwise off the critical line. Instead use
the multiset identity (1.1), then integrate x^(7/8-u). With y=x^(1/8),

    |R_chi(x)| <= 8b/[y t^2].                                    (2.8)

Indeed the integral contributes an additional factor 1/t. For the trivial
zeros, since x>=2 and u>=1,

    sum_{n>=0} x^(-2n)/(2n+1)^2 <= 1/(1-x^(-2)) <= 4/3,

and hence

    0 <= H_a(x) <= 2/[x t^2].                                    (2.9)

Both bounds account for the entire integral, including u close to 1.

Eliminating b's main term **exactly** between (2.2) and (2.6) is convenient:

    log |L(1,chi)| = F_chi(x)
       + [b/x + Re Z_chi(x) + Q/(2x) + g_a-E_a(x)]/t
       + R_chi(x) + H_a(x).                                     (2.10)

This cancellation is the reason a power of log q is not forced. Keeping
Q/(2t) and bounding everything else separately would miss it.

For x>=2, direct bounds on the series in (2.3) give

    |g_a-E_a(x)| <= (t+2)/x.                                    (2.11)

For example the even difference is
`-(t+1+gamma/2)/x + sum_{k>=1} x^(-2k-1)/[2k(2k+1)]`.
Its series is at most `x^(-3)/[6(1-x^(-2))]`. The odd series is at most
`x^(-2)/[2(1-x^(-2))]`. Using 0<gamma<1 and log 2<1 proves (2.11)
by the triangle inequality. Thus for Q>=0,

    |log |L(1,chi)| - F_chi(x)| <= J_chi(x)/t,                     (2.12)
    J_chi(x) = b[c(x)+1/x+8/(y t)]
                  + [Q/2+t+2]/x + 2/(x t).

The gamma terms have been charged in (2.12); no sign inequality from GRH
Section 5 has been carried over.

## 3. Zeta estimates under H, replacing RH-only Lemmas 2.4 and 2.6

The pre-estimation identity in the proof of LLS Lemma 2.4 is

    T_z(x) = t-(1+gamma)+log(2 pi)/x - Z_z(x)
                 - sum_{n>=1} x^(-2n-1)/[2n(2n+1)].              (3.1)

Its zero contribution is now at most c(x)b_z in absolute value, rather than
2b_z/sqrt(x).

Repeat the proof of Lemma 2.6 while retaining its zero integral. The pole at
1 and its Laurent coefficients give the exact main term below; estimating the
zero integral by (1.1), exactly as in (2.8), gives

    A_z(x) = log t + gamma - 1 + gamma/t + epsilon_z(x),
    |epsilon_z(x)| <= 8b_z/[y t^2] + 1/[3x^3 t^2].                (3.2)

For clarity, the last constant can be justified without RH: the trivial-zero
sum in that proof has n>=1, and

    sum_{n>=1} x^(-2n)/(2n+1)^2
       <= x^(-2)/[9(1-x^(-2))] <= x^(-2)/3       (x>=2).

Integration over u>=1 and division by t then give `1/(3x^3 t^2)`.
The limit at the zeta pole uses its unconditional Laurent expansion, not RH.

Combining (3.1) and (3.2), and dropping the nonpositive final series in (3.1),

    F_z(x) <= log t + gamma - 1/t + J_z(x)/t,                     (3.3)
    J_z(x) = b_z[c(x)+8/(y t)]
                    + log(2 pi)/x + 1/(3x^3 t).

This records every zeta error used in the candidate theorem. In particular
the RH-only error `2B theta/(sqrt(x)t^2)` from the published Lemma 2.6 has
not been retained. The exact constant gamma in (3.2) survives because it
comes from the pole, not from the zero estimate.

## 4. Elementary finite-sum and Euler-product estimates

### A factorial estimate independent of PR #11

For real x>1,

    x T_z(x) = sum_{n<=x} Lambda(n)(x/n-1)
       <= sum_{n<=x} Lambda(n) floor(x/n)
        = log(floor(x)!) <= x log x.                              (4.1)

The equality uses `sum_{d|m} Lambda(d)=log m`. All terms are nonnegative.
Thus T_z(x)<=log x unconditionally. This reproduces the working lemma
mentioned in the task without depending on any unmerged result.

### A loose elementary Chebyshev bound

For all real v>=1, let psi(v)=sum_{n<=v} Lambda(n). Then

    psi(v) <= 2v.                                                (4.2)

Here is a short justification, to avoid importing an unpinned prime estimate.
For an integer N>=2, put m=floor(N/2) and k=ceil(N/2). Every prime power
in (k,N] contributes its log p to the prime factorization of binomial(N,m).
All the other prime-power contributions to that binomial are nonnegative.
Therefore

    psi(N)-psi(k) <= log binomial(N,m) <= N log 2.

Induction, log 2<3/4, and the immediate bases N=1,2,3 give psi(N)<=2N:
for even N the induction bound is N+N log 2; for odd N>=5 it is
N+1+N log 2 <= 2N. Passing to floor(v) proves (4.2).

### Upper and lower Euler envelopes, including the p=2 issue

The coefficients in F_chi(x) are nonnegative, so

    F_chi(x) <= F_z(x).                                          (4.3)

For x>=100, the finite inequality of LLS Lemma 5.1 says that F_chi is bounded
below by putting chi(p)=-1 for every p<=x. This is an algebraic Euler-product
inequality, independent of GRH. The following proof fills the source's
omitted p=2 calculation, so that this report need not import an unchecked
computer assertion.

Fix a prime p<=x. Set K=floor(t/log p), r=1/p, h=log p/(x t), and

    w_k = r^k/k-h  (1<=k<=K).

These weights are nonnegative and decreasing. If chi(p)=0, its contribution
is 0, whereas the alternating sum `sum_{k<=K} (-1)^k w_k` is nonpositive.
Otherwise write chi(p)=-exp(i phi). The difference from chi(p)=-1 is

    D = sum_{k<=K} (-1)^(k-1) (1-cos(k phi)) w_k.                 (4.4)

Use `0 <= (1-cos(k phi))/(1-cos phi) <= k^2`, interpreting the quotient
continuously when phi is a multiple of 2 pi.

For p>=3, K=1 is immediate. If K>=2, dropping positive odd terms gives

    D/(1-cos phi)
      >= r - sum_{even k<=K} k r^k + h(sum_{even k<=K} k^2-1)
      >= r - 2r^2/(1-r^2)^2 >= (5/32)r > 0,                    (4.5)

since r<=1/3 and the coefficient of h is at least 3.

For p=2, x>=100 implies K>=6. Put z=cos phi. The first five quotients are

    Q_1=1, Q_2=2+2z, Q_3=(1+2z)^2,
    Q_4=8z^2(1+z), Q_5=(4z^2+2z-1)^2.

The even tail contributes at worst `-sum_{even k>=6} k/2^k = -5/36`.
Consequently

    D/(1-cos phi) >= P(z)+h H(z),
    P(z)=229/1440-(13/120)z+z^2/60-z^3/40+z^4/10,
    H(z)=-1+2z+8z^2-8z^3-16z^4.                                (4.6)

For -1<=z<=0 all nonconstant terms of P are nonnegative. For 0<=z<=1,
dropping its positive terms gives P(z)>=229/1440-13/120-1/40=37/1440.
Also

    H(z)+15=(1-z)(16z^3+24z^2+16z+14) >= 0.                      (4.7)

The cubic is increasing on [-1,1], since its derivative is
`48(z+1/2)^2+4`, and its value at -1 is 6. Finally log 2<7/10 and
log 100>9/2 imply h<7/4500. Thus

    P(z)+h H(z) > 37/1440-7/300=17/7200 > 0.                    (4.8)

This proves the finite minimum for complex as well as real characters.
No proposed choice chi(p)=+1 or -1 needs to be realizable by a character:
these are envelopes over the larger independent-prime choices.

The exact even-power rearrangement in LLS (5.3), or direct regrouping, gives

    min-envelope F_chi(x) = -F_z(x)+C_2(x),
    C_2(x)=sum_{m<=sqrt(x)} Lambda(m)/(m^2 log m)
                      - 2 psi(sqrt(x))/(x t).                   (4.9)

The infinite first sum is log zeta(2). Since Lambda(m)/log m<=1, its tail
is at most `1/(sqrt(x)-1)`. By (4.2), the subtracted term is at most
`4/(sqrt(x)t)`. For x>=100, these add to at most `2/sqrt(x)`:
`sqrt(x)/(sqrt(x)-1)<=10/9` and `4/t<8/9`. Therefore

    F_chi(x) >= -F_z(x)+log zeta(2)-2/sqrt(x).                    (4.10)

The factor zeta(2)=pi^2/6 in the final lower bound is thus fully accounted
for. We use the deliberately looser 2/sqrt(x), not LLS's quoted
3/(2 sqrt(x)) tail constant.

## 5. Full explicit budget proving the candidate range

The unconditional elementary bounds `3<pi<4` and `gamma<H_1=1` suffice
together with exact rational logarithm enclosures. The accepted `ln_bounds`
helper certifies `27/40<log 2<7/10`, `log 7<39/20`, `log 100>9/2`,
and `log 100<5`. Since `H_6-log 7<gamma` and `H_6=49/20`, these give
gamma>1/2. Also log(4pi)>log12>2, log pi<log4<2 and log(2pi)<log8<3.
In particular b_z<1/2 follows from its exact formula. These logarithm
enclosures use positive series and rigorous rational tails, not floats.
For x>=100, E_a(x)<=0 follows directly from (2.3):

    E_0(x) <= -log 2+(log x+1)/x < -1/2+6/100 < 0,
    E_1(x) <= -(1/4)(1-1/x)+1/x < 0.

Here `(log x+1)/x` decreases and log 100<5. The elementary bounds
log pi<2 and log(2 pi)<3 are sufficient throughout.

Now assume L>=32 and set x=L^8, y=L, t=8 log L. Then

    t>27,                 t/L<7/8,
    c(x)L <= (189/125)(1+32^(-3)) < 303/200,
    c(x)<6/125,           d(x)>119/125,
    b/L <= (1/2+t/L)/d(x) < 1375/952 < 29/20.                    (5.1)

The inequality t/L<7/8 holds first at L=32 using log 2<7/10 and then by
monotonicity of log L/L. These bounds give a uniform proof on the entire
infinite range, not merely a numerical sample of conductors.

Combining (2.12), (3.3), (4.3), and (4.10), both conclusions follow if the
following common budget is controlled:

    K = J_chi(x)+J_z(x)+2t/sqrt(x).

Using Q<=L, b_z<1/2 and log(2 pi)<3,

    K <= (b+1/2)[c(x)+8/(L t)]
             + [b+L/2+t+5]/L^8
             + 2/(L^8 t) + 1/(3L^24 t) + 2t/L^4.                (5.2)

The four main contributions are bounded in exact rationals by

    b c(x)        <= (29/20)(303/200) = 8787/4000,
    8b/(L t)      <= 58/135,
    c(x)/2        < 3/125,
    4/(L t)       < 1/216.                                      (5.3)

Their sum is 286741/108000 = 2.655009259... . The remaining terms of (5.2)
are less than 1/1000. In detail, `b+L/2+t+5<3L` for L>=32, so they are at
most

    3/L^7 + 1/L^8 + 1/L^24 + 7/(4L^3)
       <= 27/(4*32^3) = 27/131072 < 1/1000.                      (5.4)

Since

    8/3 - 286741/108000 - 1/1000 = 1151/108000 > 0,

we have K<8/3. It follows that

    log |L(1,chi)| <= log t+gamma+5/(3t),
    log (1/|L(1,chi)|) <= log t+gamma-log zeta(2)+5/(3t).          (5.5)

Finally `exp(s)<=1/(1-s)` for 0<=s<1 and t>27 show

    t exp(5/(3t)) <= t + (5/3)/(1-5/81)
                    = t+135/76 < t+2.                          (5.6)

Substituting t=8 log log q proves (T). LLS (1.3),
`h(-q)=sqrt(q)L(1,chi_-q)/pi` for fundamental -q with q>4, then gives (CN).

## 6. Why the shape is log log q, and what might improve

Choosing x=(log q)^8 makes log x=8 log log q. The exact cancellation (2.10)
leaves a bounded numerator divided by log x, so exponentiation changes only
an additive constant in the final Euler envelope. In particular the integrated
zero term contributes 8b/(y t) to that bounded numerator rather than a power
of log q to |L(1,chi)|. This explains the log-log shape directly.

Open next questions are reducing the threshold log q>=15 or additive constant
2, using a different truncation x=(c_0 log q)^8 and fully recomputing its range.
No optimized-c_0 theorem, smaller-conductor extension or optimal leading
constant is claimed here.

## 7. GRH-use audit of LLS Lemmas 2.3-2.6 and Section 5

| Source step | GRH/RH-dependent part | Replacement or disposition here |
|---|---|---|
| Section 2 notation | Writing every rho as 1/2+i gamma | Use alpha+i v with 1/8<=alpha<=7/8; retain unconditional functional equation and Hadamard identities. |
| Lemma 2.3 | Estimating sum x^(rho-1)/[rho(rho-1)] by 2b/sqrt(x); identifying the two denominator magnitudes termwise | Accepted bound c(x)b. The denominator for b is d(x)=1+1/x-c(x), not (1-1/sqrt(x))^2. |
| Lemma 2.4 | RH estimate of zeta's same zero kernel | Exact identity (3.1), error at most c(x)b_z; factorial estimate used when only an upper bound on T_z is needed. |
| Lemma 2.5 before integrating | Re rho=1/2 in x^(rho-u); the shifted-denominator comparison with rho for u>=1; sum of reciprocal squared magnitudes equal to 2b | Compare the shifted denominator with rho-1, use the reflected zero multiset and strip lower edge 1/8, then apply (2.8). |
| Lemma 2.5 main derivative | Relation between Re L'/L(1), b, Q, and digamma | Exact independently of GRH; retained as an identity. |
| Lemma 2.5 trivial zeros | Source error bounded by 2/(x t^2) | Unconditional and re-proved in (2.9); actual contribution is nonnegative. |
| Lemma 2.6 | RH zero integral 2B theta/(sqrt(x)t^2) | Replace by 8b_z/(y t^2). The pole main term and the separately re-proved trivial-zero bound remain. |
| Section 5.1 | Lemma-2.5 error and the lower estimate for b with (1+1/sqrt(x))^(-2) | Exact elimination (2.10) avoids importing that denominator or its sign-sensitive gamma inequality. |
| Section 5.1 upper Euler envelope | Maximal finite sum at chi(p)=1 | Unconditional: every coefficient of F is nonnegative. |
| Section 5.1 numerical conclusion | RH zeta estimates and x=(log q)^2/4; constants 3.1 and q>=10^10 | Replaced entirely by Sections 3 and 5. None of those constants or thresholds is retained. |
| Section 5.2 | Upper estimate for b with (1-1/sqrt(x))^(-2); T_chi>=-log x+1 from RH Lemma 2.4 | Avoided by (2.10), elementary bounds, and explicit absolute errors. |
| Section 5.2 Lemma 5.1 | Finite minimum at chi(p)=-1; source's omitted p=2 computation | No GRH is needed. The proof, including p=2, is given in (4.4)-(4.8). |
| Section 5.2 Euler correction | zeta(2) and tail estimate 3/(2sqrt(x)) | zeta(2) remains unconditional; independently proved looser tail 2/sqrt(x). |
| Section 5.2 final constants | Source uses x>=132, log(q/pi)<=2sqrt(x)-1, and RH-derived errors | None is used. The common budget (5.2) supplies the new constants. |

The only gamma functions needed beyond the exact definitions are their special
values g_0 and g_1 and the explicit residues E_a. The term g_a-E_a is estimated,
not silently discarded. The imaginary part of B(chi) is never needed here.

## 8. Primitive versus imprimitive characters

The theorem's q is the **primitive conductor**, not an arbitrary modulus.
A principal character is excluded: its inducing conductor is 1 and its
L-function has a pole at 1.

If a nonprincipal chi modulo Q_0 is induced by primitive chi* of conductor f,
then the exact identity is

    L(1,chi)=L(1,chi*) product_{p|Q_0, p not dividing f}
                                      (1-chi*(p)/p).             (8.1)

Consequently, if log f>=15, (T) transfers only with the explicit additional
factors

    [zeta(2)/(exp(gamma)(8 log log f+2))]
       product_{p|Q_0, p not dividing f}(1-1/p)
       <= |L(1,chi)|
       <= exp(gamma)(8 log log f+2)
          product_{p|Q_0, p not dividing f}(1+1/p).               (8.2)

Primes dividing both f and Q_0/f do not contribute an extra factor. This
report does not claim that these products can be dropped or that replacing f
by Q_0 automatically proves the identical bound for every imprimitive
character. In particular a large modulus does not guarantee the threshold
on its small inducing conductor. The class-number application uses primitive
Kronecker characters and has no such issue.

## 9. First falsification/control checks and outstanding work

The recommended first control has two parts.

1. **Restore the GRH line in the kernels.** With beta=1/2, replace 8 in
   (1.1), (2.8), and (3.2) by 2 and c(x) by 2/sqrt(x). The resulting
   Lemma-2.5 and Lemma-2.6 errors are exactly LLS's errors. Optimizing the
   general truncation with exponent 2 gives c_0=1/2 and the source leading
   constants 2 exp(gamma) and 12 exp(gamma)/pi^2. Failure of this check points
   to a lost factor of t, a wrong kernel denominator, or a missing factor 2.
2. **Falsify a naive off-line denominator replacement.** Take a formal
   reflected real pair {1/8,7/8}, integration variable u=1, and compare
   sum 1/|rho-1|^2 with b. Their ratio is 50/7, not 2. The safe 8b bound
   passes; simply retaining the GRH constant fails. Also check signs in
   (2.10) directly against the pre-estimation identities (2.2), (2.6).

The exact checker recomputes (4.6)--(4.8) by polynomial coefficients, both
the simple budget (5.1)--(5.6) and the refined Section 10 budget, elementary
logarithm enclosures and the formal-pair controls. The retained simple
certificate gives K<286849/108000<8/3 and bridge135/76<2; the current full
range uses K<603/100 and the shifted bridge in Section 10. All certificate
decisions use exact Fractions.

Six deliberate rejection controls exercise a too-small or negative pairing
constant, too-small conductor threshold, the invalid retained-GRH denominator
constant, an insufficient p=2 envelope and an overstated additive constant.
They test this certificate; except for the formal-pair obstruction, they do
not prove that another method could not improve a rejected parameter.

From the repository root (Python standard library only):

```sh
python3 research/zero-pairing/constants.py
python3 research/l-one-bounds/constants.py
python3 verify/check.py all
python3 -m unittest discover -s tests
```

Expected new-check result: `all constants and algebraic controls pass`, nine
`REJECT control` lines, p=2 margin17/7200, the retained simple margin1151/108000,
and the refined K<603/100 and bridge5637121/969800<728/125.
The shared verifier checks its existing Miller--Rabin claims; it does not
verify the new L-value theorem. Source research and author checks do not
substitute for a separate fresh-context theorem recheck.

Not checked: H(7/8) or its Lean proof, a new proof of classical analytic
continuation/functional equations/contour convergence, conductors below the stated range,
optimized truncations, optimal constants or a product-free imprimitive
statement. The proof checks the algebraic consequences of those published
analytic inputs and supplies uniform error envelopes, not a finite numerical
search over conductors or L-values. The separate AI recheck and its reviewed
snapshot are recorded in [RECHECK.md](RECHECK.md); maintainer review remains pending.

## 10. Refined truncation: the entire range log q>=15

Put a=31/50, L=log q, x=(aL)^8, y=aL and t=8 log y. This changes the
truncation, while retaining M(q)=exp(gamma)(8 log L+2) in the conclusion.
Let L0=15, y0=93/10, x0=y0^8. Exact rational logarithm bounds give

    t_- := 446/25 < 8 log y0 < 17841/1000 =: t_+,
    log(50/31) > 239/500.                                       (10.1)

In particular x>=x0>256>100, so all prior kernel and Euler-envelope ranges
hold throughout the new conductor range.

First sharpen the zeta upper estimate in (4.1). The accepted first-T1
input gives b_z<231/10000. Also the elementary harmonic lower bound
gamma>H_100-log101>57/100 is certified exactly. By (3.1), the decreasing
c(x), and log(2pi)<3, for every x>=256,

    T_z(x) <= t-1-gamma+3/x+c(x)b_z < t-3/2,

because

    3/256+(189/125)(1/2+1/16)(231/10000) < 7/100.                (10.2)

The negative trivial-zero series was dropped in this upper bound. Reusing
(2.2), E_a<=0 and Q<=L now gives

    b <= [L/2+t-3/2]/d(x).

Let c0=c2(1/y0+1/y0^4) and D0=1-c0. For L>=L0, c(x)<=c0 and d(x)>=D0>0.
The ratio (t-3/2)/L decreases because its derivative has the sign of
19/2-t, which is negative since t>t_->19/2. Consequently

    b/L <= B0 := [1/2+(t_+-3/2)/15]/D0,
    D0 = 57989077/69264075,
    B0 = 22017664161/11597815400.                                (10.3)

The product c(x)L=c2(1/a+1/(a^4 L^3)) decreases, as do c(x), 1/(yt),
t/L, t/L^4 and every reciprocal-power residual used below. These facts
follow by differentiating, using t>t_->17 and t'=8/L.

Return to J_chi and J_z before rounding b_z to 1/2 in (5.2). Their exact
upper envelopes and the lower Euler tail give

    K <= (b+b_z)[c(x)+8/(yt)]
         +[b+L/2+t+5]/x+2/(xt)+1/(3x^3t)+2t/y^4.                (10.4)

The constant5 charges the gamma correction2 and log(2pi)<3. Uniformly for
L>=15, the right side is at most the following rational number, where
z=231/10000 and c0, D0, B0 are defined above:

    K0 = B0*15*c0 + 8B0/(a*t_-)+z*c0+8z/(y0*t_-)
         +(15B0+15/2+t_++5)/x0
         +2/(x0*t_-)+1/(3x0^3*t_-)+2t_+/y0^4
       < 603/100.                                               (10.5)

The exact checker recomputes every term; K0 is about6.0182 for display
only. Each substitution above increases a nonnegative error. In particular
the uniform b/L and c(x)L estimates charge their product separately,
and the two integrated zero errors retain their factors1/t.

As in (5.5), both desired logarithmic bounds now have error at most
k/t with k=503/100. For t>0 set g(t)=t(exp(k/t)-1). Its derivative is
exp(k/t)(1-k/t)-1<=0, so g decreases. For 0<=s<3 the positive exponential
series and its geometric tail give

    exp(s) <= 1+s+s^2/[2(1-s/3)].

Using s=k/t_- yields the exact bound

    g(t) <= k+k^2/[2t_-(1-k/(3t_-))]
          = 5637121/969800 < 728/125.                             (10.6)

By (10.1), 728/125 < 2+8log(50/31). Since t=8log L-8log(50/31),

    t exp(k/t) < t+2+8log(50/31)=8log L+2.

Exponentiating the two logarithmic bounds therefore proves (T) over the
entire range L>=15. The same class-number normalization gives (CN), and
the imprimitive extension (8.2) now requires log f>=15. No smaller-conductor
enumeration, omitted Euler factor or GRH-only estimate is used.

## 11. A parameter theorem with leading factor r

Section 11 proves the following additional conditional statement. For any
real beta in [13/15,7/8], assume H(beta), including zeta, and let
r=1/(1-beta). For primitive conductor q with log q>=20, put

    M_beta(q)=exp(gamma)[r log log q+2].

Then pi^2/(6M_beta)<=|L(1,chi)|<=M_beta, with the same class-number and
explicitly factored imprimitive consequences. The leading factor is r
instead of 8. The earlier H(7/8) theorem keeps its better threshold 15;
it is not weakened by this new parameter statement.

Here beta denotes the strip parameter, while A=-Re B(chi) denotes the
quantity called b in the earlier sections. The functional equation and
conjugation again pair rho with 1-conjugate(rho) within the same character,
including complex characters, and give 1-beta<=Re rho<=beta.
For an off-line pair sigma>=1/2, the AM--GM argument of accepted Lemma0'
part2 bounds its shifted-kernel ratio by

    [x^(sigma-1)+x^(-sigma)]/[2sqrt(sigma(1-sigma))]
       <=c2[x^(beta-1)+x^(-1/2)],   c2=189/125.

This holds because beta(1-beta)>=7/64 and 7*c2^2>16. Line zeros have
ratio 2x^(-1/2), also covered. All weights and absolute summands are
nonnegative and convergent. Termwise, the static reciprocal-square bound
is rA<=8A. These statements apply to zeta as well. Thus

    |Z_chi(x)|<=c_beta(x)A,
    c_beta(x)=c2[x^(beta-1)+x^(-1/2)].                            (11.1)

For the integrated zero term, u>=1 still gives |rho-u|>=|rho-1|.
The reflected static bound is at most 8A, and now
integral_1^infinity x^(beta-u)du=x^(beta-1)/t. With y=x^(1-beta),

    |R_chi(x)|<=8A/(y t^2),   |R_z(x)|<=8b_z/(y t^2).            (11.2)

This also justifies absolute interchange and the endpoint u=1 under the
same declared classical contour and Hadamard inputs. The identities,
conductor cancellation, gamma errors, Laurent pole term and finite Euler
minimum in Sections2--4 are otherwise unchanged. In particular their
common logarithmic error numerator is

    K<= (A+b_z)[c_beta(x)+8/(yt)]
          +(A+L/2+t+5)/x+2/(xt)+1/(3x^3t)+2t/sqrt(x).           (11.3)

The last term charges the lower Euler tail. Both desired logarithmic
inequalities are bounded using (K-1)/t, with the factor zeta(2) retained
in the lower L-value direction. No r=8 identity is used in (11.2).

For L=logq>=20, choose a=31/50, y=aL, x=y^r and t=rlogy. Since
15/2<=r<=8 and y>1,

    x>=y^7,   sqrt(x)>=y^3,
    c_beta(x)<=c2(1/y+1/y^3).                                   (11.4)

All kernels are in range: at L0=20, y0=62/5 and y0^7>256>100.
The finite Euler minimum, including its p=2 certificate, requires only
x>=100 and therefore still applies. H(beta) implies H(7/8), so the
sharper principal estimate (10.2), T_z(x)<t-3/2, remains available.
It also follows directly from the same residue identity and (11.1),
because c_beta(x)<=c_(7/8)(x). Hence

    A <=[L/2+t-3/2]/d_beta(x),
    d_beta(x)=1+1/x-c_beta(x).

At the common endpoint define

    t_-=75/4 <(15/2)log(62/5),
    t_+=81/4 >8log(62/5),
    c0=c2(1/y0+1/y0^3),
    D0=1-c0=5226959/5958200>0,
    B0=[1/2+(t_+-3/2)/20]/D0=17129825/10453918.

The logarithm enclosures are rational. For every fixed r in this interval,
the derivative of (t-3/2)/L has sign r-t+3/2<0 throughout L>=20.
The lower denominator1-c2(1/y+1/y^3) increases. Therefore A/L<=B0
uniformly; no monotonicity of A itself is assumed.

Every contribution in (11.3) now has a uniform endpoint bound. For Ac,
use A/L<=B0 and Lc<=c2[1/a+1/(a^3L^2)], which decreases. For8A/(yt)
retain the factor 1/a and t>=t_-. The b_z terms decrease individually.
Replace x by its lower bound y^7 in all residual denominators and
sqrt(x) by y^3 in the Euler tail. The terms t/y^7 and t/y^3 decrease,
since their derivative signs are r-7t and r-3t. All remaining positive
power and logarithmic terms also decrease on this whole domain. It follows
that K is at most the exact rational sum

    K0=B0*20*c0+8B0/(a t_-)+b_z*c0+8b_z/(y0 t_-)
         +(20B0+10+t_++5)/y0^7
         +2/(y0^7t_-)+1/(3y0^21t_-)+2t_+/y0^3,
    b_z=231/10000,
    K0=41529079804084400024857080315711576661138167507691
         /8025592730848948716555384727022562665766912000000
       <26/5.                                                   (11.5)

The positive margin to26/5 is
204002396330133301230920264805749200849774892309 divided by the same
denominator. All powers of a and both integrated zero tails are retained.

Take k=21/5. The same decreasing function g(t)=t(exp(k/t)-1) and
exponential-series upper bound used in Section10 give

    g(t)<=k+k^2/[2t_-(1-k/(3t_-))]=8169/1735<5.

Also log(50/31)>239/500, so for every allowed r,

    2+rlog(50/31)>=2+(15/2)log(50/31)>1117/200>5.

Since t=rlogL-rlog(50/31), this proves
texp(k/t)<rlogL+2. Exponentiating both common logarithmic bounds yields
the claimed M_beta and zeta(2)/M_beta. The class-number statement is

    pi sqrt(q)/(6M_beta)<=h(-q)<=M_beta sqrt(q)/pi

for negative fundamental discriminants -q with logq>=20. For an imprimitive
character, retain the exact Euler products and the two comparison products
from Section8, replacing its envelope by M_beta and requiring logf>=20
on the primitive inducing conductor f. A large modulus alone does not
meet the condition. No product-free imprimitive assertion is made.

At beta=8748867/10000000 the leading r is exactly 10000000/1251133;
the frontier's Xu--Sang v2 reference is an optional source for this assumed
half-plane, not a certified proof of it. See
[the versioned primary theorem](https://arxiv.org/html/2610.15291v2),
which is itself conditional on its recorded analytic inputs and H(7/8).
The present result assumes H(beta) directly throughout the full interval.

The checker retains the threshold 32 and threshold 15 certificates and their
six controls. Three additional controls reject beta=9/10, the fixed
endpoint enclosure at threshold 19, and additive 1 with this budget. These
are failures of the stated certificate, not impossibility theorems for
different truncations. The parameter theorem is author-checked and awaits
its own fresh-context recheck. No earlier report certifies this new leading
factor, range or uniform parameter transfer.
