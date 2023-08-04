# Utilizando o código abaixo já implementado, continue
# a implementação para pedir um valor inteiro N do teclado,
# e exibir a quantidade de valores da variável listaValores que são maiores que N

import random

listaValores = []
n = int(input('Forneca um valor N: '))
for i in range(10):
    listaValores.append(random.randint(0, 100))

listaMaior = [k for k in listaValores if k > n]

print(listaValores)
print('Quantidade de números maior que', n, ':', len(listaMaior))