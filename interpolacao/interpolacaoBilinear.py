from PIL import Image
import numpy as np


class InterpolacaoBilinear:
    def __init__(self, img):
        self.imagem = self.obterImagem(img)
        self.largura = self.imagem.width
        self.altura = self.imagem.height

    def obterImagem(self, nome_img):
        imagem = Image.open(nome_img)
        return imagem.convert('L')  # converte para tons de cinza

    def reduzir(self, matriz, n):

        matriz_reduzida = []

        for i in range(0, self.largura, 2):
            for j in range(0, self.altura, 2):
                if i+1 < self.largura and j+1 < self.altura:
                    matriz_reduzida.append((matriz[i, j] + matriz[i, j+1] + matriz[i+1, j] + matriz[i+1, j+1]) / 4)

        return matriz_reduzida

    def ampliar(self):
        img_ampliada = Image.new('L', (int(self.imagem.width * 2), int(self.imagem.height * 2)))

        aux = img_ampliada.load()
        pixel = self.imagem.load()
        x = 1
        y = 0

        for i in range(0, self.imagem.height):
            for j in range(0, self.imagem.width):
                aux[i*2, j*2] = pixel[i, j]

        for i in range(0, self.imagem.height):
            for j in range(0, self.imagem.width-1):
                aux[x, y] = int((pixel[j, i] + pixel[j+1, i]) / 2)
                x += 2
            x = 1
            y += 2

        x = 0
        y = 1
        for i in range(0, self.imagem.height-1):
            for j in range(0, self.imagem.width):
                aux[x, y] = int((pixel[j, i] + pixel[j, i+1]) / 2)
                x += 2
            x = 0
            y += 2

        x = y = 1
        for i in range(0, self.imagem.height-1):
            for j in range(0, self.imagem.width-1):
                aux[x, y] = int((pixel[j, i] + pixel[j, i+1] + pixel[j+1, i] + pixel[j+1, i+1]) / 4)
                x += 2
            x = 1
            y += 2

        for i in range(img_ampliada.width):
            aux[i, img_ampliada.height - 1] = aux[i, img_ampliada.height - 2]

        for i in range(img_ampliada.height):
            aux[img_ampliada.width - 1, i] = aux[img_ampliada.width - 2, i]

        img_ampliada.save('ampliadaBIL.png')
        return img_ampliada

    def resolver(self):
        img1 = self.ampliar()
        img1.show()

        tamanho = int(self.largura / 2), int(self.altura / 2)
        dados = list(self.imagem.getdata())
        matriz = np.reshape(dados, (self.largura, self.altura))

        nova_img = self.reduzir(matriz, 2)
        img_reduzida = Image.new('L', tamanho)
        img_reduzida.putdata(nova_img)
        img_reduzida.save('reduzidaBIL.png')
        img_reduzida.show()
