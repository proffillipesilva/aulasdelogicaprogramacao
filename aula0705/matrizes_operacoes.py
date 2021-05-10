"""def multiplicacao_matrizes(matrizA, matrizB):
    matrizC = []
    for i in range(len(matrizB)):
        for j in range(len(matrizA)):
            ....

"""
def soma_matriz(matrizA, matrizB):
    matrizC = []
    for i in range(len(matrizA)):
        linha = matrizA[i]
        linha_resultado = []
        for j in range(len(linha)):
            linha_resultado.append( matrizA[i][j] + matrizB[i][j] )
        matrizC.append(linha_resultado)
    return matrizC

matrizA = [ [3, 4], [0,1]]
matrizB = [ [-3, 6], [0, 4]]
print( soma_matriz(matrizA, matrizB ) )