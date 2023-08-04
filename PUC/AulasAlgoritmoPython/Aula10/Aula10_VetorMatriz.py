lista = []
i = 0

for i in range(10):
    lista.append(int(input('Forneca um numero: ')))

indice = int(input('Forneca indice: '))

if indice < len(lista) and indice >= 0:
    print('Conteudo: ' + str(lista[indice]))
else:
    print('Nao esta no vetor')