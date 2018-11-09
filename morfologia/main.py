from Morfologia.aberturaFechamento import Abertura


if __name__ == '__main__':
    arq = Abertura('../img/eri.png')

    opcao = -1

    menu = "\n\nDigite 0 para sair.\nMenu:\n"
    menu += "1 - Abertura\n2 - Fechamento\n3 - Contorno\n"

    while opcao != 0:
        opcao = input(menu)
        opcao = int(opcao)
        if opcao == 1:
            arq.abertura()
        elif opcao == 2:
            arq.fechamento()
        elif opcao == 3:
            arq.extrairContorno()
        else:
            print('Escolha alguma opcao')