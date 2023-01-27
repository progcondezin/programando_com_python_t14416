

"""
Laboratório 02 - Página 117
    
    Suponha que em um caixa eletrônico existam cédulas disponíveis de 5, 10, 20 e 50 reais. 
    Usando operações de divisão inteira e resto da divisão, escrever um programa que solicite ao usuário um valor para saque e, 
    a partir deste valor, armazenar em variáveis e apresentar na tela a quantidade de cada cédula para compor o valor do saque.
    
    Obs.: Considerar neste exercício que os valores sejam sempre múltiplos de 5. Considerar também a menor quantidade possível de cédulas.
"""

# divisao_inteira = 505 // 100
# resto_divisao = 502 % 100

# Solução

def sacar():
    saque = int(input('Digite o valor que queira sacar: ')) #232

    if saque % 5 != 0: 
        return 'voce precisa digitar um valor multiplo de 5'
        
    c_50 = saque // 50
    #saque = saque % 50
    saque %= 50

    c_20 = saque // 20
    saque %= 20

    c_10 = saque // 10
    saque %= 10

    c_5 = saque // 5
    saque %= 5

    a_sacar = f'Seu saque será de: \n{c_50} notas de 50 \n{c_20} notas de 20 \n{c_10} notas de 10 \n{c_5} notas de 5'

    return a_sacar

# print(sacar())

"""
===> Laboratório 2 - página 118 <===
    
    Escrever um programa que solicite ao usuário:
    => O nome de um funcionário; 
    => Seu salário.
    
    Se o salário for superior a R$ 5.000,00 ele terá um desconto de 10% sobre o que ultrapassar R$ 5.000,00.
    No final, apresentar:
    
    => O nome do funcionário; 
    => O salário bruto; 
    => O valor do desconto; 
    => O salário líquido.
    
======================
"""

# solução
def definir_salario():
    funcionario = input('Coloque o nome do funcionário: ')
    salario = float(input(f'Coloque o salário do funcionário {funcionario}: '))

    desconto = 0.0

    if salario > 5000:
        desconto = (salario - 5000) * 10 / 100

    # pode ser assim
    # print(f'Funcionário: {funcionario}')
    # print(f'Salário Bruto: {salario}')
    # print(f'Valor do desconto: {desconto}')
    # print(f'Salário Líquido: {salario - desconto}')

    #pode ser feito assim
    salario_liquido = salario - desconto

    return funcionario, salario, desconto, salario_liquido

#pode ser assim
# print(f'Funcionário: {definir_salario()[0]}')
# print(f'Salário Bruto: {definir_salario()[1]}')
# print(f'Valor do desconto: {definir_salario()[2]}')
# print(f'Salário Líquido: {definir_salario()[3]}')

# pode ser assim
# funcionario, salario, desconto, salario_liquido = definir_salario()

# print(f'Funcionário: {funcionario}')
# print(f'Salário Bruto: {salario}')
# print(f'Valor do desconto: {desconto}')
# print(f'Salário Líquido: {salario_liquido}')


"""   
===> Laboratório 3 - página 118 <===
    
    Em um clube, o valor da entrada varia de acordo com a idade do associado.
    Os critérios são:
    
    => Até 17 anos - R$ 50,00; 
    => Entre 18 e 59 anos - R$ 60,00;
    => A partir de 60 anos - R$ 20,00.
    
    O programa deve apresentar o nome do associado e o valor do ingresso a ser pago.
    
======================
"""
#Solução
def verificar_valor_ingresso():
    associado = input('Nome do associado: ')
    idade = int(input('Idade do associado: '))

    if idade < 18:
        ingresso = 50.0
    elif idade < 60:
        ingresso = 60.00
    else:
        ingresso = 20.00

    print(f'Associado: {associado}')
    print(f'Valor do ingresso: {ingresso}')

verificar_valor_ingresso()

"""   
===> Laboratório 4 - página 119 <===
    
    Neste laboratório deverá ser usado o conceito de expressão if.
    Com base no ano fornecido pelo usuário, verificar se o ano é bissexto ou não, 
    e apresentar o número de dias referente ao mês de fevereiro.
    
"""