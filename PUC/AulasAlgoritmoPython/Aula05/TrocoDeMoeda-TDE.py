notaCemQuant = float(input("Forneça a quantidade de notas de 100 reais disponíveis: "))
notaCinquentaQuant = float(input("Forneça a quantidade de notas de 50 reais disponíveis: "))
notaVinteQuant = float(input("Forneça a quantidade de notas de 20 reais disponíveis: "))
notaDezQuant = float(input("Forneça a quantidade de notas de 10 reais disponíveis: "))
notaCincoQuant = float(input("Forneça a quantidade de notas de 5 reais disponíveis: "))
notaDoisQuant = float(input("Forneça a quantidade de notas de 2 reais disponíveis: "))
moedaRealQuant = float(input("Forneça a quantidade de moedas de 1 real disponíveis: "))
moedaCinquentaQuant = float(input("Forneça a quantidade de moedas de 50 centavos disponíveis: "))
moedaVinteCincoQuant = float(input("Forneça a quantidade de moedas de 25 centavos disponíveis: "))
moedaDezQuant = float(input("Forneça a quantidade de moedas de 10 centavos disponíveis: "))
moedaCincoQuant = float(input("Forneça a quantidade de moedas de 5 centavos disponíveis: "))

cemTroco = int(0)
nCinquentaTroco = int(0)
vinteTroco = int(0)
nDezTroco = int(0)
nCincoTroco = int(0)
doisTroco = int(0)
realTroco = int(0)
cinquentaTroco = int(0)
vinteCincoTroco = int(0)
dezTroco = int(0)
cincoTroco = int(0)

gasto = float(0)
pago = float(0)
troco = gasto - pago

caixa = (notaCemQuant * 100) + (notaCinquentaQuant * 50) + (notaVinteQuant * 20) + (notaDezQuant * 10) + (notaCincoQuant * 5) + (notaDoisQuant * 2) + (moedaRealQuant * 1.0) + (moedaCinquentaQuant * 0.50) + (moedaVinteCincoQuant * 0.25) + (moedaDezQuant * 0.10) + (moedaCincoQuant * 0.05)

while troco <= caixa:
    gasto = float(input("\nForneça o valor gasto pelo cliente: "))
    pago = float(input("Forneça o valor pago pelo cliente: "))
    troco = pago - gasto
    while (troco - 100) >= 0 and notaCemQuant > 0:
        cemTroco = cemTroco + 1
        troco = troco - 100
        notaCemQuant = notaCemQuant - 1
        caixa = caixa - 100
    while (troco - 50) >= 0 and notaCinquentaQuant > 0:
        nCinquentaTroco = nCinquentaTroco + 1
        troco = troco - 50
        notaCinquentaQuant = notaCinquentaQuant - 1
        caixa = caixa - 50
    while (troco - 20) >= 0 and notaVinteQuant > 0:
        vinteTroco = vinteTroco + 1
        troco = troco - 20
        notaVinteQuant = notaVinteQuant - 1
        caixa = caixa - 20
    while (troco - 10) >= 0 and notaDezQuant > 0:
        nDezTroco = nDezTroco + 1
        troco = troco - 10
        notaDezQuant = notaDezQuant - 1
        caixa = caixa - 10
    while (troco - 5) >= 0 and notaCincoQuant > 0:
        nCincoTroco = nCincoTroco + 1
        troco = troco - 5
        notaCincoQuant = notaCincoQuant - 1
        caixa = caixa - 5
    while (troco - 2) >= 0 and notaDoisQuant > 0:
        doisTroco = doisTroco + 1
        troco = troco - 2
        notaDoisQuant = notaDoisQuant - 1
        caixa = caixa - 2
    while (troco - 1.0) >= 0 and moedaRealQuant > 0:
        realTroco = realTroco + 1
        troco = troco - 1.0
        moedaRealQuant = moedaRealQuant - 1.0
        caixa = caixa - 1.0
    while (troco - 0.5) >= 0 and moedaCinquentaQuant > 0:
        cinquentaTroco = cinquentaTroco + 1
        troco = troco - 0.5
        moedaCinquentaQuant = moedaCinquentaQuant - 1
        caixa = caixa - 0.5
    while (troco - 0.25) >= 0 and moedaVinteCincoQuant > 0:
        vinteCincoTroco = vinteCincoTroco + 1
        troco = troco - 0.25
        moedaVinteCincoQuant = moedaVinteCincoQuant - 1
        caixa = caixa - 0.25
    while (troco - 0.1) >= 0 and moedaDezQuant > 0:
        dezTroco = dezTroco + 1
        troco = troco - 0.1
        moedaDezQuant = moedaDezQuant - 1
        caixa = caixa - 0.1
    while (troco - 0.05) >= 0 and moedaCincoQuant > 0:
        cincoTroco = cincoTroco + 1
        troco = troco - 0.05
        moedaCincoQuant = moedaCincoQuant - 1
        caixa = caixa - 0.05
    print("\nTROCO:\n")
    if troco <= caixa:
        print("Notas de 100 reais: ", cemTroco)
        print("Notas de 50 reais: ", nCinquentaTroco)
        print("Notas de 20 reais: ", vinteTroco)
        print("Notas de 10 reais: ", nDezTroco)
        print("Notas de 5 reais: ", nCincoTroco)
        print("Notas de 2 reais: ", doisTroco)
        print("Moedas de 1 real: ", realTroco)
        print("Moedas de 50 centavos: ", cinquentaTroco)
        print("Moedas de 25 centavos: ", vinteCincoTroco)
        print("Moedas de 10 centavos: ", dezTroco)
        print("Moedas de 5 centavos: ", cincoTroco)
    else:
        print("ERRO: Sem troco/moedas!")
# Feito por - Vittorio Perotto