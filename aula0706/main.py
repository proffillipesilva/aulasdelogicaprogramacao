import rhumanos
import setores

if __name__ == '__main__':

    gerente = rhumanos.Gerente(registro=1234,
              salario=6000, data_entrada="21/04/2015", cpf="242212300-64", nome="Sergio Baes",
                               data_nasc="12/05/1979", setor=1)

    operario1 = rhumanos.Operario(registro=4321,
                salario=2500, data_entrada="31/10/2020", cpf="454247823-69", nome="Carlos Santos",
                                 data_nasc="30/06/1999", setor=1)

    operario2 = rhumanos.Operario(registro=4381,
                                  salario=1900, data_entrada="01/10/2020", cpf="485247823-69", nome="Joao Beco",
                                  data_nasc="31/08/2001", setor=1)

    caldeiraria = setores.Producao(id=1, descricao="Caldeiraria", responsavel=1234)
    caldeiraria.insere_funcionario(gerente)
    caldeiraria.insere_funcionario(operario1)
    caldeiraria.insere_funcionario(operario2)

    print(caldeiraria.media_salarial_mensal())

    #lista = caldeiraria.ordena_por_salario()
    #for funcionario in lista:
        #print(funcionario)

    salarios_altos = caldeiraria.filtra_por_salario(2000)
    for funcionario in salarios_altos:
        print(funcionario)


    # Polimorfismo --> Ele exige um funcionario. Tanto gerente quanto operario são funcionarios

    #gerente.trabalha()
    #operario.trabalha()