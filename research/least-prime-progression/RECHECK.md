**Original idea: Geoffrey Irving.**

# Independent mathematical recheck: least primes in progressions

2026-10-23. Round 1. Text: CC BY 4.0.

This is a separate, fresh-context **same-model AI review** (Codex,
gpt-6.1-sol), not a human review. I did not draft the theorem and did not use
the preceding source research as a theorem review. No further agents were
used.

## Verdict

**Confirmed within the stated conditional and classical-input scope.** I found
no fatal defect, no required fix, and no numerical correction. Subject to
H(7/8) and the classical analytic inputs identified below, the argument proves
the following for G = (Z/qZ)*, H a subgroup, and a in G:

    P(aH,q) < max(80, h log q)^8       (q >= 3, h = [G:H] >= 2),
    P(a,q)  < (phi(q) log q)^8        (q >= 3, gcd(a,q) = 1).

The residue signs, complex-character treatment, conductor-3 case,
imprimitive errors, aggregate h-1 factor, principal contribution, gamma
bounds, proper-prime-power subtraction, uniform envelopes, strict endpoints,
and finite fallback all check out. The four previously flagged source
obligations have substantive replacements in the proof; none is discharged
merely by citing GRH-dependent LLS estimates.

This does **not** certify H(7/8), a Lean development, or an independent proof
of the contour shifts. Maintainer review remains separate.

## Reviewed snapshot and primary sources

I read AGENTS.md, DISCOVERY.md, all four files in this package, and both
accepted predecessor proof files. The relevant predecessor inputs checked
here are F1-F2, Lemma 0, Lemma 0', and the four gamma formulas. I did not
re-review their separate Miller--Rabin theorems or complexity conclusions.

The working branch was `session/20261023T0602-corollaries`, at base/HEAD
`d2bd5167a42b8256f1362640dc149057920e5db9`. Seed:
`f7e9c53c773500cea50225ca67a35d17`.

SHA-256 of the reviewed files, before writing this report:

| File | SHA-256 |
| --- | --- |
| PROOF.md | `d62306aa226f3fca4784f22d7506253c2171c6ebe7636fcdd166598127c92bdb` |
| constants.py | `6bc59ffa4f1c328198769a5d95c2fe91dfdfd0d811d173919bff2787fc5d73d1` |
| README.md | `b9c4a897a49750302f729ba35964c346718650206649dd9ccaf098e71041415a` |
| SOURCE-AUDIT.md | `e138dcd568890957f3d16279700b48fa0b99edcf83733e7cab02eaa1d7190b5d` |

I independently retrieved the public [LLS v3 PDF](https://arxiv.org/pdf/1309.3595v3)
and [v3 TeX source](https://arxiv.org/src/1309.3595v3). I checked the
Hadamard/functional-equation identities and Lemmas 2.1-2.4 (printed pp. 5-8),
the Euler-factor estimates of Section 3, and the relevant arguments throughout
Section 4 (pp. 13-16). The downloaded hashes match the source audit:

- PDF, 267062 bytes:
  `692b7fe38d883cf3503e247b0ebcd0c092c7e7267b06488adb9f40d45095b5a8`.
- Gzip source, 26276 bytes:
  `301cb41d96db71a722f278b1e9db437cf71c275ea07cc0289f3a916d8208528c`.
- Decompressed TeX:
  `2b5a85717f193b950ae522ad5c07f8f8bb1dc2213c073d54b4d4fa8cba6d98f8`.

External tools received only public source URLs and public-source queries.
No repository contents were sent to web services. Workspace reads and
computations used native tools; the incorrectly bound context-mode local
filesystem tools were not used or reconfigured.

## Analytic checks

### Residues, complex characters, and pairing

Let W(s) = xi'/xi(s,chi), B = W(0). Hadamard differentiation gives
W'(0) = -sum 1/rho^2. The formal residues of -W(s) X^s/s^2 are therefore

    -sum X^rho/rho^2 - B log X + sum 1/rho^2.

Separating the conductor and gamma factors gives exactly PROOF.md (1).
In particular, the constant zero sum has a **plus** sign, and B log X is a
full complex term.

For the other kernel, the residues of W(s) X^(s-1)/(s(s-1)) are

    W(1) - B/X + sum X^(rho-1)/(rho(rho-1)).

Functional equation and conjugation give W(1) = -conjugate(B), so (2) has
the stated signs. Using the digamma expansions at zero and their values at
1 and 1/2 reproduces all four E functions in the predecessor proof and LLS.
These are formal residue checks; the limiting contour justification is a
classical input, not a newly proved result of this review.

The same functional equation and conjugation map each zero of chi to
1-conjugate(rho), **within the same character**, preserving multiplicities
and height. Conjugation alone would change the character. Thus H(7/8)
gives the entire strip [1/8,7/8], including its endpoints.

The identity -Re B = sum Re(1/rho) also follows from Hadamard and
W(1) = -conjugate(B): take real parts of
W(1)-W(0) = sum 1/(rho(1-rho)), then use the same-character involution.
The real sums are absolutely convergent. This verifies the applicability
of the A weights without assuming that B itself is real.

I rederived both inequalities in Lemma 0'. For a reflected pair, put
U = 1/|rho|^2 and V = 1/|1-conjugate(rho)|^2. The first ratio is the
stated fractional-linear function of V/U; its two endpoint values give
the bound by X^sigma + 7X^(1-sigma). Convexity reduces it to the two
sigma endpoints. The comparison at sigma = 1/2 is exactly

    u^7 + 7u - 8u^4 = u(u^3-1)(u^3-7) >= 0,   u = X^(1/8), X >= 256.

For the second inequality the two denominators coincide, and weighted
AM-GM gives the factor 1/(2 sqrt(sigma(1-sigma))). Zeros on the central
line are counted once and satisfy both bounds. The exact rational slack is
7(189/125)^2 - 16 = 47/15625 > 0. Lemma 0's bound
sum |1/rho^2| <= 8A follows termwise from Re rho >= 1/8.

### Full B absorption and conductor 3

The triangle inequality applied to (2) gives

    (1 - 1/u - c(u)) |B| <= |(1/2)(1-1/u)log(f/pi) + E_a(u)| + T_zeta(u),

because A <= |B|. This is the correct full-complex denominator; replacing
it by the real-part denominator would be invalid. At u = 2^16 it is
exactly 1009383/1638400 > 3/5.

For every real x > 1, the factorial identity used in (4) is valid:
sum Lambda(n) floor(x/n) = log(floor(x)!), by summing
sum_{d|m} Lambda(d) = log m. Also x/n-1 <= floor(x/n), with nonnegative
weights. Consequently T_zeta(x) <= log x unconditionally. LLS Lemma 2.4's
RH error is not being imported.

Using |log(f/pi)| <= log f + log pi, |E| < 1, log pi < 2 and log u < 12
gives the claimed right side less than (log f)/2 + 14. Division yields
|B| < (5/6)log f + 70/3 < log q + 24. This includes f = 3 and does not
require log(f/pi) to be positive. It controls the imaginary component
needed when the coset phases are applied.

### Imprimitive factors and aggregation

Only primes dividing q but not f contribute to the difference between chi
and its inducing primitive character. They all divide r = q/f; primes
dividing both r and f contribute zero and may harmlessly be included.
Direct sums give (6) and (7), including r = 1 or 2:

- For S, each prime contributes at most (log X)^2/2, by bounding the
  decreasing sum over its exponents by an integral.
- For T, use 1-p^k/X <= 1-1/X and sum p^(-k) = 1/(p-1).

Taking real parts of (2) gives (1+1/X)A + Re Z, hence the lower factor
d(X) = 1+1/X-c(X). The correction from T(chi*) to T(chi) has the upper
sign used in the proof. Furthermore

    log f + 2 sum_{p|r} log p/(p-1) - log q
       <= sum_{p|r} (2/(p-1)-1) log p <= log 2.

After subtracting log pi this is strictly below L. Multiplication by
1-1/X still gives an upper bound L, since L > 0. This remains valid for
the negative log(3/pi) case. Thus (8) is sound.

At the identity coset, sum_{chi in Hdual} T(X,chi) is a nonnegative real
number. Subtracting the principal term proves
-Re sum_{chi != chi0} T <= T(X,chi0) <= T_zeta(X). This aggregation has
no coset phases and retains precisely h-1 terms. Only afterwards are
absolute values used to handle the phases in (10). Equation (9) follows.

### Principal contribution and complete error accounting

The zeta residues give the displayed exact principal formula. In
particular, its constant is -1 and its trivial-zero sum is nonnegative.
One way to check the constant is to differentiate the completed zeta
factorization at zero: the constant residue is
sum 1/rho^2 - 1 + pi^2/24, before combining the trivial zeros.

The two nontrivial-zero sums cost bF(X); removing the primes dividing q
costs at most omega(q)t^2/2. For each nonprincipal character, the other
terms cost

    (L+24)t + (L+2)t/2 + t^2/2 + t + 3
       = (3L/2+26)t + t^2/2 + 3.

The Euler-factor costs of the principal and h-1 nonprincipal terms sum
to at most h omega(q)t^2/2. The remaining principal cost is
log(2pi)t+1. These are exactly R(q,h,X); no constant or factor of h is
missing from (11) or (13).

### Gamma estimates and elementary enclosures

The Appendix's trapezoid identity is correct. Explicitly,
d_(k+1)-d_k equals the trapezoid error for 1/x on [k,k+1], which is
the integral of (x-k)(k+1-x)/x^3. It is positive and strictly below
(1/4) integral x^(-3). Summing gives
0 < gamma-d_N < 1/(8N^2). The log enclosures are used in the correct
directions in the code.

The author's Machin enclosure has the correct alternating-series
directions: with 16 terms, the partial arctangent sum is below the true
value and adding the next term is above it. The subtraction of the
1/239 interval reverses its endpoints as required.

I also recomputed these constants independently with exact Fractions,
using pi = 4(arctan(1/2)+arctan(1/3)), 40 alternating terms, and N = 512
for gamma. For logarithms I used the different expansion
-log(1-z) = sum_{j=1}^{100} z^j/j plus an upper tail
z^101/(101(1-z)), after reduction by powers of 2 to [1,2]. The resulting
exact enclosures imply the following outward-rounded rational bounds:

    3.1415926535897932384626 < pi < 3.1415926535897932384627,
    0.5772153470102153 < gamma < 0.5772158238473736,
    0.0230955500204622 < |B_zeta| < 0.0230957884390414 < 231/10000.

The same computation checks log 2 > 2/3, log 2 < 7/10, log 3 > 1,
log 80 < 22/5, log(65536) < 12, log(2pi) < 2 and pi^2 < 10.
I checked ln_bounds itself: binary range reduction puts the atanh
argument in [0,1/3], and its stated geometric tail bounds the positive
series. Its rational-input wrapper subtracts endpoints correctly.

For x >= 64, monotonicity of (log x+1)/x and log(2)/x gives upper
bounds -281/480 and -3451/12800 for E_0 and E_1, respectively, using
the proof's rounded constants. Once their signs are known, the absolute
value bounds are at most 1297301/1310400 and 23771/81900, both below 1.
The tilde-E tails are bounded by the two stated geometric series. The
triangle inequality, pi^2 < 10, gamma/2 < .29 and log 2+gamma/2 < .99
then imply |Etilde_a| <= t^2/2+t+3 for both parities. No zero or L-value
sampling is used in these conclusions.

### Proper powers, monotonicity, and strictness

For each p <= sqrt(X), the decreasing nonnegative summand gives

    sum_{k=2}^{floor(tau)} (tau-k) <= integral_1^tau (tau-v) dv
       = (tau-1)^2/2 <= tau^2/2.

Multiplication by (log p)^2 and counting at most sqrt(X) primes proves
the stated Q(X) bound for **all** proper prime powers, including even
and odd exponents. There is no use of LLS's RH-dependent smaller-argument
prime estimates.

In the analytic range y >= 80, log q > 1 and h >= 2 give h <= y,
L <= y/2 and omega(q) <= L/log 2 < 2L <= y. The log y/y bound decreases
there. Each residual summand is a positive multiple of
(log y)^b/y^a with a >= 6 and b <= 2; its derivative is nonpositive
since b-a log y < 0. The prime-power envelope has the same property
with a = 3, b = 2. The nonlogarithmic denominators and F envelopes also
have the asserted monotone bounds. The endpoint y = 80 is included.

There is no strictness gap: (11) and the strict certificate imply
C(X;aH) > Q(X). A prime exactly at X has weight log(X/X) = 0, so this
inequality forces a prime **strictly below** X. This also explains why
the use of sums written with n <= X does not weaken the theorem.

## Independent rational certificate

I recomputed the following using Python Fraction arithmetic, separately
from constants.py:

| Quantity | Exact value or upper envelope |
| --- | --- |
| Full complex denominator at 2^16 | `1009383/1638400 > 3/5` |
| 1-c(256) | `299/2000 > 0` |
| Lower d envelope at y=80 | `5023231811/5120000000 > 49/50` |
| Residual numerator at y=80, t=176/5 | `4256977` |
| Residual divided by 80^8 | `4256977/1677721600000000 < 1/100000000` |
| Zeta error | `231231/800000000` |
| Nonprincipal error | `47047/49000` |
| Proper-power error | `121/100000` |
| Sum, using the stated residual envelope | `5385194673/5600000000 < 1` |
| Margin | `214805327/5600000000 > 0` |

For example, this in-memory command reproduces the key rational totals
without importing the author script (run from the session directory):

```sh
python3 -B - <<'PY'
from fractions import Fraction as F
y, t, c = F(80), F(176, 5), F(189, 125)
D = 1 - F(1, 65536) - c*(F(1, 4) + F(1, 256))
R = 2*t + 1 + y*y*t*t/2 + y*((3*y/4+26)*t + t*t/2 + 3)
errors = [F(231,10000)*F(1001,1000)/y,
          F(1001,1000)*F(47,50)/F(49,50),
          F(1,10**8), 32*F(22,5)**2/y**3]
assert D == F(1009383,1638400) and D > F(3,5)
assert R == 4256977 and R/y**8 < errors[2]
assert sum(errors) == F(5385194673,5600000000) < 1
print(D, R/y**8, sum(errors), 1-sum(errors))
PY
```

## Progression reduction and independent finite check

The product formula phi(q)^2/q = product p^(a-2)(p-1)^2 proves
phi(q) >= sqrt(q/2): every odd-prime factor is at least 1, and the
2-factor is at least 1/2. For q >= 512, phi(q) >= 16 and
log q >= 9 log 2 > 6, so phi(q)log q > 96 > 80. The coset theorem
applies with H = {1}, since phi(q) >= 2 for q >= 3.

For 3 <= q <= 511, I used a different enumeration: for **each** reduced
class a, test a, a+q, a+2q, ... for primality by trial division. This
does not use a sieve, a supplied prime list, the author's certificate,
or ln_bounds. Every result satisfies the stronger exact bound

    least prime < phi(q)^8 < (phi(q)log q)^8.

The maximum of p/phi(q)^8 is 7/256. The enumeration covers 509 moduli
and **79,594 reduced classes**. The unique largest least prime is
**37363, in class 22 modulo 461**. Trial division verifies that 37363
is prime and that all 81 earlier positive members of this progression
are composite. A separate Mobius summatory-totient computation also
gives 79,594 classes.

The ordered sequence of records `q,a,p\n`, q then a increasing, has SHA-256
`4dc76edfbf66e13f2f4a17965db5cf67f5d459e5786360d6d2ea99b9c402badd`.
The following reproduces the independent finite check; it writes no files:

```sh
python3 -B - <<'PY'
from math import gcd, isqrt
from fractions import Fraction
from hashlib import sha256
def prime(n):
    if n < 2: return False
    if n % 2 == 0: return n == 2
    return all(n % d for d in range(3, isqrt(n)+1, 2))
classes, largest, ratio = 0, (0,0,0), Fraction(0)
digest = sha256()
for q in range(3,512):
    reduced = [a for a in range(1,q) if gcd(a,q) == 1]
    for a in reduced:
        p = a
        while not prime(p): p += q
        assert p < len(reduced)**8
        classes += 1
        largest = max(largest, (p,q,a))
        ratio = max(ratio, Fraction(p,len(reduced)**8))
        digest.update(f'{q},{a},{p}\n'.encode())
assert classes == 79594 and largest == (37363,461,22)
assert ratio == Fraction(7,256)
assert digest.hexdigest() == '4dc76edfbf66e13f2f4a17965db5cf67f5d459e5786360d6d2ea99b9c402badd'
print(classes, largest, ratio, digest.hexdigest())
PY
```

## Author-script replay and rejection controls

I also ran, from the repository root:

```sh
python3 -B research/least-prime-progression/constants.py
```

It exited 0 and printed exactly the total, margin, denominator, coverage
and largest prime reproduced above. All four controls printed
`REJECT control`. I separately called each control to inspect its actual
ValueError, rather than relying only on the printed label:

| Control | Actual rejection and meaning |
| --- | --- |
| c2 = 3/2 | `c2 must dominate 4/sqrt(7)`; 7c2^2 = 63/4 < 16. |
| y_min = 64 | `d(X) > 49/50`; its chosen lower envelope is `409521319/419430400 < 49/50`. |
| Prime list [2,3,5] at q=3 | Coverage error: reduced class 1 is absent. |
| Progression coefficient 1/2 at q=3 | Bound fails at a=1, p=7. |

The first two controls reject inputs that fail this particular certificate;
they do not show that no stronger proof could use a smaller constant or
cutoff. The latter controls test exhaustive coverage and the direction of
the least-prime comparison. None of these controls, individually or
together, validates the analytic theorem; the written checks above do that
within the declared inputs.

## Trust boundary and work not performed

- H(7/8) is an assumption, not a conclusion of this review. No Lean proof
  was replayed or certified.
- I take the classical analytic continuation, functional equations,
  Hadamard factorizations, standard gamma identities, and validity of the
  cited contour shifts and limiting operations as published inputs.
  I independently checked their algebraic consequences and formal
  residues used here; I did not supply a new contour-convergence proof.
- The independent finite check covers precisely q=3..511. Large moduli
  and arbitrary subgroups are covered by the uniform written inequalities,
  not by a finite search over groups or zeros.
- No optimality claim, smaller progression coefficient, unconditional
  least-prime result, or new Miller--Rabin frontier was checked or asserted.
- I did not rerun the existing baseline suite, reported passing in the
  review brief. That suite does not prove this new theorem. The new script
  and the independent computations described here were run.
- I added only this report. I did not modify the proof, script, source
  audit, README, or accepted results, or run any git mutation or public-write
  operation.
