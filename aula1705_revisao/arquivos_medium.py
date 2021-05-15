produtos = []
precos = []
with open('./lista_de_compras.txt', 'r') as compras:
    try:
        linhas = compras.readlines()
        for linha in linhas:
            [produto, preco] = linha.split(',')
            produtos.append(produto)
            precos.append(float(preco))
    except:
        print('deu ruim')
    compras.close()

with open('./nota_fiscal_plus.txt', 'w') as nota_fiscal:
    linhas_da_nota = []
    for i in range(len(produtos)):
        linhas_da_nota.append(f'{produtos[i]} \t {precos[i]}')
    linhas_da_nota.append('===========')
    linhas_da_nota.append(f'Total \t {sum(precos)}')
    nota_fiscal.write( str.join('\n', linhas_da_nota) )
    nota_fiscal.close()