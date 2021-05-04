import requests


resposta = requests.get('https://www.w3schools.com/angular/customers.php')
resultado = resposta.text
