lista = []
n = int(input("Digite um numero: "))
for cont in range(0, n):
    nV = int(input("Digite um numero: "))
    lista.append(nV)
n1 = int(input("Digite um numero: "))
n2 = int(input("Digite um numero: "))

listaMaior = [k for k in lista if k > n1]
listaMenor = [h for h in lista if h < n2]

print(lista)
print('Quantidade de números maior que', n1, ':', len(listaMaior))
print('Quantidade de números menor que', n2, ':', len(listaMenor))