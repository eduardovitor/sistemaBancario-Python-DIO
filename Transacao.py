from abc import ABC, abstractmethod
from Conta import Conta

class Transacao(ABC):
    @abstractmethod
    def registrar(conta:Conta):
        pass