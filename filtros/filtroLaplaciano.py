from PIL import Image


class Laplaciano:
    def __init__(self, img):
        self.imagem = self.obterImagem(img)

    def obterImagem(self, nome_img):
        imagem = Image.open(nome_img)

        return imagem.convert('L')  # converte para tons de cinza

    def criar_imagem(self, img):
        return Image.new('L', (int(img.width), int(img.height)))

    def calcularLaplaciano(self):
        self.imagem.show()

        pixels = self.imagem.load()
        nova_img = self.criar_imagem(self.imagem)
        img_resultado = nova_img.load()

        for i in range(1, self.imagem.width-1):
            for j in range(1, self.imagem.height-1):
                valor = int((pixels[i-1, j-1]*(-1) + pixels[i-1, j]*(-1) + pixels[i-1, j+1]*(-1) +
                            pixels[i, j-1]*(-1) + pixels[i, j]*(8) + pixels[i, j+1]*(-1) +
                            pixels[i+1, j-1]*(-1) + pixels[i+1, j]*(-1) + pixels[i+1, j+1]*(-1)) / 9)

                if valor < 0:
                    img_resultado[i, j] = 0
                else:
                    img_resultado[i, j] = valor

        nova_img.save('laplaciano.png')
        nova_img.show()