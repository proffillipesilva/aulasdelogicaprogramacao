# inicio
def exercicio1():
  nota1 = float(input("Digite a nota1: "))
  nota2 = float(input("Digite a nota2: "))

  soma = nota1 + nota2

  if soma < 10:
    print(f"Falhou com soma de notas igual a {soma}")
  else:
    print(f"Passou com soma de notas iguais a {soma}")

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

