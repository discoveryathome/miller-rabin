"""Exact deterministic Miller-Rabin reference, conditional on H(7/8) above PSI_13.

Original idea: Geoffrey Irving. The accepted theorem and its sources are in
discover/frontier.json. This implementation does not establish that hypothesis.
Run from the repository root: python3 -m impl.deterministic_mr INTEGER
"""
import argparse
from fractions import Fraction
from math import isqrt

from verify.check import ln_bounds
from verify.mr import FIRST_13_PRIMES, PSI_13, is_witness


class BaseLimitExceeded(RuntimeError):
    """The scan stopped without deciding primality; passing bases is insufficient."""


def witness_bound(n):
    """Integer upper bound, never rounded below the accepted witness limit."""
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 2:
        raise ValueError("n must be at least 2")
    if n < PSI_13:
        return FIRST_13_PRIMES[-1]
    _, log_upper = ln_bounds(n)
    upper = (Fraction(529, 1000) * log_upper) ** 8
    return max(41, -(-upper.numerator // upper.denominator))


def primes_up_to(limit):
    """Incremental segmented sieve; no allocation proportional to the final limit.

    Known primes through sqrt(high) suffice for each segment. The first segment
    discovers its own sieving primes; later segment lengths grow at most to low,
    so sqrt(high) is below low and the required primes are already known.
    """
    if limit < 2:
        return
    primes = []
    root = isqrt(limit)
    low = 2
    while low <= limit:
        high = min(limit, low + min(low, 32768) - 1)
        segment = bytearray(b"\x01") * (high - low + 1)
        for p in primes:
            if p * p > high:
                break
            first = max(p * p, ((low + p - 1) // p) * p)
            segment[first - low::p] = b"\x00" * ((high - first) // p + 1)
        for offset, present in enumerate(segment):
            if not present:
                continue
            p = low + offset
            # Keep only primes needed to sieve the eventual range. This grows
            # with consumed segments, so an early witness stays inexpensive.
            if p <= root:
                primes.append(p)
            yield p
        low = high + 1


def is_prime(n, *, max_bases=None):
    """Decide primality; True at n >= PSI_13 assumes H(7/8).

    With max_bases, raise BaseLimitExceeded if the complete scan has not finished.
    A False result needs no hypothesis. Large prime inputs are impractical.
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if max_bases is not None and (not isinstance(max_bases, int) or max_bases < 0):
        raise ValueError("max_bases must be a nonnegative integer or None")
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    bases = FIRST_13_PRIMES if n < PSI_13 else primes_up_to(witness_bound(n))
    for tested, p in enumerate(bases):
        if p >= n:
            break
        if max_bases is not None and tested >= max_bases:
            raise BaseLimitExceeded(f"inconclusive after {tested} prime bases")
        if is_witness(p, n):
            return False
    return True


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("n", type=int)
    parser.add_argument("--max-bases", type=int, default=10000,
                        help="stop inconclusively after this many bases (default: 10000)")
    parser.add_argument("--unlimited", action="store_true",
                        help="run the complete theoretical scan, which can be impractical")
    args = parser.parse_args()
    if args.max_bases < 0:
        parser.error("--max-bases must be nonnegative")
    try:
        prime = is_prime(args.n, max_bases=None if args.unlimited else args.max_bases)
    except BaseLimitExceeded as exc:
        print(str(exc) + "; no primality conclusion")
        return 2
    if prime:
        print("prime (conditional on H(7/8))" if args.n >= PSI_13 else "prime")
    else:
        print("composite" if args.n >= 2 else "not prime")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
