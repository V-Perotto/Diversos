
def calcSoma(a, b):
    return a + b

def calcSubt(a, b):
    return a - b

def calcDivs(a, b):
    return a / b

def calcMult(a, b):
    return a * b

m = str(input("Indique o tipo de operacao matematica que deseja fazer ( *, /, -, + ):"))
a = float(input("Insira o primeiro valor: "))
b = float(input("Insira o segundo valor: "))
mult = calcMult(a, b)
divs = calcDivs(a, b)
soma = calcSoma(a, b)
subt = calcSubt(a, b)

if m == '*':
    print(mult)
elif m == '/':
    print(divs)
elif m == '-':
    print(subt)
elif m == '+':
    print(soma)
else:
    print("Operacao Nao Existe!")