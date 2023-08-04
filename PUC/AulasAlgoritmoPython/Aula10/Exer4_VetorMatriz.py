palavra = str(input('Escreva uma palavra: '))
letra = palavra.split()
junto = ''.join(letra)
inverso = ''

for decr in range(len(palavra) -1, -1, -1):
    print(junto[decr])
if inverso == junto:
    print('Palíndromo')
else:
    print('Não é palíndromo')