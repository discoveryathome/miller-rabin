# Verifier

Prerequisite: Python 3.9 or later. It uses only the standard library and needs no
network access.

```sh
python3 verify/check.py all                  # every claim in candidates/, plus smalln (~10 s)
python3 -m unittest discover -s tests        # verifier self-tests, including rejections (<1 s)
python3 verify/check.py exponent FILE.json
python3 verify/check.py explicit FILE.json
python3 verify/check.py smalln --limit 2000001
```

All inputs are **exact rationals written as JSON strings** ("7/8", "0.125"). The checker
rejects floats. For an irrational θ, give a rational upper bound on it: every quantity
here is monotone in θ in the safe direction.

## `mr-exponent` claims

```json
{"kind": "mr-exponent", "theta": "8748867/10000000", "claimed_exponent": "9.992756",
 "source": "...", "assumptions": ["..."]}
```

The claim passes only if `claimed_exponent ≥ 2 + 1/(1 − θ)`, computed exactly. Rounding
down is rejected. The originally quoted "9.9984" for θ = 34999/40000 fails, because the
exact value is 50002/5001 ≈ 9.99840032. See `tests/fixtures/rounded-down-exponent.json`.

## `explicit-witness-bound` claims

```json
{"kind": "explicit-witness-bound", "theta": "7/8", "C": "...", "D": "...", "n0": 1000000,
 "template": {"w1": "...", "alpha": "...", "beta": "...", "gamma": "...", "delta": "...",
              "y_min": "..."},
 "proof": "research/<package>/proof.pdf", "assumptions": ["..."]}
```

The meaning of each field and what the check establishes are in
[template-T1.md](template-T1.md). A submission is a claim file in `candidates/` plus the
written proof of Lemma T1 with exactly these constants.

## `smalln`

This checks the small-n fallback:

- Every odd composite up to the limit has a witness among the primes ≤ 41. The checker
  also confirms it never calls a prime composite.
- The cited ψ₁₂ and ψ₁₃ factor as stated and are strong pseudoprimes to the first 12 and
  13 primes.

This is a sanity check of the cited Sorenson–Webster table, not a proof of it.

## Files

| Path | What it is |
|---|---|
| `verify/check.py` | The checker |
| `verify/mr.py` | Strong-test primitives and the ψ table |
| `candidates/*.json` | Claims that `all` checks; the frontier worked example is here |
| `tests/fixtures/*.json` | Synthetic claims, including ones that must be rejected. Never results. |
