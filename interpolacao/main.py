from Interpolacao.interpolacaoBilinear import InterpolacaoBilinear
from Interpolacao.vizinho import VizinhoMaisProximo

if __name__ == '__main__':
    print("Processamento")

    arq = InterpolacaoBilinear('../img/pinguim.jpg')
    novo = VizinhoMaisProximo('../img/pinguim.jpg')

    opcao = -1

    menu = "\n\nDigite 0 para sair.\nMenu:\n"
    menu += "1 - Interpolação Bilinear\n2 - Vizinho Mais Proximo\n"

    while opcao != 0:
        opcao = input(menu)
        opcao = int(opcao)
        if opcao == 1:
            arq.resolver()
        elif opcao == 2:
            novo.executar()
        else:
            print('Escolha alguma opcao')