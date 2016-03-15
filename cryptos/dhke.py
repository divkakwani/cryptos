"""
Implementation of the Diffie-Hellman Key Exchange Protocol

Usage:

    # Setup
    invoker = DHKEInvoker()
    other = DHKEParty(invoker.get_param())

    # Key exchange phase
    other.receive_partial_key(invoker.get_partial_key())
    invoker.receive_partial_key(other.get_partial_key())

    # Check consistency
    assert(invoker.get_key() == other.get_key)
"""

from .numt import randprime, modulo_exp
from random import randint


__author__ = 'Divyanshu Kakwani'
__license__ = 'MIT'


def DHKEparam_gen(primelen=10):
    """
    Generates parameters for the DHKE Protocol
    """
    prime = randprime(10**(primelen-1), 10**primelen)
    alpha = randint(2, prime-2)
    return (prime, alpha)


class DHKEParty:
    """
    Represents a party involved in DHKE Protocol
    """

    def __init__(self, param):
        self.prime = param[0]
        self.alpha = param[1]
        self.secret = randint(2, self.prime-2)
        self.Ka = modulo_exp(self.alpha, self.secret, self.prime)
        self.Kb = None

    def get_param(self):
        return (self.prime, self.alpha)

    def get_partial_key(self):
        return self.Ka

    def receive_partial_key(self, Kb):
        self.Kb = Kb
        self.final_key = modulo_exp(Kb, self.secret, self.prime)

    def get_key(self):
        if not self.Kb:
            raise Exception('Partial key not received')
        return self.final_key


class DHKEInvoker(DHKEParty):
    """
    The party which invokes the DHKE Protocol. A DHKEInvoker
    differs from a DHKEParty in that it has to generate the
    DHKE parameters at the outset.
    """

    def __init__(self):
        param = DHKEparam_gen()
        DHKEParty.__init__(self, param)
