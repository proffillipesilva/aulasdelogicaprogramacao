from aluno import Aluno
from turma import Turma
from coordenador import Coordenador


enrico = Aluno(rm=32608, turma_id=1, rg='4545',nome='Enrico')
isadora = Aluno(rm=32615, turma_id=1, rg='5646',nome='Isadora')
ana = Aluno(rm=32600, turma_id=1, rg='5466', nome='Ana')

coordenador = Coordenador('TI/EDIFICACOES', '564632', 'Samuel Silva')
turma_ti = Turma(criterio=6, coordenador=coordenador, turma_id=1)

enrico.insere_nota(nota=6)
enrico.insere_nota(nota=8)
ana.insere_nota(nota=10)
ana.insere_nota(nota=7)
isadora.insere_nota(nota=4)
isadora.insere_nota(nota=2)

turma_ti.insere_aluno(enrico)
turma_ti.insere_aluno(ana)
turma_ti.insere_aluno(isadora)

print(f'Media da turma {turma_ti.get_turma_id()} : {turma_ti.media_da_turma()}')
turma_ti.imprime_aprovados()




# <turma.Turma object at 0x7fdbee9f0e80>
# Localização da classe/objeto na memória --> esse é o padrão
# para sobreescrever o padrão, você deve implementar o método __str__

# Esses métodos __init__ (construtor)  e __str__ (to_string) eles têm um padrão
