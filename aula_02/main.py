"""  
    EXERCICIO 01
    
    Escrever um programa em Python que solicite informações de três pessoas, 
    como nome, idade, peso e altura. Apresentar na tela estas informações de modo que permaneçam alinhados verticalmente. 
    Usar a formatação de interpolação.

"""

# Pegar informacoes de tres pessoas
# armazenar estas informacoes em variaveis

# pegando os dados da primeira pessoa
# nome_1 = input("Escreva o nome da PRIMEIRA pessoa: ")
# idade_1 = int(input("Escreva a idade da PRIMEIRA pessoa: "))
# peso_1 = float(input("Escreva o peso da PRIMEIRA pessoa: "))
# altura_1 = float(input("Escreva a altura da PRIMEIRA pessoa: "))

# pegando os dados da segunda pessoa
# nome_2 = input("Escreva o nome da SEGUNDA pessoa: ")
# idade_2 = int(input("Escreva a idade da SEGUNDA pessoa: "))
# peso_2 = float(input("Escreva o peso da SEGUNDA pessoa: "))
# altura_2 = float(input("Escreva a altura da SEGUNDA pessoa: "))

# pegando os dados da terceira pessoa
# nome_3 = input("Escreva o nome da TERCEIRA pessoa: ")
# idade_3 = int(input("Escreva a idade da TERCEIRA pessoa: "))
# peso_3 = float(input("Escreva o peso da TERCEIRA pessoa: "))
# altura_3 = float(input("Escreva a altura da TERCEIRA pessoa: "))

# mostrar as informacoes na tela do usuario verticalmente.

# print("======== DADOS DA PRIMEIRA PESSOA ==========")
# print(f" Nome: {nome_1}, idade: {idade_1}, peso: {peso_1}, altura: {altura_1}")
# print("")

# print("======== DADOS DA SEGUNDA PESSOA ==========")
# print(f" Nome: {nome_2}, idade: {idade_2}, peso: {peso_2}, altura: {altura_2}")
# print("")

# print("======== DADOS DA TERCEIRA PESSOA ==========")
# print(f" Nome: {nome_3}, idade: {idade_3}, peso: {peso_3}, altura: {altura_3}")




numero = 10

# if numero == 10 and numero == 13:
#     print("O numero e 10")
# elif numero == 12 or numero == 11:
#     print("o numero e doze ou onze")
# else:
#     print("o numero nao e o 10")


n1 = 10
n2 = 12
n3 = 20
n4 = 39


op_1 = n1 / n2 # divisao real
op_2 = n1 // n2 # divisao inteira
op_3 = n1 % n2 # resto de divisao inteira

# print(op_1)
# print(op_2)
# print(op_3)

n1 += 2

# print("=========")
# print('')
# print(n1)

if n1 == 10:
    pass

# COLECOES

# lista => list ===== MOTAVEL

nome = 'julio'

lista = ['Julio', 17, 1.72] # 0,1,2

# imprimo o tamanho da lista
# print(len(lista))


# EXEMPLO DE USO
# pessoa_1 = []

# nome = input('coloque o nome da primeira pessoa')

# pessoa_1.append(nome)


# print(lista)
# adicionar informacoes na lista
lista.append("Pereira")

#apaga todo os dados da lista
#lista.clear()

# quantas vezes a informacao se repete na lista
num = lista.count("julio")

# apaga da lista e retorna o valor apagado = apaga pelo index ou  o ultimo elemento
# result = lista.pop(1)

# lista_2 = []

# lista_2.append(result)
# remove o elemente da lista e nao retorna nada.
# result = lista.remove("Julio")

# lista[0] = "Pereira"
# print(lista[0])


# dicionario => dict  ======== MOTAVEL

aluno = {'nome': 'Julio', 'idade': 17, 'altura':1.90} # {'chave': valor, 'chave': valor}

# print(aluno.keys())
# print(aluno.values())
# print(aluno.items())

pessoas = [
    {
        'nome': '', 
        'idade': 0, 
        'altura':0.00
    },
    {'nome': '', 'idade': 0, 'altura':0.00},
    {'nome': '', 'idade': 0, 'altura':0.00}
]


# print(aluno['nome'])
aluno['nome'] = 'Pereira'

# print(aluno['nome'])

aluno['peso'] = 10

# print(aluno)

# tupla => tuple  ======== IMOTAVEL

tupla = ('Seg', 'Ter', 'Qua', 'Qui', 'Sex')

# print(lista)
lista[0] = 'PEREIRA'
# print(lista)

# print(tupla)
tupla
# print(tupla)

# ESTRUTURA DE REPETICAO
for x in tupla:
    if x == 'Sex':
        print("Sextouuu!!!!")
    else:
        print("Haaa naoooo!!!!")













