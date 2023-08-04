# Continue a implementação para:
#
# Pedir um valor N do teclado;
# Exibir a quantidade de valores por linha na matriz que são maiores que N
# Exemplo de saida do programa:
#
# [[2, 9, 1, 4, 1], [7, 7, 7, 10, 6], [3, 1, 7, 0, 6], [6, 9, 0, 7, 4], [3, 9, 1, 5, 0]]
# Forneca um valor N: 5
# Linha 0 possui 1 valores maiores que 5
# Linha 1 possui 5 valores maiores que 5
# Linha 2 possui 2 valores maiores que 5
# Linha 3 possui 3 valores maiores que 5
# Linha 4 possui 1 valores maiores que 5

import random
random.seed(1)
cont = -1
matriz = []
n = int(input('Forneca um valor N: '))
for i in range(5):
    matriz.append([])
    for j in range(5):
        matriz[i].append(random.randint(0, 10))

while cont < len(matriz):
    for h in range(0, len(matriz[cont])):
        listaMaior = [k for k in matriz[i] if k > n]
    print('Linha', matriz[cont], 'possui', len(listaMaior), 'valores maiores que', n)
    cont += 1
print(matriz)