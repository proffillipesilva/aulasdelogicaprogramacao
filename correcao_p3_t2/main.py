# calcule media dois numeros
def media_dois(n1, n2):
    return (n1+n2)/2

# ordene uma lista e a retorne
def ordena_lista(lista):
    tam = len(lista)
    for i in range(tam):
        for j in range(i+1, tam):
            if lista[i] > lista[j]:
                temp = lista[i]
                lista[i] = lista[j]
                lista[j] = temp
    return lista

# ordene uma lista e a retorne
def ordena_lista_dec(lista):
    tam = len(lista)
    for i in range(tam):
        for j in range(i+1, tam):
            if lista[i] < lista[j]:
                temp = lista[i]
                lista[i] = lista[j]
                lista[j] = temp
    return lista

def exer3():
    lista = [6, 4, 3, 8]
    lista_ordenada = ordena_lista(lista)
    [m1, m2] = lista_ordenada[-2:]
    print(media_dois(m1,m2))

def exer4():
    produtos=[]
    precos=[]
    with open('./input.txt', 'r') as entrada:
        linhas = entrada.readlines()
        for linha in linhas:
            [produto,preco] = linha.split(',')
            produtos.append(produto)
            precos.append(float(preco))
        entrada.close()

    with open('./output.txt', 'w') as saida:
        conteudo = []
        for i in range(len(produtos)):
            conteudo.append(f'{produtos[i]} -- {precos[i]} \n')
        conteudo.append('===============\n')
        conteudo.append(f'Total -- {sum(precos)}')
        saida.writelines(conteudo)
        saida.close()


''' ==============  EXERCICIO 5 ==================  '''

def cria_matriz(nlinhas,ncolunas):
    matriz = []
    for i in range(nlinhas):
        linha = []
        for j in range(ncolunas):
            linha.append('1')
        matriz.append(linha)
    return matriz


def imprime_matriz(matriz):
    for i in range(len(matriz)):
        linha = matriz[0]
        for j in range(len(linha)):
            print(matriz[j][i], end=' ')
        print()

def transposta(matriz):
    linha = matriz[0]
    for j in range(len(linha)):
        for i in range(len(matriz)):
            print(matriz[i][j], end=' ')
        print()

def exer5():
    matriz = cria_matriz(5,3)
    imprime_matriz(matriz)

exer5()



