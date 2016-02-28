import unittest
from cryptos.caesar import CaesarEncryptor, CaesarDecryptor
from string import ascii_lowercase

class TestCaesarCipher(unittest.TestCase):

    def setUp(self):
        self.enc = CaesarEncryptor(4)
        self.dec = CaesarDecryptor(4)

    def test_consistency(self):
        pt = ascii_lowercase
        ct = self.enc.encrypt(ascii_lowercase)
        self.assertEqual(self.dec.decrypt(ct), pt)    



if __name__ == '__main__':
    unittest.main()
