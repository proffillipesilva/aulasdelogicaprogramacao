"""
Passagem aerea
# id --> numero
# empresa  --> string
# destino --> string () exponha o destino
# origem  --> string
# preco  --> float   () exponham o preco
# partida --> string () exponha a partida
"""


class Passagem:

    def __init__(self, id: int, empresa: str, destino: str, origem: str, preco: float, partida: str):
        self._id = id
        self._empresa = empresa
        self._destino = destino
        self._origem = origem
        self._preco = preco
        self._partida = partida

    def get_destino(self):
        return self._destino

    def get_preco(self):
        return self._preco

    def get_partida(self):
        return self._partida

    def __str__(self):
        return f'{self._partida}' \
               f' saindo de {self._origem} até {self._destino} ' \
               f'custando {self._preco} via {self._empresa}'
