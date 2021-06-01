class Turma:
    def __init__(self, turma_id, criterio, coordenador):
        self._lista_alunos = []
        self._criterio = criterio
        self._coordenador = coordenador
        self._turma_id = turma_id

    def get_turma_id(self):  # getter / expoe um atributo privado
        return self._turma_id

    def insere_aluno(self, aluno):
        self._lista_alunos.append(aluno)

    def media_da_turma(self):
        if len(self._lista_alunos) == 0:
            return None
        soma_das_medias = 0
        for aluno in self._lista_alunos:
            soma_das_medias += aluno.media()
        return soma_das_medias/len(self._lista_alunos)

    def _filtra_aprovados(self):
        return list(
            filter(
                lambda aluno: aluno.media() >= self._criterio,
                self._lista_alunos
            )
        )

    def imprime_aprovados(self):
        print('### APROVADOS ###')
        lista_aprovados = self._filtra_aprovados()
        for aluno in lista_aprovados:
            print(aluno)
        print('#################')
        print('## COORDENADOR RESPONSAVEL ##')
        print(self._coordenador)
        print('#################')

