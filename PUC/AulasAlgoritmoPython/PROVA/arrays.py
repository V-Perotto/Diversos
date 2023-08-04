def arrays(arr):
    lista = []
    for i in range(len(arr) -1, -1, -1):
        lista.append(arr[i])
    return numpy.array(lista, float)