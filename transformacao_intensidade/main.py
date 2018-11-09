from TransformacaoIntensidade.negativo import Negativo


if __name__ == '__main__':
    print("Processamento")

    file = Negativo('../img/pinguim.jpg')
    file.calcularNegativo()
