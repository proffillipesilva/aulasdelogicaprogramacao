class Aluno:
    # Esse método é usado na invocação de uma classe
    def __init__(self, rm, turma_id):
        self._rm = rm
        self._turma_id = turma_id
        self._notas = [10,5]

    # Esse método é chamado toda vez que você fizer o print dela
    def __str__(self):
        return f'{self._rm} com notas {self._notas}'

    def media_aluno(self):
        return sum(self._notas)/len(self._notas)


class Turma:
    def __init__(self, turma_id, lista_alunos):
        self._turma_id = turma_id
        self._lista_alunos = lista_alunos
        self._criterio = 6

    def media_turma(self):
        soma = 0
        for aluno in self._lista_alunos:
            soma += aluno.media_aluno()
        return soma/len(self._lista_alunos)

    def lista_de_aprovados(self):
        aprovados = list(
            filter(lambda aluno: aluno.media_aluno() >= self._criterio,
                   self._lista_alunos)
        )
        return aprovados

    def __str__(self):
        return f'Essa é a turma {self._turma_id}'

# Próxima aula: Definir como inserir notas para os alunos



aluno = Aluno(36531, 1)
lista_de_alunos = [aluno]
turma1 = Turma(1, lista_de_alunos)
print(turma1)
print(f'A média dela é: {turma1.media_turma()}')
print('Alunos aprovados:')
for aluno in turma1.lista_de_aprovados():
    print(aluno)

