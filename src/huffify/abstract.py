from abc import ABCMeta, abstractmethod


class Codec:
    @abstractmethod
    def encode(self, data: str) -> bytes:
        pass

    @abstractmethod
    def decode(self, data: bytes) -> str:
        pass


class PersistenceManager(metaclass=ABCMeta):
    @abstractmethod
    def save(self, data):
        pass

    @abstractmethod
    def load(self):
        pass
