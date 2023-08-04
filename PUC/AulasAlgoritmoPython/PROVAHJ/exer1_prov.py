import random

def qtValoresUnicos(lista1, lista2):
    quantLst1 = int()
    quantLst2 = int()
    for i in range(len(lista1)):
        quantLst1 = len(set([valorLista1 for valorLista1 in lista1 if lista1.count(valorLista1)]))
    for j in range(len(lista2)):
        quantLst2 = len(set([valorLista2 for valorLista2 in lista2 if lista2.count(valorLista2)]))
    print(quantLst1, quantLst2)
    print('Funcao qtValoresUnicos chamada!')

def qtValoresRepetidos(lista1, lista2):
    quantLst1 = int()
    quantLst2 = int()
    for i in range(len(lista1)):
        quantLst1 = len(set([valorLista1 for valorLista1 in lista1 if lista1.count(valorLista1)]))
    for j in range(len(lista2)):
        quantLst2 = len(set([valorLista2 for valorLista2 in lista2 if lista2.count(valorLista2)]))
    print(quantLst1, quantLst2)
    print('Funcao qtValoresRepetidos chamada!')

listaValores1 = []
listaValores2 = []
for i in range(10):
    listaValores1.append(random.randint(0, 30))
    listaValores2.append(random.randint(0, 30))

print(listaValores1)
print(listaValores2)
print("Qntd valores que ocorreram apenas 1 vez nas duas listas: " + str(qtValoresUnicos(listaValores1, listaValores2)))
print("Quantidade de valores que ocorreram nas duas listas: " + str(qtValoresRepetidos(listaValores1, listaValores2)))