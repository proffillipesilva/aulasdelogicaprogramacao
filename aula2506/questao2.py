# Leia o arquivo operacoes.txt
# criar uma classe chamada Operacao
# crie uma outra classe chamada Banco

# Nessa classe banco, implementem duas coisas:
# um filtro para mostrar apenas as operacoes de transferencia
# mostrar cada operacao da seguinte forma:
 # ID: ... Tipo: ...  De conta_origem  para ... conta_destino  valor

 # essas transferencias estão no arquivo operacoes.txt
from typing import List

class Operacao:
    def __init__(self, id, conta_origem, tipo, valor, conta_destino):
        self._id = id
        self._conta_origem = conta_origem
        self._tipo = tipo
        self._valor = valor
        self._conta_destino = conta_destino

    def get_tipo(self):
        return self._tipo

    def __str__(self):
        return f'ID {self._id} Tipo: {self._tipo} origem {self._conta_origem} ' \
               f'valor: {self._valor} destino: {self._conta_destino}'

class Banco:
    def __init__(self):
        self._operacoes: List[Operacao] = []

    def adicionar_operacao(self, operacao):
        self._operacoes.append(operacao)

    def filtrar_por_transferencia(self):
        return list(filter( lambda operacao: operacao.get_tipo() == 'Transferencia', self._operacoes))


############# MAIN #################################
banco = Banco()

with open('./operacoes.txt', 'r') as arquivo:
    linhas = arquivo.readlines()
    for linha in linhas:
       [id, conta_origem, tipo, valor, conta_destino] = linha.strip().split(',')
       banco.adicionar_operacao(Operacao(id, conta_origem, tipo, valor, conta_destino))

    lista_de_transferencias = banco.filtrar_por_transferencia()
    for operacao in lista_de_transferencias:
        print(operacao)