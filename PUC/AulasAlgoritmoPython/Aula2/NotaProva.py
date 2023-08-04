RA1 = 0.2
RA2 = 0.25
RA3 = 0.15
RA4 = 0.2
RA5 = 0.1
RA6 = 0.1

notaProva1 = 79
notaProva2 = 84

notaAtiv1 = 68
notaAtiv2 = 78
notaAtiv3 = 84
notaAtiv4 = 81
notaAtiv5 = 75
notaAtiv6 = 90

notaFinalProva = ((notaProva1 * (RA1 + RA4 + RA5) + notaProva2 * (RA2 + RA3 + RA6)) * 0.7)

notaFinalAtiv = (((notaAtiv1 * RA1) +
                 (notaAtiv2 * RA2) +
                 (notaAtiv3 * RA3) +
                 (notaAtiv4 * RA4) +
                 (notaAtiv5 * RA5) +
                 (notaAtiv6 * RA6)) * 0.3)

mediaFinal = notaFinalProva + notaFinalAtiv
print(mediaFinal)

#Vittorio Perotto - Aula 2 (Python/PyCharm)
