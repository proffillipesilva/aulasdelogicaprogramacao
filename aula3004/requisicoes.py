import requests
endereco = 'https://pt.wikipedia.org/wiki/League_of_Legends'
endereco_google = 'https://www.google.com.br/search?q=LOL'
resposta = requests.get(endereco_google)
dicionario = {}

texto = resposta.text
print(texto)