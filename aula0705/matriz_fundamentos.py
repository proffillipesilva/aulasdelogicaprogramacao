from random import randint
def cria_matriz(num_linhas, num_colunas):
    matriz = []
    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            linha.append(randint(0,10))
        matriz.append(linha)
    return matriz

def imprime_matriz(matriz):
    for i in range(len(matriz)):
        linha = matriz[i]  # pega a linha correspondente
        for j in range(len(linha)): # um for para o numero de elementos da linha (colunas)
            print(matriz[i][j], end=' ') # da um espaco para cada coluna da linha
        print()  # pula uma linha quando acabar as colunas da linha

def imprime_uns(num_linhas, num_colunas):
    for i in range(num_linhas):
        for j in range(num_colunas):
            print('1', end=' ')
        print()


matriz = cria_matriz(3, 4) # cria matriz 3x4 (3L x 4C)
print(matriz)  # imprime na forma primária (listas)
imprime_matriz(matriz) # imprime na forma de matriz
#imprime_uns(3, 4)
