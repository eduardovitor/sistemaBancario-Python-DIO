from Deposito import Deposito
from Historico import Historico
from Saque import Saque


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
        if valor < 0:
            print("Valores de saque negativos não são permitidos")
            return False
        else:
            self._saldo -= valor
            saque = Saque(valor)
            saque.registrar(self)
            return True
    def depositar(self,valor:float) -> bool:
        if valor <= 0:
            print("Não é possível depositar valores nulos ou negativos")
            return False
        else:
            deposito = Deposito(valor)
            self._saldo += valor
            deposito.registrar(self)
            return True
    @property
    def historico(self):
        return self._historico
    def atualizar_historico(self,historico_atualizado):
        self._historico = historico_atualizado
    def imprimir_historico(self):
        for op in self._historico:
            print(op)
        print(f"Saldo: {self._saldo}")