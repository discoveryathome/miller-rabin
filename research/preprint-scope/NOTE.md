# Preprint scope: does OpenAI's statement give H(7/8)? (card `preprint-scope`, assumption A2)

- **Sources read:** github.com/openai/math at commit
  `1581d4cbdd69a0faf34b2089614fe2a814316a6a` (2026-10-12). Files:
  - `preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex`
  - `lean/ComparatorChallenges/DirichletSevenEighths.lean`
  - `lean/ComparatorChallenges/DirichletSevenEighths.json`
  - `lean/docs/003.md`
- **Evidence level:** author-checked (one reader). Nothing was built or run.

## The statements, quoted exactly

**Paper, Theorem 1.1** (`paper.tex`, lines 106–111):

> Every finite-order Hecke $L$-function over $F=\mathbb Q(\sqrt{-3})$ has no zero in
> $\Re s>7/8$. The same holds for every Dirichlet $L$-function, including $\zeta(s)$.
> A pole at $s=1$ for a principal character is allowed.

**Paper, on imprimitive characters.** The paper's Quadratic transfer proposition
(`paper.tex` lines 6706–6714) concludes that "every Dirichlet $L$-function is zero-free on
that same strict half-plane". Its proof (lines 6719–6721) reads:

> The same observation for factors $1-\chi(p)p^{-s}$ reduces the Dirichlet assertion to a
> primitive Dirichlet character $\chi$ of conductor $q$.

(An earlier version of this note cited lines 176–177 instead. That remark concerns Hecke
characters over $F$, not Dirichlet characters.)

**Lean scope note** (`lean/docs/003.md`, lines 10 and 12):

> The formalization gives $\theta=7/8$ for the Riemann zeta function and every Dirichlet
> $L$-function, uniformly over all positive moduli and all characters.

> The principal-character poles at $s=1$ are excluded in the Dirichlet and Hecke statements.

**Lean comparator statement** (`DirichletSevenEighths.lean`):

```lean
theorem LFunction_ne_zero_of_seven_eighths_lt_re
    {q : ℕ} [NeZero q] (χ : DirichletCharacter ℂ q) {s : ℂ}
    (hs : (7 / 8 : ℝ) < s.re) (hpole : ¬ (χ = 1 ∧ s = 1)) :
    _root_.DirichletCharacter.LFunction χ s ≠ 0
```

**Comparator config** (`DirichletSevenEighths.json`):
- `"solution_module": "OAI.NumberTheory.DirichletL.Nonvanishing"`
- `"permitted_axioms": ["propext", "Quot.sound", "Classical.choice"]`

## Clause by clause against H(θ) in docs/template-T1.md

| H(7/8) requires | Paper | Lean statement | Verdict |
|---|---|---|---|
| every modulus q ≥ 1 | "every Dirichlet L-function" | `{q : ℕ} [NeZero q]`, which is exactly q ≥ 1 | ✓ |
| q = 1, i.e. ζ | "including $\zeta(s)$" | q = 1; Mathlib's `LFunction_modOne_eq` gives `LFunction χ = riemannZeta` | ✓ |
| every character, imprimitive included | Quadratic transfer, lines 6706–6721 | every `DirichletCharacter ℂ q` | ✓ |
| every s | — | χ is explicit and s implicit; both are universally quantified | ✓ |
| principal characters mod q > 1 | covered | `χ = 1` is the principal character mod q; only s = 1 is excluded | ✓ |
| no zero with Re s > 7/8, strict | "no zero in Re s > 7/8" | `7/8 < s.re` | ✓ |
| pole at s = 1 is not a zero | "pole … allowed" | `hpole` excludes (χ = 1, s = 1) only | ✓ |

**Verdict.** As a statement, assumption A2 holds, and the Lean statement is exactly H(7/8).
Mathlib's `DirichletCharacter.LFunction` is the analytic continuation of the Dirichlet
series:
- `LFunction_eq_LSeries` gives agreement for Re s > 1;
- `differentiableAt_LFunction` (hypothesis `s ≠ 1 ∨ χ ≠ 1`) makes it holomorphic on ℂ∖{1};
- ℂ∖{1} is connected, so the identity theorem applies.

At (χ = 1, s = 1) Mathlib's value is a junk value, and that is exactly the point `hpole`
excludes. (This was read in a current Mathlib. The revision pinned by openai/math was not
rechecked.)

## Findings beyond the card

1. **A Lean proof is claimed, not just the statement.** The comparator config names a
   solution module and allows only Lean's three standard axioms. If the comparator check
   replays, H(7/8) itself is kernel-checked. Assumption A1 would then rest on Mathlib's
   definitions, not on the unrefereed paper. Earlier summaries ("the Lean files state only
   the zero-free half-plane") understate this.
   - Replaying it was **not done**. It needs Lean `v4.34.1` (from `lean/lean-toolchain`)
     and a Mathlib build, which is several GB and a long build. Ask the maintainer before
     attempting it.
   - Follow-up: the existing card `replay-lean-proof` covers replaying it.
2. **The paper never mentions Miller–Rabin.** Its only algorithmic corollary
   (Corollary 1.2, lines 325–338) is least nonresidues and square roots mod p, deduced
   from Bhargava–Ivanyos–Mittal–Saxena's weak-GRH theorem with ε = 7/16. The
   Miller–Rabin corollary is this project's to write.
3. **The functional equation gives zeros in 1/8 ≤ Re s ≤ 7/8** (proof of
   Corollary 1.2; the paper states it for primitive χ). This symmetric strip, not just the
   half-plane, is what an explicit formula sees. Lemma T1 uses both halves: Lemma 0 part 1
   of the first T1 uses Re ρ ≥ 1/8. The left half follows from H(7/8) and the
   unconditional functional equation, so nothing beyond H(7/8) is assumed.

## Review history

**2026-10-19, independent recheck by a separate AI agent** (fresh context). It is not a human
check.
- **Verdict: confirmed with corrections.**
  - Every quotation matches the source at 1581d4c.
  - Theorem 1.1 together with the Lean statement covers exactly H(7/8).
  - The downstream proofs need nothing more.
- **Fixed:**
  - the imprimitive-character citation was a remark about Hecke characters; it is replaced
    by the Quadratic transfer proposition;
  - "Lemma T1 needs only the right half" was wrong;
  - the Mathlib proviso is now closed by an argument;
  - rows for q = 1 and for the quantifiers are added;
  - `lean/docs/003.md` is quoted.

## Suggested frontier update (maintainer only)

- Mark A2 as `closed`, citing this note.
- Reword A1: "Lean proof claimed (comparator config permits only standard axioms); not
  replayed by this project".

```discover
{"v": 0, "kind": "done", "task": "preprint-scope", "scope": "A2: OpenAI's Dirichlet 7/8 statement (paper Thm 1.1 + Lean comparator statement) matches H(7/8) clause by clause; Lean proof module exists but was not replayed", "base": "f3cc2db", "posted_at": "2026-10-19T07:12:51Z", "evidence_level": "author-checked", "artifact": "research/preprint-scope/NOTE.md"}
```
