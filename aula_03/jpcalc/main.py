from utils.utils import apresentacao, analise_for, analise_while, calcula_resultado

apresentacao()

opcao = input('Escolha a opção: ').lower()

# =w
# nova_opcao = analise_for(opcao)
nova_opcao = analise_while(opcao)

# =w
calcula_resultado(nova_opcao)
