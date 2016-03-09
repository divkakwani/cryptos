import unittest
from cryptos.rsa import RSAPrivate, RSAPublic

class TestRSA(unittest.TestCase):

    def setUp(self):
        self.priv = RSAPrivate()
        self.pub = RSAPublic(self.priv.get_pubkey())

    def test_consistency(self):
        message = "hello, Divyanshu Kakwani"
        # The public party encrypts the message
        code = self.pub.encrypt(message)
        # The private party decodes the message
        decoded = self.priv.decrypt(code)
        self.assertEqual(message, decoded)


    def test_docusign(self):
        document = """This is a contract signed by me, Divyanshu Kakwani. I declare that I have authored"""
        signed_doc = self.priv.sign_doc(document)
        self.assertTrue(self.pub.verify_sign(signed_doc['doc'], signed_doc['sign']))

if __name__ == '__main__':
    unittest.main()
