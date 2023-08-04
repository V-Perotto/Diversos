def qtDiferenca(lista1,lista2):
    lista3 = []
    for i in range(len(lista1)):
        if lista1[i] not in lista2:
            lista3.append(lista1[i])
    return len(lista3)

n=int(raw_input())
lista1 = str(raw_input()).split(' ')
n=int(raw_input())
lista2 = str(raw_input()).split(' ')
print(qtDiferenca(lista1,lista2))