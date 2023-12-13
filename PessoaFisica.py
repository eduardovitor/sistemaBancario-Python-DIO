

class PessoaFisica:
    def __init__(self, **dados):
        self._cpf = dados['cpf']
        self._nome = dados['nome']
        self._datansc = dados['datansc']
        