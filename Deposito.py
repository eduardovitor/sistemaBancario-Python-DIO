from Historico import Historico
from Transacao import Transacao

class Deposito(Transacao):
    def __init__(self,valor):
        self._valor = valor
    def registrar(self,conta):
        historico = Historico()
        historico.registrar(self,conta)
    @property
    def valor(self):
        return self._valor
    def __str__(self) -> str:
        return f"Tipo de operação: {self.__class__.__name__}, Valor: {self._valor} "
        