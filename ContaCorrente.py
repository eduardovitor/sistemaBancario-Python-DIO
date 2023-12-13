from Conta import Conta
from Saque import Saque


class ContaCorrente(Conta):
    def __init__(self, cliente, numero, limite_valor_saques, limite_qtd_saques):
        super().__init__(cliente,numero)
        self._limite_valor_saques = limite_valor_saques
        self._limite_qtd_saques = limite_qtd_saques
    def sacar(self,valor,qtd_saques_realizados):
        if qtd_saques_realizados == self._limite_qtd_saques:
            print(f"Você não pode mais realizar saques, pois já atingiu o limite mensal de {self._limite_qtd_saques}")
            return False
        else:
            if valor > self._limite_valor_saques:
                print(f"Saques que ultrapassem R$ {self._limite_valor_saques:.2f} não são permitidos")
                return False
            elif valor < 0:
                print("Valores de saque negativos não são permitidos")
                return False
            else:
                self._saldo -= valor
                saque = Saque(valor)
                saque.registrar(self)
                return True
                    

