# O TypeChecking é usado para permitir tipos e evitar o problema da importacao ciclica
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from aula1106.conta import Conta

class Deposito:

    def __init__(self, remetente: 'Conta', destinatario: 'Conta', valor: float):
        self._remetente = remetente
        self._destinatario = destinatario
        self._valor = valor
        self._remetente.altera_saldo(-valor)
        self._destinatario.altera_saldo(valor)
