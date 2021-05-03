from functools import reduce

lista = [2, 8, 9, 13, 14, 5, 0, 1, 2]

valores = list(filter(lambda x: x >= 5, lista))
quadrados = list(map(lambda x: x*x, lista))

#print(valores)
#print(quadrados)
nova_lista = ['a', 'b', 'c', 'd']

print(str.join('-', nova_lista))
print( str.join( '|--|', map( lambda x: str(x), valores ) ) )

# Some todos os valores menores que 10
# print( sum( filter(lambda x: x<10, lista) ) )

conteudo1 = { 'likes': 32, 'dislikes': 20 }
conteudo2 = { 'likes': 10, 'dislikes': 10 }
conteudo3 = { 'likes': 16, 'dislikes': 5 }
conteudos = [ conteudo1, conteudo2, conteudo3 ]

print(reduce(lambda x, y: x + y['likes'], conteudos, 0))

fatores = [7,6,5,4,3,2,1]
print( reduce( lambda x, y: x * y, fatores, 1 )