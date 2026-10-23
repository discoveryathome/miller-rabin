**Original idea: Geoffrey Irving.**

# Source audit for the H(7/8) coset transfer

2026-10-23; CC BY 4.0. A separate fresh-context Codex agent researched the
primary sources before the parent wrote PROOF.md. The parent condensed that
report to the dependencies below. This source research is **not an independent
recheck of the finished theorem or its exact certificate**.

## Pinned source

Youness Lamzouri, Xiannan Li and Kannan Soundararajan, *Conditional bounds for
the least quadratic non-residue and related problems*,
[arXiv:1309.3595v3](https://arxiv.org/abs/1309.3595v3), 2016-12-08.
The [PDF](https://arxiv.org/pdf/1309.3595v3) and
[TeX source](https://arxiv.org/src/1309.3595v3) were read. Printed page numbers
start at 1; Section 4 occupies pp. 13--16.

- PDF SHA-256: `692b7fe38d883cf3503e247b0ebcd0c092c7e7267b06488adb9f40d45095b5a8`.
- Gzip source SHA-256: `301cb41d96db71a722f278b1e9db437cf71c275ea07cc0289f3a916d8208528c`.
- Decompressed TeX SHA-256: `2b5a85717f193b950ae522ad5c07f8f8bb1dc2213c073d54b4d4fa8cba6d98f8`.

LLS Theorem 1.4 and Corollary 1.2 on p. 3 assume GRH. Their numerical
constants and finite computation do not automatically transfer to H(7/8).
The new proof instead uses the accepted local Lemma 0' from
[`../zero-pairing/PROOF.md`](../zero-pairing/PROOF.md), and Lemma 0 and facts
F1--F2 from [`../first-explicit-t1/PROOF.md`](../first-explicit-t1/PROOF.md).

## Dependencies that need replacement

1. **LLS (4.3), p. 13:** Lemma 2.1 estimates the principal character's zeta
   error using RH. The zeta pole supplies the main term X. Removing primes
   dividing q is unconditional, but the square-root error is not.
2. **LLS (4.4), p. 13:** Lemma 2.2 estimates both zero sums in the primitive
   nonprincipal S(X,chi). Keep its residue identity and replace each zero
   estimate. It contains the full complex B_chi log X term.
3. **The x = 100 use of Lemma 2.3 and (4.7), pp. 13--14:** this bounds the
   full complex B_chi, not just -Re B_chi. With c(x) from the quoted pairing
   lemma, 1-1/100-c(100) is negative. The parent's proof uses u = 2^16 and
   recomputes its positive denominator instead of retaining 2/3 and 4.
4. **Lemma 2.3 at x = X before (4.8), p. 14:** its GRH denominator and the
   joint imprimitive-factor optimization at q/f = 6 need rederivation. The
   parent uses explicit separate Euler-factor envelopes and d(X).
5. **Aggregation before (4.9), pp. 14--15:** LLS invokes Lemma 2.4, whose
   T_zeta(X) upper bound assumes RH. The new proof uses the unconditional
   factorial bound T_zeta(X) <= log X, keeping h - 1 nonprincipal terms.
6. **Section 4.2 and (4.10), p. 15:** Lemma 2.1 is invoked for odd prime
   powers at smaller arguments. Its square-root error and 1/7 constant
   cannot be copied. The new proof bounds all proper powers elementarily.
7. **Section 4.4, p. 16:** another use of Lemma 2.1 controls even powers.
   This is also replaced by the same elementary proper-power envelope.

The new argument does not use LLS's finite check below q = 20000 or its
special range X <= (q log q)^2 in Section 4.3. The initial coefficient-1
snapshot checked 3 <= q < 512. The later coefficient-0.581 refinement has
its own q < 2048 fallback; see PROOF.md Section 7 and RECHECK-REFINEMENT.md.

## Exact identities and complex characters

The Hadamard formulas and functional equation in LLS (2.1)--(2.4), p. 5,
are unconditional. For primitive nonprincipal chi, its zero multiset is
invariant under rho -> 1-conjugate(rho); it need not be invariant under
conjugation alone. This justifies the accepted pairing for complex chi.

Before estimating zeros, LLS Lemmas 2.2--2.3 and their proofs, pp. 6--8,
give exactly the two complex identities (1)--(2) in PROOF.md. In particular,
the second left side is

    -conjugate(B_chi) - B_chi/X + sum_rho X^(rho-1)/(rho(rho-1)).

Taking its real part gives the denominator 1+1/X-c(X). Bounding its
modulus by triangle inequality instead gives 1-1/X-c(X). Confusing these
denominators would invalidate the bound for the imaginary component.

In a coset, the phases conjugate(chi(a)) multiply S(X,chi), as in LLS
(4.1)--(4.2), p. 13. Pairing conjugate characters does not eliminate the
imaginary component of B_chi. A real-part-only T1 transfer is insufficient;
the parent's proof explicitly bounds |B_chi|.

The gamma expressions in Lemmas 2.2--2.3 are unconditional. The source
prints 1-n/q in the unnumbered bound following (4.7), p. 14; the weight
required by Lemma 2.3 and the following calculation is 1-n/X. The parent
uses the latter throughout.

## Euler factors and verification boundary

LLS Lemma 3.1, p. 10, (3.2), p. 11, and (4.6), p. 13, bound differences
between imprimitive character sums and their inducing primitive sums.
Only primes p dividing q but not the conductor f actually contribute;
using all p dividing q/f is an upper bound. The primitive conductor and
ambient modulus must remain distinct, including f = 3 and q/f = 1 or 2.

The source audit checked these structural dependencies and derived a
conservative provisional inequality. The initial constant 80, coefficient 1,
exact script and fallback were subsequently authored by the parent and
rechecked in RECHECK.md. The later 0.581 refinement is outside this audit;
its separate review is RECHECK-REFINEMENT.md. Neither audit nor proof verifies
H(7/8), replays a Lean proof, or reproves the cited contour shifts.
