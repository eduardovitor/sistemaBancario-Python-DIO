
from PessoaFisica import PessoaFisica

class Cliente(PessoaFisica):
    def __init__(self,contas:list,**dados):
        super().__init__(**dados)
        self._endereco = dados['endereco']
        self._contas = contas
    def realizar_transacao(self,conta,transacao) -> bool:
        print("Realizando transação ...")
    def adicionar_conta(self,conta):
        self._contas.append(conta)
    def __str__(self) -> str:
        return f"CPF: {self._cpf}, Data de nascimento {self._datansc}"