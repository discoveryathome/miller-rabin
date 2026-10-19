"""Miller-Rabin (strong probable prime) primitives, exact integer arithmetic only."""

# First 13 primes; Sorenson-Webster: every odd composite n < PSI_13 has a
# strong witness among them.
FIRST_13_PRIMES = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41)

# Sorenson & Webster, "Strong pseudoprimes to twelve prime bases",
# Math. Comp. 86 (2017) 985-1003, Theorem 1.1 (arXiv:1509.00864).
PSI_12 = 318665857834031151167461
PSI_13 = 3317044064679887385961981
PSI_12_FACTORS = (399165290221, 798330580441)
PSI_13_FACTORS = (1287836182261, 2575672364521)


def is_witness(a, n):
    """True if base a proves the odd integer n > 2 composite (strong test)."""
    a %= n
    if a == 0:
        return False  # base is a multiple of n; says nothing
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    x = pow(a, d, n)
    if x == 1 or x == n - 1:
        return False
    for _ in range(s - 1):
        x = x * x % n
        if x == n - 1:
            return False
    return True


def least_prime_witness(n, primes=FIRST_13_PRIMES):
    """Smallest prime in `primes` that is a witness for n, or None."""
    for p in primes:
        if p < n and is_witness(p, n):
            return p
    return None


def is_prime_trial(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            return False
        f += 2
    return True
