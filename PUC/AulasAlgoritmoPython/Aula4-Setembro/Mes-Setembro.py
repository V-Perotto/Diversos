# % 1
#uma semana tem 7 dias
#1 e 8 é domingo, 8 dividido por 7 dá 1
#8 + 7 = 15, dai 15 / 7 = % 1

# dia dividido por sete e o resto da divisão igual a x
# dia % 7 == 1

dia = int(input("Forneca um dia: "))

if dia % 7 == 1:
    print('Domingo')
elif dia % 7 == 2:
    print('Segunda-Feira')
elif dia % 7 == 3:
    print('Terca-Feira')
elif dia % 7 == 4:
    print('Quarta-Feira')
elif dia % 7 == 5:
    print('Quinta-Feira')
elif dia % 7 == 6:
    print('Sexta-Feira')
elif dia % 7 == 0:
    print('Sabado')

# Feito por Vittorio Perotto
