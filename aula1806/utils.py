"""
Esse arquivo terá dois métodos
1) Filtrar por destino e partida
2) Ordenacao por precos de ordem crescente
"""
from typing import List
from passagem import Passagem


# a partir de --> tem que ser maior que a data de partida
def filtra_por_destino_e_partida(passagens: List[Passagem], destino: str, partida: str):
    return list(filter(
        lambda passagem: passagem.get_destino() == destino and passagem.get_partida() >= partida,
        passagens
    ))


def ordena_por_menor_preco(passagens: List[Passagem]):
    # clonar a lista para não alterar a original
    lista_ordenada = passagens[:]
    num_passagens = len(passagens)
    for i in range(num_passagens):
        for j in range(i + 1, num_passagens):
            if lista_ordenada[i].get_preco() > lista_ordenada[j].get_preco():
                temp = lista_ordenada[i]
                lista_ordenada[i] = lista_ordenada[j]
                lista_ordenada[j] = temp
    return lista_ordenada
