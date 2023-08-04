# 1) Escreva um programa que dado uma entrada do teclado verifica se o número é divisível por 5 e 11, ou não.

numero = int(input('Forneca um numero: '))
# % mostra o resto da divisão;
if numero % 5 == 0 and numero % 11 == 0:
    print("divisivel")
else:
    print("nao divisivel")

# 2) Escreva um programa que recebe como entrada três números e os exibe ordenado

n1 = int(input("Forneca o primeiro numero: "))
n2 = int(input("Forneca o segundo numero: "))
n3 = int(input("Forneca o terceiro numero: "))

if (n1 < n2 and n1 < n3) and (n2 < n3):
    print(n1,"|", n2,"|", n3)
elif (n1 < n2 and n1 < n3) and (n2 > n3):
    print(n1,"|", n3,"|", n2)
elif (n1 > n2 and n1 < n3):
    print(n2,"|", n1,"|", n3)
elif (n1 < n2 and n1 > n3):
    print(n3,"|", n1,"|", n2)
elif (n3 < n1 and n3 < n2) and (n1 < n2):
    print(n3,"|", n1,"|", n2)
elif (n3 < n1 and n3 < n2) and (n1 > n2):
    print(n3,"|", n2, "|", n1)

# 3) Escreva um programa que recebe como entrada uma nota e a presença do teclado. Posteriormente exibe uma
#    mensagem caso o aluno possua presença maior que 70% e o seu conceito

#   CONCEITO    NOTA
#   A           Nota maior que 9
#   B           Nota maior que 8
#   C           Nota maior que 7
#   D           Nota maior que 6
#   E           Nota maior que 4
#   F           Nota menor ou igual a 4

nota = int(input("Forneca a nota: "))
presenca = float(input("Forneca a presenca em porcentagem: "))

if (nota > 9 and nota <= 10) and (presenca >= 70.0):
    print("A")
elif (nota > 8) and (presenca >= 70.0):
    print("B")
elif (nota > 7) and (presenca >= 70.0):
    print("C")
elif (nota > 6) and (presenca >= 70.0):
    print("D")
elif (nota >= 4) and (presenca >= 70.0):
    print("E")
elif (nota <= 4) and (presenca >= 70.0):
    print("F")

#Feito por Vittorio Perotto