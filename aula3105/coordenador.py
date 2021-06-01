from pessoa import Pessoa

class Coordenador(Pessoa):
    def __init__(self, setor, rg, nome):
        super().__init__(rg, nome)
        self._setor = setor

    def __str__(self):
        return f'Nome: {self._nome} - Setor: {self._setor}'
