from Historico import Historico


class Conta:
    _agencia = "0001"
    _cliente = {}
    _historico = []
    _saldo = 0
    _numero = 0
    def __init__(self,cliente,numero):
        self._cliente = cliente
        self._numero = numero
    @classmethod
    def nova_conta(self,cliente,numero):
        self._cliente = cliente
        self._numero = numero
        return self
    def saldo(self) -> float:
        return self._saldo
    def sacar(self,valor:float) -> bool:
        pass
    def depositar(self,valor:float) -> bool:
        pass
    