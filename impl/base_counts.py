"""Reproduce worst-size base budgets without enumerating their enormous prime sets.

Rosser-Schoenfeld (1962), p. 69, Corollary 1:
    x / ln x < pi(x) < 1.25506 x / ln x  for x >= 17.
The rational log enclosure preserves both inequality directions.
"""
import json
from fractions import Fraction

from impl.deterministic_mr import primes_up_to, witness_bound
from verify.check import ln_bounds


def prime_count_bounds(bound):
    if bound < 17:
        count = sum(1 for _ in primes_up_to(bound))
        return count, count
    lo, hi = ln_bounds(bound)
    lower = Fraction(bound) / hi
    upper = Fraction(125506, 100000) * bound / lo
    # pi(bound) is an integer strictly between these two rational bounds.
    return lower.numerator // lower.denominator + 1, -(-upper.numerator // upper.denominator) - 1


def report():
    rows = []
    for bits in (64, 128, 1024):
        bound = witness_bound((1 << bits) - 1)
        if bound == 41:
            lower = upper = len(tuple(primes_up_to(bound)))
        else:
            lower, upper = prime_count_bounds(bound)
        rows.append(dict(bits=bits, input="2^bits - 1", prime_base_limit=bound,
                         base_count_lower=lower, base_count_upper=upper,
                         exact_count=lower == upper))
    return dict(source="https://doi.org/10.1215/ijm/1255631807",
                source_location="p. 69, Corollary 1, equations (3.5)-(3.6)",
                meaning="Full prime-base budget at the largest integer of each bit size, before any early witness",
                large_counts="rigorous bounds, not exact enumeration", rows=rows)


if __name__ == "__main__":
    print(json.dumps(report(), indent=2))
