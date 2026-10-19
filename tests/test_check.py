"""Tests for the verifier. Run: python3 -m unittest discover -s tests"""

import json
import math
import sys
import unittest
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "verify"))
import check  # noqa: E402
import mr  # noqa: E402

FIX = ROOT / "tests" / "fixtures"


def load(name):
    return json.loads((FIX / name).read_text())


class LnBounds(unittest.TestCase):
    def test_brackets_math_log(self):
        for n in (1, 2, 3, 10, 1000003, 2**64 + 13, mr.PSI_13):
            lo, hi = check.ln_bounds(n)
            self.assertLessEqual(lo, hi)
            self.assertLess(hi - lo, Fraction(1, 10**30))
            self.assertAlmostEqual(float(lo), math.log(n), places=9)


class MillerRabin(unittest.TestCase):
    def test_known_strong_pseudoprimes(self):
        # Smallest strong pseudoprimes to bases {2}, {2,3}, {2,3,5} (OEIS A014233).
        for n, bases in ((2047, (2,)), (1373653, (2, 3)), (25326001, (2, 3, 5))):
            self.assertFalse(any(mr.is_witness(b, n) for b in bases))
            self.assertIsNotNone(mr.least_prime_witness(n))

    def test_primes_have_no_witness(self):
        for p in (3, 5, 41, 43, 1000003, 2**61 - 1):
            self.assertIsNone(mr.least_prime_witness(p))

    def test_prime_factor_is_witness(self):
        self.assertTrue(mr.is_witness(3, 9))
        self.assertTrue(mr.is_witness(7, 7 * 11))


class Exponent(unittest.TestCase):
    def test_frontier_values(self):
        self.assertEqual(check.mr_exponent(Fraction(7, 8)), 10)
        self.assertEqual(check.mr_exponent(Fraction(1, 2)), 4)  # GRH / Bach
        self.assertEqual(check.mr_exponent(Fraction(34999, 40000)), Fraction(50002, 5001))

    def test_rejects_rounded_down(self):
        with self.assertRaises(check.Reject):
            check.check_exponent(load("rounded-down-exponent.json"))

    def test_rejects_bad_theta(self):
        for theta in ("1", "2/5", "0.3"):
            with self.assertRaises(check.Reject):
                check.check_exponent({"theta": theta, "claimed_exponent": "100"})

    def test_rejects_float_input(self):
        with self.assertRaises(check.Reject):
            check.check_exponent({"theta": 0.875, "claimed_exponent": "10"})


class Explicit(unittest.TestCase):
    def test_synthetic_pass(self):
        check.check_explicit(load("synthetic-explicit-pass.json"))

    def test_synthetic_pass_holds_numerically(self):
        # Independent float evaluation of the T1 inequality at x = W(n).
        c = load("synthetic-explicit-pass.json")
        th, C, D = (float(Fraction(c[k])) for k in ("theta", "C", "D"))
        t = {k: float(Fraction(v)) for k, v in c["template"].items()}
        for e in range(6, 400, 7):
            L = e * math.log(10)
            x = (C * L + D) ** (1 / (1 - th))
            lhs = t["w1"] * x - x**th * (t["alpha"] * L + t["beta"]) - (t["gamma"] * L + t["delta"])
            self.assertGreater(lhs, 0, f"n = 1e{e}")

    def test_synthetic_fail(self):
        with self.assertRaises(check.Reject):
            check.check_explicit(load("synthetic-explicit-fail.json"))

    def test_rejects_n0_above_psi13(self):
        c = load("synthetic-explicit-pass.json")
        c["n0"] = mr.PSI_13 + 1
        with self.assertRaises(check.Reject):
            check.check_explicit(c)

    def test_rejects_failure_at_n0(self):
        c = load("synthetic-explicit-pass.json")
        c["template"]["beta"] = "1000"  # constant term swamps g at n0
        with self.assertRaises(check.Reject):
            check.check_explicit(c)

    def test_rejects_below_y_min(self):
        c = load("synthetic-explicit-pass.json")
        c["template"]["y_min"] = "1000"
        with self.assertRaises(check.Reject):
            check.check_explicit(c)


class SmallN(unittest.TestCase):
    def test_smalln_quick(self):
        out = check.check_smalln(20001)
        self.assertEqual(out["largest_least_witness_seen"], 3)


class Candidates(unittest.TestCase):
    def test_all_candidates_pass(self):
        for path in sorted((ROOT / "candidates").glob("*.json")):
            with self.subTest(path=path.name):
                check.run_claim(path)


if __name__ == "__main__":
    unittest.main()
