"""  
    EXERCICIO 01
    
    Escrever um programa em Python que solicite informações de três pessoas, 
    como nome, idade, peso e altura. Apresentar na tela estas informações de modo que permaneçam alinhados verticalmente. 
    Usar a formatação de interpolação.

"""


# Pegar informacoes de tres pessoas
# armazenar estas informacoes em variaveis

# pegando os dados da primeira pessoa
nome_1 = input("Escreva o nome da PRIMEIRA pessoa: ")
idade_1 = int(input("Escreva a idade da PRIMEIRA pessoa: "))
peso_1 = float(input("Escreva o peso da PRIMEIRA pessoa: "))
altura_1 = float(input("Escreva a altura da PRIMEIRA pessoa: "))

# pegando os dados da segunda pessoa
nome_2 = input("Escreva o nome da SEGUNDA pessoa: ")
idade_2 = int(input("Escreva a idade da SEGUNDA pessoa: "))
peso_2 = float(input("Escreva o peso da SEGUNDA pessoa: "))
altura_2 = float(input("Escreva a altura da SEGUNDA pessoa: "))

# pegando os dados da terceira pessoa
nome_3 = input("Escreva o nome da TERCEIRA pessoa: ")
idade_3 = int(input("Escreva a idade da TERCEIRA pessoa: "))
peso_3 = float(input("Escreva o peso da TERCEIRA pessoa: "))
altura_3 = float(input("Escreva a altura da TERCEIRA pessoa: "))

# mostrar as informacoes na tela do usuario verticalmente.

print("======== DADOS DA PRIMEIRA PESSOA ==========")
print(f" Nome: {nome_1}, idade: {idade_1}, peso: {peso_1}, altura: {altura_1}")
print("")

print("======== DADOS DA SEGUNDA PESSOA ==========")
print(f" Nome: {nome_2}, idade: {idade_2}, peso: {peso_2}, altura: {altura_2}")
print("")

print("======== DADOS DA TERCEIRA PESSOA ==========")
print(f" Nome: {nome_3}, idade: {idade_3}, peso: {peso_3}, altura: {altura_3}")

