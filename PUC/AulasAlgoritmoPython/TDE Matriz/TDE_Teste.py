from random import randint
from random import seed
seed (1)

matriz = []

def matrizBuilder(num):
    for lin in range (num):
        matriz.append([])
        for col in range (num):
            matriz[lin].append(randint(0, 1000))

    for i in range (len(matriz)):
        print (matriz[i])

def matrizQuery(num, lenQuery, matriz):
    summCol = int()
    summRow = int()
    summ = int()

    for num in range(0, num, 1):
        summCol += matriz[num][lenQuery]
    for num in range(0, num, 1):
        summRow += matriz[lenQuery][num]

    summ = summCol + summRow

    return summ

num = int(input('digite o tamanho da matriz: '))
lenQuery = int(input('digite o alcance: '))

matrizBuilder(num)
score = matrizQuery(num, lenQuery , matriz)

print ()
print ('**' * 30)
print ('maior score é: ',score)

# Abdiel