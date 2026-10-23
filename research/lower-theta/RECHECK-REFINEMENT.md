Original idea: **Geoffrey Irving**.

# Independent recheck of the C=0.5272 refinement

**Verdict: PASS for the stated conditional refinement, with no required fix
or unresolved mathematical objection.** The frozen inputs support
C=659/1250, D=0 and n>=3317044064679887385961981, under H(8748867/10000000),
with witness exponent 10000000/1251133. They separately support the same C,
D and domain under H(7/8), with witness exponent 8. The smaller-theta bit
exponent remains exactly 12502266/1251133<10, with gap 9064/1251133.
Maintainer acceptance is separate.

Review date: 2026-10-23. Reviewer: a fresh Codex / gpt-6.1-sol context.
The task brief supplied the proposed constants, expected controls and prior
review summary. Thus this was a separate reconstruction, not a blind review
or a review by a different model. I did not use the parent's checker run as
evidence. I independently executed the changed checker after reconstructing
the arithmetic without either repository checker.

## Snapshot and scope

Worktree:
`/root/.t3/scratch/2026-10-23-fetch-https-discoveryathome-org-v0-7d492a7d/theta`.

Branch: `session/20261023-lower-theta`.
Published HEAD: `37b2326698c5c73f8a085d5035bd64743266983f`.
Accepted base: `d2bd5167a42b8256f1362640dc149057920e5db9`, confirmed to be
an ancestor of HEAD. The five frozen files were modified relative to HEAD;
HEAD alone therefore does not identify the reviewed refinement. Their
SHA-256 hashes below identify it.

I read AGENTS.md, DISCOVERY.md, the accepted frontier, the lower-theta
proof, checker and README, both current candidate records, and the changes
from published HEAD. I examined the prior report for its verdict, scope and
objection disposition. I inspected the shared substitution and logarithm code.
The accepted proof inputs, shared verifier and tests are unchanged from
the accepted base. All six artifact hashes listed in the frontier match
the local files. The frontier still accepts the older H(7/8), C=.529
result; it does not accept this contribution.

The historical [RECHECK.md](RECHECK.md) has no required fixes or unresolved
objections. Its C=.528 verdict and historical hashes are not evidence for
the new coefficients. Its file remains unchanged. The frozen proof, README
and candidate source fields correctly describe this refinement review as
pending at that snapshot and distinguish it from the old review.

## Uniform factor 28 and the new domain

For b=8748867/10000000, put r=1/(1-b). Exact subtraction gives

    r/2-3-99/100 = 797933/125113300 > 0,
    r-7-99/100   = 344733/125113300 > 0.

For b=7/8, both differences are 1/100. Also r<=8 in both cases.
The required integer comparison is exactly

    14883^99 > 28^100 * 500^99.

It proves Y^(99/100)>28 for Y=14883/500. For every y>=Y>1,
both y^(r/2-3) and y^(r-7) exceed 28: these powers increase with y,
and their exponents exceed 99/100. Consequently all three inequalities
in Section 6, equation (7), hold throughout the half-line:

    y^(-r/2)      <= 1/(28 y^3),
    y^(2-r)       <= 1/(28 y^5),
    r log y/y^(r-1) <= 8 log y/(28 y^6).

The third comparison also uses log y>0 and r<=8. This is a uniform
argument, not an endpoint evaluation of a fractional power.

I independently certified 1/6<log Y<17/5 by rational exponential-series
bounds. Hence (log y/y^6)'=(1-6 log y)/y^7<0 for every y>=Y.
It follows that a=34/(35Y^6) bounds log X/X^b uniformly.
Further, X=y^r>=Y^r>Y^7>256. Thus the pairing range X>=256
and the four gamma-sign ranges X>=64 remain satisfied everywhere.

For the denominator, dropping the positive 1/X in d(X) and using the
uniform half-power bound gives

    d(X) >= 1-(189/125)[1/Y+1/(28Y^3)]
         = 115895402389/122097755681 = Dmin > 0.

The direction is correct. Taking reciprocals therefore gives
A<=L/(2Dmin); it does not reverse the desired upper bound on A.
Likewise F(X)/X^b<=1+7s with s=1/(28Y^5).

## Refined coefficients and the static charge

I reconstructed the coefficients by eliminating b1 rather than calling
the author's certificate:

    alpha_need = (1+7s+a+Dmin*a)/(2Dmin),
    beta_need  = [231(1+7s)+18379a]/10000,
    gamma_need = 4/Dmin.

These give exactly the three fractions printed in Section 6:

    alpha_need =
      238168329447264162697001708275930457
      /452139580341872249446204481994840666,
    beta_need =
      17573285443376355449035050473
      /760748194917465671495023830000,
    gamma_need = 488391022724/115895402389.

Integer cross multiplication proves that each is strictly below its
candidate cap: alpha=13169/25000, beta=29/1250, gamma=843/200.
For orientation only, the respective positive cap slacks are about
1.58335e-6, 9.99972e-5 and .000932723. No floating value decides a check.

The coefficient collection has the correct signs. In the two S bounds,
A(F+log X) contributes b1(1+7s+a)L X^b and the conductor-log term
contributes at most (a/2)L X^b. The zeta F term and log(2pi) term give
beta_need. The remaining rA is bounded by 8b1 L. Enlarging these
subtracted coefficients weakens the contradiction inequality in the
required direction.

No residue identity changed. Using the unchanged elementary constants,
I recomputed the four rational sign bounds:

    E_0  <= -22947/25600,
    E_1  <= -34963/128000,
    Et_0 <= -4112241/500000,
    Et_1 <= -2841077/1000000.

Their stated uniformity for X>=64 remains applicable on the stricter
new domain. Since r<=8,

    r*zeta_b+1+Et_a < 8(231/10000)+1-284/100
                    = -2069/1250 < 0.

Dropping this nonpositive static charge justifies delta=0. It is not
an unaccounted positive error. Combining these comparisons with the
accepted residue/character argument yields precisely (T1r), with
w1=1 and y_min=14883/500, at both half-planes.

## Substitution on the entire n>=PSI_13 domain

Write L=log n, C=659/1250 and X=(CL)^r. Dividing (T1r) by X^b>0
gives exactly

    h_r(L) = (11/25000)L - 29/1250
             - (843/200) C^(1-r) L^(2-r).

Here r>2, so the positive tail being subtracted decreases on all L>0.
In fact

    h_r'(L) = 11/25000
              +(843/200) C^(1-r)(r-2)L^(1-r) > 0.

The applicability condition CL>=Y is also preserved as L increases.
Thus an endpoint certificate suffices for the entire half-line.

Without importing either checker, I certified

    56.461116276231780068816086067829
       < log PSI_13
       < 56.461116276231780068816086067830.

At this independent lower endpoint, y0=C*Llo exceeds Y by about
.000300500829394. Since r-1>=6 and y0>1, replacing the true tail
by (843/200)Llo/y0^6 enlarges it. Exact rational arithmetic gives

    g6 = (11/25000)Llo-29/1250-(843/200)Llo/y0^6
       > 41/25000 > 0.

Its display is .0016425490262551017. This proves the complete
n>=PSI_13 range for both hypotheses, without sampling n or y.
The independent bracket also strictly contains the shared verifier's
logarithm enclosure, as checked separately; the shared l0 is therefore
larger than Llo and satisfies the same inequality.

I inspected verify/check.py:103--174 rather than relying on its PASS.
Its m=b/(1-b)=r-1, slope=C*w1-alpha=11/25000 and reduced expression
agree with the algebra above. For D=delta=0 its tail-monotonicity test
reduces to 0<=(m-1)C*gamma*l0. Its endpoint replacement
y0^(-m)<=y0^(-floor(m)) is correct because y0>1.
The floors are 6 and 7 respectively. Independent endpoint displays
are .0016425490262551017 and .0016428796674939784; the shared report
prints .00164255 and .00164288. Its floating calculations only format
results or compute comparison metrics after the exact checks.

Both candidate records agree exactly with the proved template, C, D,
PSI_13, their respective b, and the proof path. The witness exponents,
bit exponent and gap are unchanged and exactly checked. The separate
Sorenson--Webster input applies strictly below PSI_13; the refined
theorem begins at PSI_13, so the two domains leave no gap.
The all-odd-composite bound is max(41,(C log n)^r).

## Positive and rejection controls

The changed checker retains the complete old C=.528 claim in memory
and checks it at both half-planes. I independently reconstructed both
positive endpoints, about .0022071628049659116 and .002207490935421254.

I independently checked the reason for each of the ten historical
rejections: old-template C=.5279 fails its endpoint certificate;
C=.5275 has negative slope; y_min=30 misses the old cutoff;
9.9927 rounds the exact bit exponent down; alpha=.52753 is below
the old required coefficient; c2=3/2 is too small; negative c2 has
the wrong sign; and copied powers 4,6,7 violate their directed exponent
requirements at the smaller theta. The separate rational check against
the old logarithmic cap also remains valid; it is not an extra counted
rejection control.

The three new controls check the refinement itself. The independently
certified *upper* logarithm bound proves (.5271)log PSI_13<Y.
Also .52675<alpha_need, and

    Y^99 < 29^100.

These are meaningful failures of this fixed certificate. The factor29
probe rejects the chosen 99/100 integer-power comparison; it does not
establish that every possible factor29 argument is impossible.
Similarly, an old-template rejection of C=.5279 says nothing against
the new C=.5272 theorem. Altering the coefficient certificate changes
the inequality under review.

My own run of research/lower-theta/constants.py under Python 3.13.5
exited 0, passed both current candidates, retained both old positives
and rejected exactly thirteen probes with the expected reasons.
That run supplements the independent derivation; it is not its basis.

## Assumptions, issues and limits

There are no required corrections to the frozen refinement and no
unresolved prior objections. The source-status text is appropriate for
the frozen bytes; this report does not edit or retroactively upgrade it.

The assumptions remain explicit: H(theta) is taken directly for the
smaller-theta theorem, and H(7/8) separately for the backport. Each covers
all required Dirichlet characters and zeta, permitting principal poles.
The accepted handling of imprimitive characters via Euler factors
adds no zeros in the relevant right half-plane. I checked these
declarations against the local template/frontier and accepted inputs.
I did not newly audit the external preprints or use H(7/8) as a proved
route to H(theta).

The inherited classical inputs include the functional equations,
Hadamard real-part identities and convergent regrouping of zero sums,
the unconditional pre-GRH residue identities cited from LLS,
the contour shifts and limiting arguments behind them, the subgroup
reduction and primitive-character passage, the elementary constants in
Section 3, and the small-n Sorenson--Webster theorem. This refinement
changes the directed numerical envelopes, not these inputs.

Neither half-plane hypothesis, Xu--Sang's proof or analytic inputs,
OpenAI's imported inputs, a Lean replay, classical contour foundations,
exhaustive pseudoprime minimality, optimality, nor bit-cost foundations
is newly proved here. I did not perform zero computations or build a
Miller--Rabin implementation. The unchanged full verifier/small-n run,
unittest suite and accepted zero-pairing checker were not gratuitously
rerun; the previous report records their baseline results. No new result
is inferred from those historical runs.

This is same-model AI review. A fresh context and different calculation
method reduce direct reuse of an error but do not eliminate correlated
reasoning, supplied-target bias, or implementation mistakes. It is not
human review, formal verification, or maintainer acceptance.

No public post, PR-content edit, git mutation, installation, further
delegation or frozen-input edit was performed. The only repository file
written by this review is RECHECK-REFINEMENT.md.

## Reproducible independent calculation

From the repository root, run the following without Python optimization
(`-O`). It imports no repository module. Decimal log endpoints are merely
candidates: the exponential Taylor bounds certify them by exact rational
comparisons. For t>=0, the first omitted term after degree 256 and the
ratio t/258 bound the whole remaining exponential tail geometrically.

```sh
PYTHONDONTWRITEBYTECODE=1 python3 - <<'PY'
from fractions import Fraction as F
from pathlib import Path
import json

def exp_interval(t, terms=256):
    # For t >= 0, the first omitted term starts a geometric upper bound.
    t = F(t)
    assert 0 <= t < terms + 2
    term = total = F(1)
    for j in range(1, terms + 1):
        term = term * t / j
        total += term
    ratio = t / (terms + 2)
    omitted = term * t / (terms + 1)
    return total, total + omitted / (1 - ratio)

N = 3317044064679887385961981
Llo = F("56.461116276231780068816086067829")
Lhi = F("56.461116276231780068816086067830")
# exp is increasing. These rational comparisons certify the log bracket.
assert exp_interval(Llo)[1] < N < exp_interval(Lhi)[0]
Y, C = F(14883, 500), F(659, 1250)
assert exp_interval(F(1, 6))[1] < Y < exp_interval(F(17, 5))[0]
assert 14883**99 > 28**100 * 500**99
assert 14883**99 < 29**100 * 500**99

c = F(189, 125)
assert c > 0 and 7*c*c > 16
assert 256**11 > 7**30 and Y**7 > 256
for b in (F(8748867, 10000000), F(7, 8)):
    r = 1 / (1-b)
    assert F(13, 15) <= b <= F(7, 8)
    assert b/(1-b) <= 7 and b-F(1, 2) >= F(11, 30)
    assert r/2-3 > F(99, 100) and r-7 > F(99, 100)
    assert 7 < r <= 8
    print("directed exponent slacks", b,
          r/2-3-F(99,100), r-7-F(99,100))

# Independently eliminate b1 from the coefficient formula.
d = (28*Y**3 - c*(28*Y**2 + 1)) / (28*Y**3)
s, a = 1/(28*Y**5), F(34, 35)/Y**6
alpha = (1+7*s+a+d*a)/(2*d)
beta = (231*(1+7*s)+18379*a)/10000
gamma = 4/d
assert d == F(115895402389, 122097755681) > 0
assert alpha == F(238168329447264162697001708275930457,
                  452139580341872249446204481994840666)
assert beta == F(17573285443376355449035050473,
                 760748194917465671495023830000)
assert gamma == F(488391022724, 115895402389)
A, B, G = F(13169, 25000), F(29, 1250), F(843, 200)
for name, need, cap in (("alpha",alpha,A),("beta",beta,B),("gamma",gamma,G)):
    cross = cap.numerator*need.denominator-need.numerator*cap.denominator
    assert cross > 0
    print("required",name,need,"cap slack (display)",float(cap-need))

# Old signed residuals are uniform for X>=64; Y^r>256 is stricter.
e0 = -F(693,1000)-F(577,2000)*F(63,64)+F(516,100)/64
e1 = -F(577,2000)*F(63,64)+F(694,1000)/64
t0 = F(42,100)-F(4158,1000)**2/2
t1 = F(124,100)-(F(693,1000)+F(577,2000))*F(4158,1000)
assert (e0,e1,t0,t1) == (-F(22947,25600),-F(34963,128000),
                        -F(4112241,500000),-F(2841077,1000000))
assert max(e0,e1) < 0 and max(t0,t1) < -F(284,100)
assert 8*F(231,10000)+1-F(284,100) == -F(2069,1250) < 0

assert C-A == F(11,25000)
y0 = C*Llo
g6 = (C-A)*Llo-B-G*Llo/y0**6
assert y0 > Y and g6 > F(41,25000)
print("independent log bracket", Llo, Lhi)
print("y0-Y (display)",float(y0-Y),"common g6 (display)",float(g6))

root = Path.cwd()
claims = (("explicit-t1-lower-theta.json",F(8748867,10000000)),
          ("explicit-t1-paired-refinement-7-8.json",F(7,8)))
for name,b in claims:
    claim = json.loads((root/"candidates"/name).read_text())
    assert claim["kind"] == "explicit-witness-bound"
    assert F(claim["theta"]) == b
    assert F(claim["C"]) == C and F(claim["D"]) == 0 and claim["n0"] == N
    expected = dict(w1=F(1),alpha=A,beta=B,gamma=G,delta=F(0),y_min=Y)
    assert {k:F(v) for k,v in claim["template"].items()} == expected
    assert claim["proof"] == "research/lower-theta/PROOF.md"
    assert "refinement review pending" in claim["source"]
    r = 1/(1-b)
    m = r-1
    assert m > 1 and (m-1)*C*G*Llo > 0  # shared derivative condition
    assert 2-r < 0                       # true tail decreases for all L>0
    floor_m = m.numerator//m.denominator
    g = (C-A)*Llo-B-G*Llo/y0**floor_m
    assert g > 0
    print("current candidate",name,"floor",floor_m,"endpoint (display)",float(g))
    old_C,old_A,old_G = F(66,125),F(10551,20000),F(4221,1000)
    assert old_C*Llo > 29
    old_g = (old_C-old_A)*Llo-B-old_G*Llo/(old_C*Llo)**floor_m
    assert old_g > F(2207,1000000)
    print("old positive control",b,"endpoint (display)",float(old_g))

# Independently check the reasons for all thirteen deliberate rejections.
old_d = 1-c*(F(1,29)+F(1,29**3))
old_s,old_a = F(1,29**5),8*F(33673,10000)/29**6
old_alpha = (1+7*old_s+old_a+old_d*old_a)/(2*old_d)
old_C,old_A,old_G = F(66,125),F(10551,20000),F(4221,1000)
bad_C = F(5279,10000)
bad_g = (bad_C-old_A)*Llo-B-old_G*Llo/(bad_C*Llo)**6
assert bad_g < 0                              # 1: old endpoint certificate
assert F(5275,10000)-old_A < 0                 # 2: old slope
assert old_C*Lhi < 30                         # 3: old cutoff
r = F(10000000,1251133)
exponent = r+2
assert F("9.9927") < exponent                 # 4: rounded exponent
assert F(52753,100000) < old_alpha            # 5: old alpha
assert 7*F(3,2)**2 < 16                       # 6: pairing size
assert -c < 0                                # 7: pairing sign
assert 4 > r/2                               # 8: copied half power
assert 6 > r-2                               # 9: copied pair power
assert 7 > r-1                               # 10: copied log power
assert F(5271,10000)*Lhi < Y                  # 11: new cutoff
assert F(2107,4000) < alpha                   # 12: new alpha
assert Y**99 < 29**100                       # 13: factor29 certificate
# An extra old-cap sign check, outside the count of thirteen:
assert exp_interval(F(336,100))[1] < 29       # ln29 > 3.36
assert r*(1+(8-r)*F(336,100)) > 8
assert exponent == F(12502266,1251133)
assert 10-exponent == F(9064,1251133) > 0
print("exact exponent",exponent,"gap",10-exponent)
print("PASS independent reconstruction: both candidates, old positives, 13 control reasons")

PY
```

The observed final line was
`PASS independent reconstruction: both candidates, old positives, 13 control reasons`.

The separate shared-enclosure comparison is reproducible as follows.
This imports the shared function only to compare its output with the
already independently certified interval.

```sh
PYTHONDONTWRITEBYTECODE=1 python3 - <<'PY'
from fractions import Fraction as F
from pathlib import Path
import sys
sys.path.insert(0, str(Path("verify").resolve()))
import check
lo, hi = check.ln_bounds(3317044064679887385961981)
a = F("56.461116276231780068816086067829")
b = F("56.461116276231780068816086067830")
assert a < lo < hi < b
assert sys.flags.optimize == 0
print("Shared log enclosure lies strictly inside the independent exp-certified bracket.")
PY
PYTHONDONTWRITEBYTECODE=1 python3 research/lower-theta/constants.py
```

## Exact reviewed SHA-256 hashes

The five frozen inputs:

```text
91840380ddf53c710603a195f1c19677c88f2c84c35dd3a5abee14145a93cb4c  research/lower-theta/PROOF.md
a71dedb89a3905c6949872dada4734e6cca91c94a6d2889411b3a96db83dffed  research/lower-theta/constants.py
00a77e63dda1bf4b440b4b1d29ab3d69ca77a7a92abc4fa253ea412ecc86a0bc  research/lower-theta/README.md
9cee05765e401355c9306d8b63246267c7ebf56dc6dcc6c2d733b717c033d169  candidates/explicit-t1-lower-theta.json
460de409df976b030efa56315a6d32e5fa7171551ee33a08f0f752ae77400a39  candidates/explicit-t1-paired-refinement-7-8.json
```

Guidance, historical report and supporting input identities:

```text
e8f93ce38983d792791c3f9ad9b8b0a367668b3b7b945b071b6f360c45babd62  AGENTS.md
e603c2aaf4b9c692b315213f6c7dd5aebdfba5932e67155e53c76a6590ec4ddf  DISCOVERY.md
9ca629138c133ac8547efba9b47f4d862ae82e7079c4da0998961d8fa5c964a4  discover/frontier.json
6810693f6c701557ac23c99f2068a599446ad83499f33458fc939e819527f3b9  research/lower-theta/RECHECK.md
ace2b055b5279284d04d37b6c6dde77af86088245846700c502effb3e812e709  verify/check.py
ba252ae554ac3f4ca372b692ef6ed7966772716dfa57c5b65ed22ae84fe5a1f1  verify/mr.py
824af09db62887a04107e72f9aafb56345aef45c1ea3ccf6499956d6896e914c  research/zero-pairing/PROOF.md
b71772dee37a2b068677c2800c2dce6d0737a94d03380f47b2f9d87ec6e610a7  research/zero-pairing/constants.py
abd066b2d27961e93ae007e5fb8897b5a841aff875b24af3eb0216d73bed8cbb  research/first-explicit-t1/PROOF.md
91343a3289cccfd69b022478412e44d53fe1354f7808da8e24c392b9e1be21f5  docs/template-T1.md
09b128dc0febdd15768b00c12fad6a4ec4ce4aa8cba774d6721b9f80675f2c8e  docs/verifier.md
1e5f766a3b3c39c9d03263056cf636a1b06c8f5e2ed9d3e1c8f1d1e2926b6082  tests/test_check.py
```

Recompute the frozen hashes from the repository root:

```sh
sha256sum research/lower-theta/PROOF.md research/lower-theta/constants.py \
  research/lower-theta/README.md candidates/explicit-t1-lower-theta.json \
  candidates/explicit-t1-paired-refinement-7-8.json
git rev-parse HEAD
git status --short
git diff --name-only d2bd5167a42b8256f1362640dc149057920e5db9 -- \
  verify tests research/zero-pairing research/first-explicit-t1
```

The final command had empty output. Before this review artifact was added,
git status listed exactly the five frozen modifications; the report is
the sole additional file. The five frozen hashes and HEAD were rechecked
after writing the report.
