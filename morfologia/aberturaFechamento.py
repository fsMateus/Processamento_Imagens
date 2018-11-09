from PIL import Image


class Abertura:
    def __init__(self, img):
        self.imagem = self.obterImagem(img)

    def obterImagem(self, nome_img):
        imagem = Image.open(nome_img)

        return imagem.convert('L')  # converte para tons de cinza

    def criar_imagem(self, img):
        return Image.new('L', (int(img.width), int(img.height)))
    
    def binaria(self, img):
        pixels = img.load()
        nova_img = self.criar_imagem(img)
        img_resultado = nova_img.load()

        for i in range(self.imagem.width):
            for j in range(self.imagem.height):
                if pixels[i, j] < 127:
                    img_resultado[i, j] = 0
                else:
                    img_resultado[i, j] = 255
                    
        return nova_img
    
    def dilatacao(self, img):
        imagem = self.binaria(img)
        
        mascara = [[1, 1, 1],
                   [1, 1, 1],
                   [1, 1, 1]]
        
        pixels = imagem.load()
        img_dilatada = self.criar_imagem(imagem)
        img_aux = img_dilatada.load()
        
        for i in range(1, self.imagem.width-1):
            for j in range(1, self.imagem.height-1):
                if pixels[i, j] == 255:
                    img_aux[i-1, j-1] = 255
                    img_aux[i-1, j] = 255
                    img_aux[i-1, j+1] = 255
                    img_aux[i, j-1] = 255
                    img_aux[i, j] = 255
                    img_aux[i, j+1] = 255
                    img_aux[i+1, j-1] = 255
                    img_aux[i+1, j] = 255
                    img_aux[i+1, j+1] = 255
                    
        return img_dilatada

    '''
    def dilatar(self, img):
        imagem = self.binaria(img)

        m = [[255, 255, 255],
             [255, 255, 255],
             [255, 255, 255]]

        p = imagem.load()
        img_dilata = self.criar_imagem(imagem)
        img_aux = img_dilata.load()

        for i in range(1, self.imagem.width - 1):
            for j in range(1, self.imagem.height - 1):
                if p[i, j] == m[1][1] or p[i - 1, j - 1] == m[0][0] or p[i - 1, j] == m[0][1] \
                        or p[i - 1, j + 1] == m[0][2] or p[i, j - 1] == m[1][0] or p[i, j + 1] == m[1][2] \
                        or p[i + 1, j - 1] == m[2][0] or p[i + 1, j] == m[2][1] or p[i + 1, j + 1] == m[2][2]:
                    img_aux[i, j] = 255

        return img_dilata
    '''

    def erosao(self, img):
        imagem = self.binaria(img)

        mascara = [[1, 1, 1],
                   [1, 1, 1],
                   [1, 1, 1]]

        p = imagem.load()
        img_erosao = self.criar_imagem(imagem)
        img_aux = img_erosao.load()
        
        for i in range(1, self.imagem.width-1):
            for j in range(1, self.imagem.height-1):
                if p[i, j] == 255 and p[i-1, j-1] == 255 and p[i-1, j] == 255 and p[i-1, j+1] == 255 \
                and p[i, j-1] == 255 and p[i, j+1] == 255 and p[i+1, j-1] == 255 and p[i+1, j] == 255 and p[i+1, j+1] == 255:
                    img_aux[i, j] = 255
                    
        return img_erosao

    def abertura(self):
        self.imagem.show()

        imgE = self.erosao(self.imagem)
        img_abertura = self.dilatacao(imgE)

        #imgE.save('erosao.png')
        #imgE.show()

        img_abertura.save('abertura.png')
        img_abertura.show()

    def fechamento(self):
        self.imagem.show()

        imgD = self.dilatacao(self.imagem)
        img_fechamento = self.erosao(imgD)

        #imgD.save('dilatacao.png')
        #imgD.show()

        img_fechamento.save('fechamento.png')
        img_fechamento.show()

    def extrairContorno(self):
        aux = self.imagem.load()

        imgE = self.erosao(self.imagem)
        pixels = imgE.load()

        contorno_img = self.criar_imagem(self.imagem)
        img_resultado = contorno_img.load()

        for i in range(self.imagem.width):
            for j in range(self.imagem.height):
                valor = int(aux[i, j] - pixels[i, j])
                if valor < 0:
                    img_resultado[i, j] = 0
                else:
                    img_resultado[i, j] = valor

        contorno_img.save('contorno.png')
        contorno_img.show()