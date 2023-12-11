from Conta import Conta
from Transacao import Transacao

class Deposito(Transacao):
    def __init__(self,valor):
        self._valor = valor
    def registrar(conta: Conta):
        print("Registrando depósito na conta ...")