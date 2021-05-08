import json
texto = '''{ "fiec": "instituicao_feliz", "alunos": [5,6,9], "prof": { "ti": { "hard": "Fillipe"}}}'''
dicionario = json.loads(texto)
print(dicionario)

#1) imprima o valor da chave fiec   ex: print( resultado['fiec'] )
print(dicionario['fiec'])
#2) imprima o tamanho da lista alunos
print( len(dicionario['alunos']) )
#3) imprima o valor do professor de ti
print( dicionario['prof'])
print( dicionario['prof']['ti'])
print( dicionario['prof']['ti']['hard'])

texto_de_novo = json.dumps(dicionario)
print(texto_de_novo)



