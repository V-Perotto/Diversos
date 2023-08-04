# impares = 0
# cont = 0
#
# num = int(input("Forneca um numero: "))
# for cont in range(1, num + 1, 1):
#     impares = impares
#     print(cont)

num = int(input('Insira um numero: '))
for cont in range(1, num + 1):
             linha = ""
             for i in range(0, cont):
                    linha += str(cont) + ''
             print(linha)