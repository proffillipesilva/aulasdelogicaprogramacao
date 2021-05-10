"""   Posicoes de uma lista   """
lista = [ 5, 3, 6, 8, 6, 7, 8 ]

# O Clone da lista
print(lista[:])

# Todos menos os dois primeiros
print(lista[2:])
# Os dois primeiros
print(lista[ : 2])

# O segundo e o terceiro elemento
print( lista[1:3])

# Os tres ultimos
print(lista[-3:])
# Sem ser os dois primeiros nem os dois ultimos
print(lista[ 2 : -2])