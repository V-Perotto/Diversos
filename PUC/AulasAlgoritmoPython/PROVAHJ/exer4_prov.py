lista1 = []
lista2 = []
lista1.append(lista2)

num = int(input('Insira um numero: '))
for cont in range(1, num + 1):
    linha = ""
    for i in range(0, cont):
        linha += str(cont) + ''
    lista2.append(cont)
    print(lista2)