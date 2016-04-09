from .abstract import AbstractEncryptor, AbstractDecryptor
from random import randint


class CaesarEncryptor(AbstractEncryptor):

    def __init__(self, shift):
        self.key = shift

    def encrypt(self, message):
        pt = message.lower()
        ctl = map(lambda c: chr((ord(c)-ord('a')+self.key)%26+ord('a')), pt)
        ct = ''.join(ctl)
        return ct


class CaesarDecryptor(AbstractDecryptor):

    def __init__(self, shift):
        self.key = shift

    def decrypt(self, ciphertext):
        ptl = map(lambda c: chr((ord(c)-ord('a')-self.key)%26+ord('a')), ciphertext)
        pt = ''.join(ptl)
        return pt


class CaesarEncDec(CaesarEncryptor, CaesarDecryptor):

    def __init__(self):
        shift = randint(2, 10)
        CaesarEncryptor.__init__(self, shift)
        CaesarDecryptor.__init__(self, shift)
