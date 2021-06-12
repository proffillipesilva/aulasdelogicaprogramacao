# O TypeChecking é usado para permitir tipos e evitar o problema da importacao ciclica

from typing import TYPE_CHECKING, List
if TYPE_CHECKING:
    from aula1106.pessoa import Pessoa
    from aula1106.movimentacoes import Deposito

class Conta:

    def __init__(self, id: int, pessoa: 'Pessoa'):  # construtor
        self._id = id
        self._pessoa = pessoa
        self._saldo = 0

        self._depositos: List['Deposito'] = []

    def altera_saldo(self, valor: float):  #setter
        self._saldo += valor

    def __str__(self):   # to string
        return f'{self._id} {self._pessoa.get_nome()}'

    def get_saldo(self) -> float:  # getter
        return self._saldo

    def get_pessoa(self) -> 'Pessoa':
        return self._pessoa

    def insere_deposito(self, deposito: 'Deposito'):
        self._depositos.append(deposito)
