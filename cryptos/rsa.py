"""
Implementation of the RSA algorithm

@author: Divyanshu Kakwani <divkakwani@gmail.com>
@license: MIT
"""

from .abstract import AbstractEncryptor, AbstractDecryptor
from .numt import randprime, modulo_inv, gcd
from random import randint


def RSA_keygen(keylen=10):
    """
    RSA key generation algorithm:
    1. Generate two large primes, p and q
    2. Find ϕ(n), where n = p.q
    3. Select the public key exponent e ϵ {1..ϕ(n)-1} such that:
        gcd(e, ϕ(n)) = 1
    4. Compute the private key d such that:
        d.e ≡ 1 mod ϕ(n)
    """
    primelen = keylen // 2
    p = randprime(10 ** (primelen-1), 10 ** primelen)
    q = randprime(10 ** (primelen-1), 10 ** primelen)
    phi = (p-1) * (q-1)
    e = phi
    while gcd(e, phi) != 1:
        e = randint(1, phi-1)
    d = modulo_inv(e, phi) % phi
    return (n, e, d)
