Original idea: Geoffrey Irving.

# Independent mathematical recheck, ROUND3: the real parameter interval

**Verdict: PASS for the conditional Section 11 theorem at the frozen hashes
below.** I found no required mathematical, checker, or scope correction and
no unresolved objection. The argument covers every real beta in the closed
interval [13/15,7/8] and the entire closed conductor range log q>=20.
The earlier H(7/8) theorem retains its threshold log q>=15.

Reviewer: Codex, fresh-context same-model AI review, 2026-10-23. This is not
human review, formal verification, maintainer acceptance, or a proof of any
H(beta). I independently reconstructed the parameter transfer, integrated
zero estimate, conductor cancellation, endpoint majorants and arithmetic.
The author's checker was executed afterward as additional evidence.
Parent checks, source research, and the two earlier PASS reports were not
counted as verification of this new theorem.

I read `AGENTS.md`, `DISCOVERY.md`, `discover/frontier.json`, this package's
proof, checker, README and prior reviews, the relevant accepted first-T1
and zero-pairing inputs, and the separately recorded negative-c2 guard
disposition. The accepted record, rather than historical draft banners,
determines the status of those inputs. No unmerged sibling theorem is used.
There were no unresolved mathematical objections in the previous package
reviews. The guard correction remains present and was checked again here;
it does not itself verify the parameter theorem.

Worktree: `lone/`, branch `session/20261023-lone`. Local HEAD is
`be895346f6b510a17f1f7517f064b93c00559509`, matching the published
[PR #13](https://github.com/discoveryathome/miller-rabin/pull/13) head
specified in the review brief. The accepted base is
`d2bd5167a42b8256f1362640dc149057920e5db9`, also the checked merge-base.
Remote HEAD and CI were not refreshed. The three frozen inputs were
uncommitted at review start; this verdict attaches to their bytes below,
not to HEAD alone.

## Conclusion and exact scope

Assume H(beta), explicitly including zeta, for a real
13/15<=beta<=7/8. Write

    r=1/(1-beta),             15/2<=r<=8,
    L=log q>=20,
    M_beta(q)=exp(gamma)(r log L+2).

For each primitive Dirichlet character of conductor q, the checked result is

    zeta(2)/M_beta(q) <= |L(1,chi)| <= M_beta(q),
    zeta(2)=pi^2/6.

Equivalently the reciprocal is at most
`(6 exp(gamma)/pi^2)(r log log q+2)`. The exact threshold is q>=exp(20).
A primitive principal character has conductor 1 and is excluded by this
range. No assertion for smaller conductors is established here. At beta=7/8,
Section 10 additionally supplies the same envelope throughout log q>=15.

For negative fundamental discriminant -q in the parameter range, q>4 and
the primitive Kronecker character has positive real L-value. Thus
`h(-q)=sqrt(q)L(1,chi_-q)/pi` gives precisely

    pi sqrt(q)/(6M_beta(q)) <= h(-q) <= M_beta(q)sqrt(q)/pi.

For a nonprincipal imprimitive character modulo Q induced by primitive chi*
of conductor f, Section 11 retains

    L(1,chi)=L(1,chi*) product_{p|Q, p not dividing f}(1-chi*(p)/p).

With log f>=20, its modulus lies between

    [zeta(2)/M_beta(f)] product_{p|Q, p not dividing f}(1-1/p)

and

    M_beta(f) product_{p|Q, p not dividing f}(1+1/p).

Increasing prime exponents at primes already dividing f creates no extra
factor. A large Q with a small inducing conductor does not meet the
threshold. There is no product-free imprimitive conclusion.

The exact specialization at theta=8748867/10000000 is
`r=10000000/1251133`, and theta is strictly inside the checked interval.
No rounded exponent or decimal leading coefficient is substituted for r.
The Xu--Sang reference is optional provenance for an assumed half-plane;
its proof and its analytic premises are not certified or used to discharge
H(beta) in this review.

## Reconstruction of the zero bounds

Put A=-Re B(chi)=sum_rho Re(1/rho). This is the real-part quantity, not
the modulus of the complex Hadamard constant. Functional equation plus
conjugation gives the same-character involution
`rho -> 1-conjugate(rho)`, also for complex characters, with multiplicity.
H(beta) therefore gives the closed strip
`1-beta<=Re rho<=beta`. The accepted Hadamard identity and positive terms
give

    sum 1/|rho|^2 <= r A <= 8A,
    sum 1/|1-rho|^2 = sum 1/|rho|^2.

The second equality uses the reflected multiset, not a false termwise
equality of |rho| and |1-rho| off the critical line.

For a reflected off-line pair with sigma=Re rho>=1/2, set
U=|rho|^-2, V=|1-conjugate(rho)|^-2. Its absolute shifted-kernel sum
divided by its A mass is at most

    (x^(sigma-1)+x^(-sigma))*sqrt(UV)/(sigma U+(1-sigma)V)
      <= [x^(sigma-1)+x^(-sigma)]/[2sqrt(sigma(1-sigma))].

On the whole parameter interval, beta(1-beta)>=7/64, and

    c2=189/125>0,             7*c2^2-16=47/15625>0.

Since sigma<=beta and sigma>=1/2, the ratio is consequently at most
`c2[x^(beta-1)+x^(-1/2)]`. A line zero has ratio `2x^(-1/2)`;
`x^(beta-1)>=x^(-1/2)` and c2>1 cover it as well. Positive convergent
sums may be regrouped into these pairs. Hence, for every x>1,

    |Z_chi(x)| <= c_beta(x) A,
    c_beta(x)=c2[x^(beta-1)+x^(-1/2)].

Only the argument of accepted Lemma 0' part 2 is required. Its part 1
and any witness-theorem coefficient are unnecessary. The same reasoning
applies to zeta, with A replaced by b_z=-B_z.

For the integrated term let t=log x and u>=1. Direct subtraction gives

    |rho-u|^2-|rho-1|^2=(u-1)(u+1-2Re rho)>=0.

It follows, before the outside 1/t in the residue identity, that

    sum_rho integral_1^infinity |x^(rho-u)/(rho-u)^2| du
       <= 8A integral_1^infinity x^(beta-u) du
       = 8A x^(beta-1)/t.

For y=x^(1-beta) this proves

    |R_chi(x)|<=8A/(y t^2),      |R_z(x)|<=8b_z/(y t^2).

The estimate includes u=1, gives absolute domination for the interchange
and endpoint limit under the declared classical contour inputs, and has
both factors 1/t. It does not retain the r=8 relation y=x^(1/8): the
identity here is `x^(beta-1)=1/y` for the actual real parameter beta.
Using the looser static coefficient 8 instead of r is valid uniformly.

## Unchanged identities and their applicability

I consulted the primary [LLS v3 TeX source](https://arxiv.org/src/1309.3595v3)
and [versioned PDF](https://arxiv.org/pdf/1309.3595v3), the latter 23 pages
and stamped 8 December 2016. Relevant source lines are 500-546 for the
character residue identity, 565-566 for zeta's zero-term sign, 593-595 and
639-640 for the kernels before their RH estimates, 651-665 for the pole
limit, and 1291-1328 for the finite minimum and even-power rearrangement.
Equation (1.3), PDF page 4, fixes the class-number normalization.
Actual downloaded hashes are recorded below.

To avoid confusing the scale a=31/50 with character parity, write epsilon
for parity in this paragraph. With Q=log(q/pi), the two real identities are

    (1+1/x)A+Re Z_chi=(1-1/x)Q/2-T_chi+E_epsilon,
    log|L(1,chi)|=A_chi+(Q/2+g_epsilon-A)/t+R_chi+H_epsilon.

Their exact elimination, with F_chi=A_chi+T_chi/t, is

    log|L(1,chi)|=F_chi
       +[A/x+Re Z_chi+Q/(2x)+g_epsilon-E_epsilon]/t
       +R_chi+H_epsilon.

This checks the conductor cancellation and each correction sign. For
x>=100, the displayed residue series imply E_epsilon<=0 and
`|g_epsilon-E_epsilon|<=(t+2)/x`. The even series has tail at most
`x^-3/[6(1-x^-2)]`, the odd one at most
`x^-2/[2(1-x^-2)]`. The elementary gamma and logarithm bounds in the
package suffice for those inequalities. Throughout this conductor range
Q>0 and Q<=L. The entire trivial-zero integral satisfies
`0<=H_epsilon<=2/(x t^2)`. These facts give

    |log|L(1,chi)|-F_chi| <= J_chi/t,
    J_chi=A[c_beta+1/x+8/(yt)]+[Q/2+t+2]/x+2/(xt).

Zeta's T_z identity has `-Z_z` and a negative trivial-zero series.
Its pole calculation retains the main term
`A_z=log t+gamma-1+gamma/t+epsilon_z`, where

    |epsilon_z|<=8b_z/(y t^2)+1/(3x^3t^2).

For an independent check of the pole constant, put delta=u_0-1>0.
The pole integral is

    I(delta)=integral_delta^infinity exp(-tv)/v^2 dv
            =exp(-t delta)/delta-t E_1(t delta).

Using the unconditional expansions
`E_1(z)=-gamma-log z+O(z)`,
`log zeta(1+delta)=-log delta+O(delta)`, and
`zeta'/zeta(1+delta)=-1/delta+gamma+O(delta)`, one obtains

    I(delta)+t log zeta(1+delta)+zeta'/zeta(1+delta)
       -> t(log t+gamma-1)+gamma.

Dividing by t gives the stated main term independently of RH. Zeta's
trivial zeros start at n=1; their sum is at most x^-2/3 for x>=2,
which supplies the stated `1/(3x^3t^2)` allowance. Combining A_z and T_z
therefore retains the essential -1/t:

    F_z<=log t+gamma-1/t+J_z/t,
    J_z=b_z[c_beta+8/(yt)]+log(2pi)/x+1/(3x^3t).

Thus the changed half-plane replaces all zero-dependent RH estimates in
LLS Lemmas 2.3-2.6. The pole, digamma values and trivial-zero residues
remain classical inputs with explicit error charges. No RH estimate for
T_chi from Section 5, RH real-B denominator `(1+-1/sqrt(x))^2`, LLS
threshold q>=10^10, or source truncation `(log q)^2/4` is imported.

I also rechecked the finite Euler minimum's applicability and algebra.
With p fixed, K=floor(t/log p), v=1/p and h=log p/(xt), its weights
`w_k=v^k/k-h` are nonnegative and decreasing for 1<=k<=K. They apply to
real x as well as integer x; endpoint weights vanish. Primes with chi(p)=0
are covered by the nonpositive alternating envelope. For nonzero phases,
`Q_k=(1-cos(k phi))/(1-cos phi)` lies in [0,k^2], continuously at phi=0.
For p>=3 the lower ratio is at least

    v-2v^2/(1-v^2)^2 >= (5/32)v>0.

The omitted h coefficient is nonnegative when K>=2; K=1 is immediate.
For p=2, x>=100 gives K>=6. Independently generating cos(k phi) by its
polynomial recurrence reproduces the package's first five Q_k, and the
even tail from k=6 is 5/36. The resulting polynomials are

    P(z)=229/1440-(13/120)z+z^2/60-z^3/40+z^4/10,
    H(z)=-1+2z+8z^2-8z^3-16z^4.

On [-1,1], P>=37/1440 and H>=-15. The factorization of H+15 has a
positive cubic, whose derivative is `48(z+1/2)^2+4` and value at -1 is 6.
Since h<7/4500,

    P+hH>37/1440-15*(7/4500)=17/7200>0.

This proves the minimum for arbitrary complex phases, rather than just
real sign choices. The minimizing independent prime choices need not be
realizable by a Dirichlet character.

The even-power rearrangement is exactly

    min-envelope F_chi=-F_z+C_2,
    C_2=sum_{m<=sqrt(x)} Lambda(m)/(m^2 log m)-2psi(sqrt(x))/(xt).

The binomial-coefficient induction in Section 4 proves psi(v)<=2v for
all real v>=1. Its odd-integer induction step is valid already for N>=5.
The missing infinite sum and subtracted Chebyshev term are bounded by
`1/(sqrt(x)-1)+4/(sqrt(x)t)<=2/sqrt(x)` when x>=100. Hence

    -F_z+log zeta(2)-2/sqrt(x) <= F_chi <= F_z.

The lower L-value factor zeta(2) and Euler-tail charge 2t/sqrt(x) are
therefore both retained. This entire finite argument is independent of RH.

## Uniform endpoint proof for all real parameters

Choose a=31/50, y=aL, x=y^r and t=r log y. Since y>=62/5>1 and
15/2<=r<=8,

    x>=y^7,       sqrt(x)>=y^3,
    c_beta(x)<=c_bar(L):=c2[(aL)^-1+(aL)^-3].

In particular x>=y_0^7>256>100. All residue, sign, integral and finite
Euler ranges hold, including for irrational beta and noninteger x.

H(beta) implies H(7/8). The sharper zeta estimate (10.2) is an estimate
for every x>=256, not just for Section 10's choice of x. Independently,
the harmonic lower bound gives gamma>57/100, the exact b_z formula gives
b_z<231/10000, and its positive charge at x=256 is

    3/256+c2*(9/16)*(231/10000)=313653/10000000<7/100,
    7/100-313653/10000000=386347/10000000>0.

Here c_beta(x)<=c_(7/8)(x). Dropping the negative trivial-zero series
in T_z gives T_z<t-3/2 throughout the new range. I independently
certified both gamma and b_z constants in the arithmetic below.

Since -T_chi<=T_z and E_epsilon<=0, the exact identity gives

    A<=[L/2+t-3/2]/d_beta(x),
    d_beta(x)=1+1/x-c_beta(x)>=D(L):=1-c_bar(L)>0.

The endpoint logarithm enclosures are

    t_lo=75/4 <(15/2)log(62/5),
    8log(62/5)<81/4=t_hi.

For every fixed real r in the interval, t'=r/L and

    ((t-3/2)/L)'=(r-t+3/2)/L^2<0,
    r-t+3/2<8-75/4+3/2=-37/4.

D(L) increases and the numerator of A/L's envelope is positive and
decreases. Thus throughout the whole ray L>=20,

    c0=731241/5958200,
    D0=1-c0=5226959/5958200,
    A/L<=B0=[1/2+(t_hi-3/2)/20]/D0=17129825/10453918.

This does not assume A itself decreases.

Combining the two logarithmic estimates and the Euler envelopes gives
the common numerator K=J_chi+J_z+2t/sqrt(x), bounded by

    (A+b_z)[c_beta(x)+8/(yt)]
      +(A+L/2+t+5)/x+2/(xt)+1/(3x^3t)+2t/sqrt(x).

The constant 5 charges the gamma allowance 2 and log(2pi)<3. Both
desired logarithmic inequalities have error at most (K-1)/t; the lower
direction also retains -log zeta(2) in the reciprocal bound.

Every substitution in the following endpoint budget is uniform:

- `A c_beta <= (A/L)(L c_bar)`, where
  `L c_bar=c2[1/a+1/(a^3L^2)]` decreases.
- `8A/(yt)<=8B0/(a t)` decreases. The factor 1/a is essential.
- Both b_z terms decrease after replacing b_z by z=231/10000.
- `A/x<=B0/(a^7L^6)` and `L/(2x)<=1/(2a^7L^6)` decrease.
  Also 5/y^7 decreases and `(t/y^7)'` has sign
  `r-7t<8-7*(75/4)=-493/4`.
- `1/(y^7t)` and `1/(y^21t)` decrease, since both positive factors in
  their denominators increase.
- The Euler-tail majorant 2t/y^3 decreases, since its derivative has
  sign `r-3t<8-3*(75/4)=-193/4`.

At L=20, each numerator t may consequently be bounded by t_hi and each
denominator t by t_lo. In particular t_hi is not asserted to bound t
globally. No differentiation in beta, parameter grid, monotonicity of A,
or finite sampling of conductors is needed. These signs apply uniformly
to every real r in the closed interval.

The eight endpoint contributions are as follows. Decimals are displays
only; the expressions and sum were evaluated as exact rationals.

| Term | Endpoint expression | Display |
|---|---|---:|
| A c_beta | B0*20*c0 | 4.02206689396262722 |
| Character zero integral | 8B0/(a*t_lo) | 1.12764101140516567 |
| Zeta shifted kernel | z*c0 | 0.00283502854889060 |
| Zeta zero integral | 8z/(y0*t_lo) | 0.00079483870967742 |
| Conductor and gamma residual | (20B0+10+t_hi+5)/y0^7 | 0.00000150903053580 |
| Character trivial-zero residual | 2/(y0^7*t_lo) | 0.00000000236633881 |
| Zeta trivial-zero residual | 1/(3*y0^21*t_lo) | 1.9409845783e-25 |
| Lower Euler tail | 2t_hi/y0^3 | 0.02124173408076265 |

Their sum and margin are exactly

    K0=41529079804084400024857080315711576661138167507691
       /8025592730848948716555384727022562665766912000000,

    26/5-K0=204002396330133301230920264805749200849774892309
       /8025592730848948716555384727022562665766912000000>0.

Thus K<=K0<26/5 on the whole domain. The powers a^3, a^7 and a^21 in
these coarser integer-power majorants, as well as both integrated tails,
have all been charged.

## Exponentiation and the two directions

Set k=21/5. The common budget gives

    log|L(1,chi)| <= log t+gamma+k/t,
    log(1/|L(1,chi)|) <= log t+gamma-log zeta(2)+k/t.

For g(t)=t(exp(k/t)-1),
`g'(t)=exp(k/t)(1-k/t)-1<=0`. The positive exponential series gives
`exp(s)<=1+s+s^2/[2(1-s/3)]` for 0<=s<3, because the successive
factorials from degree two dominate 2*3^(n-2). Since t>t_lo,

    g(t)<=k+k^2/[2t_lo(1-k/(3t_lo))]=8169/1735<5,
    5-8169/1735=506/1735>0.

The independently enclosed scale logarithm satisfies

    log(50/31)>239/500,
    2+rlog(50/31)>=2+(15/2)log(50/31)>1117/200>5.

Using `t=rlog L-rlog(50/31)` therefore proves
`t exp(k/t)<rlog L+2`. Exponentiating each logarithmic inequality gives
exactly the two L-value bounds stated above, followed by their class-number
and factored imprimitive consequences. Strict internal margins leave both
parameter endpoints and L=20 covered by the stated non-strict conclusions.

## Independently reproducible arithmetic

This standard-library calculation was executed in an isolated read-only
calculation, without importing `constants.py` or `verify/check.py`.
In particular it uses positive exponential series to prove the needed
logarithm enclosures, rather than the author's `ln_bounds` helper.
For v>=0, the omitted exponential tail after degree N is at most its
first term divided by `1-v/(N+2)`; all subsequent term ratios are smaller.

The b_z check also supplies an independent bound beyond its accepted F1
input. If A_N=H_N-log N, then

    A_N-gamma
      =sum_{n>=N}[log(1+1/n)-1/(n+1)]
      >(1/2)sum_{m>=N+1}m^-2>1/[2(N+1)].

The first inequality follows by integrating
`(n+1-u)/(u(n+1))` over [n,n+1]. Machin's identity and alternating
arctangent partial sums give the required rational lower bound on pi.
These facts make the exponential comparison for b_z below rigorous.

```python
from fractions import Fraction as F

def exp_bounds(v, N=80):
    assert 0 <= v < N+2
    term = total = F(1)
    for j in range(1, N+1):
        term *= v/j
        total += term
    return total, total + (term*v/(N+1))/(1-v/F(N+2))

def atan_partial(v, N):
    return sum(((-1)**j*v**(2*j+1)/F(2*j+1)
                for j in range(N)), F(0))

a, ell, c2, z = F(31,50), F(20), F(189,125), F(231,10000)
y = a*ell
tlo, thi = F(75,4), F(81,4)
assert exp_bounds(F(5,2))[1] < y
assert exp_bounds(F(81,32))[0] > y
assert exp_bounds(F(239,500))[1] < 1/a
H100 = sum((F(1,j) for j in range(1,101)), F(0))
assert exp_bounds(H100-F(57,100))[0] > 101
pi_lo = 16*atan_partial(F(1,5),20)-4*atan_partial(F(1,239),5)
N = 250
HN = sum((F(1,j) for j in range(1,N+1)), F(0))
assert exp_bounds(2+HN-F(1,2*(N+1))-2*z)[1] < 4*pi_lo*N
assert exp_bounds(F(27,40))[1] < 2 < exp_bounds(F(7,10))[0]
assert exp_bounds(F(9,2))[1] < 100 < exp_bounds(F(5))[0]
assert c2 > 0 and 7*c2*c2-16 == F(47,15625)
assert y**7 > 256
assert F(3,256)+c2*F(9,16)*z == F(313653,10000000) < F(7,100)

c = c2*(1/y+1/y**3)
D = 1-c
B = (F(1,2)+(thi-F(3,2))/ell)/D
assert D == F(5226959,5958200)
assert B == F(17129825,10453918)
terms = [B*ell*c, 8*B/(a*tlo), z*c, 8*z/(y*tlo),
         (B*ell+ell/2+thi+5)/y**7, 2/(y**7*tlo),
         1/(3*y**21*tlo), 2*thi/y**3]
K = sum(terms)
assert K == F(41529079804084400024857080315711576661138167507691,
              8025592730848948716555384727022562665766912000000)
assert F(26,5)-K == F(204002396330133301230920264805749200849774892309,
                      8025592730848948716555384727022562665766912000000)
assert K < F(26,5)
k = F(21,5)
bridge = k+k*k/(2*tlo*(1-k/(3*tlo)))
assert bridge == F(8169,1735) < 5 < F(1117,200)
assert 2+F(15,2)*F(239,500) == F(1117,200)
assert 8-tlo+F(3,2) < 0 and 8-7*tlo < 0 and 8-3*tlo < 0

# Generate the p=2 polynomials independently from cos(k phi)'s recurrence.
T = [[F(1)], [F(0),F(1)]]
for k in range(2,6):
    twice_z = [F(0)]+[2*v for v in T[-1]]
    older = T[-2]+[F(0)]*(len(twice_z)-len(T[-2]))
    T.append([u-v for u,v in zip(twice_z,older)])
P, H = [F(0)]*5, [F(0)]*5
for k, Tk in enumerate(T[1:],1):
    numerator = [1-Tk[0]]+[-v for v in Tk[1:]]
    quot, running = [], F(0)
    for coef in numerator:
        running += coef
        quot.append(running)
    assert quot[-1] == 0
    for degree, coef in enumerate(quot[:-1]):
        P[degree] += (-1)**(k-1)*coef/F(k*2**k)
        H[degree] += (-1)**k*coef
P[0] -= F(5,36)
assert P == [F(229,1440),-F(13,120),F(1,60),-F(1,40),F(1,10)]
assert H == [-1,2,8,-8,-16]
assert F(37,1440)-15*F(7,4500) == F(17,7200) > 0
print(D, B, K, F(26,5)-K, bridge, 'independent arithmetic PASS')
```

The real-variable proofs above, rather than execution at finitely many beta
values, establish uniformity. The script certifies their rational endpoints
and arithmetic; it does not prove H(beta) or the contour identities.

## Author checker and rejection reasons

I ran `python3 -B research/l-one-bounds/constants.py` from the repository
root: exit 0, all nine `REJECT control` lines, p=2 margin 17/7200, and
`all constants and algebraic controls pass`. The old simple and refined
positive certificates were retained and executed in that run. Their
reported bounds remained 286849/108000 and the Section 10 K0, respectively.
The new helper returned exactly the K0, positive margin and 8169/1735
bridge above at beta=13/15, beta=7/8 and beta=8748867/10000000.

I separately called each control and inspected its actual ValueError:

| Control | Actual rejection message |
|---|---|
| c2=3/2 | pairing constant must dominate 4/sqrt(7) |
| c2=-189/125 | pairing constant must dominate 4/sqrt(7) |
| Refined threshold 14 | refined t endpoint enclosure |
| Retained GRH multiplier 2 | off-line reciprocal-square envelope |
| p=2 h allowance 1/500 | positive p=2 minimum envelope |
| Refined additive 1 | refined additive envelope |
| Parameter beta=9/10 | parameter pairing strip range |
| Parameter threshold 19 | parameter t endpoint enclosure |
| Parameter additive 1 | parameter additive envelope |

The reasons agree with the mathematics. The formal strip pair {1/8,7/8}
has reciprocal-square ratio 50/7, so a retained multiplier 2 fails; the
central-line positive control has ratio 2. This is a formal strip-bound
test, not an assertion that these are actual zeros. The h=1/500 trial
changes the certified p=2 margin to -31/7200. The threshold controls fail
their pinned t enclosures, and the additive controls fail their fixed
bridge comparisons. They do not establish sharp thresholds or rule out
other truncations, budgets or theorems. In particular the beta=9/10
control asserts only that it lies outside this proved parameter interval.

For the inherited exposed c2 guard, independent exact probes at
0, 3/2 and -189/125 rejected with the pairing-constant message; 189/125
and 1513/1000 passed. The conjunction `c2>0 and 7*c2**2>=16` is present.
The new helper fixes c2=189/125 internally and also checks its positivity.
The earlier guard objection is therefore disposed of at these bytes.

The checker itself operates with rational parameters and endpoint
inequalities. Its endpoint equality assertion is an execution check of a
uniform budget, not a numerical proof for all real beta. The written
parameter estimates supply that missing quantifier, including irrational
parameters and both closed endpoints. No issue was found in the README's
conductor, imprimitive-factor, conditionality or evidence statements.

## Exact reviewed snapshot and sources

These SHA-256 hashes were computed from actual bytes. The three frozen
input hashes were unchanged at the end of the substantive review.

| Frozen file | Bytes | SHA-256 |
|---|---:|---|
| `research/l-one-bounds/PROOF.md` | 35006 | `d7db4e2966035e0fcc78bb57fe18eb83259694833ce0ea6259b61dd0ae6cbca1` |
| `research/l-one-bounds/constants.py` | 10687 | `3b4155455b93cc38210ef51710a2b0c9f038b72a315ed2c36a2f1c85a59e41f2` |
| `research/l-one-bounds/README.md` | 4404 | `761a6937535f9fde760cc0ef731f6de5c42a0e78327d32e60d3f92d79ea8776d` |

The analytic input proofs and `verify/check.py` were byte-for-byte equal
in the worktree, HEAD and accepted base. Their hashes also match the
frontier's artifact records. The other frontier artifact hashes were
checked against disk as provenance checks, not as new theorem reviews.

| Input or evidence file | SHA-256 |
|---|---|
| `research/first-explicit-t1/PROOF.md` | `abd066b2d27961e93ae007e5fb8897b5a841aff875b24af3eb0216d73bed8cbb` |
| `research/zero-pairing/PROOF.md` | `824af09db62887a04107e72f9aafb56345aef45c1ea3ccf6499956d6896e914c` |
| `verify/check.py` | `ace2b055b5279284d04d37b6c6dde77af86088245846700c502effb3e812e709` |
| `AGENTS.md` | `e8f93ce38983d792791c3f9ad9b8b0a367668b3b7b945b071b6f360c45babd62` |
| `DISCOVERY.md` | `e603c2aaf4b9c692b315213f6c7dd5aebdfba5932e67155e53c76a6590ec4ddf` |
| `discover/frontier.json` | `9ca629138c133ac8547efba9b47f4d862ae82e7079c4da0998961d8fa5c964a4` |
| `research/l-one-bounds/RECHECK.md` | `f2ba422870a3cc90b44d819dc3bdb4cfef67e92a77707aef08e7b81747149037` |
| `research/l-one-bounds/RECHECK-REFINEMENT.md` | `ac39bb42be4caae371411da54e6f4bea499f600b5b00dec80028042f2fa55576` |
| `../nonresidue/research/least-nonresidue/GUARD-RECHECK.md` | `c75db68a3b80e6ebf38232a9298d0be16000898cd229a38045c68c485c28ca31` |

The versioned primary LLS downloads made during this review were:

| Source bytes | Length | SHA-256 |
|---|---:|---|
| `https://arxiv.org/src/1309.3595v3`, gzip response | 26276 | `301cb41d96db71a722f278b1e9db437cf71c275ea07cc0289f3a916d8208528c` |
| Decompressed TeX | 93372 | `2b5a85717f193b950ae522ad5c07f8f8bb1dc2213c073d54b4d4fa8cba6d98f8` |
| `https://arxiv.org/pdf/1309.3595v3` | 267062 | `692b7fe38d883cf3503e247b0ebcd0c092c7e7267b06488adb9f40d45095b5a8` |

The decompressed-source hash matches the hash stated in PROOF.md.
Only public source URLs were sent externally; repository text was not
submitted to a search service.

## Trust boundary and work not rerun

The verdict assumes H(beta), including its zeta application. It does not
establish the OpenAI or Xu--Sang source proofs or their analytic inputs.
Classical analytic continuation, functional equations, the Hadamard
real-part identity and convergence facts, contour-shift foundations,
special gamma-function values, and Dirichlet's class-number formula remain
declared classical inputs. I checked their use and the displayed residue,
pole, kernel, sign and finite-product calculations; I did not rebuild
those foundations. No Lean proof, kernel replay or formalization was run.

I did not rerun `python3 verify/check.py all`, the repository unittest
suite, the accepted zero-pairing numerical/grid checker, or unrelated
sibling-package checkers. Those check existing different claims and were
not used as verification of this parameter theorem. The old L-value
certificates and nine controls were executed within the package's own
checker, as distinguished above. No optimization, small-conductor
enumeration, L-value sampling or theorem outside the stated beta interval
was attempted. Arbitrary Python numeric-type behavior is not certified.

The only filesystem output created by this review is this report, written
with native `apply_patch`. Frozen inputs and prior reports were preserved;
there were no installs, further delegates, branch/index/commit mutations,
frontier changes, PR-content edits or public comments. Python execution
used bytecode-disabled or isolated calculations. Maintainer review and
any subsequent PR update remain separate steps.
