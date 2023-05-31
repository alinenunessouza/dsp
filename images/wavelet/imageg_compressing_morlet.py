import cv2
import numpy as np
import pywt
from scipy.signal import morlet2

# Carregar a imagem
imagem = cv2.imread('lena.jpg', 0)

# Definir os parâmetros do wavelet Morlet
omega_0 = 6  # Fator de escala da frequência central
sigma = 2 * np.pi / omega_0

# Criar o kernel do wavelet Morlet
kernel_size = (31, 31)  # Tamanho do kernel
kernel = morlet2(*kernel_size, sigma)

# Normalizar o kernel para ter média zero
kernel -= np.mean(kernel)

# Realizar a convolução da imagem com o kernel do wavelet Morlet
coeffs = cv2.filter2D(imagem, cv2.CV_64F, kernel.real)

# Definir o nível de decomposição desejado
nivel = 3

# Aplicar a compressão de coeficientes descartando detalhes de alta frequência
coeffs_nivel = pywt.wavedec2(coeffs, 'haar', level=nivel)
for i in range(1, len(coeffs_nivel)):
    coeffs_nivel[i] = tuple([np.zeros_like(v) for v in coeffs_nivel[i]])

# Realizar a reconstrução da imagem utilizando apenas os coeficientes preservados
imagem_reconstruida = pywt.waverec2(coeffs_nivel, 'haar')

# Converter a imagem reconstruída para o tipo uint8 (imagem em tons de cinza)
imagem_reconstruida = np.uint8(imagem_reconstruida)

# Exibir a imagem original e a imagem reconstruída
cv2.imshow('Imagem Original', imagem)
cv2.imshow('Imagem Reconstruída', imagem_reconstruida)
cv2.waitKey(0)