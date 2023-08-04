def isSubset(lista1,lista2):
    return 'True'


nCasos=int(raw_input())
for i in range(nCasos):
    tamanhoLista1 = int(raw_input())
    lista1 = str(raw_input()).split(' ')
    tamanhoLista2 = int(raw_input())
    lista2 = str(raw_input()).split(' ')
    print(isSubset(lista1, lista2))