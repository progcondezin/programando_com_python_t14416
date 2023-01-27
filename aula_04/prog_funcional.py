
x = True

# declarando o if (como fazer)
# if x == True:
#     print('verdadeiro')
# else:
#     print('falso')


# expressao do if (o que quero)
# print('verdadeiro') if x == True else print('falso')
'''
#declaracao
numeros = [2,3,4]

total = 0

for num in numeros:
    total += num

print(total)

#expressivo = funcional
def somar(valores):
    total = 0

    for num in numeros:
        total += num

    return total

print(somar(numeros))
'''

# CONCEITO DE IMUTABILIDADE
'''
#mutavel
numeros = [2,3,4]

numeros.append(5)

print(numeros)


#Imutavel

x = [2,3,4]

novo_numeros = x + [5]

print(novo_numeros)
'''

'''
# mutavel
def soma_mutavel(valores):
    total = 0

    for v in valores:
        total += v

    return total

print(soma_mutavel([2,3,5]))

# imutavel
# recursão
def soma_imutavel(valores):
    if not valores:
        return 0

    primeiro = valores[0] # [2]
    resto = valores[1:] # [3,5]

    return primeiro + soma_imutavel(resto)

print(soma_imutavel([2,3,5]))
'''
'''
# funcoes sem composicao
def limpar_espaco(texto:str):
    return texto.strip().lower()

print(limpar_espaco('            JULIO pereira'))

#composicão de função
import toolz

limpar_espaco_2 = toolz.compose(str.strip, str.lower)

print(limpar_espaco_2('            JULIO pereira'))
'''
# expressao lambda => funcao anonima
'''
def dobrar_valor(valor):
    return valor * 2

dobrar = dobrar_valor(4)

print(dobrar)

dobrar = lambda x: x* 2

dobrar_2 = lambda x:dobrar_valor(x)

print(dobrar(4))
print(dobrar_2(4))
'''

# List Comprehensions
numeros = [3,4,5]

total = []

for n in numeros:
    total.append(n)
    
print(total)

total_2 = [x for x in numeros]

print(total_2)



class Aluno:
    pass