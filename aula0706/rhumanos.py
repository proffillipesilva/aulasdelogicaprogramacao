class Pessoa:
    def __init__(self, cpf, nome, data_nasc):
        self._cpf = cpf
        self._nome = nome
        self._data_nasc = data_nasc

    def aloha(self):
        pass


class Funcionario(Pessoa):
    def __init__(self, registro, salario, data_entrada, cpf, nome, data_nasc, setor):
        super().__init__(cpf, nome, data_nasc)
        self._registro = registro
        self._salario = salario
        self._data_entrada = data_entrada
        self._setor = setor

    def get_salario(self):
        return self._salario

    def trabalha(self):
        print("Funcionario trabalhando")

    def __str__(self):
        return f'{self._registro} \t {self._nome} \t {self._salario} '


class Operario(Funcionario):
    def __init__(self, registro, salario, data_entrada, cpf, nome, data_nasc, setor):
        super().__init__(registro, salario, data_entrada, cpf, nome, data_nasc, setor)

    def get_salario_anual(self):
        # 12x + 13 + ferias + PLR (1.2 salarios) + Horas Extra



class Gerente(Funcionario):
    def __init__(self, registro, salario, data_entrada, cpf, nome, data_nasc, setor):
        super().__init__(registro, salario, data_entrada, cpf, nome, data_nasc, setor)

    def trabalha(self):  # Especialização
        print("Gerente trabalhando")

    def get_salario_anual(self):
        # 12x + 13 + PLR (1.6 salarios)