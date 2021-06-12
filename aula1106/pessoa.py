class Pessoa:
    def __init__(self, cpf: str, nome: str):
        self._cpf = cpf
        self._nome = nome

    def get_nome(self):
        return self._nome
