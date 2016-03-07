import unittest
import cryptos.numt as numt


class TestNumT(unittest.TestCase):

    def setUp(self):
        self.primes = [7, 13, 47, 53, 59, 541, 8831, 15485959, 15487469, 179424691, 32416190071]
        self.composites = [55, 444, 957]

    def general_primality_test(self, algorithm):
        for p in self.primes:
            self.assertEqual(algorithm(p), True) 
        for c in self.composites:
            self.assertEqual(algorithm(c), False) 

    def test_naive_primality(self):
        self.general_primality_test(numt.naive_primality_test)

    def test_fermat_primality(self):
        self.general_primality_test(numt.fermat_primality_test)


if __name__ == '__main__':
    unittest.main()
