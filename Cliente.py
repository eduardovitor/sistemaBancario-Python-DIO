from Conta import Conta
from PessoaFisica import PessoaFisica
from Transacao import Transacao

class Cliente(PessoaFisica):
    def __init__(self,endereco:str,contas:list):
        self._endereco = endereco
        self._contas = contas
    def realizar_transacao(conta:Conta,transacao:Transacao) -> bool:
        pass
    def adicionar_conta(conta:Conta):
        pass