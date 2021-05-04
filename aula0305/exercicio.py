# peguem o conteudo do site https://www.w3schools.com/angular/customers.php
# usando o requests

# Transforme o texto em dicionario usando o json.loads
# Obtenha a lista records desse dicionario
# imprimam somente a chave "Name" para essa lista records

import requests
import json
resposta = requests.get('https://www.w3schools.com/angular/customers.php')  # API
dicionario = json.loads(resposta.text)  # traduzo via json
# processo a informacao
records = dicionario['records']

for record in records:
    print(record["Country"])
