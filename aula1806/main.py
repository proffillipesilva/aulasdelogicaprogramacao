from typing import List
from passagem import Passagem
# usando import ao invés de from visto que é um utilitário e evita problemas de importação
import utils

# atencao: evite usar from <algumarquivo> import *  --> O * não é boa idéia no python

"""
Dado o arquivo de passagens.csv
Quero que vocês me retornem a lista crescente de precos
Dos voos cujo destino é Ourinhos e a partir da data 20210222
"""
with open('passagens.csv', 'r') as texto:
    linhas = texto.readlines()
    lista_passagens: List[Passagem] = []
    for linha in linhas:
        [id, empresa, destino, origem, preco, partida] = linha.strip().split(',')
        lista_passagens.append( Passagem(int(id), empresa, destino, origem, float(preco), partida))

    #primeiro filtra a lista
    passagens_para_ourinhos = utils.filtra_por_destino_e_partida(lista_passagens, "Ourinhos", "20210122")
    #depois ordeno ela
    lista_ordenada = utils.ordena_por_menor_preco(passagens_para_ourinhos)

    for passagem in lista_ordenada:
        print(passagem)
