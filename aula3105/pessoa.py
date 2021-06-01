class Pessoa:
    def __init__(self, rg, nome):
        self._rg = rg
        self._nome = nome

    def __str__(self):
        return self._nome
