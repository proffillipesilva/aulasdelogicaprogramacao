from aluno import Aluno
from prova import Prova
from responsavel import Responsavel

if __name__ == '__main__':
    responsavel = Responsavel(idade=39, rg='345666')
    prova1 = Prova(id=1, materia='Matematica',conceito=9.5)
    prova2 = Prova(id=2, materia='Geometria', conceito=4.5)
    weslley = Aluno(idade=17, responsavel=responsavel, provas=[prova1, prova2])

    print(weslley)
    print(weslley.get_media_notas())