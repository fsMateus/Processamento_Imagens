from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


class Histograma:
    def __init__(self, img):
        self.imagem = self.obterImagem(img)
        self.nivelcinza = 255
        self.vetorFrequencia = np.zeros(256)
        self.vetorPixelReferente = np.zeros(256)
        self.vetorSomaFrequencias = np.zeros(256)
        self.vetorEqualizado = np.zeros(256)

        self.contarPixels()

    def obterImagem(self, nome_img):
        imagem = Image.open(nome_img)

        return imagem.convert('L')  # converte para tons de cinza

    def criar_imagem(self, img):
        return Image.new('L', (int(img.width), int(img.height)))

    def imprimirTabela(self):
        for i in range(256):
            print('Nivel: {} --> {} - {} -  {} - {} '.format(i, self.vetorPixelReferente[i],
                                                             self.vetorFrequencia[i],
                                                             self.vetorSomaFrequencias[i],
                                                             self.vetorEqualizado[i]))

    ''' verificar a quantidade deste pixel na imagem ( nk )'''
    def contarPixels(self):
        img_pixels = self.imagem.load()
        for i in range(self.imagem.width):
            for j in range(self.imagem.height):
                self.verificar(img_pixels[i, j])

    def verificar(self, pixel):
        self.vetorPixelReferente[pixel] += 1

    ''' calculo da frequencia Pr(rk)'''
    def calcularFrequencia(self):
        total_pixels = self.imagem.width * self.imagem.height
        for i in range(256):
            qtdPixel = self.vetorPixelReferente[i]
            self.vetorFrequencia[i] = qtdPixel / total_pixels

    def somarFrequencias(self):
        self.vetorSomaFrequencias[0] = self.vetorFrequencia[0]
        for i in range(1, 256):
            self.vetorSomaFrequencias[i] = self.vetorFrequencia[i] + self.vetorSomaFrequencias[i-1]

    def equalizar(self):
        for i in range(256):
            self.vetorEqualizado[i] = round(self.vetorSomaFrequencias[i] * self.nivelcinza)

    def histograma(self):
        self.calcularFrequencia()
        self.somarFrequencias()
        self.equalizar()

        img_pixels = self.imagem.load()
        nova_img = self.criar_imagem(self.imagem)
        imagem_equalizada = nova_img.load()

        for i in range(self.imagem.width):
            for j in range(self.imagem.height):
                imagem_equalizada[i, j] = int(self.vetorEqualizado[img_pixels[i, j]])

        self.imprimirTabela()

        nova_img.save('histograma.png')
        #nova_img.show()

        plt.hist(x=self.vetorEqualizado, bins=50, alpha=0.5)
        plt.xlabel('Pixels')
        plt.ylabel('Frequencia')
        plt.title('Histograma Equalizado')
        plt.show()
