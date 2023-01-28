# Programação Procedural ou estruturada
# (programação funcional)

# CRIAR 02 PROFESSORES | 02 ALUNOS | 01 DISCIPLINA
# IMPRIMIR OS NOMES DOS PROFESSORES, OS EMAILS DOS ALUNOS, NOME E CARGA HORÁRIA DAS DISCIPLINAS.
# CRIAR AÇÃO PARA IMPRIMIR OS NOMES (PROFESSOR_1, ALUNO_1 E DISCIPLINAS) EM MAIÚSCULO E TAMBÉM EM MINÚSCULOS.
'''
#Criação
#funções auxiliadora
def cria_professor(nome, email):
    return {
        'nome': nome,
        'email': email,
}

criar_aluno = lambda nome, email: {'nome': nome, 'email':email}

#Coleções
professor_1 = cria_professor('Julio', 'julio@gmail.com')

professor_2 = cria_professor('Helio','helio@gmail.com')

aluno_1 = criar_aluno('Barbara', 'barbara@gmail.com')

aluno_2 = criar_aluno('Pedro', 'pedro@gmail.com')

disciplina = {
    'nome': 'Programando em python',
    'carga_horaria': '32 Horas'
}


# impressão
#funções auxiliadora
def imprimir_professores(professores: list):
    
    for professor in professores:
        posicao = professores.index(professor) + 1
        print(f'Professor 0{posicao} : {professor}')
        
def imprimir_alunos(alunos: list):
    
    for aluno in alunos:
        posicao = alunos.index(aluno) + 1
        print(f'Aluno 0{posicao} : {aluno}')
        
# impressão   
imprimir_professores([professor_1["nome"], professor_2["nome"]])
imprimir_alunos([aluno_1["nome"], aluno_2["nome"]])
print(f'Disciplina : {disciplina["nome"]}')
print('======== *** ==========')


# Ações em variáveis
#funções auxiliadora
imprimir_maiusculo = lambda pessoa, valor: print(f'{pessoa} em Maiúsculo: {valor["nome"].upper()}')
imprimir_minusculo = lambda pessoa, valor: print(f'{pessoa} em Maiúsculo: {valor["nome"].lower()}')
# impressão
imprimir_maiusculo('Professor 01', professor_1)
imprimir_minusculo('Prefessor 01', professor_1)
imprimir_maiusculo('Aluno 01', aluno_1)
imprimir_minusculo('Aluno 01', aluno_1)
imprimir_maiusculo('Disciplina', disciplina)
imprimir_minusculo('Disciplina', disciplina)

print('======== *** ==========')

'''