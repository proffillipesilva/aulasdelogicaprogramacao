import os

pasta_downloads = os.environ['HOME'] + '/Downloads'

file = open(pasta_downloads + "/exemplopython.txt", "r")
conteudo = file.read()  # flush / leu apaga da memória
file.close()
print(conteudo)