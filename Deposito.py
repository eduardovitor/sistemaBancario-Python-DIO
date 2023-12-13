from Transacao import Transacao

class Deposito(Transacao):
    def __init__(self,valor):
        self._valor = valor
    def registrar(self,conta):
        print("Registrando depósito na conta ...")