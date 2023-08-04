fatorial = 1

n = int(input("Insira um numero para fatorar: "))
for n in range (n, 0, -1):
    fatorial = fatorial * n
print(fatorial)