from Transacao import Transacao

class Saque(Transacao):
    def __init__(self,valor):
        self._valor = valor
    def registrar(self,conta):
        print("Registrando saque na conta ...")