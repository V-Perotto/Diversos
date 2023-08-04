#contador = 0
#soma = 0

#while contador < 10:
#    n = int(input("Forneca o numero: "))
#    soma = soma + contador
#    contador = contador + 1
#    if n % 2 == 0:
#        print('Par')
#    if n % 2 == 1:
#        print('Impar')
#print(contador)

a = 0
b = 1
x = 0
contador = 0

n = int(input("Fibonacci: "))
while contador < n:
    contador = contador + 1
    x = a + b
    b = a
    a = x
    print(b)
