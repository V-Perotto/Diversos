lista = []
unicos = []

for i in range(10):
    numero = int(input('Forneca um numero: '))
    lista.append(numero)
print(lista)

for i in range(len(lista)):
    if lista[i] not in unicos:
        unicos.append(lista[i])
print(unicos)