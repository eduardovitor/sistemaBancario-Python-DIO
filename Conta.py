

from Cliente import Cliente
from Historico import Historico


class Conta:
    _agencia = "0001"
    _cliente:Cliente
    _historico:Historico
    _saldo:float
    _numero:int
    @classmethod
    def nova_conta(self,cliente:Cliente,numero:int):
        self._cliente = cliente
        self._numero = numero
        return self
    def saldo(self) -> float:
        return self._saldo
    def sacar(self,valor:float) -> bool:
        pass
    def depositar(self,valor:float) -> bool:
        pass
    