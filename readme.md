# Cryptos

Implementation of some crytographic algorithms.

## Usage
i
To use any cryptographic algorithm, first import it:
```
from crytpos.rsa import RSAEncryptor
```

In general, there are two classes associated with every cryptosystem - an Encryptor and
a Decryptor class.

To use any cryptosystem, first create an encryptor object, passing the secret information:
```
encobj = Encryptor(encryption_key, **params)
```
To decrypt, one can similarly use an instance of Decryptor object:
```
decobj = Decryptor(decryption_key, **params)
```
