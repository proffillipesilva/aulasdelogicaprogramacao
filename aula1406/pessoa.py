class Pessoa:
    def __init__(self, idade: int):
        self._idade = idade

    def __str__(self):
        return f'idade  {self._idade}'
