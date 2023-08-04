from random import seed
import random
seed(1)

nCol = int(input('Digite o tamanho da Matriz [ M , N ]: '))
cont = nCol
nLin = nCol
aux = nCol
matriz = []
m = int(input('Selecione a quantidade de casas para percorrer: '))
print()
points = 0
somaCol = int()
maior = int()
somaLin = int()

for col in range(nCol):
    linha = []
    for lin in range(nCol):
        linha.append(random.randint(0, 1000))
    matriz.append(linha)

while cont > 0:
    cont = cont - 1
    print(matriz[cont])

for nCol in range(0, nCol, 1):
    somaCol += matriz[nCol][m]
for nLin in range(0, nLin, 1):
    somaLin += matriz[m][nLin]

maior = somaCol + somaLin

print('\nMatriz [', aux, ',', m, ']')
print('Maior Valor:', maior, '')