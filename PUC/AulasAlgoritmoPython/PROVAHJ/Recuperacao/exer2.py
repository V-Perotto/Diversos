numero = int(input("Insira um numero de 0 a 1000: "))

if numero > 0 and numero < 1000:
    if numero % 2 == 1 and numero <= 500:
        print("Pequeno Impar")
    elif numero % 2 == 0 and numero <= 500:
        print("Pequeno Par")
    elif numero % 2 == 1 and numero > 500:
        print("Grande Impar")
    elif numero % 2 == 0 and numero > 500:
        print("Grande Par")
elif numero < 0:
    print("Insira um numero novamente!")
elif numero >= 1000:
    print("Insira um numero novamente!")