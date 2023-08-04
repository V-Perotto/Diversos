from random import seed
import random
seed(1)

lista=[]

def adicionar(a, b, c):
    for i in range(len(lista)):
        if a in lista:
            print('Esse nome de usuario ja foi escolhido.')
            return
        x = (a + ',' + b + '| ID do usuario:' + c)
        lista.append(x)
        return

def remover(a):
    lista.remove(a)
    return

def listar():
    print(lista)

def filtrar(a):
    for i in range(len(lista)):
        if a in lista[i]:
            print(lista[i])
            return

while True:
    print('-='*30)
    print('Qual das seguintes opcoes voce gostaria de executar?')
    print('Digite 1 para adicionar.')
    print('Digite 2 para remover.')
    print('Digite 3 para listar.')
    print('Digite 4 para filtrar.')
    opcao= input('Informe a opcao: ')
    if opcao == '1':
        nUsuario= input('Digite o nome de usuario: ')
        iUsuario= input('Digite a idade do usuario: ')
        adicionar(nUsuario, iUsuario, str(random.randint(0, 10000)))
        print('Usuario adicionado.')
    if opcao == '2':
        rUsuario= input('Digite o usuario que sera removido: ')
        remover(rUsuario)
        print('Usuario removido.')
    if opcao == '3':
         print(lista)
    #
    #     listar()
    if opcao == '4':
        fUsuario= input('Digite o usuario que gostaria de filtrar: ')
        filtrar(fUsuario)

# Arthur