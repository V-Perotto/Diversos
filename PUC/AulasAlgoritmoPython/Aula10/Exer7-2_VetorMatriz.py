lista = []
unicos = []

for i in range(10):
    numero = int(input('Forneca um numero: '))
    lista.append(numero)
print(lista)

for i in range(len(lista)):
    existe = False
    for j in range(len(unicos)):
        if lista[i] == unicos[j]:
            existe = True
            break
        if not existe:
            unicos.append(lista[i])
print(unicos)