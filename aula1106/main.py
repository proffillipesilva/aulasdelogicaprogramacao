from conta import Conta
from movimentacoes import Deposito
from pessoa import Pessoa

if __name__ == '__main__':
    naruto = Pessoa(cpf="15845221-01", nome="Naruto Usumaki")
    kakashi = Pessoa(cpf="125442452-01", nome="Kakashi Sensei")
    conta_kakashi = Conta(id=1234, pessoa=kakashi)
    print(conta_kakashi)
    conta_naruto = Conta(id=3565, pessoa=naruto)
    print(conta_naruto)


    print(conta_kakashi.get_saldo())
    print(conta_naruto.get_saldo())

    deposito1 = Deposito(remetente=conta_naruto, destinatario=conta_kakashi, valor=36)

    print(conta_kakashi.get_saldo())
    print(conta_naruto.get_saldo())


