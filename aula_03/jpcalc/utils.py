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
    print(nome.upper())

deixar_em_maiusculo(aluno)




