Original idea: Geoffrey Irving.

# Independent mathematical recheck, ROUND1

**Verdict: PASS for the stated conditional theorem.** I found no fatal issue or
mathematical correction required in the checked versions of `PROOF.md`,
`constants.py`, and `README.md`. This package is ready for maintainer review at
the hashes below. This verdict does not establish H(7/8) or confer acceptance.

Reviewer: Codex, in a separate fresh context using the same model as the author;
2026-10-23. This is an independent AI mathematical review, not human review or
formal verification. I read the instructions, the entire new proof and certificate,
and the relevant accepted source lemmas. I independently reconstructed the
cancellation, integrated zero estimates, zeta pole limit, finite Euler minimum,
and uniform numerical budget. Running the author's certificate was an additional
check, not the basis of the verdict. The source-research context and parent author
checks were not counted as independent reviews. No unmerged PR #11 theorem was
used. This review makes no finding about validation copied into other packages.

Worktree: `lone/`, branch `session/20261023-lone`, HEAD
`d2bd5167a42b8256f1362640dc149057920e5db9`. The package was uncommitted.
Card: `corollaries/l-one-bounds`, claim `19141176`, seed
`f7e9c53c773500cea50225ca67a35d17`.

## Checked conclusion and domain

All logarithms are natural. Assume H(7/8) for the relevant Dirichlet
L-functions **and zeta**. For every primitive character with conductor q and
`L = log q >= 32`, the proof establishes, with
`M = exp(gamma)(8 log log q + 2)`,

    zeta(2)/M <= |L(1,chi)| <= M,       zeta(2) = pi^2/6.

The estimates are uniform in the character, conductor in this range, and zero
height. No finite sample of L-values or zeros is used to establish that domain.
Principal characters and smaller inducing conductors are excluded.

For a negative fundamental discriminant `-q` in the same range, `q>4`, so the
unit factor is 2 and the class number formula is
`h(-q) = sqrt(q)L(1,chi_-q)/pi`. In particular this real L-value is positive.
The claimed bounds `pi sqrt(q)/(6M) <= h(-q) <= M sqrt(q)/pi` follow with the
correct normalization. I checked the normalization against
[LLS (1.3), PDF page 4](https://arxiv.org/pdf/1309.3595v3#page=4).

The imprimitive extension in Section 8 is also correct: for a nonprincipal
character modulo Q induced by primitive chi* of conductor f,

    L(1,chi) = L(1,chi*) product_{p|Q, p not dividing f}(1-chi*(p)/p).

Each extra factor has modulus between `1-1/p` and `1+1/p`. The threshold must
hold on f. Primes already dividing f produce no extra factor, even when the
modulus contains higher powers of them. The proof does not drop these products
or infer the conductor threshold from a large imprimitive modulus.

## Analytic and algebraic rederivation

**Zero symmetry and convergence.** For primitive complex chi, combining the
functional equation with conjugation gives the same-character involution
`rho -> 1-conjugate(rho)`, with multiplicity. This does not require the zeros
of chi to be invariant under conjugation alone. H and this involution give
`1/8 <= Re rho <= 7/8`. With the unconditional Hadamard real-part identity,

    b = -Re B(chi) = sum Re(1/rho),
    sum 1/|rho|^2 <= 8b,
    sum 1/|1-rho|^2 = sum 1/|rho|^2.

Thus the argument uses the real-part quantity b, not the modulus of the
complex Hadamard constant. I checked the accepted pairing lemma's part 2
directly: for a reflected pair, put `A=|rho|^-2`, `A'=|rho'|^-2`, and
`sigma=Re rho>=1/2`. Its absolute kernel sum is
`(x^(sigma-1)+x^(-sigma))sqrt(AA')`, and its b mass is
`sigma A+(1-sigma)A' >= 2sqrt(sigma(1-sigma))sqrt(AA')`.
This gives the stated `c(x)b` bound; a central-line zero also satisfies it.
The rational replacement is valid because
`7*189^2 - 16*125^2 = 47 > 0` and `189/125>0`.

For real `u>=1`, `|rho-u|>=|rho-1|`. Consequently, before the outside factor
`1/t`, the absolute integrated zero sum is at most

    sum integral_1^infinity |x^(rho-u)/(rho-u)^2| du
       <= 8b integral_1^infinity x^(7/8-u) du
       = 8b/(x^(1/8)t),          t=log x.

This finite bound proves absolute sum/integral interchange and domination
for the limit down to u=1, including the entire neighborhood of that endpoint.
It yields exactly `8b/(x^(1/8)t^2)` in (2.8). Comparing the shifted denominator
termwise to `|rho|` would be unjustified; the proof correctly avoids that step.
The same argument applies to zeta. The finiteness of the Hadamard sums and the
underlying contour identities remain classical inputs, as specified below.

**Signs in the exact identities.** I compared the pre-estimation residues in
[LLS Lemmas 2.3--2.6](https://arxiv.org/pdf/1309.3595v3#page=7) with the
[versioned TeX](https://arxiv.org/src/1309.3595v3), particularly TeX lines
496--546 and 585--620. They give

    (1+1/x)b + Re Z = (1-1/x)Q/2 - T_chi + E_a,
    log|L(1,chi)| = A_chi + (Q/2+g_a-b)/t + R_chi + H_a.

The signs of both integrated terms in the second equation are positive
before estimating the complex zero term; H_a itself is nonnegative. Solving
the first equation gives the useful independent check

    Q/2-b = T_chi + b/x + Re Z + Q/(2x) - E_a.

Substitution proves (2.10) with **all four correction signs as printed**.
In particular the conductor main term cancels exactly. Bounding it before
this cancellation would lose the claimed shape of the result.

For the trivial zeros, the integrand is bounded by
`x^(-u) sum_{n>=0} x^(-2n)/(2n+1)^2 <= (4/3)x^(-u)` for x>=2.
After integration and division by t this is smaller than `2/(x t^2)`.
The even and odd gamma differences are, respectively,

    g_0-E_0 = -(t+1+gamma/2)/x
                  + sum_{k>=1} x^(-2k-1)/(2k(2k+1)),
    g_1-E_1 = -(gamma/2+log 2)/x
                  + sum_{k>=0} x^(-2k-2)/((2k+1)(2k+2)).

Their geometric tail bounds prove (2.11) for every x>=2. For x>=100 the
separate sign bounds for E_0 and E_1 used to estimate b are valid. In (2.4),
`-T_chi <= T_z` because its original weights are nonnegative. The factorial
argument proves `T_z<=t` for real x>1, giving `(L/2+t)/d(x)` when Q>=0.
No sign-sensitive gamma inequality from GRH Section 5 is needed.

**Zeta pole and gamma.** The zero term in the exact Lemma 2.4 identity has a
minus sign, as in (3.1). For Lemma 2.6, take `sigma_0=1+epsilon` and keep t
fixed. Independently expanding the pole integral gives

    integral_epsilon^infinity exp(-tv)/v^2 dv
       = 1/epsilon + t(log(t epsilon)+gamma-1) + o(1).

Also `t log zeta(1+epsilon)=-t log epsilon+o(1)` and
`zeta'/zeta(1+epsilon)=-1/epsilon+gamma+o(1)`. Their sum, divided by t, is
`log t+gamma-1+gamma/t`. Thus the gamma constant in (3.2) is preserved
without an RH zero estimate. This calculation also agrees with the pole
calculation in the primary TeX, lines 631--665, and the PDF on pages 9--10.
The zeta trivial zeros start at n=1, giving the charged
`1/(3x^3 t^2)` bound. Combining A_z and T_z/t leaves **`-1/t`** in F_z,
which is essential for the final `5/(3t)` rather than `8/(3t)`.

**Finite Euler envelope.** The identity `F=A+T/t` gives, at a prime p,
weights `w_k=p^(-k)/k-log p/(x log x)`, for
`1<=k<=floor(log x/log p)`. They are decreasing and nonnegative. This also
handles nonintegral x, and each original weight vanishes when n=x, so there
is no endpoint half-weight correction. Upper domination by F_z is immediate.
When chi(p)=0, the alternating envelope is nonpositive by pairing successive
decreasing weights, so it is still a lower bound.

For nonzero chi(p), write `chi(p)=-exp(i phi)` and use
`Q_k=(1-cos(k phi))/(1-cos phi)` with `0<=Q_k<=k^2`.
For p>=3, retaining the first odd term and the finite even h terms gives
the bound in (4.5); the coefficient of h is at least 3 when K>=2.
The function `2r/(1-r^2)^2` is increasing for `0<r<=1/3`, giving the
positive factor `5/32`. K=1 and phi a multiple of 2pi are covered separately
or by continuity; neither case requires a strict minimum.

For p=2 I generated the Chebyshev polynomials from their recurrence, then
divided `1-T_k(z)` by `1-z`, instead of using the certificate's supplied Q
arrays. The resulting ascending coefficient vectors are

    P = [229/1440, -13/120, 1/60, -1/40, 1/10],
    H = [-1, 2, 8, -8, -16].

The even tail is exactly `sum_{even k>=6} k/2^k=5/36`. Dropping its h
terms is valid in the required lower-bound direction. The printed
factorization of H+15 is correct; its cubic has derivative
`48(z+1/2)^2+4` and value 6 at -1. Thus H>=-15 on [-1,1].
P>=37/1440 there by the two interval arguments in the proof. Since
`h<7/4500` for every x>=100, the resulting strict gap is `17/7200`.
This supplies the omitted p=2 calculation rather than trusting the source's
computer assertion. The argument covers every complex phase, not just signs.

**Chebyshev estimate and lower tail.** For N=m+k, with
`m=floor(N/2)`, `k=ceil(N/2)`, each prime-power exponent in the binomial
coefficient is a nonnegative floor difference. Every prime power in (k,N]
has floor difference 1. Therefore `psi(N)-psi(k)<=N log 2`.
The stated induction is valid: its even bound is `N+N log 2`, and its odd
bound is `N+1+N log 2<=2N` for odd N>=5, using log 2<3/4.
The bases and passage to floor(v) establish psi(v)<=2v for all real v>=1.

Regrouping the even prime powers gives exactly (4.9), including the factor
2 in front of psi(sqrt x). For real u=sqrt x, the omitted series is at
most `sum_{m>u}m^-2 <= 1/(u-1)`, and the psi contribution is at most
`4/(u log x)`. At x>=100, multiplying their sum by u gives at most
`10/9+8/9=2`. Hence the lower envelope and the factor zeta(2) are correct.
Independent choices chi(p)=-1 need not be simultaneously realizable by a
character to provide this lower envelope.

## Uniform arithmetic and independent reproduction

At L>=32, t=8 log L is increasing and t/L is decreasing, since log L>1.
The bounds on log 2 give `t>27` and `t/L<7/8`. Both c(x) and c(x)L decrease
with L. These observations establish every range reduction in (5.1) on the
entire half-line, not just at sampled conductors. In particular
`d>119/125` and `b/L<1375/952<29/20`.

I independently summed the four main terms to `286741/108000`. The remaining
terms are bounded by

    3/L^7 + 1/L^8 + 1/L^24 + 7/(4L^3)
       <= 27/(4*32^3) < 1/1000.

This verifies the charged bound `K<286849/108000<8/3` and its margin
`1151/108000`. The exponential bridge is exactly
`(5/3)/(1-5/81)=135/76<2`.

As a second route, retain the rational endpoint c instead of rounding all
four main contributions separately. Put

    C = (189/125)(1/32+1/32^4),
    B = (11/8)/(1-C) = 180224000/124878659.

Uniformly, `b/L<B`, `c(x)L<=32C`, `c(x)<=C`, `t>27`, and `t/L<7/8`.
Direct substitution into (5.2) gives the rational majorant K_* in the code
below, with `K_*<53/20<8/3`. This independently reproduces the budget with
margin at least `1/60` to 8/3, without relying on the four author-rounded
main terms.

The following standard-library-only code was executed independently. It
reconstructs the polynomial coefficients by recurrence and checks the budget
with exact Fractions. Its alternating-series logarithm enclosures use a
different route from `verify/check.py`'s atanh implementation. The code does
not import the author's certificate and writes no files.

```python
from fractions import Fraction as F

def add(a, b):
    c = [F(0)] * max(len(a), len(b))
    for j, v in enumerate(a): c[j] += v
    for j, v in enumerate(b): c[j] += v
    return c

def scale(a, v):
    return [v * x for x in a]

T = [[F(1)], [F(0), F(1)]]
for k in range(2, 6):
    T.append(add([F(0)] + scale(T[-1], 2), scale(T[-2], -1)))
Q = []
for k in range(1, 6):
    numerator = add([F(1)], scale(T[k], -1))
    q, running = [], F(0)
    for v in numerator[:-1]:
        running += v
        q.append(running)
    assert -q[-1] == numerator[-1]
    Q.append(q)
P, H = [-F(5, 36)], []
for k, q in enumerate(Q, 1):
    P = add(P, scale(q, F((-1)**(k-1), k * 2**k)))
    H = add(H, scale(q, (-1)**k))
assert P == [F(229,1440), -F(13,120), F(1,60), -F(1,40), F(1,10)]
assert H == [-1, 2, 8, -8, -16]
assert P[0] + P[1] + P[3] - 15*F(7,4500) == F(17,7200)
r = F(1,3)
assert 1 - 2*r/(1-r*r)**2 == F(5,32)

l = F(32)
C = F(189,125) * (1/l + 1/l**4)
B = F(11,8)/(1-C)
K_star = (B*l*C + 8*B/27 + C/2 + 4/(27*l)
          + ((B+F(11,8))*l+5)/l**8 + 2/(27*l**8)
          + 1/(81*l**24) + F(7,4)/l**3)
assert B == F(180224000,124878659)
assert K_star < F(53,20) < F(8,3)
main = sum([F(8787,4000), F(58,135), F(3,125), F(1,216)], F(0))
assert main == F(286741,108000)
assert F(27,4)/l**3 < F(1,1000)
assert main + F(1,1000) == F(286849,108000)
assert F(8,3) - main - F(1,1000) == F(1151,108000)
assert F(5,3)/(1-F(5,81)) == F(135,76) < 2
assert 7*F(189,125)**2 > 16
assert (F(64)+F(64,49))/(F(8)+F(8,7)) == F(50,7)

def log_plus(u, n=80):
    # Even partial sum for log(1+u), and the next odd partial sum.
    s = sum(((-1)**(k-1)*u**k/k for k in range(1,n+1)), F(0))
    return s, s + u**(n+1)/(n+1)

a, b = log_plus(F(1,3))
c, d = log_plus(F(1,2))
e, f = log_plus(F(1,4))
lo2, hi2 = a+c, b+d  # 2=(4/3)(3/2)
v = F(1,8)
s = sum((v**k/k for k in range(1,81)), F(0))
tail = v**81/(81*(1-v))
lo7, hi7 = 3*lo2-s-tail, 3*hi2-s  # 7=8(1-1/8)
assert F(27,40) < lo2 < hi2 < F(7,10)
assert hi7 < F(39,20) and F(49,20)-hi7 > F(1,2)
assert F(9,2) < 6*lo2+2*e < 6*hi2+2*f < 5  # 100=2^6(5/4)^2
assert c+3*lo2 > 2  # 12=(3/2)*8
assert 2*hi2 < 2 and 3*hi2 < 3
assert 40*lo2 > 27 and 40*hi2/32 < F(7,8)
print('Independent polynomial, logarithm, and uniform budget checks pass')
print('K_star < 53/20 < 8/3; p=2 gap 17/7200; author margin 1151/108000')
```

The two Euler inequalities and the absolute character error imply

    log |L(1,chi)| <= log t+gamma+(-1+K)/t,
    log (1/|L(1,chi)|) <= log t+gamma-log zeta(2)+(-1+K)/t.

Thus (5.5) follows, and `exp(s)<=1/(1-s)` for `0<=s<1`, with t>27,
gives `t exp(5/(3t)) < t+135/76 < t+2`. This completes both claimed
L-value inequalities with t=8 log log q. The GRH kernel control also checks:
on the central line the reciprocal-square factor is 2 and the paired kernel
can be `2/sqrt(x)`. Taking `x=(c_0 log q)^2` then gives the source's leading
`2 exp(gamma)` and `12 exp(gamma)/pi^2`; minimizing the asymptotic additive
term `2 log c_0+1/c_0-1` gives c_0=1/2. Those GRH constants are not retained
in the off-line argument.

## Executed certificates and control meanings

From `lone/`, with bytecode generation disabled, all four commands passed:

```sh
python3 -B research/l-one-bounds/constants.py
python3 -B research/zero-pairing/constants.py
python3 -B verify/check.py all
python3 -B -m unittest discover -s tests
```

The new certificate printed p=2 margin `17/7200`, K upper bound
`286849/108000`, margin `1151/108000`, bridge `135/76`, and all six
rejections. The shared test suite ran 16 tests successfully. The shared
verifier checks existing Miller--Rabin claims; it does not certify this new
analytic theorem. Sampling in the accepted pairing script is also only a
sanity check; the pairing argument above supplies the uniform justification.

I invoked the six controls separately and checked the actual rejection reasons:

| Changed input | Rejection actually exercised |
|---|---|
| c2=3/2 | The chosen pairing bound requires 7*c2^2>=16. |
| c2=-189/125 | The explicit c2>0 condition rejects it before the squared comparison can pass. |
| L_min=16 | The required t>27 endpoint bound fails. |
| Shifted multiplier=2 | The formal reflected pair gives ratio 50/7>2. |
| h upper bound=1/500 | The chosen polynomial lower bound minus 15h is negative. |
| Additive constant=1 | The bridge 135/76 does not fit below 1. |

For the formal pair `{1/8,7/8}`, `b=64/7` and the shifted reciprocal-square
sum is `3200/49`, giving ratio `50/7<8`. A central real formal zero gives
ratio 2. These are exact algebraic kernel controls, not assertions that such
zeros occur in an L-function. The p=2 control deliberately loosens its error
charge until this certificate fails; it is not an actual phase counterexample.
Except for the formal obstruction to a strip-only constant 2, rejection of a
parameter here does not prove that a better argument could not use it.

## Exact inputs checked

SHA-256 values are for the actual bytes, not a rendered or normalized copy.
The three package hashes were checked again after the mathematical review and
were unchanged. Native workspace hashes and context-mode's proof hash agreed.
The frontier's artifact hashes agree with the accepted local sources used here.

| Path, relative to lone/ | SHA-256 |
|---|---|
| `research/l-one-bounds/PROOF.md` | `a43870d8f25afc5d13cd86eda587bbec5c2f96f2d7b96be99893a2e554200886` |
| `research/l-one-bounds/constants.py` | `8eeedd8a215ae689169955de1b49e3c3499ca9adfe80b24c2b07d86db888ef5c` |
| `research/l-one-bounds/README.md` | `c21d3a97aec9685326c91c24e05426171ac4bb14a27af35f75e53fe8624dc5b4` |
| `research/zero-pairing/PROOF.md` | `824af09db62887a04107e72f9aafb56345aef45c1ea3ccf6499956d6896e914c` |
| `research/first-explicit-t1/PROOF.md` | `abd066b2d27961e93ae007e5fb8897b5a841aff875b24af3eb0216d73bed8cbb` |
| `research/zero-pairing/constants.py` | `b71772dee37a2b068677c2800c2dce6d0737a94d03380f47b2f9d87ec6e610a7` |
| `verify/check.py` | `ace2b055b5279284d04d37b6c6dde77af86088245846700c502effb3e812e709` |
| `discover/frontier.json` | `9ca629138c133ac8547efba9b47f4d862ae82e7079c4da0998961d8fa5c964a4` |
| `AGENTS.md` | `e8f93ce38983d792791c3f9ad9b8b0a367668b3b7b945b071b6f360c45babd62` |
| `DISCOVERY.md` | `e603c2aaf4b9c692b315213f6c7dd5aebdfba5932e67155e53c76a6590ec4ddf` |

Primary source: Lamzouri--Li--Soundararajan, *Conditional bounds for the least
quadratic non-residue and related problems*, arXiv:1309.3595v3. I retrieved
the versioned source, verified its decompressed hash independently, and used
the TeX for exact signs and coefficients. I also checked the PDF's version,
class number formula, and Lemma 2.5--2.6 residue and pole formulas. Relevant
TeX ranges were lines 303--369, 470--665, 1132--1177, and 1240--1343.

| Public primary object | Bytes | SHA-256 |
|---|---:|---|
| [Versioned PDF](https://arxiv.org/pdf/1309.3595v3), 23 pages, arXiv stamp 8 Dec 2016 | 267062 | `692b7fe38d883cf3503e247b0ebcd0c092c7e7267b06488adb9f40d45095b5a8` |
| [Versioned source](https://arxiv.org/src/1309.3595v3), gzip response | 26276 | `301cb41d96db71a722f278b1e9db437cf71c275ea07cc0289f3a916d8208528c` |
| Decompressed `QuaResL1Corrected.tex` | 93372 | `2b5a85717f193b950ae522ad5c07f8f8bb1dc2213c073d54b4d4fa8cba6d98f8` |

## Classical inputs and limits of this verdict

The trust boundary consists of classical analytic continuation and functional
equations of primitive Dirichlet L-functions and zeta; the order-one Hadamard
identities and convergence of their real-part sums; the published contour
residue identities before GRH error estimates; the zeta Laurent expansion and
Euler-constant integral identity; digamma special values; the Euler product at
2; and the quadratic Dirichlet class number formula. The relevant accepted
local inputs are F1--F2 and Lemma 0 of `first-explicit-t1`, and Lemma 0'
part 2 of `zero-pairing`. Only these inputs, rather than either witness
theorem's numerical coefficients, enter this L-value proof.

I checked the consequences of those classical identities and supplied the
absolute domination needed for the new off-line integrated estimates. I did
not independently re-prove classical analytic continuation, the Hadamard
factorization, or the horizontal/left-edge contour limits from first
principles. The global convergence required to obtain the published residue
identities remains within that explicit classical trust boundary. The new
integrated sum interchanges and endpoint domination have been checked above.

H(7/8), any Lean replay, smaller conductors, optimal constants, improved
truncations, and a product-free imprimitive bound were not certified. A new
human or formal proof check would add a different kind of assurance. This
report certifies the stated conditional argument at the listed hashes to the
extent of this fresh-context same-model AI review; maintainer review remains.

Only this `RECHECK.md` was created. No other project file, git state, public
record, or external service was changed, and no further agent was launched.
