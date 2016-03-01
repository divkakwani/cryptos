"""
Collection of some useful number theoretic functions

@author: Divyanshu Kakwani <divkakwani@gmail.com>
@license: MIT
"""

from math import sqrt

def isprime(n):
    """
    Returns true iff n is a prime number
    """
    return all(n % i for i in range(2, int(sqrt(n))+1))

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
