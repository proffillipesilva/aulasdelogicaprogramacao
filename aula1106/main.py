import conta
import movimentacoes
import pessoa
if __name__ == '__main__':

    naruto = pessoa.Pessoa(cpf="15845221-01", nome="Naruto Usumaki")
    kakashi = pessoa.Pessoa(cpf="125442452-01", nome="Kakashi Sensei")
    conta_kakashi = conta.Conta(id=1234, pessoa=kakashi)
    print(conta_kakashi)
    conta_naruto = conta.Conta(id=3565, pessoa=naruto)
    print(conta_naruto)


    print(conta_kakashi.get_saldo())
    print(conta_naruto.get_saldo())

    deposito1 = movimentacoes.Deposito(remetente=conta_naruto, destinatario=conta_kakashi, valor=36)

    print(conta_kakashi.get_saldo())
    print(conta_naruto.get_saldo())

    conta_naruto.insere_deposito(deposito1)


