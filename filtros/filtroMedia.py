from PIL import Image


class Media:
    def __init__(self, img):
        self.imagem = self.obterImagem(img)

    def obterImagem(self, nome_img):
        imagem = Image.open(nome_img)

        return imagem.convert('L')  # converte para tons de cinza

    def criar_imagem(self, img):
        return Image.new('L', (int(img.width), int(img.height)))

    def calcularMedia(self):
        self.imagem.show()

        pixels = self.imagem.load()
        nova_img = self.criar_imagem(self.imagem)
        img_resultado = nova_img.load()

        for i in range(1, self.imagem.width-1):
            for j in range(1, self.imagem.height-1):
                valor = int((pixels[i-1, j-1] + pixels[i, j-1] + pixels[i+1, j-1] +
                                       pixels[i-1, j] + pixels[i, j] + pixels[i+1, j] +
                                       pixels[i-1, j+1] + pixels[i, j+1] + pixels[i+1, j+1]) / 9)

                if valor < 0:
                    img_resultado[i, j] = 0
                else:
                    img_resultado[i, j] = valor

        nova_img.save('media.png')
        nova_img.show()
