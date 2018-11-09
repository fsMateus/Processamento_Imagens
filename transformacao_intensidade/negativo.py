from PIL import Image


class Negativo:
    def __init__(self, img):
        self.imagem = self.obterImagem(img)
        self.nivelcinza = 255

    def obterImagem(self, nome_img):
        imagem = Image.open(nome_img)

        return imagem.convert('L')  # converte para tons de cinza

    def criar_imagem(self, img):
        return Image.new('L', (int(img.width), int(img.height)), color='white')

    def calcularNegativo(self):
        nova_img = self.criar_imagem(self.imagem)
        img_pixels = self.imagem.load()
        imagem_negativa = nova_img.load()

        for i in range(self.imagem.width):
            for j in range(self.imagem.height):
                imagem_negativa[i, j] = self.nivelcinza - img_pixels[i, j]

        nova_img.save('negativa.png')
        nova_img.show()

        return nova_img
