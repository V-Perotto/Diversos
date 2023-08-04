# Escreva um algoritmo que dado o peso de um boxeador, informe a categoria a qual ele pertence, seguindo a tabela abaixo:

#   Categoria       Peso (kg)
#   Palha           Menor que 50 Kg
#   Pluma           50 - 59,99 Kg
#   Leve            60 - 75,99 Kg
#   Pesado          76 - 87,99 Kg
#   Super Pesado    Maior que 88 Kg

pesoBoxeador = float(input("Insira o peso do boxeador: "))
if (pesoBoxeador < 50.00):
    print("Palha")
elif (pesoBoxeador >= 50.00 and pesoBoxeador <= 59.99):
    print("Pluma")
elif (pesoBoxeador >= 60.00 and pesoBoxeador <= 75.99):
    print("Leve")
elif (pesoBoxeador >= 76.00 and pesoBoxeador <= 87.99):
    print("Pesado")
elif (pesoBoxeador >= 88.00):
    print("Super Pesado")

# feito por Vittorio Perotto