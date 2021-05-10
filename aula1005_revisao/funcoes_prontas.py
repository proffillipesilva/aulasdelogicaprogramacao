"""
1) Operadores de uma linha
   max, min, sum, len, sorted
2) Operadores com lambda
   filter e map
3) Converter para texto --> str.join
3) Criação de lista com uma linha
  [ valor for x in range(tamanho_da_lista) ]
"""
lista = [8,6,5,4,12,2,-3,0,9]

# maximo
print( max(lista) )
# minimo
print( min(lista) )
# soma
print( sum(lista))
# tamanho
print( len(lista))
# media --> soma/tamanho
print( sum(lista)/len(lista))
# ordenacao
print( sorted(lista))
# ordenacao decrescente
print( sorted(lista, reverse=True))

# FILTRAGEM
def eh_par(num):                # -->  lambda num: num % 2 == 0
    if num % 2 == 0:
        return True
    else:
        return False

print( eh_par(4) )
# print(   filter( eh_par, lista ) )

# FILTER POR BAIXO DOS PANOS
def meu_filtro( fn, lista):
    filtrados = []
    for elemento in lista:
        if fn(elemento):
            filtrados.append(elemento)
    return filtrados

print(meu_filtro( lambda num : num > 3, lista ) )

# Usando o filter do python
print( list( filter( lambda num : num > 3, lista )) )   # stream --> #lista

# Usando o MAP --> mapeia um elemento em outro
# 1) Exemplo: Vou multiplicar por 2 cada elemento

print( list(map( lambda n: n*2, lista )))
# 2) Exemplo: converter para numero
lista_precos = ['13.99', '45.90', '1.99', '3.99']

print ( list( map( lambda preco: float(preco), lista_precos) ))

# Quero converter uma lista em um texto, usando um delimitador para cada posição
# JOIN é o contrário do SPLIT
texto = "Aloha 123 Konoha Naruto"
lista_texto = texto.split(' ')
print(lista_texto)
# Testando o JOIN
print( str.join(' ', lista_texto))

print( str.join('--', lista_precos))
print( str.join('\n', lista_precos))
