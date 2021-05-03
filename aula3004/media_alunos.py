with open('../aluninhos.csv', 'r') as file:
    # file.read() --> le o arquivo inteiro
    # file.readlines() --> converte cada linha em uma posição de uma lista
    dicionario = {}
    linhas = file.readlines()
    for linha in linhas:
        linha = linha.strip('\n').strip()
        lista = linha.split(',')
        nome = lista[0]
        notas = lista[1:]
        notas = list(map(lambda x: float(x), notas))
        media = sum(notas)/len(notas)
        dicionario[nome] = media

    print(dicionario)
    file.close()