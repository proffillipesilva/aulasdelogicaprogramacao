# Funcionarios
# Gerente / Operario
# Gerente terá salario, registro, e um metodo trabalho - imprime sou gerente
# Operario terá salario, registro, Gerente e um metodo trabalho - imprime sou operario
# criar um classe chamada RH. Esse classe fará o seguinte:
#   Computar a media dos salarios dos funcionarios
#   Ela vai ordenar os salarios do menor para maior
from typing import List

class Funcionario:
    def __init__(self, registro: int, salario: float):
        self._registro = registro
        self._salario = salario

    def get_salario(self):
        return self._salario


class Gerente(Funcionario):
    def __init__(self, registro: int, salario: float):
        super().__init__(registro, salario)


class Operario(Funcionario):
    def __init__(self, registro: int, salario: float, gerente: Gerente):
        super().__init__(registro, salario)
        self._gerente = gerente


class RH:
    def __init__(self, funcionarios: List[Funcionario]):
        self._funcionarios = funcionarios

    def calcula_media_salarios(self):
        soma = 0
        for funcionario in self._funcionarios:
            soma += funcionario.get_salario()
        return soma/len(self._funcionarios)

    def ordena_salarios(self):
        lista = self._funcionarios[:]
        # quando trabalhar com posicao da lista, usar for i in range() ao invés de for elemento in lista
        for i in range(len(lista)):
            for j in range(i+1, len(lista)):
                if lista[i].get_salario() > lista[j].get_salario():
                    temp = lista[i]
                    lista[i] = lista[j]
                    lista[j] = temp
        return lista

#########  Estará pronto MAIN ############
gerente = Gerente(24, 6000)
operario1 = Operario(34, 4000, gerente)
operario2 = Operario(82, 1000, gerente)
operario3 = Operario(10, 8000, gerente)

funcionarios = [gerente, operario1, operario2, operario3]
rh = RH(funcionarios)
print(rh.calcula_media_salarios())
lista_ordenada = rh.ordena_salarios()
for funcionario in lista_ordenada:
    print(funcionario.get_salario())