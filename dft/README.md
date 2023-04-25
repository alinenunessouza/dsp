## Como executar o projeto localmente

```python
pip install --upgrade pip
pip install matplotlib
```

- *main.py*: arquivo com a implementação da dft sem a função pronta do numpy e um plot da fft do nympy para comparação
- *main_dft.py*: arquivo com somente a implementação da dft sem a função pronta do numpy
- *main_test.py*: arquivo de teste para verificar o comportamento das harmônicas

## Comparação da DFT implementada e a FFT do numpy:
<img align="center" alt="Csharp" height="400" width="400" src="https://user-images.githubusercontent.com/72985725/234274372-1f32b2e8-fd94-431c-9491-e7469b5d1d2a.png">

## Testes para analisar e validar o comportamento da DFT implementada:
1) No somatório de sinais, ao colocar somente o plot do primeiro sinal, um seno, podemos ver o seno na saída 
![image](https://user-images.githubusercontent.com/72985725/231164692-c702b43f-b44b-402c-b5bb-576cf060b923.png)

2) Ao somar os sinais de entrada, seno fundamental e sua terceira harmonica defasada 90, podemos ver no sinal de saída o somatório
- f1 = 100 
- f2 = 300

```python
x1_n = np.sin(2 * np.pi * f1 * t + 0)
x2_n = np.sin(2 * np.pi * f2 * t + np.pi)

x_n = x1_n + x2_n
```

![image](https://user-images.githubusercontent.com/72985725/231165058-9a6fb9fb-a2b1-4a8b-a77c-fa6ce8bfe7c9.png)

3) 
- f1 = 100
- f2 = 300
- intervalo de amostragem de até 0.02s, quanto menor o tempo de amostragem maior o "zoom" no sinal
![image](https://user-images.githubusercontent.com/72985725/231164101-bd72b191-45ca-4be1-8a86-269cf95c2d7b.png)

4) Ao aumentar a frequência de amostragem, podemos visualizar o somatório com melhor resolução e são utilizados mais pontos para amostrar o sinal
- Fs = 15000

![image](https://user-images.githubusercontent.com/72985725/231164337-8bba0157-06e6-4433-bd8e-d1488c6d1328.png)

5) Teste para plotar onda quadrada

Representação de uma onda quadrada ideal com amplitude de 1 pode ser representada como uma soma infinita de ondas senoidais:
![image](https://user-images.githubusercontent.com/72985725/231187023-acc9924a-b3f1-4c13-b73f-1b8d23ca2fc9.png)
https://en.wikipedia.org/wiki/Square_wave

-  2ª harmônica
f1 = 100 
f2 = 3 * f1 = 300

1 e 0,3 de amplitude

```python
x1_n = np.sin(2 * np.pi * f1 * t)
x2_n = np.sin(2 * np.pi * f2 * t)
x_n = x1_n + 0.3*x2_n
```

![image](https://user-images.githubusercontent.com/72985725/231187309-a098ea36-747d-4179-90a2-906a733ba19a.png)

-  3ª harmônica
f1 = 100 
f2 = 300
f3 = 500

```python
f1 = 100 
f2 = 3 * f1
f3 = 5 * f1

x1_n = np.sin(2 * np.pi * f1 * t)
x2_n = np.sin(2 * np.pi * f2 * t)
x3_n = np.sin(2 * np.pi * f3 * t)
x_n = x1_n + 0.3*x2_n + 0.2*x3_n
```

![image](https://user-images.githubusercontent.com/72985725/231187814-6bb297fd-66fd-4fbf-994e-06a02296b471.png)

-  4ª harmônica

f1 = 100 
f2 = 300
f3 = 500
f4 = 700
f5 = 900

```python
f1 = 100 
f2 = 3 * f1
f3 = 5 * f1
f4 = 7 * f1
f5 = 9 * f1

x1_n = np.sin(2 * np.pi * f1 * t)
x2_n = np.sin(2 * np.pi * f2 * t)
x3_n = np.sin(2 * np.pi * f3 * t)
x4_n = np.sin(2 * np.pi * f4 * t)
x5_n = np.sin(2 * np.pi * f5 * t)
x_n = x1_n + (1/3)*x2_n + (1/5)*x3_n + (1/7)*(x4_n) + (1/9)*(x5_n)
```

![image](https://user-images.githubusercontent.com/72985725/231189750-5ffebe04-e676-4ea3-8974-1c5bd24f82f3.png)

podemos ver que a aceleração do ripple em relação aos novos componentes de harmonica estão mais rápidos
ripple só "para de existir" quando colocar infinitas componentes
menos o Fenômeno de Gibbs que não é facilmente removido

-  5ª harmônica

f1 = 100 
f2 = 300
f3 = 500
f4 = 700
f5 = 900
f6 = 1100

```python
f1 = 100 
f2 = 3 * f1 = 300
f3 = 5 * f1 = 500
f4 = 7 * f1 = 700
f5 = 9 * f1 = 900
f6 = 11 * f1 = 1100

x1_n = np.sin(2 * np.pi * f1 * t)
x2_n = np.sin(2 * np.pi * f2 * t)
x3_n = np.sin(2 * np.pi * f3 * t)
x4_n = np.sin(2 * np.pi * f4 * t)
x5_n = np.sin(2 * np.pi * f5 * t)
x6_n = np.sin(2 * np.pi * f6 * t)
```

x_n = x1_n + (1/3)*x2_n + (1/5)*x3_n + (1/7)*(x4_n) + (1/9)*(x5_n) + (1/11)*(x6_n)
![image](https://user-images.githubusercontent.com/72985725/231192017-fae01f6b-67a3-42a2-8e75-62d7782d814c.png)

-  6ª harmônica

f1 = 100 
f2 = 300
f3 = 500
f4 = 700
f5 = 900
f6 = 1100
f7 = 1300

```python
f1 = 100 
f2 = 3 * f1
f3 = 5 * f1
f4 = 7 * f1
f5 = 9 * f1
f6 = 11 * f1
f7 = 13 * f1

x1_n = np.sin(2 * np.pi * f1 * t)
x2_n = np.sin(2 * np.pi * f2 * t)
x3_n = np.sin(2 * np.pi * f3 * t)
x4_n = np.sin(2 * np.pi * f4 * t)
x5_n = np.sin(2 * np.pi * f5 * t)
x6_n = np.sin(2 * np.pi * f6 * t)
x7_n = np.sin(2 * np.pi * f7 * t)

x_n = x1_n + (1/3)*x2_n + (1/5)*x3_n + (1/7)*(x4_n) + (1/9)*(x5_n) + (1/11)*(x6_n) + (1/13)*(x7_n)
```

![image](https://user-images.githubusercontent.com/72985725/231192643-c1e46ff4-cd46-4b9b-8a0d-10cb47a4721f.png)

- 11ª harmônica

f1 = 100 
f2 = 300
f3 = 500
f4 = 700
f5 = 900
f6 = 1100
f7 = 1300
f8 = 1500
f9 = 1700
f10 = 1900
f11 = 2100
f12 = 2300

```python
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
```

![image](https://user-images.githubusercontent.com/72985725/231196435-7b7dd418-0ec8-42ee-af05-511e274db8d1.png)
