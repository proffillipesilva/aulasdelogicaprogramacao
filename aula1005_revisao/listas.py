"""
Usando nossas proprias funcoes
"""
def maximo( lista ):
    maximo = lista[0]
    for elemento in lista:
        if elemento > maximo:
            maximo = elemento
    return maximo

def maximo_4_valores(a, b, c, d):
    if a > b and a > c and a > d:
        return a
    elif b > c and b > d:
        return b
    elif c > d:
        return c
    else:
        return d

def maximo_4_valores_smart(a, b, c, d):
    return maximo([a, b, c, d])

def ordena_lista( lista ):
    # eu pego o primeiro menor
    # depois, o segundo menor
    # depois, o terceiro menor...
    for i in range( len(lista) ):
        for j in range(i+1, len(lista)):
            if lista[i] > lista[j]:
                temp = lista[i]
                lista[i] = lista[j]
                lista[j] = temp
    return lista

def soma(lista):
    total = 0
    for elemento in lista:
        total += elemento
    return total


lista = [3, 1, 5, 2]
print(maximo_4_valores(3, 1, 5, 2))
print(maximo_4_valores_smart(3, 1, 5, 2))
print( soma(lista))
print(  ordena_lista(lista)[ -2 : ] )
""" somar os dois maiores elementos"""
print( soma(ordena_lista(lista)[-2:]) )
""" media dos dois últimos elementos elementos"""
print( soma(ordena_lista(lista)[-2:])/2 )
maiores = ordena_lista(lista)[-2:]
print(soma(maiores)/len(maiores))


