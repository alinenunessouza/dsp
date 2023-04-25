Implementação no micro controlador STM M4 do filtro Sallen Key utilizando a foram canônica para seu design digital.

ARM STM32

Configurações:
frequência no gerador de sinais: 1k
function: sin
volts out: 0-2V

Pinagem:
A0 -> entrada do gerador de funções
PA4 -> saída

Amostragem: 5k
Nquist-> consegue mostrar até 10k
Frequência de corte definida: 
fc = 900Hz
Então a partir de 900Hz, o sinal não deve ser amostrado 
