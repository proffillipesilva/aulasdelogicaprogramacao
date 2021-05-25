def maximo(n1,n2):
    if n1 > n2:
        return n1
    else:
        return n2

def media(lista):
    soma = 0
    for elemento in lista:
        soma += elemento
    return soma/len(lista)

def exer3():
    lista = [ 3, 7, 9, 0, 2, 11]
    media_primeiros = media(lista[:3])
    media_ultimos = media(lista[-3:])
    print(maximo(media_primeiros, media_ultimos))


def exer4():
    notas = []
    with open('./input.txt', 'r') as entrada:
        linhas = entrada.readlines()
        notas = list(map(lambda n: int(n), linhas))
        entrada.close()
    with open('./saida.txt', 'w') as saida:
        conteudo = []
        conteudo.append(f'Minimo   {min(notas)}')
        conteudo.append(f'Maximo   {max(notas)}')
        conteudo.append(f'Media   {sum(notas)/len(notas)}')
        saida.write(str.join('\n', conteudo))
        saida.close()


def exer5(nlinhas, ncolunas):
    from random import randint
    matriz = []
    for i in range(nlinhas):
        linha = []
        for j in range(ncolunas):
            linha.append(randint(0,9))
        matriz.append(linha)
    return matriz


def imprime_matriz(matriz):
    for i in range(len(matriz)):
        linha = matriz[i]
        for j in range(len(linha)):
            print(matriz[i][j], end=' ')
        print()

def exer5_testar():
    matriz = exer5(5,8)
    imprime_matriz(matriz)




