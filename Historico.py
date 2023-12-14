
from Transacao import Transacao


class Historico(Transacao):
    def registrar(self,transacao,conta):
        historico_atual = conta.historico
        historico_atual.append(transacao)
        conta.atualizar_historico(historico_atual)

