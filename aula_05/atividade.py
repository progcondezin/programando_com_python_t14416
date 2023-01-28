'''

# CRIAR 02 PROFESSORES | 02 ALUNOS | 01 DISCIPLINA
# IMPRIMIR OS NOMES DOS PROFESSORES, DOS ALUNOS, DA DISCIPLINA.
# CRIAR AÇÃO PARA IMPRIMIR OS NOMES (PROFESSOR_1, ALUNO_1 E DISCIPLINA) EM LETRA MAIÚSCULA E TAMBÉM EM MINÚSCULA.

INFORMAÇÕES
PROFESSORES => Nome e email
ALUNOS => Nome e email
Disciplina => Nome e carga horária

'''

from oop import Professor, Aluno, Disciplina


Professor_1 = Professor('julio Pereira', 'julio@gmail.com', 'programando com python')
Professor_2 = Professor('helio', 'helio@gmail.com', 'programando com python')

aluno_1 = Aluno('Barbara', 'barbara@gmail.com', 't13416')
aluno_2 = Aluno('pedro', 'pedro@gmail.com', 't13416')

disciplina = Disciplina('Programando em python', 32)


print(f'Professor 01 : {Professor_1.nome}')
print(f'Professor 02 : {Professor_2.nome}')

print(f'Aluno 01: {aluno_1.nome}')
print(f'Aluno 02: {aluno_2.nome}')


print(f'Professor 01 em Maiúsculo: {Professor_1.nome_em_maiusculo()}')
print(f'Professor 01 em minúsculo: {Professor_1.nome_em_minusculo()}')


print(f'Aluno 01 em Maiúsculo: {aluno_1.nome_em_maiusculo()}')
print(f'Aluno 01 em minúsculo: {aluno_1.nome_em_minusculo()}')


print(f'Disciplina em Maiúsculo: {disciplina.nome_em_maiusculo()}')
print(f'Disciplina em minúsculo: {disciplina.nome_em_minusculo()}')
