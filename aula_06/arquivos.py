#DBA
# ED
# CD
# AD
# BI
import os

'''
try:
    transforma_inteiro =  int('r10')
#    print('deu super certo')

except AttributeError:
    print('ERRO DE ATRIBUTO')

except ValueError as erro:
    print(erro)
'''

# CRIAR ARQUIVO

usuarios = [
    'julio',
    'ana',
    'ricardo'
]

# abrir para gravar informações(w)
arquivo_para_gravar = open('usuarios.txt', 'w') #r = read, w=write

arquivo_para_gravar.write(f'nome\n') # primeira linha(cabeçalho)

# Gravo cada nome em usuarios no arquivo que abri
for user in usuarios:
    arquivo_para_gravar.write(f'{user}\n')

#Fecho o arquivo
arquivo_para_gravar.close()


# LER ARQUIVOS

try:
    #lendo usuarios
    arquivo_para_ler = open('usuarios.txt', 'r')

    arquivo = ''

    for linha in arquivo_para_ler:
        arquivo += linha
        # print(linha[:-1])

    # print(arquivo)

    arquivo_para_ler.close()


    #Lendo a disciplina
    nome_mateira = open('materia.txt')

    materia = nome_mateira.read(11)

    posicao = nome_mateira.tell()

    nome_1 = nome_mateira.read()

    # print(materia)
    # print(posicao)
    # print(nome_1)

    nome_mateira.close()

    # Renomear arquivo
    # os.rename('materia.txt', 'disciplina.txt')

    # remover arquivos
    # os.remove('usuarios.txt')


except: # FileNotFoundError:

    print('Este arquivo não essta nesta pasta!')



arquivo = 'arquivos.py'

verifica_arquivo = os.path.exists(arquivo)

if verifica_arquivo:
    pass
    # print('Encontrou o arquivo!')
else:
    pass
    # print('O arquivo não existe na pasta!')

# verificar se e arquivo
verifica_se_e_arquivo = os.path.isfile(arquivo)

# print(verifica_se_e_arquivo)

pasta = '../aula_01'
# verifica se é uma pasta
verifica_pasta = os.path.isdir(pasta)

# print(verifica_pasta)

#Qual pasta estamos
onde_estou = os.getcwd()
# print(onde_estou)

#navegar por pastas
os.chdir(f'../aula_05')

onde_estou_atualizado = os.getcwd()

# print(onde_estou_atualizado)


os.chdir(f'../aula_06')
#criar pasta
# os.mkdir('nome_da_pasta')

#remover pasta
# os.rmdir('nome_da_pasta')

# ver arquivos e pastas
dados = os.listdir()

for x in dados:
    if x == 'usuarios.csv':
        pass
        # print('peguei a planilha')



#CSV
import csv


#Ler arquivo csv
with open('usuarios.csv') as arquivo_csv:
    arquivo_csv_lido = csv.reader(arquivo_csv, delimiter=',')

    colunas = []

    for i, linha in enumerate(arquivo_csv):
        if i == 0:
            # print(f'Cabeçalho: {linha[:4]}')
            pass
        else:
            # criar uma lista separando por virgula
            dados = linha.split(',')
            # print(dados)
            # print(f'Usuario 0{i}: {dados[0]}')


# Gravar arquivo csv

alunos_novos = [
    ['julio pereira', 'julio@mail.com'],
    ['grabiel', 'gabriel@email.com']
]

with open('alunos_novos.csv', 'w') as arquivo_csv:
    gravar = csv.writer(arquivo_csv, delimiter=';')
    gravar.writerow(['nome', 'email'])
    gravar.writerows(alunos_novos)


# EXCEL

import openpyxl

pasta = openpyxl.load_workbook(filename='usuarios.xlsx')


for dados in pasta['usuarios'].iter_rows(values_only=True):
    print(dados[0])





