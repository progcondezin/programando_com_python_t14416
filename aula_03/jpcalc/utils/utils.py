from soma.sum import minha_funcao_de_somar

def apresentacao():
    print('=== Calculadora do Julio ====')
    print('Bem vindo a minha calculadora, escolha uma das opções abaixo:')
    print('')

    # soma, subtracao, multiplicacao, divisao

    print('A = Soma')
    print('B = Subtracao')
    print('C = Multiplicacao')
    print('D = Divisao')


def analise_for(opcao):
    opcoes = ['a', 'b', 'c', 'd']

    # fOR
    for letra in opcoes: # breaak ou continue
        if opcao == letra:
            break
    else:
        opcao = input('Voce digitou a opção errada. tente mais uma vez: ').lower()

        # verificar se ainda há erro!
        if not opcao in opcoes:
            print('Infelizmente voce ainda não acertou. executa o programa novamente.')
            print('Saindo...')
            exit()
        else:
            return opcao


def analise_while(opcao):
    opcoes = ['a', 'b', 'c', 'd']

    # while
    if not opcao in opcoes:
        a = 0
        while a < 1:
            opcao = input('Voce digitou a opção errada. tente outra vez: ').lower()

            if opcao in opcoes:
                return opcao
    else:
        return opcao


def calcula_resultado(opcao):
    x =  10 # int(input('Coloque o primeiro numero:'))
    y = 2 # int(input('Coloque o segundo numero:'))

    if opcao == 'a':
        #print(x + y) # funcao que imprime na tela
        resultado = minha_funcao_de_somar(x,y)
        print(resultado)
    elif opcao == 'b':

        print(x - y)
    elif opcao == 'c':
        print(x * y)
    else:
        print(x / y)