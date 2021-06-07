class Setor:
    def __init__(self, id, descricao, responsavel):
        self._id = id
        self._descricao = descricao
        self._responsavel = responsavel
        self._funcionarios = []

    def insere_funcionario(self, funcionario):
        self._funcionarios.append(funcionario)

    def demite_funcionario(self, funcionario):
        # para implementar

    def media_salarial_mensal(self):
        # implementem esse método
        soma = 0
        for funcionario in self._funcionarios:
            soma += funcionario.get_salario()
        return soma/len(self._funcionarios)

    def ordena_por_salario(self):
        # ordenar por salario em ordem decrescentes
        lista = self._funcionarios[:]  # clone para não modificar a lista original
        for i in range(len(lista)):
            for j in range(i+1, len(lista)):
                if lista[i].get_salario() < lista[j].get_salario():  # talvez mude
                    temp = lista[i]
                    lista[i] = lista[j]
                    lista[j] = temp
        return lista

    def filtra_por_salario(self, salario):
        return list(filter(lambda funcionario: funcionario.get_salario() >= salario, self._funcionarios))



class Producao(Setor):
    def __init__(self, id, descricao, responsavel):
        super().__init__(id, descricao, responsavel)


class Administrativo(Setor):
    def __init__(self, id, descricao, responsavel):
        super().__init__(id, descricao, responsavel)

