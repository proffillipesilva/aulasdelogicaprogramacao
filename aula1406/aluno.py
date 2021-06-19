from typing import TYPE_CHECKING, List
if TYPE_CHECKING:
    from responsavel import Responsavel
    from prova import Prova
    from pessoa import Pessoa

from typing import TYPE_CHECKING, List
from pessoa import Pessoa
if TYPE_CHECKING:
    from responsavel import Responsavel

class Aluno(Pessoa):
    def __init__(self, idade: int, responsavel: 'Responsavel', provas: List['Prova']):
        super().__init__(idade)
        self._responsavel = responsavel
        self._provas = provas

    def get_media_notas(self):
        soma = 0
        for prova in self._provas:
            soma += prova.get_conceito()
        return soma/len(self._provas)

