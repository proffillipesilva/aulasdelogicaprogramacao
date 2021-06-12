from pessoa import Pessoa


class Conta:
    def __init__(self, id: int, pessoa: Pessoa):  # construtor
        self._id = id
        self._pessoa = pessoa
        self._saldo = 0

    def altera_saldo(self, valor: float):  #setter
        self._saldo += valor

    def __str__(self):   # to string
        return f'{self._id} {self._pessoa.get_nome()}'

    def get_saldo(self) -> float:  # getter
        return self._saldo

    def get_pessoa(self) -> Pessoa:
        return self._pessoa
