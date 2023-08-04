from random import seed
import random
seed(1)

lista = []
cont = 0

for i in range(1000):
    lista.append(random.randint(0, 10000))
for j in lista:
    menor = min(lista[cont:len(lista)])
    while menor in lista:
        lista.remove(menor)
    lista.insert(0, menor)
    cont = cont + 1
print(lista)