**Original idea: Geoffrey Irving.**

# Explicit least nonresidues under H(7/8)

AI-authored conditional draft (Codex), 2026-10-23. Author checks and a separate
fresh-context same-model AI recheck pass; see [RECHECK.md](RECHECK.md).
The input-guard fix and its regression control were separately confirmed in
[GUARD-RECHECK.md](GUARD-RECHECK.md). Maintainer review is pending.
Text: CC BY 4.0; code: Apache-2.0. Reports pin their reviewed snapshots;
subsequent edits record review status and links only.

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

These coefficients are close to forced small-modulus constraints:
0.682 fails the uniform general-modulus statement at q = 6, and 0.677
fails the prime quadratic statement at q = 5. Neither optimality nor an
unconditional large-modulus theorem is asserted.

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
same domains, fail. The six rejection controls also test positivity of the pairing
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

Expected new-check result: `all constants and direct checks pass`, six
`REJECT control` lines, and 6540 directly checked prime moduli. The shared
verifier checks its recorded Miller--Rabin claims; the new theorem is
supported by this written proof and its separate exact checker.

Not checked here: H(7/8) or its Lean proof, new contour-convergence arguments,
optimal coefficients, or all large-modulus character values by enumeration.
The accepted zero-pairing and gamma estimates are declared inputs. The new
proof and the guard fix have separate AI rechecks with their precise scopes
recorded above; maintainer acceptance remains separate.

Open next questions: sharpen the gaps between the impossible and sufficient
constants, or obtain a coefficient nearer 1/2 above a new explicit cutoff
while keeping a complete piecewise bound for the smaller moduli.
