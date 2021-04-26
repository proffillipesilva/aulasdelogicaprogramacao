import os

# print( os.environ["HOME"]  )

file = open("./teste.txt", "r")
conteudo = file.read()  # flush / leu apaga da memória
linhas = file.readlines()  # quando esse tentar ler, não vai ter mais nada
file.close()
# print(conteudo)
print(linhas)


