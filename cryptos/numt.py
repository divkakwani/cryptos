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

