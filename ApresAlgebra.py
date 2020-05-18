import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

#Uma imagem de forma digital contem linha, coluna e camada.
#por exemplo um cubo magico

#Lendo a imagem pirate.jpg
img = Image.open("imagemAL.jpg")

#Transformando a imagem em um array do Numpy
#Valores de 0 a 1 ao inves de 0 a 255
matrizImg = np.asarray(img, dtype = np.float32) / 255
#Para sabermos a dimensao da imagem
#print(matrizImg.shape)

#Visualizando os valores da matriz
#print(matrizImg)


#Print da imagem original
'''
#Removendo os eixos (coordenadas) do plot
plt.axis("off")
im = plt.imshow(matrizImg)
plt.show()
'''



#Alterando o valor dos pixels de toda a imagem
'''
#Alterar a cor de um pixel da imagem nao faz muita diferenca
#Utilizaremos o ":" para alterar varias linhas/colunas

#Zerando todas as linhas e colunas da camada vermelha
#matrizImg[:,:,0] = 0

#Zerando todas as linhas e colunas da camada verde
matrizImg[:,:,1] = 0

#Zerando todas as linhas e colunas da camada azul
matrizImg[:,:,2] = 0

#Visualizando a imagem
plt.axis("off")
im = plt.imshow(matrizImg)
plt.show()

#Visualizando os valores da matriz
#print(matrizImg)
'''



#Alterando a cor de metade da imagem
'''
#Armazenando os dados de altura, largura e dimensao (Lin, Col, Dim)
metadeCol = matrizImg.shape[1] / 2
metadeCol = int(metadeCol)
metadeLin = matrizImg.shape[0] / 2
metadeLin = int(metadeLin)

linMax = int(matrizImg.shape[0])
colMax = int(matrizImg.shape[1])
dimensao  = int(matrizImg.shape[2])

#Zerando todas as linhas ate a metade das colunas da respectiva camada
matrizImg[:, 0:metadeCol, 0] = 0

#Visualizando a imagem
plt.axis("off")
im = plt.imshow(matrizImg)
plt.show()
print(matrizImg)
'''



#Alterar para valor maximo e minimo de cada camada
'''
#Armazenando os dados de altura, largura e dimensao (Lin, Col, Dim)
metadeCol = matrizImg.shape[1] / 2
metadeCol = int(metadeCol)
metadeLin = matrizImg.shape[0] / 2
metadeLin = int(metadeLin)

linMax = int(matrizImg.shape[0])
colMax = int(matrizImg.shape[1])
dimensao  = int(matrizImg.shape[2])

#Zerando todas as linhas ate a metade das colunas da respectiva camada
matrizImg[0:metadeLin, 0:metadeCol, 0] = 0 #Variar o valor!

#Zerando todas as linhas ate a metade das colunas da respectiva camada
matrizImg[0:metadeLin, 0:metadeCol, 1] = 0 #Variar o valor!

#Zerando todas as linhas ate a metade das colunas da respectiva camada
matrizImg[0:metadeLin, 0:metadeCol, 2] = 0 #Variar o valor!

#Visualizando a imagem
plt.axis("off")
im = plt.imshow(matrizImg)
plt.show()
#print(matrizImg)
'''




#Alterando cada quadrante da imagem
'''
#Armazenando os dados de altura, largura e dimensao (Lin, Col, Dim)
metadeCol = matrizImg.shape[1] / 2
metadeCol = int(metadeCol)
metadeLin = matrizImg.shape[0] / 2
metadeLin = int(metadeLin)

linMax = int(matrizImg.shape[0])
colMax = int(matrizImg.shape[1])
dimensao  = int(matrizImg.shape[2])

matrizImg[0:metadeLin, 0:metadeCol, 0] = 1
matrizImg[0:metadeLin, metadeCol:colMax, 1] = 1
matrizImg[metadeLin:linMax, 0:metadeCol, 2] = 1

#Visualizando a imagem
plt.axis("off")
im = plt.imshow(matrizImg)
plt.show()
#print(matrizImg)
'''


#Fazendo a transposicao da imagem
'''
#Fazemos a transposta de cada camada da matrizImg
mtR = np.transpose(matrizImg[:,:,0])
mtG = np.transpose(matrizImg[:,:,1])
mtB = np.transpose(matrizImg[:,:,2])

#Criamos uma nova matriz com base nos dados
dimensaoImg = matrizImg.shape

#Invertemos a linha e a coluna, por conta da transposicao
#Ou seja, a nova coluna sera a antiga linha e vice-e-versa
colNova = dimensaoImg[0]
linNova = dimensaoImg[1]
dimNova = dimensaoImg[2]

#Atribui o valor 0 (zero) aos campos da nova matriz
novaMatriz = np.zeros((linNova, colNova, dimNova))
#Verificando os valores zerados da matriz
#print(novaMatriz)

#Fazendo as devidas atribuicoes
#A imagem vai simplesmente deitar

#E se nao atribuirmos algum valor...
#novaMatriz[:,:,0] = mtR
novaMatriz[:,:,1] = mtG
#novaMatriz[:,:,2] = mtB

#Visualizando a imagem
plt.axis("off")
im = plt.imshow(novaMatriz)
plt.show()
#print(matrizImg)
'''











