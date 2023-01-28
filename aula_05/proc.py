# CRIAR 02 PROFESSORES | 02 ALUNOS | 01 DISCIPLINA
# IMPRIMIR OS NOMES DOS PROFESSORES, OS EMAILS DOS ALUNOS, NOME E CARGA HORÁRIA DAS DISCIPLINAS.
# CRIAR AÇÃO PARA IMPRIMIR OS NOMES (PROFESSOR_1, ALUNO_1 E DISCIPLINAS) EM MAIÚSCULO E TAMBÉM EM MINÚSCULOS.

#Criação
professor_1 = {
    'nome': 'Julio',
    'email':'julio@gmail.com',
}

professor_2 = {
    'nome': 'Helio',
    'email':'helio@gmail.com',
}

aluno_1 = {
    'nome': 'Barbara',
    'email':'barbara@gmail.com'
}

aluno_2 = {
    'nome': 'Pedro',
    'email':'pedro@gmail.com'
}

disciplina = {
    'nome': 'Programando em python',
    'carga_horaria': '32 Horas'
}

# impressão
print(f'Professor 01 : {professor_1["nome"]}')
print(f'Professor 02 : {professor_2["nome"]}')
print(f'Aluno 01 : {aluno_1["nome"]}')
print(f'Aluno 02 : {aluno_2["nome"]}')
print(f'Disciplina : {disciplina["nome"]}')
print('======== *** ==========')

# Ações em variáveis
print(f'Professor 01 em Maiúsculo: {professor_1["nome"].upper()}')
print(f'Professor 01 em Minúsculo: {professor_1["nome"].lower()}')
print(f'Aluno 01 em Maiúsculo: {aluno_1["nome"].upper()}')
print(f'Aluno 01 em Minúsculo: {aluno_1["nome"].lower()}')
print(f'Disciplina em Maiúsculo: {disciplina["nome"].upper()}')
print(f'Disciplina em Minúsculo: {disciplina["nome"].lower()}')

print('======== *** ==========')

