idUser = []
nomeUser = []
idadeUser = []
cadastro = []
allCad = []
verification = []

x = 0
iden = 0

def cadastroUser():
    nome = str(input(" >> Insira o nome para adicionar: "))
    if nome not in verification:
        idade = int(input(" >> Insira a idade para adicionar: "))
        idUser.append(iden)
        nomeUser.append(nome)
        idadeUser.append(idade)
        verification.append(nome)

        print("\n /---------------------------------------------\ ")
        print("|\t\t\t\tPessoa cadastrada!\t\t\t\t|")
        print(" \---------------------------------------------/\n")

    elif nome in verification:
        print("- Este nome já foi adicionado")
        cadastroUser()

def deleteUser():
    nome = str(input(" >> Insira o nome para deletar: "))
    pos = -1

    if nome in cadastro:
        for i in range(len(cadastro), -1, -1):
            pos = i

        print("- Quem você procura:", cadastro)
        print("- Deseja deletar", cadastro, "? [S/N]")
        resp = str(input("- Digite: "))

        if resp == "S":
            allCad.remove(allCad[i-1])
            print("\n /---------------------------------------------\ ")
            print("|\t\t\t\tPessoa removida!\t\t\t\t|")
            print(" \---------------------------------------------/\n")

        elif resp == "N":
            pass

        else:
            deleteUser()

    elif nome not in nomeUser:
        print("- Quem você procura não foi adicionado ainda!")
        pass

def chooseFunc():
    print("\n/===============================================\ ")
    print("|\tPARA ADICIONAR USUARIO DIGITE: \t\t [1]\t|")
    print("|\tPARA DELETAR USUARIO DIGITE: \t\t [2]\t|")
    print("|\tPARA VISUALIZAR CADASTROS: \t\t\t [3]\t|")
    print("\===============================================/\n")
    chooses = str(input(" >> Digite a entrada: "))
    return chooses

def qntdCad():
    print("\n/===============================================\ ")
    print("|-----------------------------------------------|")
    print("|\t\t\t\tTodos os usuarios:\t\t\t\t|")
    print(allCad)
    print("|-----------------------------------------------|")
    print("|\t\t\tUltimo usuario adicionado:\t\t\t|")
    print(cadastro)
    print("|-----------------------------------------------|")
    print("\===============================================/\n")

while x != -1:
    choose = chooseFunc()
    if choose == "1":
        iden += 1
        addItens = cadastroUser()
        cadastro = (idUser + nomeUser + idadeUser)

        idUser.remove(idUser[0])
        nomeUser.remove(nomeUser[0])
        idadeUser.remove(idadeUser[0])

        allCad.append(cadastro)

    elif choose == "2":
        rmvItens = deleteUser()

    elif choose == "3":
        qntdItens = qntdCad()

    else:
        choose = chooseFunc()

print(cadastroUser())