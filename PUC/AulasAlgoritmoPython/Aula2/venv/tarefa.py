#nota1 = float(input("Insira a nota 1: "))
#nota2 = float(input("Insira a nota 2: "))
#nota3 = float(input("Insira a nota 3: "))
#nota4 = float(input("Insira a nota 4: "))

#media = (nota1 + nota2 + nota3 + nota4) / 4
#print(media)

######################################################

horas = int(input("Insira a hora: "))
minutos = int(input("Insira os minutos: "))

#horaEntrada
#minutoEntrada
#horaSaida
#minutoSaida

# 7:30 e 23:10

if (horas <= 7 and minutos < 30) or (horas >= 23 and minutos > 10):
    print("o bloco esta fechado")
elif (horas >= 7 and minutos >= 30) or (horas <= 23 and minutos <= 10):
    print("o bloco ainda esta funcionando")

# Vittorio Perotto - Exerc 3