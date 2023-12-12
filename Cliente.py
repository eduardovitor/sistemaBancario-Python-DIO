from datetime import date
from Conta import Conta
from PessoaFisica import PessoaFisica
from Transacao import Transacao

class Cliente(PessoaFisica):
    def __init__(self,contas:list,**dados):
        super(dados).__init__
        self._endereco = dados["endereco"]
        self._contas = contas
    def realizar_transacao(conta:Conta,transacao:Transacao) -> bool:
        pass
    def adicionar_conta(conta:Conta):
        pass