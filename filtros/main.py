from Filtros.filtroMedia import Media
from Filtros.filtroLaplaciano import Laplaciano
from Filtros.filtroSobel import Sobel

if __name__ == '__main__':
    arq = Media('../img/pinguim.jpg')
    novo = Laplaciano('../img/pinguim.jpg')
    file = Sobel('../img/pinguim.jpg')

    opcao = -1

    menu = "\n\nDigite 0 para sair.\nMenu:\n"
    menu += "1 - Filtro Média\n2 - Filtro Laplaciano\n3 - Filtro Sobel\n"

    while opcao != 0:
        opcao = input(menu)
        opcao = int(opcao)
        if opcao == 1:
            arq.calcularMedia()
        elif opcao == 2:
            novo.calcularLaplaciano()
        elif opcao == 3:
            file.sobelHorizontal()
            file.sobelVertical()
        else:
            print('Escolha alguma opcao')