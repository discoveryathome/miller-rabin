**Original idea: Geoffrey Irving.**

# Explicit least nonresidues under H(7/8)

AI-authored conditional draft (Codex), 2026-10-23. Author checks and a separate
fresh-context same-model AI recheck pass; see [RECHECK.md](RECHECK.md).
The input-guard fix and its regression control were separately confirmed in
[GUARD-RECHECK.md](GUARD-RECHECK.md). Maintainer review is pending.
Text: CC BY 4.0; code: Apache-2.0. Reports pin their reviewed snapshots;
subsequent edits record review status and links only. The smaller-theta
extension in Section 5 passed its own fresh-context same-model AI recheck;
see [RECHECK-THETA.md](RECHECK-THETA.md).
The sharp coefficients in Section 6 passed their own fresh-context same-model
AI recheck; see [RECHECK-SHARP.md](RECHECK-SHARP.md).

## Results

Assume H(7/8): every Dirichlet L-function, including zeta, has no nontrivial
zero with real part greater than 7/8. Logarithms are natural.
For a proper subgroup H of G = (Z/qZ)*, let ell(q,H) be the least prime
not dividing q whose residue is outside H.

> **Theorem.** For every q >= 5 and every proper H,
>
> ell(q,H) < (0.683 log q)^8.
>
> If q != 6, the stronger bound ell(q,H) < (0.678 log q)^8 holds.
> At q = 6, ell(q,H) = 5. At q = 3 and 4 the least outside primes are
> respectively 2 and 3.

> **Quadratic corollary.** For every prime q >= 5, the least positive
> quadratic nonresidue modulo q is a prime ell satisfying
>
> ell < (0.678 log q)^8.

Section 6 identifies the sharp coefficients, with a non-strict inequality
at the forced small cases. For H(b), 13/15<=b<=7/8, and r=1/(1-b), these
are C5=2^(1-b)/log5 for q>=5,q!=6 (and the quadratic theorem), and
C6=5^(1-b)/log6 for every q>=5. Equality occurs exactly at q=5 or q=6,
respectively. The earlier decimal bounds remain useful separate corollaries.

These coefficients are close to forced small-modulus constraints:
0.682 fails the uniform general-modulus statement at q = 6, and 0.677
fails the prime quadratic statement at q = 5. The preceding rounded
coefficients are not claimed optimal; Section 6 proves the exact sharp
coefficients. No unconditional large-modulus theorem is asserted.

## Inputs and predecessor credit

This is the `corollaries` / `least-nonresidue` card at upstream base
`d2bd5167a42b8256f1362640dc149057920e5db9`, original seed
`f7e9c53c773500cea50225ca67a35d17`. It follows Bach's conditional method,
the character argument in [Lamzouri--Li--Soundararajan,
arXiv:1309.3595v3](https://arxiv.org/abs/1309.3595v3), Theorem 1.1,
Corollary 1.1 and Section 3, and Claude's accepted first-T1 and
zero-pairing packages (PRs #6 and #8).

The [LLS v3 PDF](https://arxiv.org/pdf/1309.3595v3) SHA-256 is
`692b7fe38d883cf3503e247b0ebcd0c092c7e7267b06488adb9f40d45095b5a8`.
LLS Lemmas 2.1--2.3 are on printed pp. 5--8, Lemma 3.1 and the
Section 3 proof on pp. 10--12. The source statements assume GRH;
the zero estimates used here are their H(7/8) replacements already proved in
[`../zero-pairing/PROOF.md`](../zero-pairing/PROOF.md), Lemma 0' and
(L2.1'')--(L2.3''), using
[`../first-explicit-t1/PROOF.md`](../first-explicit-t1/PROOF.md), Step 0.
No result from an unmerged sibling PR is an input.

Put b = 231/10000, c2 = 189/125, and, for X >= 256,

    F(X) = X^(7/8) + 7X^(1/8) + 8,
    c(X) = c2 (X^(-1/8) + X^(-1/2)),   d(X) = 1 + 1/X - c(X).

For a primitive nonprincipal character chi* of conductor f >= 3 write

    A = -Re B(chi*) = sum_rho Re(1/rho),
    S(X,chi*) = sum_{n<=X} Lambda(n) chi*(n) log(X/n),
    T(X,chi*) = sum_{n<=X} (Lambda(n)/n) chi*(n) (1-n/X),
    S_zeta(X) = sum_{n<=X} Lambda(n) log(X/n),   t = log X.

The accepted zero-pairing bounds and residue formulas give

    S_zeta(X) >= X - bF(X) - log(2pi)t - 1,                               (1)
    Re S(X,chi*) <= A(F(X)+t) + (1/2)log(f/pi)t + Etilde_a(X),            (2)
    d(X)A <= (1/2)(1-1/X)log(f/pi) - Re T(X,chi*) + E_a(X).               (3)

Here E_a and Etilde_a are the unconditional real gamma functions in LLS
Lemmas 2.2--2.3. Both are nonpositive for X >= 64, as proved in the first-T1
Step 0; |B_zeta| < b is an inherited zeta constant. The checker recomputes
the new coefficients from these accepted inputs, not the analytic inputs
themselves. The same-character reflection rho -> 1-conjugate(rho) makes
the paired estimates valid for complex primitive characters too.

## 1. Reduction and imprimitive corrections

Suppose that no prime p <= X, p not dividing q, is outside H. A nonprincipal
character chi modulo q trivial on H exists by finite-abelian-group duality.
Every n <= X coprime to q factors into primes lying in H, so chi(n) = 1.
Consequently S(X,chi) = S(X,chi0) is real and T(X,chi) = T(X,chi0) >= 0,
where chi0 is the principal character modulo q.

Let chi* induce chi, let f divide q be its conductor, and put r = q/f.
The conductor is at least 3. Direct sums over prime powers (LLS Lemma 3.1
and (3.2)) give

    |S(X,chi)-S(X,chi*)| <= (omega(r)/2)t^2,
    |T(X,chi)-T(X,chi*)| <= (1-1/X)U(r),
    U(r) = sum_{p|r} log p/(p-1).

Only primes dividing q but not f actually contribute; including all p|r
enlarges the bounds. For S, each prime contributes at most t^2/2 by an
integral bound on its decreasing exponent sum. For T, use
1-p^k/X <= 1-1/X and sum_{k>=1} p^(-k) = 1/(p-1).
The principal correction is at most omega(q)t^2/2. It follows that

    Re S(X,chi*) >= S_zeta(X) - omega(q)t^2.                              (4)

Since T(X,chi) >= 0, (3) and the T correction imply

    d(X)A <= (1/2)(1-1/X)[log(f/pi)+2U(r)].

The conductor saving absorbs U(r):

    log f + 2U(r) - log q
       <= sum_{p|r} (2/(p-1)-1)log p <= log 2.

The 2-factor contributes log 2, the 3-factor zero and every larger prime
a nonpositive quantity. Since 2 < pi and log q > 0, we obtain

    A <= L/(2d(X)),   L = log q,                                        (5)

whenever d(X) > 0. This also covers f = 3, where log(f/pi) is negative;
no sign assumption about that logarithm was used.

This one-character argument uses real parts. There is no arbitrary coset
phase requiring a full complex-B bound: chi is 1 on every unit in the
contradiction range. No GRH estimate for T_zeta or primes is imported.

## 2. A completely charged criterion

Combine (1)--(5), drop Etilde_a <= 0, and use log(2pi) < 2. The
no-outside-prime assumption forces

    1 <= (F(X)/X)[b+L/(2d(X))]
          + [(L/(2d(X))+L/2+2)t+1+omega(q)t^2]/X.                        (6)

Thus a strict upper bound below 1 for the right side proves an outside
prime strictly below X. Indeed, a prime equal to X has zero weight and
would not change the contradiction for the positive-weight sums.

Set C = 339/500 = 0.678, y = C L and X = y^8. For q >= 65536,

    y >= C*16 log 2 > C*(32/3) = 904/125 > 7.

For all y >= 7, direct rational bounds give

    d(X) > 39/50,   F(X)/X < (1001/1000)/y,
    log 7 < 2,     omega(q) <= L/log 2 < 2L = 2y/C.

The paired zero-sum range holds since 7^8 > 256. The residual upper bound
after substituting L = y/C in (6) is

    [(y/(2C*(39/50))+y/(2C)+2)t + 1 + (2y/C)t^2]/y^8.

Each summand is a positive multiple of (log y)^b/y^a with a >= 7,
0 <= b <= 2. It decreases for y >= 7, since log 7 > 1. The zeta
term b/y also decreases, and the leading L/y term is constant.
Evaluate at y = 7, replacing t = 8 log 7 by 16, to bound (6) above by

    (1001/1000)[(231/10000)/7 + 1/(2C*(39/50))]
      + [(7/(2C*(39/50))+7/(2C)+2)*16+1+(14/C)*16^2]/7^8
      = 241522181840005231/254054780070000000 < 1.                       (7)

The positive normalized margin is 12532598229994769/254054780070000000.
The same certificate improves when C increases. Equation (7) proves the
stronger coefficient 0.678 for all general moduli q >= 65536.

## 3. The complete small-modulus range

Unconditionally, every proper H misses a prime p < q coprime to q.
Otherwise each reduced representative a in 1..q-1 factors into primes in
H, so H would contain all of G. This elementary observation handles an
entire interval without enumerating its subgroups.

The function (C log q)^8/q has derivative with the sign of 8-log q.
It has a single interior maximum, so its minimum on [7,65536] occurs
at an endpoint. Exact lower logarithm bounds certify

    (C log 7)^8 > 7,
    C log 65536 > 7,   7^8 > 65536.

It follows that (C log q)^8 > q throughout this interval. The unconditional
p < q observation proves the coefficient-0.678 bound for 7 <= q <= 65536.

At q = 5, 2 generates all four units (its powers are 1,2,4,3), so every
proper H excludes the prime 2. Exact arithmetic gives (0.678 log 5)^8 > 2.
At q = 6, the unit group is {1,5}, its only proper subgroup is {1}, and
ell(6,H) = 5. Exact arithmetic gives (0.683 log 6)^8 > 5.
Combining these cases proves the stated uniform general theorem and the
stronger 0.678 result except at q = 6. The q = 3 and 4 unit groups give
their stated exact outside primes 2 and 3.

For prime q >= 5, take H to be the subgroup of nonzero squares, of index 2.
The smallest positive quadratic nonresidue is prime: if it factored as
u*v with both smaller factors, minimality would make both factors residues,
and hence their product a residue. Thus the outside-prime bound proves the
quadratic corollary as stated, for every prime q >= 5.

## 4. Exact controls and direct checks

The script uses accepted `verify/check.py` logarithm enclosures and exact
Fractions; floating point is not used for certificate decisions. It recomputes
(7), the range endpoints and the two finite group generators. Independently
of the interval proof, it checks the least quadratic nonresidue directly
for every one of the 6540 primes 5 <= q < 65536, using trial division for
primality and Euler's criterion for quadratic character values. Each found
least nonresidue is required to be prime and below the lower rational bound.
The largest least nonresidue in this direct range is 31, last occurring at
q = 31391. These finite checks are supplementary; the all-group small-range
proof above already covers the interval without a subgroup search.

For the negative controls, use the **upper** logarithm bounds:

    (0.677 log 5)^8 < 2 = least quadratic nonresidue modulo 5,
    (0.682 log 6)^8 < 5 = ell(6,{1}).

They prove that those proposed coefficients, and any smaller ones in the
same domains, fail. The eight rejection controls also test positivity of the pairing
constant, analytic cutoff, positive small-modulus endpoints and the invalid
use of Euler's criterion with a composite modulus.

## Replay, limitations and open next questions

From the repository root:

```sh
python3 research/zero-pairing/constants.py
python3 research/least-nonresidue/constants.py
python3 verify/check.py all
python3 -m unittest discover -s tests
```

Expected new-check result: `all constants and direct checks pass`, eight
`REJECT control` lines, and 6540 directly checked prime moduli. The shared
verifier checks its recorded Miller--Rabin claims; the new theorem is
supported by this written proof and its separate exact checker.

Not checked here: H(b) or a Lean replay, new contour-convergence arguments,
or all large-modulus character values by enumeration. Section 6 proves
optimality only for its stated all-q coefficient shapes and domains.
The accepted zero-pairing and gamma estimates are declared inputs. The new
proof and the guard fix have separate AI rechecks with their precise scopes
recorded above; maintainer acceptance remains separate.

Section 6 resolves the all-q coefficient gaps. Open next question: obtain
a coefficient nearer 1/2 above a new explicit cutoff
while keeping a complete piecewise bound for the smaller moduli.

## 5. The exact smaller-theta exponent

Assume instead H(theta), where theta=8748867/10000000 and

    r=1/(1-theta)=10000000/1251133.

This is an explicit assumption, corresponding to the Xu--Sang reference point
A1b in the frontier, not a certification of that unreviewed preprint or its
analytic inputs. Under this assumption the same constants and domains above
hold with exponent **r instead of 8**, including the quadratic corollary and
the q=6 exception. The H(7/8) statements remain separate results.

Here is the required parameter transfer, proved from the accepted pairing
argument rather than assuming an unmerged sibling theorem. The functional
equation places the zeros in 1-theta<=Re rho<=theta. In the proof of Lemma0'
part1, use R=7, since theta/(1-theta)=r-1<7. The two fractional-linear
endpoint ratios are bounded by
g(sigma)=X^sigma+7X^(1-sigma). Convexity reduces to sigma=1/2 or theta.
Writing u=X^(theta-1/2),

    [g(theta)-g(1/2)]/sqrt(X)=(u-1)(u-7)/u >= 0

for X>=256: theta-1/2>11/30 and 256^11>7^30 imply u>=7. Thus the main
paired sum is at most (X^theta+7X^(1-theta))A. In part2, the same c2=189/125
is safe because theta(1-theta)>=7/64. The constant zero sum costs rA<=8A.
Both results also hold for zeta. They follow from the same nonnegative
zero-pair regrouping, including complex characters, as the accepted proof.

Set y=X^(1-theta), so X=y^r exactly. We have 799/100<r<8. For y>=7,

    X^(theta-1)=1/y,   X^(-1/2)=y^(-r/2)<=y^(-3),
    X^(theta-1)+7X^(-theta)+8/X
       <= 1/y+7/y^6+8/y^7 < (1001/1000)/y,
    d(X)>=1-c2(1/y+1/y^3)>77/100,
    X>=y^7,   log X=r log y<=8 log y.                              (8)

The main-zero part of the third bound uses r*theta=r-1>6. Every
fractional power has been bounded in the safe direction by an integer
power; there is no floating-point evaluation of X or r.

The character reduction, both S corrections, T correction, conductor saving
and gamma signs in Sections 1--2 are unchanged. Their criterion (6) holds
with F(X)=X^theta+7X^(1-theta)+8 and the new d(X). Choose X=(C log q)^r,
C=0.678. For q>=65536, y=C log q>7, so (8) gives the uniform error bound

    (1001/1000)[(231/10000)/7+1/(2C*(77/100))]
      +[(7/(2C*(77/100))+7/(2C)+2)*16+1+(14/C)*16^2]/7^7
      =29748536893681951/30709918470000000 < 1.                     (9)

The positive margin is 961381576318049/30709918470000000. The derivative
argument still applies: residual summands have denominator powers at least6
and log powers at most2, and they decrease for y>=7. Increasing C helps.

For the interval [7,65536], (C log q)^r/q again has a single interior
maximum, now at log q=r. Its endpoints exceed1: at the upper endpoint
C log65536>7 and 7^r>7^7>65536. For q=5,6,7, use r>799/100 and a
downward-rounded rational lower enclosure l_q for log q, retaining eight
decimal places. Exact integer-power comparisons certify

    (0.678*l_5)^799>2^100,
    (0.683*l_6)^799>5^100,
    (0.678*l_7)^799>7^100.

All three bases exceed1. These comparisons establish the q=5 and6 cases
and the lower interval endpoint without evaluating a noninteger power.
The unconditional p<q argument and the quadratic subgroup argument finish
the same complete domains as before. The direct check also verifies the new
bound for all6540 small prime moduli, using the weaker integer exponent7
for q>=7 and the displayed rational exponent bound for q=5.

The old small-modulus obstructions persist: each bad base exceeds1 and
r<8, so the old upper bound with exponent8 remains an upper bound for the
new power. Coefficients0.677 and0.682 therefore still fail in their
respective domains. The seventh rejection control prevents applying these
fixed envelopes to an unsupported weaker zero-free line.

This extension is author-checked and separately independently AI-rechecked.
It does not verify H(theta), Xu--Sang's proof or a Lean replay. The rounded
coefficients in this section are not claimed optimal; Section 6 identifies
the exact sharp coefficients.

## 6. Sharp coefficients for the complete domains

Assume H(b), including zeta, for 13/15<=b<=7/8. Put

    r=1/(1-b),  C5=2^(1-b)/log5,  C6=5^(1-b)/log6.

Then, for every proper subgroup H of (Z/qZ)*,

    ell(q,H) <= (C6 log q)^r                    for every q>=5,
    ell(q,H) <= (C5 log q)^r                    for q>=5,q!=6.     (10)

Equality in the first statement occurs exactly at q=6, and in the second
exactly at q=5. The prime quadratic theorem has sharp coefficient C5 and
equality exactly at q=5. These are the best possible coefficients in these
same non-strict statements; any smaller one fails at the indicated modulus.
The exact q=3,4 exceptions remain 2,3 and are outside the domains in (10).

It suffices to prove the stronger strict subdomain bound

    ell(q,H) < (.677 log q)^r                   for every q>=7.   (11)

The Section 5 pairing proof works throughout this parameter interval:
b/(1-b)<=7, b-1/2>=11/30, b(1-b)>=7/64, and 15/2<=r<=8. Hence the
same R=7, positive c2=189/125 and X>=256 certify the two paired sums;
the static sum costs rA<=8A. Reflection, nonnegative regrouping and the
line-zero bounds are identical. Criterion (6) therefore still applies,
including the two S corrections, the T correction, conductor saving and
gamma signs. This argument uses accepted lemmas and the written transfer,
not a theorem from an unmerged sibling.

Use C0=677/1000 and y=X^(1-b)=C0 log q. For q>=65536 we have y>7.
The integer envelopes in (8) still hold: they require only r>7 and r<=8.
Thus d>77/100, F/X<(1001/1000)/y, X>=y^7 and log X<=8log y.
With the same monotone residual bounds as Section 5, the total error is
at most

    (1001/1000)[(231/10000)/7+1/(2C0*(77/100))]
      +[(7/(2C0*(77/100))+7/(2C0)+2)*16+1+(14/C0)*16^2]/7^7
      =8499538701758399/8761321030000000 <1,                     (12)

with margin 261782328241601/8761321030000000. This proves (11) there.

For 7<=q<=65536, the function (.677 log q)^r/q again has a single
interior maximum, so its minimum is at an endpoint. The upper endpoint
follows from .677 log65536>7 and 7^7>65536. At q=7 the exact rational
lower logarithm bound gives

    (.677 ln_bounds(7)[0])^15 > 7^2,
    .677 ln_bounds(7)[0] >1.

Since r>=15/2, this proves (.677 log7)^r>7, including at b=13/15.
The unconditional prime p<q outside every proper subgroup then proves
(11) on the entire interval. The supplementary direct prime computation
also checks the stronger coefficient .677 with integer exponent 7 for
each of the 6539 primes q>=7 below 65536. These finite prime checks support,
and do not replace, the all-subgroup interval argument.

To compare the exact coefficients, the old obstruction gives
(.677 log5)^8<2 with base>1. Since r<=8, it follows that C5>.677.
Also the exact logarithm comparison

    (ln_bounds(6)[1]/ln_bounds(5)[0])^8 <5/2

proves log6/log5<(5/2)^(1/8)<=(5/2)^(1-b). Rearranging gives C6>C5.
Consequently every q>=7 has a strict inequality in both parts of (10).
At q=5, 2 generates the full unit group, so every proper subgroup excludes
it and ell(5,H)=2=(C5 log5)^r. At q=6 the only proper subgroup is {1},
and ell(6,H)=5=(C6 log6)^r. Since C6>C5, the first bound is strict at
q=5. This proves both complete domains and their equality cases.

For a prime q, apply the second statement to the subgroup of nonzero
squares. As before the least positive nonresidue is prime. The equality
at q=5 proves sharpness also in the prime quadratic domain. No numerical
evaluation of C5 or C6 is needed in the proof or certificate.

The old H(7/8) and exact smaller-theta decimal results remain separately
certified positive controls. For other b in this interval, (10) is the
parameter theorem; the old decimal constants are not asserted uniformly
in b. H(b) is assumed directly. The source and analytic-foundation limits
above remain; no proof of Xu--Sang or either half-plane is supplied.
This sharp-coefficient theorem passed its own fresh-context independent AI
review in RECHECK-SHARP.md; previous reports do not certify it. That report
pins its snapshot. Later edits record status, links and the clarification
that the earlier rounded coefficients were not asserted optimal.
