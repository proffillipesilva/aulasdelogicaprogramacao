# MENU

# DIFERENCA EXERCICIO MENU x EXERCICIO LISTA
# Exercício do Banco
# Crie um menu no qual:
# 1) faz um deposito de um valor a ser colocado pelo cliente, se o usuario entrar com 1
# 2) faz um saque de um valor a ser colocado pelo cliente se opção for 2
# 3) faz uma transferencia para um valor a ser colocado pelo cliente se opção for 3
# 4) mostra o saldo se opção for 4
# 5) Se opção for 0
# 6) Mostra Inválido

# Criem uma classe Operacao (conta, valor, tipo) e outra Conta para esse exercicio
# Criem um classe Conta (nome, saldo)
# Salvem as operacoes em uma lista
class Conta:
    def __init__(self, nome: str, saldo: float):
        self._nome = nome
        self._saldo = saldo

    def get_saldo(self):        # Você terá que mostrar o saldo
        return self._saldo

    def altera_saldo(self, valor):  # Você terá que alterar o saldo
        self._saldo += valor

class Operacao:
    def __init__(self, conta: Conta, valor: float, tipo: str):
        self._conta = conta
        self._valor = valor
        self._tipo = tipo

# ========== MAIN ========= #
conta_nicolle = Conta('Nicolle', 25)
conta_alexandre = Conta('Alexandre', 42)
operacoes = []

# Assumindo que você é a nicolle
opcao = int(input())
while opcao != 0:
    if opcao == 1:
        valor_do_deposito = float(input("Digite o valor a ser depositado: "))
        conta_nicolle.altera_saldo(valor_do_deposito) # aqui você adiciona um valor na conta da nicolle
        operacoes.append(Operacao(conta_nicolle, valor_do_deposito, 'Deposito'))
    elif opcao == 2:
        valor_do_saque = float(input("Digite o valor a ser sacado: "))
        conta_nicolle.altera_saldo(-valor_do_saque)  # aqui você tira da nicolle
        operacoes.append(Operacao(conta_nicolle, valor_do_saque, 'Saque'))
    elif opcao == 3:
        valor_da_transferencia = float(input("Digite o valor a ser transferencia: "))
        conta_nicolle.altera_saldo(-valor_da_transferencia) # você tira da nicolle
        conta_alexandre.altera_saldo(valor_da_transferencia) # você coloca pro alexandre
        operacoes.append(Operacao(conta_nicolle, valor_da_transferencia, 'Transferencia'))
    elif opcao == 4:
        print(conta_nicolle.get_saldo())
    else:
        print('Opcao inválida')

    opcao = int(input())















# loop
    # lista
    # inicio --> 0
    # condicao --> menor que len(lista)
    # passo --> i += 1 (de um em um)

    # menu
    # inicio --> input()
    # não pode ser condicao de parada (termino)
    # passo --> input()

   # lista --> for i in range(tam)  ou  for elem in lista
   # menu -->  o=input() - while o != <termino> - o=input()