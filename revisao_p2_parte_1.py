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

