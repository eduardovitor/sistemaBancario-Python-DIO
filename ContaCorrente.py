from Conta import Conta


class ContaCorrente(Conta):
    def __init__(self, cliente, numero, limite_valor_saques, limite_qtd_saques):
        super().__init__(cliente,numero)
        self._limite_valor_saques = limite_valor_saques
        self._limite_qtd_saques = limite_qtd_saques

