Original idea: Geoffrey Irving.

# Independent mathematical recheck, ROUND2: threshold 15

**Verdict: PASS for the threshold-15 conditional theorem at the hashes below.**
I found no mathematical correction or required code/documentation fix. Section 10
extends both L-value bounds, the stated class-number corollary, and the factored
imprimitive extension to their stated conductor range. This is a fresh-context,
same-model AI review by Codex on 2026-10-23, not human review, formal verification,
maintainer acceptance, or a proof of H(7/8).

I read `AGENTS.md`, `DISCOVERY.md`, the package proof, certificate, README and
ROUND1 report, and the relevant accepted analytic inputs. I independently
reconstructed the changed estimates and recomputed their constants with a
different logarithm series. Executing the author's checker was an additional
check. The source-research context, parent checks, ROUND1 PASS, and earlier
shared-verifier/test results were not counted as verification of this refinement.
There were no unresolved ROUND1 objections to carry forward. The earlier
negative-c2 guard correction concerns the certificate's input validation; it is
not evidence for the new analytic range.

Reviewed worktree: `lone/`, branch `session/20261023-lone`. Published
[PR #13](https://github.com/discoveryathome/miller-rabin/pull/13) head and current
local HEAD: `f41ba0a120bca88406331a46027aa1500b714d49`.
Accepted upstream base: `d2bd5167a42b8256f1362640dc149057920e5db9`.
The refinement was uncommitted: only `PROOF.md`, `constants.py`, and `README.md`
were modified at review start. This verdict applies to their actual frozen
bytes, not to the published head alone. Maintainer review remains pending;
PR CI status was not refreshed or certified by this review.

## Conclusion and domains checked

Assume H(7/8), explicitly including zeta. For every primitive Dirichlet character
of conductor q with `L=log q>=15`, put

    M(q) = exp(gamma)(8 log log q+2).

The proof establishes

    zeta(2)/M(q) <= |L(1,chi)| <= M(q),    zeta(2)=pi^2/6.

The range is the whole closed half-line `L>=15`; it is not a sample of
conductors or zero heights. Primitive principal characters have conductor 1
and are excluded. The theorem and README explicitly make no claim for smaller
primitive conductors.

For a negative fundamental discriminant `-q` in this range, q>4 and the
class-number formula is `h(-q)=sqrt(q)L(1,chi_-q)/pi`, with positive real
L-value. Thus the stated bounds are exactly

    pi sqrt(q)/(6M(q)) <= h(-q) <= M(q)sqrt(q)/pi.

For a nonprincipal imprimitive character modulo Q induced by primitive chi*
of conductor f, the extension retains the exact factors

    L(1,chi)=L(1,chi*) product_{p|Q, p not dividing f}(1-chi*(p)/p).

Each factor has modulus between `1-1/p` and `1+1/p`. The threshold is
`log f>=15`, not a threshold merely on Q. Primes already dividing f introduce
no extra factor, even when their exponents in Q increase. Section 8 retains
both products; there is no product-free imprimitive claim.

## Analytic inputs and the changed application

I checked the relevant pre-GRH residues in the primary
[LLS v3 source](https://arxiv.org/src/1309.3595v3) and its
[23-page versioned PDF](https://arxiv.org/pdf/1309.3595v3), stamped 8 December
2016. In particular, source lines 500-546 fix the real-B identity; 565-566
fix the zeta zero-term sign; 593-595 and 639-640 give the integrated kernels;
and 1320-1324 give the even-power correction. Equation (1.3), PDF page 4,
fixes the class-number normalization. I used these identities before their
RH estimates, not the published RH thresholds or final numerical bounds.

The accepted local inputs remain F1-F2 and Lemma 0 in `first-explicit-t1`,
and Lemma 0' part 2 in `zero-pairing`. Their bytes match the accepted base
and frontier artifact hashes. The historical draft banners do not override
that accepted record. Their witness-theorem numerical coefficients are not
needed here. In particular, the same-character symmetry for complex chi is
`rho -> 1-conjugate(rho)`, not conjugation alone. With
`b=-Re B(chi)=sum Re(1/rho)`, H gives

    1/8 <= Re rho <= 7/8,
    sum 1/|1-rho|^2 = sum 1/|rho|^2 <= 8b,
    |Z_chi(x)| <= c(x)b,
    c(x)=(189/125)(x^(-1/8)+x^(-1/2)).

The coefficient is positive and `7*189^2-16*125^2=47>0`. The same bounds apply
to zeta. The b used throughout is the real-part quantity, not |B(chi)|.

For u>=1, `|rho-u|>=|rho-1|`. Therefore the absolute zero integral, before
its outside factor 1/t, is at most

    8b integral_1^infinity x^(7/8-u) du = 8b/(y t),
    y=x^(1/8), t=log x.

This gives `8b/(y t^2)` after that division, including the endpoint u=1.
It supplies the absolute domination for the integrated sum and limit here;
the same calculation gives `8b_z/(y t^2)`. The trivial-zero bounds remain
`2/(x t^2)` for chi and `1/(3x^3 t^2)` for zeta. The Laurent pole main term
of the zeta calculation is unchanged. None of these facts requires y=L.

Eliminating the conductor main term from the two exact character identities
still gives (2.10), with correction signs

    [b/x + Re Z_chi + Q/(2x) + g_a-E_a]/t,    Q=log(q/pi).

Together with the unchanged gamma estimate this yields, for general x,

    J_chi = b[c(x)+1/x+8/(yt)] + [Q/2+t+2]/x + 2/(xt),
    J_z   = b_z[c(x)+8/(yt)] + log(2pi)/x + 1/(3x^3t),
    F_z <= log t+gamma-1/t+J_z/t.

The `-1/t` is retained. I use the unchanged finite Euler minimum for complex
phases, including p=2, proved in Section 4 and independently checked in
ROUND1. I checked its applicability here: its hypotheses require only x>=100,
and the new x is larger. Its lower correction is `log zeta(2)-2/sqrt(x)`.
Thus with `x=y^8`, its contribution to a common numerator is exactly
`2t/sqrt(x)=2t/y^4`. No RH-only lower bound for T_chi or gamma cancellation
from LLS Section 5 has been imported.

## Sharpened zeta bound and real-B ratio

Set `a=31/50`, `y=aL`, `x=y^8`, `t=8log y`, and `L0=15`. Independently,
using the positive logarithm series below, I obtained

    446/25 < 8log(93/10) < 17841/1000,
    log(50/31) > 239/500,
    H_100-log101 > 57/100.

The margins to these rounded endpoints are approximately 0.0001152013,
0.0008847987, 0.00003580094, and 0.002257001, respectively; all decisions
were rational. The elementary lower bound on gamma follows because
`H_N-log(N+1)` increases strictly to gamma.

The accepted first-T1 F1 records `b_z<=231/10000` and the unconditional exact
identity `b_z=1+gamma/2-log(4pi)/2`. I did not infer the strict decimal bound
from its displayed digits. The independent command below certifies it using
a harmonic upper bound on gamma and alternating Machin bounds on pi. It gives
the rigorous rational upper bound displayed as `0.02309591704970828439...`,
strictly below 231/10000. In fact the accepted non-strict bound already
suffices for the error charge used here.

For that independent upper bound, if `A_N=H_N-log N`, then

    A_N-gamma
      = sum_{n=N}^infinity [log(1+1/n)-1/(n+1)]
      > (1/2) sum_{m=N+1}^infinity m^(-2)
      > 1/[2(N+1)].

The first inequality follows by writing each summand as
`-log(1-v)-v`, `v=1/(n+1)`, and using its positive series. Hence
`gamma<H_1000-log1000-1/2002`. Machin's identity and alternating arctangent
remainders give the pi enclosure used in the command, without a float input.

Now the exact zeta identity (3.1) has both `-Z_z` and a negative trivial-zero
series. Dropping the latter is valid for an upper bound. Since c decreases,
for x>=256 its remaining positive charge is bounded by

    3/256+(189/125)(1/2+1/16)(231/10000)
      = 313653/10000000 < 7/100.

Together with gamma>57/100 and log(2pi)<3 this proves
`T_z<t-3/2` with the correct sign. This step uses H for zeta through its
paired zero bound. Also `x>256>100` throughout the new range, so the unchanged
`E_a<=0` bounds apply. From (2.2), `-T_chi<=T_z`, and `0<Q<=L`,

    b <= (L/2+t-3/2)/d(x),    d(x)=1+1/x-c(x).

Put `c0=(189/125)(1/y0+1/y0^4)`, `y0=93/10`. Then

    d(x) >= 1-c0 = D0 = 57989077/69264075 > 0.

The derivative of `(t-3/2)/L` is `(19/2-t)/L^2<0`. Bounding its numerator
ratio at 15 and its positive denominator below by D0 gives

    b/L <= B0 = [1/2+(17841/1000-3/2)/15]/D0
              = 22017664161/11597815400.

This does not assume that b itself decreases, or require monotonicity of the
full d(x). The increasing lower bound `1-c(x)` suffices.

## Uniform common budget, with every power of a retained

Define `K=J_chi+J_z+2t/y^4`. Substitution of Q<=L and log(2pi)<3 gives

    K <= (b+b_z)[c(x)+8/(yt)]
         +[b+L/2+t+5]/x + 2/(xt) + 1/(3x^3t) + 2t/y^4.

The constant 5 is exactly the gamma allowance 2 plus the log(2pi) allowance 3.
No replacement of b_z by 1/2 has been made in this refined budget.

The uniform endpoint substitutions are justified term by term:

- `bc=(b/L)(Lc)`, where `Lc=(189/125)(1/a+1/(a^4L^3))` decreases.
  Consequently `bc<=B0*15*c0`. Bounding b and c separately without their
  compensating L factors would not supply this uniform argument.
- `8b/(yt)=8(b/L)/(at)<=8B0/(a*t_-)`. This explicitly retains the factor 1/a.
- `b_z c<=z c0` and `8b_z/(yt)<=8z/(y0*t_-)`, with z=231/10000.
- `b/x<=B0/(a^8L^7)` and `L/(2x)=1/(2a^8L^7)` decrease. For the t/x term,
  `(t/L^8)'=L^(-9)(8-8t)<0`. The constant/x term also decreases.
- `1/(xt)` and `1/(x^3t)` decrease since x and t increase positively.
- `t/y^4=t/(a^4L^4)` decreases because its derivative has sign `8-4t<0`.

All these signs hold at and above L=15 since `t>t_-=446/25>17`. They also
justify the stated monotonicity of t/L and t/L^4. Thus evaluating these
majorants at 15, using t_- in denominators and t_+ in numerators, increases
each nonnegative error. The eight resulting contributions in (10.5) are:

| Contribution | Decimal display only |
|---|---:|
| `B0*15*c0` | 4.63548035637815032 |
| `8B0/(a*t_-)` | 1.37308840138763442 |
| `z*c0` | 0.00376028199033915 |
| `8z/(y0*t_-)` | 0.00111384348329235 |
| `(15B0+15/2+t_++5)/x0` | 0.00000105109707536 |
| `2/(x0*t_-)` | 0.00000000200341793 |
| `1/(3x0^3*t_-)` | 1.06633368832733e-25 |
| `2t_+/y0^4` | 0.00476998918831860 |

The exact sum and margin are

    K0 = 5113764377742555010523829662740392050354129097905056152508533169
         /849714623146054389860120518677886715592305851100098537264125000,

    603/100-K0
       = 10014799828152960332697064887264844667475184228538027194140581
         /849714623146054389860120518677886715592305851100098537264125000.

Thus `K<=K0=6.018213925528228137...<603/100`, with positive margin
`0.01178607447...`. All residuals retain `x0=(a*15)^8`, `x0^3=(a*15)^24`,
and `y0^4=(a*15)^4`; no power of a was discarded. The two integrated zero
errors retain their extra 1/t in K, hence 1/t^2 in the logarithmic errors.

## Exponential bridge and the endpoint

The upper Euler envelope and the lower one with its charged tail imply

    log |L(1,chi)| <= log t+gamma+(K-1)/t,
    log(1/|L(1,chi)|) <= log t+gamma-log zeta(2)+(K-1)/t.

Therefore k=503/100 is valid in both errors. For `g(t)=t(exp(k/t)-1)`,

    g'(t)=exp(k/t)(1-k/t)-1 < 0    (t>0).

Indeed `exp(s)(1-s)` decreases from 1 for s>=0, since its derivative is
`-s exp(s)`. For 0<=s<3, `n!>=2*3^(n-2)` for n>=2 gives the positive-series
bound

    exp(s) <= 1+s+s^2/[2(1-s/3)].

Here `k/t_-<3`, so decreasing g and that series bound give

    g(t) <= k+k^2/[2t_-(1-k/(3t_-))]
          = 5637121/969800 < 728/125.

The rational slack is `54971/4849000>0`. Crucially, the logarithm is bounded
in the sufficient direction:

    728/125 = 2+8*(239/500) < 2+8log(50/31).

Since `t=8log L-8log(50/31)`, this proves

    t exp(k/t) < 8log L+2.

Exponentiating the two logarithmic inequalities gives the claimed M(q)
and zeta(2)/M(q) bounds. The strict rational enclosures hold at L=15 itself;
no limiting argument excluding that endpoint, or smaller-conductor
enumeration, is needed.

## Independent exact reproduction

The following standard-library command was executed successfully. It imports
neither the author's certificate nor `verify/check.py`. It uses the positive
series `log r=sum (1-1/r)^j/j`, after reduction to 1<=r<=2, rather than the
author's atanh implementation or ROUND1's alternating-log decomposition.
Its rational tail is at most `u^(N+1)/[(N+1)(1-u)]`. The budget is regrouped
as character, zeta, and Euler-tail contributions. All assertions use Fractions.

Run from `lone/`:

```sh
python3 -B - <<'PY'
from fractions import Fraction as F
from functools import lru_cache

@lru_cache(None)
def unit_log(r):
    assert 1 <= r <= 2
    u, n = 1-1/r, 96
    lo = sum((u**j/j for j in range(1, n+1)), F(0))
    return lo, lo + u**(n+1)/((n+1)*(1-u))

def log_bounds(r):
    r, k = F(r), 0
    assert r >= 1
    while r > 2:
        r /= 2
        k += 1
    lo, hi = unit_log(r)
    l2, u2 = unit_log(F(2))
    return lo+k*l2, hi+k*u2

def atan_bounds(v, n=12):
    s = sum(((-1)**j*v**(2*j+1)/(2*j+1)
             for j in range(n)), F(0))
    nxt = (-1)**n*v**(2*n+1)/(2*n+1)
    return min(s, s+nxt), max(s, s+nxt)

l, a, z, c2 = F(15), F(31,50), F(231,10000), F(189,125)
y, tm, tp = a*l, F(446,25), F(17841,1000)
x = y**8
assert x > 256 and tm > F(19,2)
assert c2 > 0 and 7*c2*c2 > 16
lo, hi = log_bounds(y)
assert tm < 8*lo < 8*hi < tp
log_inv_a_lo = log_bounds(1/a)[0]
assert log_inv_a_lo > F(239,500)
H100 = sum((F(1,j) for j in range(1,101)), F(0))
assert H100-log_bounds(101)[1] > F(57,100)
assert log_bounds(2)[1] < F(7,10)
assert F(9,2) < log_bounds(100)[0] < log_bounds(100)[1] < 5
assert log_bounds(8)[1] < 3

p5lo, p5hi = atan_bounds(F(1,5))
p239lo, p239hi = atan_bounds(F(1,239))
pi_lo, pi_hi = 16*p5lo-4*p239hi, 16*p5hi-4*p239lo
assert F(31415926535,10**10) < pi_lo < pi_hi < F(31415926536,10**10)
H1000 = sum((F(1,j) for j in range(1,1001)), F(0))
gamma_hi = H1000-log_bounds(1000)[0]-F(1,2002)
bz_hi = 1+gamma_hi/2-log_bounds(4*pi_lo)[0]/2
assert bz_hi < z
charge = F(3,256)+c2*F(9,16)*z
assert charge == F(313653,10000000) < F(7,100)

c0 = c2*(1/y+1/y**4)
D0 = 1-c0
B0 = (F(1,2)+(tp-F(3,2))/l)/D0
assert D0 == F(57989077,69264075) > 0
assert B0 == F(22017664161,11597815400)
Jchi0 = B0*l*(c0+1/x+8/(y*tm)) + (l/2+tp+2)/x + 2/(x*tm)
Jz0 = z*(c0+8/(y*tm)) + 3/x + 1/(3*x**3*tm)
K0 = Jchi0+Jz0+2*tp/y**4
assert K0 == F(
    5113764377742555010523829662740392050354129097905056152508533169,
    849714623146054389860120518677886715592305851100098537264125000)
assert K0 < F(603,100)
k = F(503,100)
assert 0 < k/tm < 3
bridge = k+k*k/(2*tm*(1-k/(3*tm)))
assert bridge == F(5637121,969800) < F(728,125)
assert F(728,125) == 2+8*F(239,500) < 2+8*log_inv_a_lo
assert F(728,125)-bridge == F(54971,4849000)
print('Independent refined logarithm, zeta, budget and bridge checks PASS')
print('K0 =', K0)
print('603/100-K0 =', F(603,100)-K0)
print('bridge =', bridge)
PY
```

The positive series and alternating arctangent tails justify the enclosures;
no displayed decimal is used to make a decision. Machin's identity here is
`pi=16 atan(1/5)-4 atan(1/239)`, obtainable by the tangent addition formula
with its angle in the correct quadrant.

## Author checker, controls, and documentation

I ran `python3 -B research/l-one-bounds/constants.py`: exit 0, the exact K0
and margin above, bridge `5637121/969800`, p=2 margin `17/7200`, all six
rejections, and `all constants and algebraic controls pass`. I also invoked
each control separately and checked its actual ValueError reason:

| Changed input | Rejection actually exercised |
|---|---|
| Baseline c2=3/2 | `pairing constant must dominate 4/sqrt(7)` |
| Baseline c2=-189/125 | Same guard, including the required positive sign |
| Refined L_min=14 | `refined t endpoint enclosure` |
| Shifted multiplier=2 | `off-line reciprocal-square envelope` |
| p=2 h bound=1/500 | `positive p=2 minimum envelope` |
| Refined additive=1 | `refined additive envelope` |

In particular, the threshold-14 control uses the fixed t_- and t_+ pinned for
L_min=15. Its rejection means that this certificate's endpoint enclosure
fails; it does not establish that a different certificate could not prove a
theorem at 14. The formal-pair ratio 50/7 is an algebraic obstruction to a
strip-only constant 2, not an assertion about actual zeros. The p=2 control
deliberately weakens an error bound, not a character counterexample.

The retained baseline default is still a positive control:
`budget_certificate()` returns `(286849/108000,1151/108000)`. The current six
controls use the refined threshold and refined additive test; the old
baseline threshold-16 control is no longer used. The proof, script and README
agree on that meaning and on the new conductor threshold. The historical
ROUND1 report correctly remains pinned to threshold 32 and its earlier
snapshot; the current docs explicitly said that this separate review was
pending at the frozen hashes.

The earlier 16 shared tests and Miller--Rabin claim checks were not rerun in
this round and are not evidence for this L-value extension. No new classical
analytic theorem is certified by a successful arithmetic script.

## Exact reviewed bytes

SHA-256 values below were checked against native local reads. The four package
inputs remained unchanged through the review. Paths are relative to `lone/`.

| Path | SHA-256 |
|---|---|
| `research/l-one-bounds/PROOF.md` | `96883f36baddc5f9098195d48094251632c1fb3534bf4ae72cd3a5ed780d61c0` |
| `research/l-one-bounds/constants.py` | `b0062eb9f2f92b414c85ca85dbd561808ca4870a7125378fc56caf6c202e1ea5` |
| `research/l-one-bounds/README.md` | `601c35b9a930bab403deaa059b4238de2f802f41ac27d792e93d3ac3243d231e` |
| `research/l-one-bounds/RECHECK.md` | `f2ba422870a3cc90b44d819dc3bdb4cfef67e92a77707aef08e7b81747149037` |
| `research/first-explicit-t1/PROOF.md` | `abd066b2d27961e93ae007e5fb8897b5a841aff875b24af3eb0216d73bed8cbb` |
| `research/zero-pairing/PROOF.md` | `824af09db62887a04107e72f9aafb56345aef45c1ea3ccf6499956d6896e914c` |
| `research/zero-pairing/constants.py` | `b71772dee37a2b068677c2800c2dce6d0737a94d03380f47b2f9d87ec6e610a7` |
| `verify/check.py` | `ace2b055b5279284d04d37b6c6dde77af86088245846700c502effb3e812e709` |
| `discover/frontier.json` | `9ca629138c133ac8547efba9b47f4d862ae82e7079c4da0998961d8fa5c964a4` |
| `AGENTS.md` | `e8f93ce38983d792791c3f9ad9b8b0a367668b3b7b945b071b6f360c45babd62` |
| `DISCOVERY.md` | `e603c2aaf4b9c692b315213f6c7dd5aebdfba5932e67155e53c76a6590ec4ddf` |

I independently retrieved and hashed the public primary objects in memory:

| Primary object | Bytes | SHA-256 |
|---|---:|---|
| [LLS v3 PDF](https://arxiv.org/pdf/1309.3595v3) | 267062 | `692b7fe38d883cf3503e247b0ebcd0c092c7e7267b06488adb9f40d45095b5a8` |
| [LLS v3 source](https://arxiv.org/src/1309.3595v3), gzip response | 26276 | `301cb41d96db71a722f278b1e9db437cf71c275ea07cc0289f3a916d8208528c` |
| Decompressed `QuaResL1Corrected.tex` | 93372 | `2b5a85717f193b950ae522ad5c07f8f8bb1dc2213c073d54b4d4fa8cba6d98f8` |

Useful read-only commands from `lone/`, in addition to the independent command
above, are:

```sh
git rev-parse HEAD
git diff f41ba0a120bca88406331a46027aa1500b714d49 -- research/l-one-bounds
sha256sum research/l-one-bounds/PROOF.md research/l-one-bounds/constants.py research/l-one-bounds/README.md research/l-one-bounds/RECHECK.md
python3 -B research/l-one-bounds/constants.py
```

## Trust boundary and limits

The unchanged classical inputs also relied on in ROUND1 are analytic
continuation and functional equations; the Hadamard real-part identities and
their convergent sums; the published contour residue identities before GRH
estimation; zeta's Laurent expansion and Euler-constant integral identity;
digamma special values; the Euler product at 2; and the quadratic Dirichlet
class-number formula. I checked their use and the new uniform consequences.
The absolute domination of the integrated zero errors was checked above;
the underlying contour shifts, horizontal and left-edge limits, and classical
analytic continuation were not proved anew from first principles.

I did not certify H(7/8), replay Lean, calculate actual zeros or L-values,
certify conductors below 15, optimize the truncation/constants, or prove a
product-free imprimitive result. The result remains conditional and pending
maintainer review. A human or formal review would supply a different kind of
assurance from this same-model AI review.

Only this report was added to the worktree, using native `apply_patch`.
No other project file was edited, no public write or git mutation was made,
no package was installed, and no further agent was spawned. External source
requests used only the public primary arXiv URLs; repository material was not
sent to external research services.
