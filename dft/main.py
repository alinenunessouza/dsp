"""
Created on 2023

@author: Aline Nunes de Souza

Implementação de um somatório de DFT (Discrete Fourier Transform)

DFT -> operação que converte um sinal de domínio do tempo em seu correspondente espectro de frequência

"""

import matplotlib.pyplot as plt
import numpy as np

Fs = 1000  # taxa de amostragem
Ts = 1.0 / Fs  # periodo de amostragem
t = np.arange(0, 1, Ts)  # vetor de tempo que represente o tempo de amostragem do sinal que será analisado pela DFT

f1 = 100  # frequencia do sinal 1
x1_n = np.sin(2 * np.pi * f1 * t + 0)

f2 = 1000  # frequencia do sinal 2
x2_n = np.sin(2 * np.pi * f2 * t + np.pi)

x_n = x1_n + x2_n

n = len(x_n)  # tamanho do sinal
k = np.arange(n)  # vetor em k
T = n / Fs

frq = k / T  # os dois lados do vetor de frequencia
frq = frq[range(int(n/2))]  # apenas um lado

X = np.zeros(int(n/2), dtype=np.complex64)

for m in range(0, int(n/2)):
    mysumm = 0
    for nn in range(0, n):
        mysumm += x_n[nn] * (np.cos(2 * np.pi * nn * m / n) - 1j * np.sin(2 * np.pi * nn * m / n))
    X[m] = mysumm

fig, ax = plt.subplots(2, 1)

ax[0].plot(t, x_n)
ax[0].set_xlabel('Tempo')
ax[0].set_ylabel('Amplitude')
ax[1].plot(frq, np.abs(X), 'r')
ax[1].set_xlabel('Freq (Hz)')
ax[1].set_ylabel('|X(freq)|')

plt.show()
