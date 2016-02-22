from abc import ABCMeta, abstractmethod


class AbstractEncryptor:
    __metaclass__ = ABCMeta

    @abstractmethod
    def encrypt(message):
        pass


class AbstractDecryptor:
    __metaclass__ = ABCMeta

    @abstractmethod
    def decrypt(message):
        pass

