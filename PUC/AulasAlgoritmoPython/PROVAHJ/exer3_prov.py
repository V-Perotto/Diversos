import random

def mediaValoresVetor(media):
    soma = int()

    for j in range(0, len(listaValores)):
        soma += listaValores[j]
    media = soma / len(listaValores)
    print(media)
    print('Funcao chamada!')

listaValores = []
for i in range(10):
    listaValores.append(random.randint(0, 100))

print(listaValores)
print("Media dos valores do vetor e: ", mediaValoresVetor(listaValores))