lista = []
unicos = []

for i in range(10):
    numero = int(input('Forneca um numero: '))
    if numero not in lista:
        lista.append(numero)
print(lista)


