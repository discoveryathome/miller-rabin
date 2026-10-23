**Original idea: Geoffrey Irving.**

# Independent mathematical recheck: uniform parameter and sharp coefficient

Reviewed 2026-10-23 by a fresh-context Codex review agent, `gpt-6.1-sol`,
max reasoning effort. This is a separate, same-model AI review. Text:
CC BY 4.0; the executable check below: Apache-2.0.

## Verdict and issues

**Confirmed within the stated conditional and classical-input scope.**
No blocking issue, required mathematical fix, or numerical correction was
found in the frozen inputs. For every fixed `13/15 <= b <= 7/8`, assuming
H(b), including zeta and the relevant primitive characters at all heights,
the argument proves, with `r = 1/(1-b)`,

    P(aH,q) < max(80,h log q)^r       (q >= 3, h = [G:H] >= 2),
    P(a,q) <= [c_b phi(q) log q]^r    (q >= 3, gcd(a,q) = 1),
    c_b = 7^(1-b)/(2 log 3).

For every `q >= 4` it proves the stronger strict bound

    P(a,q) < [(29/50) phi(q) log q]^r.

The all-q coefficient is sharp for each fixed b. Its only equality case
is `q=3`, the residue class `a=1` in `(Z/3Z)*`, whose least prime is 7.
The coefficient `581/1000` also works strictly at both `b=7/8` and
`b=8748867/10000000`, with the respective exponent r. This last decimal
comparison is not asserted for the entire parameter interval.

The uniform kernel argument, complex phases, exactly h-1 nonprincipal
terms, principal input, Euler losses, proper-power subtraction, exponent
directions, complete finite domain, and equality statement were checked.
The new finite comparison was independently recomputed with a different
search algorithm and different logarithm series. Historical reviews and
the author's successful replay were not treated as proof of this extension.

This verdict does not establish H(b), verify the source papers' proofs,
constitute formal verification, or claim human or maintainer acceptance.

## Exact reviewed snapshot

Working directory:
`/root/.t3/scratch/2026-10-23-fetch-https-discoveryathome-org-v0-7d492a7d/repo`.

- Branch: `session/20261023T0602-corollaries`.
- Local HEAD, also the published PR #11 head specified in the brief:
  `75f9135220389a3dc48b92e5443313b02842e9cb`.
- Accepted base: `d2bd5167a42b8256f1362640dc149057920e5db9`.
- Reviewed new inputs: the uncommitted PROOF.md, constants.py and README.md
  in this package. The review is pinned to their bytes, not just HEAD.

SHA-256:

```text
research/least-prime-progression/PROOF.md
725cff10144eacee1819140c4ec9fec2cf3a8938ed19cf017321e6c2fa71314e
research/least-prime-progression/constants.py
b28e47ef7df20c6ca731525ce2108ed5c92380526f24e7a2dbb8bd19eb92c14a
research/least-prime-progression/README.md
c6443282d574446e08fe2264866aec42b75f402f5d8c893df9e275e3996febe7
AGENTS.md
e8f93ce38983d792791c3f9ad9b8b0a367668b3b7b945b071b6f360c45babd62
DISCOVERY.md
e603c2aaf4b9c692b315213f6c7dd5aebdfba5932e67155e53c76a6590ec4ddf
discover/frontier.json
9ca629138c133ac8547efba9b47f4d862ae82e7079c4da0998961d8fa5c964a4
research/zero-pairing/PROOF.md
824af09db62887a04107e72f9aafb56345aef45c1ea3ccf6499956d6896e914c
research/first-explicit-t1/PROOF.md
abd066b2d27961e93ae007e5fb8897b5a841aff875b24af3eb0216d73bed8cbb
verify/check.py
ace2b055b5279284d04d37b6c6dde77af86088245846700c502effb3e812e709
```

The last three dependency files were byte-compared with `git show
d2bd5167a42b8256f1362640dc149057920e5db9:<path>` and match that base.
AGENTS.md, DISCOVERY.md and the frontier were read. No frontier update,
git mutation, installation, delegation, public comment or source-input
edit was performed. Unrelated untracked work, including SOURCE-DRAFT.md
material, is outside this review. This report is the only file written.

## Primary sources and prior findings

I consulted [LLS arXiv:1309.3595v3](https://arxiv.org/html/1309.3595v3),
especially the unreduced residues in the proofs of Lemmas 2.2--2.3 and
Section 4's orthogonality, complex constant, imprimitive corrections and
h-1 aggregation. The GRH estimates in those statements are not used
unchanged. The local proof replaces the square-root zero estimates,
the x=100 absorption, the RH-based auxiliary sum, and proper-power bounds.
The contour-shift foundations remain classical inputs.

[Xu--Sang v2, Theorem 1.1](https://arxiv.org/html/2610.15291v2#S1.SS2)
explicitly covers every Dirichlet L-function, including zeta. It assumes
its recorded analytic inputs, including the family-wide 7/8 zero-free
half-plane. This agrees with the new paragraph and the frontier's open
A1b assumption. Here H(b) is assumed directly; no sibling theorem or
source-paper proof is needed to discharge that assumption.

Both primary HTML pages were fetched independently with Python's standard
`urllib.request.urlopen`, as well as inspected through the web tool.
The fetched response bytes, not PDF or source archives, were:

```text
https://arxiv.org/html/1309.3595v3
685354 bytes; SHA256 a9560eb9b5b15592df481488765aea74d7a199c3c74553cdd4464ddbf09b7b4f
https://arxiv.org/html/2610.15291v2
667265 bytes; SHA256 74ace7acb59fe416c7891da3b29b0a0ea1c8601304aa9274d40b4f662c2afbc8
```

The context-mode HTML conversion failed with `Cannot find module
'turndown'`; no installation was attempted. Direct standard-library
fetching and the web rendering supplied the source checks above.

Prior findings and their disposition:

- [RECHECK.md](RECHECK.md), SHA256
  `7ba56b4b9fd9afd856c1b310969f018efddea8e6e9ebfdd6e07bc3f19caac098`,
  confirmed the original coset theorem and coefficient-1 corollary.
  Its complex-character, residue, gamma, Euler and power accounting were
  reread in their present uses. No unresolved objection was inherited.
- [RECHECK-REFINEMENT.md](RECHECK-REFINEMENT.md), SHA256
  `04c1d72040b7497269fc8d6155337d61973d4665c2fa570b490fb6d00befc877`,
  confirmed coefficient .581 and its finite remainder. Its optional
  historical-cutoff clarification was already incorporated in the current
  SOURCE-AUDIT.md, whose SHA256 is
  `187e7f639fdee81410d58102aaf042de00a5b5cae6cb715e83e73314a34ad429`.
  Neither old review covers the new uniform-parameter claim.
- `../nonresidue/research/least-nonresidue/GUARD-RECHECK.md`, SHA256
  `c75db68a3b80e6ebf38232a9298d0be16000898cd229a38045c68c485c28ca31`,
  records the repaired negative-c2 guard. The current progression guard
  and its regression control were independently probed again below.
  That issue remains resolved.

The frozen text's statements that this extension awaits review describe
its pre-review status accurately. Updating that status belongs to the
parent's subsequent edits; the frozen inputs were left intact.

## Independent reconstruction of the parameter transfer

I write beta for the new parameter and `b_zeta=231/10000` for the older
constant named b in Sections 1--7. This keeps the coefficient of the
principal zero error distinct from the strip parameter.

For a primitive character, the functional equation followed by complex
conjugation sends a zero rho of that same character to
`1-conjugate(rho)`, preserving multiplicities. It does not require a real
character. H(beta) therefore puts the nontrivial zeros in
`1-beta <= Re rho <= beta`. Zeta has the same reflection. Real zeros,
including a hypothetical exceptional zero, are covered as well.

For an off-line pair, put `sigma >= 1/2`, `alpha=1-sigma`,
`v=1/(sigma^2+gamma^2)` and `w=1/(alpha^2+gamma^2)`. Its A weight is
`sigma*v+alpha*w`. The ratio `s=w/v` lies between 1 and
`sigma^2/alpha^2`. The first absolute-kernel ratio is

    (X^sigma + s X^alpha)/(sigma + alpha s).

This fractional-linear function has its maximum at an endpoint. The
endpoint values are exactly the two expressions displayed in Section 8.
Since `alpha/sigma <= 1` and `sigma/alpha <= beta/(1-beta) <= 7`, both
are at most `g(sigma)=X^sigma+7X^(1-sigma)`. Convexity on `[1/2,beta]`
reduces to `g(1/2)=8 sqrt(X)` and g(beta). With
`z=X^(beta-1/2)`, their difference divided by sqrt(X) is
`(z-1)(z-7)/z`. The required `z>=7` holds throughout the claimed range:

    beta-1/2 >= 11/30,
    256^11 - 7^30 = 286945669530652810636917807 > 0.

A line zero has the smaller ratio `2 sqrt(X)`. Thus the first kernel is
bounded by `(X^beta+7X^(1-beta))*A`, uniformly for X>=256.

For the second kernel, the pair's absolute numerator is
`(X^(sigma-1)+X^(-sigma))*sqrt(v*w)`. AM--GM bounds its ratio to its A
weight by

    [X^(sigma-1)+X^(-sigma)]/[2 sqrt(sigma(1-sigma))]
      <= (189/125)[X^(beta-1)+X^(-1/2)].

Here `sigma(1-sigma)>=beta(1-beta)>=7/64`, and the rational replacement
has the required positive sign and square bound:
`7*189^2-16*125^2=47>0`. A line zero's ratio `2X^(-1/2)` also satisfies
the stated envelope. Finally, term by term,

    1/|rho|^2 <= r Re(1/rho),    r=1/(1-beta)<=8.

All the weights and absolute-kernel summands being regrouped are
nonnegative and convergent. The conclusion is valid for complex
characters and zeta, with the static +8 and exactly the F_beta in (18).
This is a continuum proof in beta, not inference from endpoint samples.

At the fixed `u=65536`, `c(u;beta)<=c(u;7/8)`. In the complex identity
(2), the reverse triangle inequality gives
`|-conjugate(B)-B/u| >= (1-1/u)|B|`, and `A<=|B|`. Therefore the full
complex constant, including its imaginary part, is absorbed with

    1-1/u-c(u;beta) >= 1009383/1638400 > 3/5.

The same triangle bound gives `|B| < (5/6)log f+70/3 < log q+24`.
This does not assume `log(f/pi)>0`, so f=3 remains covered.

I also checked the transfer of the remaining counting argument:

- The real-part use of (2) gives `d(X;beta)A <= L/2-Re T(X,chi)`
  after the Euler-factor correction. The inequality
  `log f+2 sum_(p|q/f) log p/(p-1) <= log q+log 2`, followed by `pi>2`,
  remains valid without a sign assumption on `log(f/pi)`.
- At the identity coset, the character sum of the T weights is
  nonnegative. Hence `-Re sum_(chi!=chi0) T <= T(chi0) <= T_zeta <= t`.
  This proves `sum A <= [(h-1)L/2+t]/d` with exactly h-1 terms.
  Phases are introduced only afterward in (10); their moduli are 1.
  Absolute S bounds and the full complex B bound justify that step.
- Only primes dividing q and absent from the primitive conductor need
  removal. The overcounts using q/f and then q are safe. The principal
  and h-1 nonprincipal S corrections total at most `h omega(q)t^2/2`.
- The zeta pole contributes X. Its constant -1 and the dropped
  nonnegative trivial-zero sum have the displayed signs. Its remaining
  zero error is `b_zeta F_beta(X)`. Independently enclosing gamma at
  N=512, pi by 24-term arctangent sums and logarithms by a 60-term
  non-atanh series again gave `0<A_zeta<231/10000` in exact arithmetic.
  The diagnostic interval was approximately
  `(0.023095550020462267, 0.02309578843904137)`; rounded decimals were
  not used in a decision.
- The gamma functions and the estimates (3) are independent of beta.
  The nonprincipal nonzero-sum costs remain
  `(L+24)t+(L+2)t/2+t^2/2+t+3 = (3L/2+26)t+t^2/2+3`.
  Thus R in (11) retains every principal, conductor and gamma term.
- Summing proper powers of each p<=sqrt(X) gives at most t^2/2 per
  prime. Criterion (13) must and does retain `h t^2/(2 sqrt(X))`.
  Assuming no prime strictly below X is enough: a prime at X has zero
  logarithmic weight. The final conclusions are therefore strict where
  stated, even if the real cutoff happens to be a prime integer.

Only primitive nonprincipal conductors and zeta enter the zero sums.
Imprimitive Euler-factor zeros are not fed into the pairing lemma. Every
application here has X>=256, including the fixed-u argument; the gamma
range X>=64 is consequently also satisfied.

## Directed envelopes and every new budget

For `y=X^(1-beta)`, the actual exponent range is `15/2 <= r <= 8`.
The weaker `7<r<=8` used in the proof is safe. For y>=80,

    F_beta(X)/X = 1/y + 7/y^(r-1) + 8/y^r
                 <= 1/y + 7/y^6 + 8/y^7,
    d(X;beta) >= 1-(189/125)(1/y+1/y^3),
    X>=y^7,    t<=8 log y,    sqrt(X)>=y^(7/2).

In particular `X^(-1/2)<=y^(-3)` is safe here. Reusing the old
`y^(-4)` bound for beta<7/8 would not be safe; it is not used.

With `h<=y/C`, `L<=y/(2C)` and `omega(q)<=y/C`, the new residual
envelope expands into precisely

    (16 log y+1)/y^7
      +(32/C^2)(log y)^2/y^5 +(6/C^2)log y/y^5
      +(208/C)log y/y^6 +(32/C)(log y)^2/y^6 +(3/C)/y^6.

Use C=1 for cosets and C=29/50 for progressions. Each summand has
nonnegative coefficient, denominator degree at least 5 and log degree
at most 2. Its derivative is nonpositive when `k log y >= j`, hence
throughout both domains. The analogous functions `log y/y` and
`(log y)^2/y^2` also decrease there. This establishes the entire y range;
endpoint arithmetic is not being used in place of monotonicity.

For cosets take `y=max(80,hL)`. The facts `L>1`, `h>=2` and
`omega(q)<2L` give the stated C=1 substitutions. At y=80,

    d_lower = 62790211/64000000 > 49/50,
    1+7/y^5+8/y^6 = 32768000071/32768000000 < 1001/1000,
    R/X <= 4256977/20971520000000 < 1/10^6.

Here t<176/5 follows from log80<22/5, and
`sqrt(X)>=y^(7/2)>8y^3` follows from y>=80>64. The power error is at
most `4(log y)^2/y^2`. The four charged errors, in order, are

    231231/800000000,  6721/7000,  1/1000000,  121/10000.

They sum to `5446184217/5600000000`, leaving
`153815783/5600000000>0`. This independently reproduces (20).

For progressions, the elementary prime-factor product proves
`phi(q)^3>=2q^2/9` for every q. At q>=2048,
`2*2048^2-9*96^3=425984>0`, so h>96; also L>22/3. With C=29/50,
`y=C hL>10208/25>400`. This threshold does not depend on beta.
At y=400,

    d_lower = 7969759811/8000000000 > 249/250,
    1+7/y^5+8/y^6 = 512000000000351/512000000000000 < 1001/1000,
    R/X <= 476593821577/1377894400000000000000 < 1/10^9.

All factors of 1/C and 1/C^2 are included. Now
`sqrt(X)>=y^(7/2)>=20y^3`, so the power error is at most
`8(log y)^2/(5C y^2)`. With log400<6, the four charged errors are

    231231/4000000000,  178178/180525,  1/1000000000,  9/14500.

Their sum is `5705615549587/5776800000000`, with margin
`71184450413/5776800000000>0`, independently reproducing (21).
The standalone check below also reproduces both residual fractions and
hashes the complete rational budget records.

## Independent complete finite check and sharpness

The decisive computation did not call any package function or import
verify/check.py. It used an Euler linear least-prime-factor sieve through
262144, then checked its primality classification for **every** integer
2..262144 by trial division. This produces 23000 primes. Instead of
marking classes in increasing prime order, it enumerated reduced classes
by direct gcd and searched each progression `a, a+q, a+2q, ...` for its
first prime, rejecting any search that reached the cap without a prime.
Thus both primality and leastness are checked, with no probabilistic test
or imported totient table.

Independent logarithm intervals use

    -log(1-z) = sum_(k>=1) z^k/k,
    0 <= tail_after_N <= z^(N+1)/((N+1)(1-z)),

with N=40 and dyadic reduction to `1<=x<2`; log2 uses z=1/2. This differs
from verify/check.py's atanh expansion. Every finite inequality uses the
lower rational endpoint, and every obstruction uses an upper endpoint.

Results:

- q=4..2047: all **1274558** reduced classes satisfy
  `P(a,q) < [(29/50)phi(q)log_lower(q)]^7`.
- The positive control q=3..2047 also rechecked all **1274560** classes
  against the original `[(581/1000)phi(q)log_lower(q)]^8` bound.
- Both ranges have largest least prime **169937**, at q=1945,a=722.
  The q=3 classes were independently found to have least primes 2 and 7.
- The minimum new lower base occurs at q=4 and is >8/5 (diagnostically
  about 1.608101458899). The smallest new bound/P is at q=4,a=1,P=5
  and is >5 (about 5.56191205118). All comparisons are strict.

There is also a computation-free base check: for q>=4, phi(q)>=2 and
`log q>=2log2>4/3`, so the base exceeds `116/75>1`. Since r>7, the
seventh-power comparison implies the desired r-th-power comparison.
The author's lack of a separate `require(base>1)` in finite_certificate
does not create a hole: its successful comparison with a positive prime
at power 7 already forces this, and the analytic check is stronger.

The canonical data hashes are over ASCII rows, no header, newline after
every row, ordered by increasing q and then increasing reduced a:

```text
all q=3..2047 rows "q,a,P(a,q)\n":
d3cbf54f933da04873ff6482d18081a88ac75c626fc3310a64b521ced057c27c
new q=4..2047 rows "q,a,P(a,q)\n":
28d869741016dccb0cd2fbadb06edcbf65e00bceb31c1ff07bc84df88c39a9f5
one row per q=3..2047, "q,phi(q),largest_P,its_a\n":
e5b6b72cfa161156f3bfd1fc2a66bf1c42c0a059756904a116f2428681a78d62
all primes <=262144, "p\n" in increasing order:
7657ca3fb8aae28495a3420e5246606f64f7c64bdced594d73226baac3990de5
coset rational budget record:
493d6135885a9b2f0404b68c4719ef53f4cfa6926ac61fe4feb483c0c18387a2
progression rational budget record:
93c3d094c6d58d4825d432661ca89915ef9f5bc1597c2b5adf6a57eea53aef19
```

For sharpness, write `delta=(29/50)*2log3`. Independent rational
enclosures give `delta>1` and `delta^8<7`. Since r<=8,
`delta^r<=delta^8<7`; hence `29/50<c_b` on the whole parameter interval.
The strict q>=4 bound is therefore strictly below the claimed all-q
bound. At q=3 the latter is identically
`[c_b*2log3]^r=7`; class 2 has least prime 2 and class 1 has least prime
7. This proves both the unique equality class and necessity of c_b.

For the two claimed .581 specializations, the independent lower log
`l3=27465307/25000000=1.09861228` gives, in exact integer/rational
arithmetic,

    ((581/1000)*2*l3)^799 > 7^100,
    (581/1000)*2*l3 > 1,
    10000000/1251133 - 799/100 = 344733/125113300 > 0.

Thus .581 exceeds c_b at both specified parameters. The fractional
exponents are compared using a base >1 in the correct direction.

## Replays, controls and reproducibility

Executed from the repository root, with bytecode writes disabled:

```sh
python3 -B research/least-prime-progression/constants.py
env PYTHONDONTWRITEBYTECODE=1 python3 -B research/zero-pairing/constants.py
env PYTHONDONTWRITEBYTECODE=1 python3 -B verify/check.py all
env PYTHONDONTWRITEBYTECODE=1 python3 -B -m unittest discover -s tests
git diff --check -- research/least-prime-progression/PROOF.md research/least-prime-progression/constants.py research/least-prime-progression/README.md
```

The package replay exited 0, printed both new totals and finite counts,
and rejected all seven controls: insufficient positive pairing constant,
negative pairing constant, too-small analytic cutoff, missing class,
false coefficient .5, the .58 obstruction at q=3, and beta=9/10.
Its captured stdout SHA256 was
`213627596b7e43cb578f06c7ed1329829f581cb5c9360845d9e86f29fa4ff62f`.
The accepted zero-pairing replay passed; its sampled diagnostics are
not used as a proof of pairing. The repository verifier passed all five
candidate files and smalln; all 16 unit tests passed. Those commands
check the repository's recorded Miller--Rabin claims, not this theorem.
The frozen diff whitespace check also passed.

Using `runpy.run_path` with bytecode disabled, theta_certificate was
additionally tested at beta=13/15, 8748867/10000000 and 7/8. All returned
the same two claimed rational budgets. Inputs 13/15-1/10^8,
7/8+1/10^8 and 9/10 were rejected at the strip guard. The inherited
analytic_certificate accepted c2=189/125 and rejected -189/125, 3/2
and 0. Compiling a separate in-memory copy with only `c2 > 0 and`
removed caused failure_controls to raise
`failure control was accepted: negative pairing constant`, as required.
No mutated copy was written to disk.

The following self-contained check is the reproducible independent
calculation. It imports only the standard library and writes no files.
It includes the distinct finite search, independent logarithms, rational
budgets, and sharpness comparisons. The initial independent finite run
took approximately 45.5 seconds; the version below moves the identical
per-modulus bounds out of the inner class loop.

Run its marked code from this report with:

```sh
python3 -B - <<'PY'
from pathlib import Path
text = Path('research/least-prime-progression/RECHECK-SHARP.md').read_text()
code = text.split('<!-- independent-check -->\n```python\n', 1)[1]
code = code.split('\n```\n<!-- /independent-check -->', 1)[0]
exec(compile(code, '<independent-sharp-check>', 'exec'))
PY
```

<!-- independent-check -->
```python
from fractions import Fraction as F
from hashlib import sha256
from math import gcd, isqrt

def unit_log(x, terms=40):
    z = 1 - 1/x
    s = sum((z**k/k for k in range(1, terms+1)), F(0))
    return s, s + z**(terms+1)/((terms+1)*(1-z))

l2lo, l2hi = unit_log(F(2))
def log_bounds(n):
    k = n.bit_length()-1
    lo, hi = unit_log(F(n, 1 << k))
    return k*l2lo+lo, k*l2hi+hi

assert l2lo > F(2, 3) and log_bounds(3)[0] > 1
for n, cap in [(80, F(22, 5)), (400, F(6)), (65536, F(12))]:
    assert log_bounds(n)[1] < cap
assert 256**11 - 7**30 == 286945669530652810636917807
for beta in [F(13, 15), F(8748867, 10000000), F(7, 8)]:
    r = 1/(1-beta)
    assert F(15, 2) <= r <= 8 and beta-F(1, 2) >= F(11, 30)
    assert beta/(1-beta) <= 7 and beta*(1-beta) >= F(7, 64)
c2, bz, factor = F(189, 125), F(231, 10000), F(1001, 1000)
assert c2 > 0 and 7*c2*c2-16 == F(47, 15625)
assert 1-F(1, 65536)-c2*(F(1, 4)+F(1, 256)) == F(1009383, 1638400)
assert F(1009383, 1638400) > F(3, 5)
assert 2*2048**2-9*96**3 == 425984
assert F(29, 50)*96*F(22, 3) == F(10208, 25) > 400
assert 11*l2lo > F(22, 3)

for name, y, lg, C, d, charge, expected, expected_hash in [
    ('coset', F(80), F(22, 5), F(1), F(49, 50), F(1, 10**6),
     F(5446184217, 5600000000),
     '493d6135885a9b2f0404b68c4719ef53f4cfa6926ac61fe4feb483c0c18387a2'),
    ('progression', F(400), F(6), F(29, 50), F(249, 250), F(1, 10**9),
     F(5705615549587, 5776800000000),
     '93c3d094c6d58d4825d432661ca89915ef9f5bc1597c2b5adf6a57eea53aef19')
]:
    t = 8*lg
    d0 = 1-c2*(1/y+1/y**3)
    ff = 1+7/y**5+8/y**6
    residual = (2*t+1+y*y*t*t/(2*C*C)
                +(y/C)*((3*y/(4*C)+26)*t+t*t/2+3))/y**7
    z = bz*factor/y
    non = factor*(1/(2*C)+t/y)/d
    powers = (4 if name == 'coset' else F(8, 5)/C)*lg*lg/y**2
    total = z+non+charge+powers
    assert d0 > d and ff < factor and residual < charge
    assert total == expected < 1
    record = '\n'.join(map(str, [name, d0, ff, residual, z, non,
                                  charge, powers, total, 1-total]))+'\n'
    digest = sha256(record.encode()).hexdigest()
    assert digest == expected_hash
    print(name, 'residual', residual, 'total', total, 'margin', 1-total)
    print(name, 'budget_sha256', digest)

l3, h3 = log_bounds(3)
assert F(29, 50)*2*l3 > 1 and (F(29, 50)*2*h3)**8 < 7
scaled = l3*10**8
short = F(scaled.numerator//scaled.denominator, 10**8)
assert short == F(27465307, 25000000)
assert F(581, 1000)*2*short > 1
assert (F(581, 1000)*2*short)**799 > 7**100
assert F(10000000, 1251133)-F(799, 100) == F(344733, 125113300) > 0
print('independent logarithm and sharpness comparisons PASS')

limit = 1 << 18
least = [0]*(limit+1)
primes = []
for n in range(2, limit+1):
    if least[n] == 0:
        least[n] = n
        primes.append(n)
    for p in primes:
        if p > least[n] or p*n > limit:
            break
        least[p*n] = p
assert len(primes) == 23000
trial = [n for n in range(2, isqrt(limit)+1)
         if all(n%d for d in range(2, isqrt(n)+1))]
assert all((least[n] == n) == all(n%p for p in trial if p*p <= n)
           for n in range(2, limit+1))
prime_hash = sha256(''.join(f'{p}\n' for p in primes).encode()).hexdigest()
assert prime_hash == '7657ca3fb8aae28495a3420e5246606f64f7c64bdced594d73226baac3990de5'

hall, hnew, hsum = sha256(), sha256(), sha256()
classes = newclasses = 0
largest = (0, 0, 0)
minbase = closest_new = closest_old = None
for q in range(3, 2048):
    residues = [a for a in range(1, q) if gcd(a, q) == 1]
    phi = len(residues)
    lo = log_bounds(q)[0]
    base_old, base_new = F(581, 1000)*phi*lo, F(29, 50)*phi*lo
    old_bound, new_bound = base_old**8, base_new**7
    row = []
    for a in residues:
        n = a if a >= 2 else a+q
        while n <= limit and least[n] != n:
            n += q
        assert n <= limit and n%q == a and gcd(n, q) == 1
        assert n < old_bound
        row.append((n, a))
        classes += 1
        encoded = f'{q},{a},{n}\n'.encode()
        hall.update(encoded)
        largest = max(largest, (n, q, a))
        if q >= 4:
            assert base_new > 1 and n < new_bound
            newclasses += 1
            hnew.update(encoded)
    p, a = max(row)
    hsum.update(f'{q},{phi},{p},{a}\n'.encode())
    if q == 3:
        assert row == [(7, 1), (2, 2)]
    if q >= 4:
        if minbase is None or base_new < minbase[0]:
            minbase = (base_new, q)
        ratio = new_bound/p
        if closest_new is None or ratio < closest_new[0]:
            closest_new = (ratio, q, a, p)
    ratio = old_bound/p
    if closest_old is None or ratio < closest_old[0]:
        closest_old = (ratio, q, a, p)
assert (classes, newclasses) == (1274560, 1274558)
assert largest == (169937, 1945, 722)
assert minbase[1] == 4 and minbase[0] > F(8, 5)
assert closest_new[1:] == (4, 1, 5) and closest_new[0] > 5
assert closest_old[1:] == (3, 1, 7) and closest_old[0] > 1
for label, got, expected in [
    ('all_rows', hall.hexdigest(),
     'd3cbf54f933da04873ff6482d18081a88ac75c626fc3310a64b521ced057c27c'),
    ('new_rows', hnew.hexdigest(),
     '28d869741016dccb0cd2fbadb06edcbf65e00bceb31c1ff07bc84df88c39a9f5'),
    ('q_phi_p_a_rows', hsum.hexdigest(),
     'e5b6b72cfa161156f3bfd1fc2a66bf1c42c0a059756904a116f2428681a78d62')
]:
    assert got == expected
    print(label+'_sha256', got)
print('prime_list_sha256', prime_hash)
print('classes', classes, 'new_classes', newclasses, 'largest(p,q,a)', largest)
print('all independent rational, finite and positive-control checks PASS')
```
<!-- /independent-check -->

The exact code block above, excluding its Markdown fence and the newline
immediately before the closing fence, has SHA256
`9487096a1070bdc578e147ed6c568829284afeac3b7e3e2eae7ca8994524e6f2`.
Its replay exited 0 in approximately 12.4 seconds and ended with
`all independent rational, finite and positive-control checks PASS`.
Captured stdout SHA256:
`0eaac4c2e4f7eed92aa03046c02ea9246732c030370367c027e60b09c9745b34`.
All three frozen input hashes were rechecked afterward and remained
unchanged. Final repository status showed this report as the only new
review file, alongside the original three input edits and unrelated
pre-existing untracked work.

## Limits of the conclusion

This review reconstructs the new inequalities and their uniform domains
and independently checks the complete finite remainder. The computations
are exact Python integer/rational computations, not proof-assistant
certificates; they retain the usual trust in Python and the execution
environment. The analytic argument still assumes the classical completed
L-function identities, functional equations, Hadamard product facts,
contour justifications and gamma formulas identified in the source audit
and the earlier review. Their use and algebra were checked; their entire
classical foundations were not reproved here.

Neither H(7/8), the stronger H(b), the OpenAI/Xu--Sang paper proofs nor a
Lean replay was verified. Source scope verification is narrower than
source proof verification. The source response hashes pin the fetched
HTML only. Finite computation covers precisely q<2048 and does not
replace the analytic proof for q>=2048 or enumerate all subgroups.
The new all-q coefficient's optimality follows from the exact q=3
equality, not numerical optimization. No improvement or optimality of
the coset cutoff 80 is claimed. No new T1 claim or accepted-frontier
change is part of this report.
