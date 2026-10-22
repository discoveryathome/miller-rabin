"""Reference-test regression and exhaustive small-input correctness checks."""
import contextlib
import io
import sys
import unittest
from fractions import Fraction
from itertools import islice
from unittest.mock import patch

from impl import deterministic_mr as impl
from impl.base_counts import prime_count_bounds
from verify.mr import FIRST_13_PRIMES, PSI_12, PSI_13, is_prime_trial, is_witness


class WitnessBound(unittest.TestCase):
    def test_strict_cutoff_and_known_bounds(self):
        self.assertEqual(impl.witness_bound(PSI_13 - 1), 41)
        self.assertGreater(impl.witness_bound(PSI_13), 41)
        self.assertEqual(impl.witness_bound(2**128 - 1), 23546633375396)
        self.assertEqual(impl.witness_bound(2**1024 - 1), 395046954211813343884)

    def test_exact_ceiling_including_integer_boundary(self):
        # Inject rational log upper bounds to exercise both ceiling cases.
        for log_upper, expected in [(Fraction(2000, 529), 256),
                                    (Fraction(2001, 529), 258)]:
            with patch.object(impl, "ln_bounds", return_value=(Fraction(0), log_upper)):
                self.assertEqual(impl.witness_bound(PSI_13), expected)

    def test_cannot_round_below_upper_enclosure(self):
        for n in (PSI_13, PSI_13 + 2, 2**128 + 51, 10**100 + 267):
            _, upper = impl.ln_bounds(n)
            exact = (Fraction(529, 1000) * upper) ** 8
            bound = impl.witness_bound(n)
            self.assertGreaterEqual(Fraction(bound), exact)
            self.assertLess(Fraction(bound - 1), exact)

    def test_invalid_input(self):
        for n in (-1, 0, 1):
            with self.assertRaises(ValueError):
                impl.witness_bound(n)
        with self.assertRaises(TypeError):
            impl.witness_bound(3.0)


class PrimeSieve(unittest.TestCase):
    def test_all_small_limits_and_segment_boundaries(self):
        for limit in (*range(35), 63, 64, 65, 32767, 32768, 32769, 65535, 65536, 65537):
            self.assertEqual(list(impl.primes_up_to(limit)),
                             [n for n in range(2, limit + 1) if is_prime_trial(n)])

    def test_lazy_large_bound(self):
        self.assertEqual(list(islice(impl.primes_up_to(10**100), 13)),
                         list(FIRST_13_PRIMES))


class BaseCounts(unittest.TestCase):
    def test_rigorous_count_interval_contains_actual_count(self):
        for bound in (0, 1, 2, 3, 13, 16, 17, 18, 41, 59, 113, 114, 1000, 10000, 100000):
            lower, upper = prime_count_bounds(bound)
            actual = sum(1 for _ in impl.primes_up_to(bound))
            self.assertLessEqual(lower, actual, bound)
            self.assertGreaterEqual(upper, actual, bound)


class ReferenceTest(unittest.TestCase):
    def test_exhaustive_below_one_million(self):
        for n in range(1_000_000):
            self.assertEqual(impl.is_prime(n), is_prime_trial(n), n)

    def test_edges_and_large_known_primes(self):
        for n in (-10, -1, 0, 1):
            self.assertFalse(impl.is_prime(n))
        for n in (*FIRST_13_PRIMES, 43, 2**61 - 1):
            self.assertTrue(impl.is_prime(n))
        self.assertFalse(impl.is_prime(PSI_13 + 1))

    def test_pseudoprime_boundaries(self):
        # Strong pseudoprime regressions; PSI_12/13 are from Sorenson-Webster,
        # Theorem 1.1. Passing k initial bases does not authorize stopping at k.
        table = [(1, 2047), (2, 1373653), (3, 25326001), (4, 3215031751),
                 (5, 2152302898747), (6, 3474749660383), (7, 341550071728321),
                 (8, 341550071728321), (9, 3825123056546413051),
                 (10, 3825123056546413051), (11, 3825123056546413051),
                 (12, PSI_12), (13, PSI_13)]
        for k, n in table:
            with self.subTest(k=k, n=n):
                self.assertFalse(any(is_witness(p, n) for p in FIRST_13_PRIMES[:k]))
                self.assertFalse(impl.is_prime(n, max_bases=100))
        self.assertTrue(is_witness(43, PSI_13))
        with self.assertRaises(impl.BaseLimitExceeded):
            impl.is_prime(PSI_13, max_bases=13)
        self.assertFalse(impl.is_prime(PSI_13, max_bases=14))

    def test_large_branch_can_finish_and_must_visit_last_base(self):
        # Make the exhaustive branch reachable with a small independently
        # checkable prime. A witness at the last supplied base must be tested.
        with patch.object(impl, "PSI_13", 43), patch.object(impl, "witness_bound", return_value=41):
            self.assertTrue(impl.is_prime(43, max_bases=13))
        with patch.object(impl, "PSI_13", 43), \
                patch.object(impl, "witness_bound", return_value=41), \
                patch.object(impl, "is_witness", side_effect=lambda p, n: p == 41):
            self.assertFalse(impl.is_prime(43, max_bases=13))

    def test_cap_is_inconclusive_not_prime(self):
        with self.assertRaises(impl.BaseLimitExceeded):
            impl.is_prime(43, max_bases=12)
        self.assertTrue(impl.is_prime(43, max_bases=13))
        self.assertFalse(impl.is_prime(9, max_bases=1))
        with self.assertRaises(impl.BaseLimitExceeded):
            impl.is_prime(9, max_bases=0)
        for value in (-1, 1.5):
            with self.assertRaises(ValueError):
                impl.is_prime(43, max_bases=value)
        with self.assertRaises(TypeError):
            impl.is_prime(3.0)

    def test_cli_inconclusive_exit_and_hypothesis_label(self):
        for n, args, code, phrase in [(PSI_13, ["--max-bases", "13"], 2, "inconclusive"),
                                     (PSI_13, [], 0, "composite"),
                                     (43, [], 0, "prime")]:
            with patch.object(sys, "argv", ["deterministic_mr", str(n), *args]), \
                    contextlib.redirect_stdout(io.StringIO()) as out:
                self.assertEqual(impl.main(), code)
                self.assertIn(phrase, out.getvalue())
        with patch.object(sys, "argv", ["deterministic_mr", str(PSI_13)]), \
                patch.object(impl, "is_prime", return_value=True), \
                contextlib.redirect_stdout(io.StringIO()) as out:
            self.assertEqual(impl.main(), 0)
            self.assertIn("conditional on H(7/8)", out.getvalue())


if __name__ == "__main__":
    unittest.main()
