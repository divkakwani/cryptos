import unittest
from cryptos.dhke import DHKEInvoker, DHKEParty

class TestDHKE(unittest.TestCase):

    def test_consistency(self):
        for x in range(1000):
            invoker = DHKEInvoker()
            other = DHKEParty(invoker.get_param())
            other.receive_partial_key(invoker.get_partial_key())
            invoker.receive_partial_key(other.get_partial_key())
            assert(invoker.get_key() == other.get_key())


if __name__ == '__main__':
    unittest.main()
