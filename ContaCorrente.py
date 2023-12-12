from Cliente import Cliente
from Conta import Conta


class ContaCorrente(Conta):
    def __init__(self, cliente:Cliente, numero, limite_valor_saques, limite_qtd_saques):
        super(cliente,numero).__init__()
        self._limite_valor_saques = limite_valor_saques
        self._limite_qtd_saques = limite_qtd_saques

