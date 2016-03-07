"""
Collection of some useful number theoretic functions

@author: Divyanshu Kakwani <divkakwani@gmail.com>
@license: MIT
"""

from math import sqrt
import random

def naive_primality_test(n):
    """
    Returns true iff n is a prime number
    """
    return (n > 2) and (n % 2 != 0) and all(n % i for i in range(3, int(sqrt(n))+1, 2))


def gcd(a, b):
    """
    Returns gcd of a and b using the euclid's algorithm
    """
    return gcd(b, a % b) if b != 0 else a


def ext_euclid(x, y):
    """
    Returns (g, a, b) such that g = gcd(x, y) = ax + by
    """
    if y == 0:
        # gcd = x and gcd = x = (1)x + (0)y
        return (x, 1, 0)
    else:
        # Recursively, g = a1 * (y) + b1 * (x % y)
        (g, a1, b1) = ext_euclid(y, x % y)
        # a1 * (y) + b1 * (x % y) = b1 * x + (a1 - (x//y)) * y = g
        (g, a, b) = (g, b1, a1 - (x // y) * b1)
        return (g, a, b)


"""
Modular arithmetic operations
"""

def modulo_inv(a, m):
    (g, s, t) = ext_euclid(a, m)
    return s if g == 1 else None


def modulo_exp(a, n, m):
    """
    Returns (a^n) modulo m
    """
    # Base Case
    if n == 0:  return 1
    # Recursive Case
    if n % 2 == 0:
        halfexp = modulo_exp(a, n//2, m)
        return (halfexp * halfexp) % m
    else:
        return (modulo_exp(a, n-1, m) * a) % m


def composite_witness_fermat(a, p):
    """
    Test for primality, based on the following theorem, aka Fermat's little theorem:
        a^(p-1) ≡ 1 (mod p) if p is a prime
    If (a, p) do not satisfy the equation, then p is necessarily a composite.
    However, if (a, p) do satisfy the equation, then p may or may not be prime.
    There, if the function returns False, then p is likey a prime, but not certainly. 
    """
    return False if modulo_exp(a, p-1, p) == 1 else True


def fermat_primality_test(n, accuracy=100):
    """
    :param n: the input number whose primality is to be tested
    :param accuray: Greater accuracy <=> greater confidence in the primality of n if the
                    return value is True
    
    Performs composite_witness_fermat test s times on n.
    """
    # Prelim tests
    if n % 2 == 0:
        return False
    for i in range(s):
        a = random.randint(2, n-2)
        if composite_witness_fermat(a, n):
            return False
    return True
