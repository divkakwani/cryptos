"""
Implementation of the RSA algorithm

@author: Divyanshu Kakwani <divkakwani@gmail.com>
@license: MIT
"""

from .abstract import AbstractEncryptor, AbstractDecryptor
from .numt import randprime, modulo_inv, gcd, modulo_exp
from random import randint
from .string import num2str, str2num


def RSA_keygen(keylen=200):
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
    return (p*q, e, d)


def encrypt(message, key, n):
    return num2str(modulo_exp(str2num(message), key, n))


def decrypt(message, key, n):
    return encrypt(message, key, n)


"""
The following two classes are wrapper classes for the above functionality,
and merely provision for the convenience of users.
"""


class RSAPublic(AbstractEncryptor, AbstractDecryptor):

    def __init__(self, public_key):
        self.pub_key = public_key
        self.n = public_key[0]
        self.d = public_key[1]

    def encrypt(self, message):
        return encrypt(message, self.d, self.n)

    def decrypt(self, message):
        return decrypt(message, self.d, self.n)

    def verify_sign(self, doc, sign):
        return self.decrypt(sign) == doc


class RSAPrivate(AbstractEncryptor, AbstractDecryptor):

    def __init__(self, keys=None):
        self.keys = keys if keys else RSA_keygen()
        (self.n, self.pub_key, self.pri_key) = self.keys

    def encrypt(self, message):
        return encrypt(message, self.pri_key, self.n)

    def decrypt(self, message):
        return decrypt(message, self.pri_key, self.n)

    def sign_doc(self, doc):
        return {'doc': doc, 'sign': self.encrypt(doc)}

    def get_pubkey(self):
        return (self.n, self.pub_key)
