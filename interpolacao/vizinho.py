from PIL import Image
import numpy as np


class VizinhoMaisProximo:
    def __init__(self, img):
        self.imagem = self.obterImagem(img)

    def obterImagem(self, nome_img):
        imagem = Image.open(nome_img)

        return imagem.convert('L')  # converte para tons de cinza

    def reducaoVMP(self):
        img_reduzida = Image.new('L', (int(self.imagem.width / 2), int(self.imagem.height / 2)), color='white')

        aux = img_reduzida.load()
        pixel = self.imagem.load()
        x = y = 0

        for i in range(0, self.imagem.height, 2):
            for j in range(0, self.imagem.width, 2):
                aux[x, y] = pixel[i, j]
                y += 1
            y = 0
            x += 1

        img_reduzida.save('reducaoVMP.png')
        return img_reduzida

    def ampliacaoVMP(self):
        img_ampliada = Image.new('L', (int(self.imagem.width * 2), int(self.imagem.height * 2)))

        aux = img_ampliada.load()
        pixel = self.imagem.load()
        x = y = 0

        for i in range(0, img_ampliada.height, 2):
            for j in range(0, img_ampliada.width, 2):
                aux[i, j] = pixel[x, y]
                if j < img_ampliada.width:
                    aux[i, j+1] = pixel[x, y]
                if i < img_ampliada.height:
                    aux[i+1, j] = pixel[x, y]
                if i < img_ampliada.height and j < img_ampliada.width:
                    aux[i+1, j+1] = pixel[x, y]

                y += 1
            y = 0
            x += 1

        img_ampliada.save('ampliacaoVMP.png')
        return img_ampliada

    def executar(self):
        img1 = self.reducaoVMP()
        img1.show()

        img2 = self.ampliacaoVMP()
        img2.show()