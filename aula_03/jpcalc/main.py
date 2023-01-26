from utils.utils import apresentacao, analise_for, analise_while, calcula_resultado

apresentacao()

opcao = input('Escolha a opção: ').lower()

# =w
# opcao = analise_for(opcao)
opcao = analise_while(opcao)

# =w
calcula_resultado(opcao)
