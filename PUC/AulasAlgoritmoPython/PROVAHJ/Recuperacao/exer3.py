res = 0

n = int(input('Digite um numero: '))
for cont in range (1, n):
    if cont % 3 == 0 or cont % 5 == 0:
        res = res + cont
print(res)