# inicio
def exercicio1():
  nota1 = float(input("Digite a nota1: "))
  nota2 = float(input("Digite a nota2: "))

  soma = nota1 + nota2

  if soma < 10:
    return(f"Falhou com soma de notas igual a {soma}")
  else:
    return(f"Passou com soma de notas iguais a {soma}")

# fim

#inicio
def exercicio2():
  num_entradas = int(input("Digite o numero de entradas: "))
  lista = []
  #i = 0
  #while i < num_entradas:
    # instrucoes
    #lista.append( input() )
    # passo
    #i += 1
  for i in range(num_entradas):
    lista.append( input() )
  return(lista)
#fim

#inicio
def exercicio3():
  menu = {
    '1': "Sorvete",
    '2': "Chocolate",
    '3': "Torta"
  }
  opcao = input()  # input retorna string, ou texto
  while opcao != '9':
    # instrucoes
    if opcao in menu:
      print(menu[opcao])
    else:
      print("Invalido")
    # passo
    opcao = input()

  ''' Forma alternativa: 
  while opcao != '9':
    # instrucoes
    if opcao == '1':
      print("Sorvete")
    elif opcao == '2':
      print("Chocolate")
    elif opcao == '3':
      print("Torta")
    else:
      print("Inválido")
    # passo
    opcao = input()
  '''
#fim

#inicio
def exercicio4(lista):
  num_presencas = 0

  #exemplo3
  for elemento in lista:
    if elemento == 'p':
      num_presencas += 1

# como saber se o num_presencas é maior que ausencias.
# Se você só tem dois valores possíveis, p e f.
#   Se o numero de p(s) for maior que 50% tenho mais p(s)

  if num_presencas/len(lista) >= 0.5:
    return("Passou")
  else:
    return("Bombou")
#fim

