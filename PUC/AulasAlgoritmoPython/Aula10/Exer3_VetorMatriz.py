listaSorteada = []
listaEscolhida = []
qtAcertos = 0

for i in range(6):
    listaSorteada.append(int(input('Forneca um numero sorteado: ')))

for j in range(6):
    listaEscolhida.append(int(input('Forneca um numero escolhido: ')))

for i in range(len(listaSorteada)):
    if listaEscolhida[i] in listaSorteada:
        qtAcertos = qtAcertos + 1

print(qtAcertos)