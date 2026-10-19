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

**Paper, on imprimitive characters** (line 176):

> Imprimitive characters have the same possible zeros in $\Re s>0$, because the finitely
> omitted Euler factors are nonzero there.

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
| every modulus q ≥ 1 | "every Dirichlet L-function" | `{q : ℕ} [NeZero q]` | ✓ |
| every character, imprimitive included | line 176 remark | every `DirichletCharacter ℂ q` | ✓ |
| principal characters mod q > 1 | covered | `χ = 1` is the principal character mod q; only s = 1 is excluded | ✓ |
| no zero with Re s > 7/8, strict | "no zero in Re s > 7/8" | `7/8 < s.re` | ✓ |
| pole at s = 1 is not a zero | "pole … allowed" | `hpole` excludes (χ = 1, s = 1) only | ✓ |

**Verdict.** As a statement, assumption A2 holds. The Lean statement is exactly H(7/8),
provided Mathlib's `DirichletCharacter.LFunction` agrees with the Dirichlet series for
Re s > 1 (Mathlib proves this as `LFunction_eq_LSeries`) and is its analytic
continuation elsewhere.

## Findings beyond the card

1. **A Lean proof is claimed, not just the statement.** The comparator config names a
   solution module and allows only Lean's three standard axioms. If the comparator check
   replays, H(7/8) itself is kernel-checked. Assumption A1 would then rest on Mathlib's
   definitions, not on the unrefereed paper. Earlier summaries ("the Lean files state only
   the zero-free half-plane") understate this.
   - Replaying it was **not done**. It needs Lean `v4.34.1` (from `lean/lean-toolchain`)
     and a Mathlib build, which is several GB and a long build. Ask the maintainer before
     attempting it.
   - Suggested new card: `replay-comparator` in the `verify-premise` track.
2. **The paper never mentions Miller–Rabin.** Its only algorithmic corollary
   (Corollary 1.2, lines 325–338) is least nonresidues and square roots mod p, deduced
   from Bhargava–Ivanyos–Mittal–Saxena's weak-GRH theorem with ε = 7/16. The
   Miller–Rabin corollary is this project's to write.
3. **The functional equation gives zeros in 1/8 ≤ Re s ≤ 7/8** (proof of
   Corollary 1.2). This symmetric strip, not just the half-plane, is what an explicit
   formula sees. Lemma T1 needs only the right half.

## Suggested frontier update (maintainer only)

- Mark A2 as `closed`, citing this note.
- Reword A1: "Lean proof claimed (comparator config permits only standard axioms); not
  replayed by this project".

```discover
{"v": 0, "kind": "done", "task": "preprint-scope", "scope": "A2: OpenAI's Dirichlet 7/8 statement (paper Thm 1.1 + Lean comparator statement) matches H(7/8) clause by clause; Lean proof module exists but was not replayed", "base": "6f85127", "posted_at": "2026-10-19T09:40:00Z", "evidence_level": "author-checked", "artifact": "research/preprint-scope/NOTE.md"}
```
