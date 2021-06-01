from pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, rm, turma_id, rg, nome):
        super().__init__(rg, nome)
        self._rm = rm
        self._turma_id = turma_id
        self._notas = []

    def media(self):
        if len(self._notas) > 0:
            return sum(self._notas)/len(self._notas)
        else:
            return None

    def insere_nota(self, nota):
        self._notas.append(nota)

    #to_string --> várias linguagens --> transforma um objeto em uma representação do mesmo em texto
    def __str__(self):
        return f'RM: {self._rm} - Nome: {self._nome}'


