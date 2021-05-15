# Objetivo:
# Criar um arquivo que mostre:
# Aluno -- media
# ===============================
# Aprovados  ---   total_aprovado ( media >= 6 )

alunos = []
medias = []
with open('./alunos.txt', 'r') as arquivo_alunos:
    try:
        linhas = arquivo_alunos.readlines()
        for linha in linhas:
            linha_com_split = linha.split(',')
            alunos.append(linha_com_split[0])
            notas = list(map(lambda nota: float(nota), linha_com_split[1:]))
            media = sum(notas)/len(notas)
            medias.append(media)
        print(medias)
    except:
        print('deu ruim')
    arquivo_alunos.close()

with open('./boletim_classe.txt', 'w') as boletim:
    linhas_do_boletim = []
    for i in range(len(alunos)):
        linhas_do_boletim.append(f'{alunos[i]} \t {medias[i]}')
    linhas_do_boletim.append('================')
    aprovados =  len( list( filter(lambda media: media >= 6, medias) ) )

    linhas_do_boletim.append(f'Aprovados \t {aprovados}')
    boletim.write(str.join('\n', linhas_do_boletim))

    boletim.close()