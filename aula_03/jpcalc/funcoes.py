a = 10
b = 20

# funcao que retorna dados
def retorna_soma(num_1, num_2):
    return num_1 + num_2

resultado = retorna_soma(a,b)
# print(resultado)


#funcao que nao retorna
def nao_retorna_soma(num_1, num_2):
    if type(num_1) == int or type(num_1) == float and type(num_2) == int or type(num_2) == float:
        print(num_1+num_2)
    else:
        print('dados errados')


# nao_retorna_soma(10.5,23)

# Funcao com inferencia e retorno declarado
aluno = 'julio'

def deixar_em_maiusculo(nome:str)-> str:
    return nome.upper()

resultado = deixar_em_maiusculo(aluno)
# print(resultado)


# funcao com parametro opcional
def soma_de_dois_com_opcional(preco, v_entrega=0):
    print(preco + v_entrega)

# soma_de_dois_com_opcional(2, 100)

# funcao com parametros ilimitados
def somar_varios_numeros(*args):
    soma = 0
    #repetindo os items no parametro args e atualizando a variavel soma.
    for item in args:
        soma += item

    return soma

resultado = somar_varios_numeros(1,2,4,3,9, 10, 10 ,10)

# print(resultado)


# funcao com parametros ilimitado opcionais (kargs)


# exemplo como sao os calculos
'''
produto = 100
margem = 0
entrega = 10

preco_final = produto + (produto*margem/100) + entrega

# print(preco_final)

'''

def preco_final(preco, **kargs):
    margem = 0
    entrega = 0

    v_margem = kargs.get('margem')

    if v_margem:
        margem = preco * v_margem / 100

    v_entrega = kargs.get('entrega')
    if v_entrega:
        entrega = v_entrega

    preco_final = preco + margem + entrega
    
    print(preco_final)


preco_final(100, margem=10, entrega=10)











