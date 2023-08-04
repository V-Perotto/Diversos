lista = []

for i in range(10):
    lista.append(int(input('Forneca um numero: ')))

while True:
    n = int(input('Forneca novo numero: '))
    indice = int(input('Forneca indice: '))

    if indice >= 0 and indice < len(lista):
        lista[indice] = n

    for i in range(len(lista)):
        print(lista[i])