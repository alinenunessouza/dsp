"""
Created on 2023

@author: Aline Nunes de Souza

Implementação de um somatório de DFT (Discrete Fourier Transform)

DFT -> operação que converte um sinal de domínio do tempo em seu correspondente espectro de frequência

- escolher a taxa de amostragem, sugestão de começar com 1000 e 100hz para teste
- deve atender ao Critério de Nyquist: fs > 2 * fmax
- não é permitido o uso das funções prontas do Python (a não ser para conferência do algoritmo), tais como fft, angle e abs.
"""

import matplotlib.pyplot as plt
import numpy as np

Fs = 5000  # taxa de amostragem
Ts = 1.0 / Fs  # periodo de amostragem
t = np.arange(0, 0.02, Ts)  # vetor de tempo que represente o tempo de amostragem do sinal que será analisado pela DFT

f1 = 100 
f2 = 3 * f1
f3 = 5 * f1
f4 = 7 * f1
f5 = 9 * f1
f6 = 11 * f1
f7 = 13 * f1
f8 = 15 * f1
f9 = 17 * f1
f10 = 19 * f1
f11 = 21 * f1
f12 = 23 * f1

x1_n = np.sin(2 * np.pi * f1 * t)
x2_n = np.sin(2 * np.pi * f2 * t)
x3_n = np.sin(2 * np.pi * f3 * t)
x4_n = np.sin(2 * np.pi * f4 * t)
x5_n = np.sin(2 * np.pi * f5 * t)
x6_n = np.sin(2 * np.pi * f6 * t)
x7_n = np.sin(2 * np.pi * f7 * t)
x8_n = np.sin(2 * np.pi * f8 * t)
x9_n = np.sin(2 * np.pi * f9 * t)
x10_n = np.sin(2 * np.pi * f10 * t)
x11_n = np.sin(2 * np.pi * f11 * t)
x12_n = np.sin(2 * np.pi * f12 * t)

x_n = x1_n + (1/3)*x2_n + (1/5)*x3_n + (1/7)*(x4_n) + (1/9)*(x5_n) + (1/11)*(x6_n) + (1/13)*(x7_n) + (1/15)*(x8_n) + (1/17)*(x9_n) + (1/19)*(x10_n) +  (1/21)*(x11_n) + (1/23)*(x12_n)


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

fig.tight_layout()

ax[0].plot(t, x_n)
ax[0].set_xlabel('Tempo')
ax[0].set_ylabel('Amplitude')
ax[1].plot(frq, np.abs(X), 'r')
ax[1].set_xlabel('Freq (Hz)')
ax[1].set_ylabel('|X(freq)|')
fig.suptitle('Main title')
plt.show()
