# opcional: variáveis de ambiente
# obrigatoria: open

# duas formas de interagir com arquivos:  (leitura, escrita)
  # para leitura, você tem um modo: 'r'.
  # para escrita, você tem dois modos: 'w' --> escreve do zero   'a' --> incrementa no arquivo

# nota fiscal:
# produto   \tab     preco
# ========================
# total:           sum(precos)

with open('./lista_precos.txt', 'r') as arquivo_de_entrada:
    try:
        linhas = arquivo_de_entrada.readlines()
        precos = list(map( lambda x: float(x), linhas))
    except:
        print('deu errado')
    arquivo_de_entrada.close()

with open('./nota_fiscal.txt', 'w') as nota_fiscal:
    linhas_da_nota = []
    for preco in precos:
        linhas_da_nota.append(f'tomate \t {preco}')
    linhas_da_nota.append('====================')
    linhas_da_nota.append(f'Total \t {sum(precos)}')
    # nota_fiscal.writelines(conteudo)
    nota_fiscal.write(str.join('\n', linhas_da_nota))
    nota_fiscal.close()