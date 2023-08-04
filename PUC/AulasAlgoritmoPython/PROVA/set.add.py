def qtElementosUnicos(lista1, lista2):
    lista3 = []
    for i in range(len(lista1)):
        if lista1[i] not in lista3:
            lista3.append(lista1[i])

    for i in range(len(lista2)):
        if lista2[i] not in lista3:
            lista3.append(lista2[i])

    return len(lista3)