**Original idea: Geoffrey Irving.**

# Independent mathematical recheck of the sharp coefficients

Reviewed 2026-10-23 by a fresh-context Codex review agent, using the same
model as the author (`gpt-6.1-sol`, max reasoning effort). This is an
independent AI review, not human review, formal verification, or maintainer
acceptance.

**Verdict: PASS for the frozen bytes below, conditional on H(b), including
zeta, and the declared classical analytic inputs, for every real
13/15 <= b <= 7/8. No blocking mathematical or checker issue was found.**

With r=1/(1-b), Section 6 correctly proves the sharp non-strict bounds

```text
ell(q,H) <= (C5 log q)^r,  C5=2^(1-b)/log 5,  q>=5, q!=6,
ell(q,H) <= (C6 log q)^r,  C6=5^(1-b)/log 6,  q>=5,
```

for every proper unit subgroup, including composite moduli. Equality occurs
exactly at q=5 in the first statement and q=6 in the second. The prime
quadratic statement has the same sharp C5 and equality exactly at q=5.
The stronger strict bound with coefficient 677/1000 holds for every q>=7
throughout the parameter interval. The exact q=3,4 exceptions remain 2,3.
The old decimal statements are separately certified at 7/8 and the exact
smaller theta; they are not being extended uniformly in b.

One optional documentation correction: `PROOF.md:44-45` still says
“Neither optimality ... is asserted” immediately after the new summary of
sharp constants. Qualify this as referring to the preceding rounded
coefficients, as the README and Section 5 already do. This is a wording
inconsistency, not a defect in Section 6's proof. The frozen pending-review
status text and all three inputs were left untouched.

## Frozen snapshot and dependencies

Working directory:
`/root/.t3/scratch/2026-10-23-fetch-https-discoveryathome-org-v0-7d492a7d/nonresidue`.
HEAD is `dc610bcfde0b341a6e0633dbb14a0413e840f4de`; accepted upstream base
`d2bd5167a42b8256f1362640dc149057920e5db9` is an ancestor. At entry the only
working-tree changes were the three supplied files. This review covers
their uncommitted delta, not a claim that Section 6 is already published.

SHA-256 of the actual frozen inputs, relative to the repository root:

```text
a6a363eb155fffa141095561935f519453923e4b4258bb1486e50a87364b251c  research/least-nonresidue/PROOF.md
66c12cd8c310d0656710a80f3ba804d302b1a24791481b4d554599eccf4c257f  research/least-nonresidue/constants.py
40d118a124336afd3da5f9ed50343c3a105a381de93a98ef529a897c349d425c  research/least-nonresidue/README.md
```

I read AGENTS.md, DISCOVERY.md, the frontier, the package and historical
review dispositions, the accepted analytic/pairing arguments, and the
imported logarithm implementation. The following dependencies were hashed
and individually compared with `git show` at the accepted base; all were
byte-identical:

```text
824af09db62887a04107e72f9aafb56345aef45c1ea3ccf6499956d6896e914c  research/zero-pairing/PROOF.md
b71772dee37a2b068677c2800c2dce6d0737a94d03380f47b2f9d87ec6e610a7  research/zero-pairing/constants.py
abd066b2d27961e93ae007e5fb8897b5a841aff875b24af3eb0216d73bed8cbb  research/first-explicit-t1/PROOF.md
ace2b055b5279284d04d37b6c6dde77af86088245846700c502effb3e812e709  verify/check.py
ba252ae554ac3f4ca372b692ef6ed7966772716dfa57c5b65ed22ae84fe5a1f1  verify/mr.py
9ca629138c133ac8547efba9b47f4d862ae82e7079c4da0998961d8fa5c964a4  discover/frontier.json
```

The frontier establishes acceptance of the predecessor lemmas from PRs #6
and #8 despite older draft labels inside their files. Its A1 and A1b
half-plane assumptions remain open. No unmerged sibling theorem is used.

## Parameter transfer and source boundary

For a primitive character, conjugating the functional equation shows that
rho -> 1-conjugate(rho) preserves the zero multiset of the same character,
including multiplicities. This remains true for complex characters. H(b)
therefore places nontrivial zeros in [1-b,b]. Write
A=sum Re(1/rho)=-Re B>=0, using the classical completed-L-function identity.
The same reasoning applies to zeta.

On the entire real interval, b/(1-b) and r increase, b-1/2 increases, and
b(1-b) decreases. Their endpoint values prove

```text
b/(1-b) <= 7,        b-1/2 >= 11/30,
b(1-b) >= 7/64,      15/2 <= r <= 8.
```

These inequalities establish the continuum claim, including irrational b;
the finite helper probes below are additional implementation checks.

For an off-line reflected pair, put v=1/|rho|^2, w=1/|rho'|^2 and
sigma=Re rho>=1/2. The ratio w/v is in [1,sigma^2/(1-sigma)^2]. Dividing
the main zero contribution by sigma*v+(1-sigma)*w gives a fractional-linear
function with endpoint values

```text
X^sigma + X^(1-sigma),
((1-sigma)/sigma) X^sigma + (sigma/(1-sigma)) X^(1-sigma).
```

Both are bounded by g(sigma)=X^sigma+7X^(1-sigma). Its convexity reduces
the maximum to sigma=1/2 or b. For u=X^(b-1/2),

```text
(g(b)-g(1/2))/sqrt(X) = (u-1)(u-7)/u,
256^11 = 309485009821345068724781056,
7^30   = 22539340290692258087863249.
```

Thus X>=256 implies u>=256^(11/30)>7, including b=13/15, and the desired
endpoint is g(b). A zero on the line has ratio 2*sqrt(X), also covered.

For the second kernel, the common absolute denominator of the pair is
|rho|*|rho'|. AM-GM gives ratio at most

```text
(X^(sigma-1)+X^(-sigma))/(2 sqrt(sigma(1-sigma)))
 <= (X^(b-1)+X^(-1/2))/(2 sqrt(b(1-b))).
```

The positive c2=189/125 suffices since
`7*c2^2-16=47/15625>0`. Line zeros are covered as well, since c2>1 and
X^(b-1)>=X^(-1/2). The static sum is bounded by
sum 1/|rho|^2 <= r*A <= 8*A. All regrouping is of nonnegative terms.
Consequently F_b=X^b+7X^(1-b)+8 and
d_b=1+1/X-c2*(X^(b-1)+X^(-1/2)) have the asserted roles for every b.

I inspected the versioned primary [LLS v3 PDF](https://arxiv.org/pdf/1309.3595v3),
the residue expansions in Lemmas 2.1--2.3 and the character/induction
argument in Section 3. The source's GRH estimates require replacement by
the preceding paired estimates; the residue signs and gamma formulas
agree with the accepted local inputs. Lemma 3.1 supplies unconditional
prime-power corrections. Classical contour convergence and the
completed-L-function identities remain declared analytic inputs.

An in-memory HTTPS download of that PDF succeeded: 267062 bytes, SHA-256
`692b7fe38d883cf3503e247b0ebcd0c092c7e7267b06488adb9f40d45095b5a8`,
matching the frozen proof. This independently resolves the binary-hash
limitation recorded in the earlier reviews; it does not certify the
analytic foundations.

The four gamma errors have the required negative signs. Dropping their
negative series, using pi^2<10, 2/3<log 2<7/10, and gamma>1/2 gives, for
X>=64, the respective upper bounds

```text
Etilde_0 <= -91/12,   Etilde_1 <= -29/12,
E_0 <= -3193/3840,    E_1 <= -301/1280.
```

Here log 64 is between 4 and 21/5, (log X+1)/X decreases, and
1-1/X>=63/64. The coarse Euler-constant bound also follows from
gamma>=H_6-log 7 and the independently enclosed log 7<39/20, since
H_6=49/20. The inherited zeta constant |B_zeta|<231/10000 is an input.

## All subgroups, imprimitive corrections, and criterion

Suppose every prime p<X coprime to q lies in a proper H. A nonprincipal
character chi modulo q trivial on H exists by finite abelian duality.
Every positively weighted unit in S and T then has character value 1;
both sums agree with their principal-character versions and T>=0.
Let chi* be the inducing primitive character of conductor f>=3 and set
m=q/f, avoiding confusion with exponent r.

For t=log X, direct prime-power summation gives

```text
|S(chi)-S(chi*)| <= omega(m)*t^2/2,
|T(chi)-T(chi*)| <= (1-1/X)*U(m),
U(m)=sum_{p|m} log p/(p-1).
```

Only primes dividing q but not f actually contribute. Enlarging to every
p|m is safe, even when m and f share primes or m=1. For S, integrate the
decreasing function log p*(t-u log p) from 0 to t/log p. For T, use
1-p^k/X<=1-1/X and sum p^(-k)=1/(p-1).

The principal correction separately costs omega(q)*t^2/2. Hence

```text
Re S(chi*) >= S_zeta - (omega(q)+omega(m))*t^2/2
           >= S_zeta - omega(q)*t^2.
```

Using T>=0 and E_a<=0 in the transferred T identity gives

```text
d_b*A <= (1/2)(1-1/X)*(log(f/pi)+2U(m)).
log f + 2U(m) - log q
 <= sum_{p|m} (2/(p-1)-1)*log p <= log 2.
```

The p=2 term is log 2, p=3 contributes zero, and larger primes contribute
nonpositively; prime-power multiplicities only strengthen the saving.
Since 2<pi and L=log q>0, this implies A<=L/(2d_b) whenever d_b>0.
No step assumes log(f/pi)>=0, so f=3 is covered. Both S corrections and
the T correction have been charged.

Substitution into the zeta lower bound and primitive S upper bound yields
exactly the no-outside-prime implication

```text
1 <= (F_b/X)*(231/10000 + L/(2d_b))
     + ((L/(2d_b)+L/2+2)*t + 1 + omega(q)*t^2)/X.
```

The coefficients use log(2*pi)<2 and log(f/pi)<=L. Taking real parts is
sufficient for complex chi: its contradiction-range unit values are 1.
This uses no GRH estimate for a principal T sum. A prime equal to X has
zero weight in both kernels, so an upper bound below 1 proves ell<X,
including the possible integer endpoint X.

## Uniform strict subdomain and independent exact arithmetic

Set c=677/1000, y=c*L and X=y^r. For y>=7 and 15/2<=r<=8,

```text
F_b/X = 1/y + 7/y^(r-1) + 8/y^r
      <= 1/y + 7/y^6 + 8/y^7 < (1001/1000)/y,
d_b >= 1-c2*(1/y+1/y^3) >= 191/245 > 77/100,
X>=y^7>256,          t<=8 log y.
```

The exact slacks at y=7 are 47/4900 in the denominator bound and
60649/117649000 in `1001/1000-(1+7/7^5+8/7^6)`.
For q>=65536, log 2>2/3 gives y>2708/375>7.
Also omega(q)<=L/log 2<2L=2y/c.

After substituting these envelopes, the residual terms are positive
constant multiples of (log y)^j/y^a, with a>=6 and 0<=j<=2.
Their derivatives have sign j-a*log y<0 for y>=7. The zeta term decreases
as 1/y and the leading character term is constant. Evaluating at y=7,
with t<16, therefore bounds the entire unbounded range.

I reconstructed the five charged contributions directly with Fractions,
without importing the author's certificate function:

```text
zeta main:        33033/10000000
character main:  650/677
all linear logs: 1654304/6132924721
constant:        1/823543
omega*t^2:       512000/79648373
sum:             8499538701758399/8761321030000000 < 1
margin:          261782328241601/8761321030000000 > 0.
```

The error lies between 0.970120678451 and 0.970120678452. These decimal
figures are display bounds; every decision was an exact rational comparison.

For independent logarithms I used the exponential Taylor series, rather
than `verify/check.py`'s reduced-argument atanh series. For rational x>0,
let P_50=sum_{k=0}^{50} x^k/k!. For the arguments below,

```text
P_50 < exp(x) < P_50 + (x^51/51!)/(1-x/52).
```

Exact Fraction evaluation of the upper exponential at each proposed lower
logarithm, and the lower exponential at each upper logarithm, proved

```text
0.69314718 < log 2 < 0.69314719,
1.60943791 < log 5 < 1.60943792,
1.79175946 < log 6 < 1.79175947,
1.94591014 < log 7 < 1.94591015.
```

Each finite decimal denotes an exact rational with denominator 10^8.
The same procedure independently proved exp(2/3)<2. No floating-point
logarithm or fractional power was used for a certificate decision.

## Complete small range and exact sharpness

The all-group finite argument is unconditional. If every prime p<q
coprime to q belonged to H, factor each reduced representative a in
1,...,q-1 into primes. Those factors are all such primes, so every unit
would belong to H, contradicting properness. Thus ell(q,H)<q for every
proper H. This establishes the required composite-modulus statement
without subgroup enumeration or extrapolation from quadratic data.

For fixed r, the derivative of (c log q)^r/q has sign r-log q. It has
one interior maximum on [7,65536], and its minimum is at an endpoint.
The independent logarithms prove the lower endpoint using only integers:

```text
c*1.94591014 = 1.31738116478 > 1,
(c*1.94591014)^15 > 62 > 49=7^2.
```

Since r>=15/2, (c log 7)^r>7, including b=13/15. At the upper endpoint,
`c*16*0.69314718=7.50817025376>7` and `7^7=823543>65536`.
Therefore (c log q)^r>q on the entire interval. Combining with ell<q
and the analytic range proves strict coefficient c for every q>=7.

The exact coefficient comparisons were independently checked with the
opposite directed logarithms where required:

```text
c*1.60943791 > 1,
(c*1.60943792)^8 < 2,
(1.79175947/1.60943791)^8 < 5/2.
```

Thus 1<c log 5 and r<=8 imply (c log 5)^r<2, so C5>c.
The ratio comparison gives
`log 6/log 5 < (5/2)^(1/8) <= (5/2)^(1-b)`, hence C6>C5.
All powers involved have positive bases; the directions are preserved at
both parameter endpoints. Consequently both sharp bounds are strict for
every q>=7.

Repeated multiplication independently gave the complete unit groups:

```text
q=3, generator 2: 1,2;       q=4, generator 3: 1,3;
q=5, generator 2: 1,2,4,3;   q=6, generator 5: 1,5.
```

Every proper subgroup at q=5 excludes 2, so ell=2=(C5 log 5)^r.
At q=6 the only proper subgroup is {1}, and ell=5=(C6 log 6)^r.
C6>C5 makes its q=5 case strict. These facts prove exactly the claimed
equality sets, and force failure of every smaller positive coefficient
in the corresponding domain. The q=3,4 exact values remain separate.

For prime q>=5 the nonzero squares form a proper subgroup. Its least
positive nonresidue lies below q; if composite, its two smaller factors
would be nonzero residues by minimality, making their product a residue.
It is therefore prime. The equality at q=5 also forces sharpness in the
prime quadratic domain.

## Independent data, controls, and regression replays

I independently generated every prime below 65536 by the sieve of
Eratosthenes. For each prime q>=5 I marked all nonzero square residues
using the additive recurrence

```text
s=0
for a=1,...,(q-1)/2:
    s=(s+2*a-1) mod q
    square[s]=true
```

The first unmarked integer a>=2 is the least nonresidue; the sieve also
checks its primality. This route uses neither trial primality nor Euler
exponentiation nor a reciprocity routine. It shares no repository helper
with the author's direct algorithm.

For the 6539 primes q>=7 I checked ell<(c*B_q)^7 with exact rationals,
using B_7=19/10 and, for q>=11,
`B_q=(2/3)*floor(log_2 q)`, computed by integer bit length.
The exponential certificates above prove B_q<log q. All these bases
exceed 1, so these checks imply the bound for every r>=15/2.
At q=5 the independent data gives ell=2 and the sharp statement is exact.

Results: 6540 prime moduli, all checks passed, largest least nonresidue 31,
occurring only at q=31391. The complete frequency distribution was

```text
{2:3277, 3:1644, 5:826, 7:408, 11:212, 13:98,
 17:43, 19:22, 23:5, 29:4, 31:1}.
```

For ascending q, encode each row as ASCII `q,ell` followed by one LF,
with no header. The independent data SHA-256 is
`8da430f7ba3ffbfcf93b44e89197d65545dff10e620dee65d933b6712e468fa2`.
A subsequent computation using the author's trial/Euler helper produced
the same count and digest. These finite checks supplement the complete
all-subgroup proof; they do not certify that proof's infinite domain.

I separately invoked all eight negative controls and inspected their
actual ValueError reasons:

```text
c2=3/2                  -> pairing constant must dominate 4/sqrt(7)
c2=-189/125             -> pairing constant must dominate 4/sqrt(7)
y_min=6                 -> d(X) > 39/50
prime_c=677/1000        -> q=5 endpoint
general_c=341/500      -> q=6 endpoint
Legendre modulus 9      -> modulus must be prime and at least 5
theta=9/10              -> refined exponent interval
sharp beta=9/10         -> sharp pairing strip range
```

The sharp helper also rejected 13/15-1/10^9 and 7/8+1/10^9 at its range
guard. It accepted both closed endpoints, their midpoint 209/240, and
8748867/10000000, returning exactly the same displayed error. Its product
condition b(1-b)>=7/64 follows analytically from the checked interval.

The independent exponential logarithms also re-established the old
positive endpoint comparisons with exponent 799/100 at q=5,6,7, and the
0.682 obstruction at q=6. Separate Fraction substitution reproduced

```text
C=.678, d0=.78, power8: 241522181840005231/254054780070000000 < 1,
C=.683, d0=.78, power8: 483056762993653607/511856680790000000 < 1,
C=.678, d0=.77, power7: 29748536893681951/30709918470000000 < 1.
```

All documented commands were freshly replayed with bytecode writes
disabled, using `python3 -B`:

```text
research/zero-pairing/constants.py        exit 0
research/least-nonresidue/constants.py    exit 0; eight REJECT controls; 6540 primes
verify/check.py all                      exit 0
-m unittest discover -s tests            exit 0; 16 tests passed
```

The shared verifier and tests check their recorded Miller--Rabin claims.
The sharp least-nonresidue theorem is supported by the written argument
and the distinct exact computations above.

## Prior-response disposition and limits

The historical review files were read for scope and prior objections;
their current SHA-256 values are

```text
84ff33b94198b224425b50892c29c0cbe0eb9f0a243982bf78ede7f6eaeb5618  research/least-nonresidue/RECHECK.md
c75db68a3b80e6ebf38232a9298d0be16000898cd229a38045c68c485c28ca31  research/least-nonresidue/GUARD-RECHECK.md
7d5b5f4466471493c34f7331f8c4e408c6628131b03de35c480b1e9b876bf97d  research/least-nonresidue/RECHECK-THETA.md
```

The original H(7/8) review passed its mathematics and raised only the
negative-c2 guard issue. The response adding an explicit positive sign
check is accepted: the guard remains present, and the fresh negative
probe rejects at that guard. The targeted guard review's related-package
audit was not repeated. The theta review passed its own frozen extension;
its transfer is reconstructed here over the larger closed interval.
There are no unresolved prior objections. The single new wording note
above is nonblocking and was not silently corrected in frozen material.

H(b), H(7/8), and the Xu--Sang half-plane remain assumptions. No preprint
proof, Lean replay, kernel certificate, or numerical zero certification
is supplied. Classical Hadamard/zero identities, analytic validity of
the residue expansions and contour limits, and the inherited zeta
constant are declared dependencies. I checked the applicable signs and
parameter inequalities; I did not establish those analytic foundations
from first principles or certify arbitrary future helper changes.

The exact arithmetic runs use Python's standard rational/integer
implementation. Same-model fresh-context agreement and matching finite
data provide review evidence, not human or formal acceptance. Maintainer
review remains separate.

No further agents, installations, public posts, PR updates, or git
mutations were made. The sole created workspace file is this report,
written with native `apply_patch`. The frozen inputs and the accepted
dependencies were rehashed without changes before completion.
