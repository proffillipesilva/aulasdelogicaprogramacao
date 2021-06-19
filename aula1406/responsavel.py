from typing import TYPE_CHECKING
from pessoa import Pessoa

class Responsavel(Pessoa):
    def __init__(self, idade: int, rg: str):
        super().__init__(idade)
        self._rg = rg
