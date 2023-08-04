tipo_de_dinheiro = [200, 100, 50, 20, 10, 5, 2, 1, 0.5, 0.25, 0.1, 0.05, 0.01]

dinheiro_na_maquina = 0

bebida_na_maquina = 1
preco_bebida = 4.5

n200reais = 1
n100reais = 1
n50reais = 1
n20reais = 1
n10reais = 1
n5reais = 1
n2reais = 1

m1real = 1
m50cents = 1
m25cents = 1
m10cents = 1
m5cents = 1
m1cents = 1

devolver_dinheiro = []
dinheiro_a_devolver = 0

print()
print("*"*42)
print("| \tMáquina de Refrigerantes\t |")
print("*"*42)
while True:
    print('\n- Deseja acessar a máquina? [S/N]')
    resposta = str(input("> "))
    if resposta == "n" or resposta == "N":
        print('\n| Obrigado por utilizar nossos serviços! Volte sempre!')
        break
    elif resposta == "s" or resposta == "S":
        while True:
            print("\n| Quem está utilizando o programa? (C = Consumidor | A = Administrador | S = Sair)")
            user = str(input('> '))
            if user == "s" or user == "S":
                break
            elif user == "a" or user == "A":
                while True:
                    print('\n| Selecione a atividade: ')
                    print("| 0 - Sair")
                    print("| 1 - Adicionar bebida")
                    print("| 2 - Adicionar dinheiro")
                    atividade = input("> ")
                    if atividade == '0' or atividade == 0:
                        break
                    elif atividade == '1' or atividade == 1:
                        while True:
                            print(f"\n| A quantidade atual de bebidas é: {bebida_na_maquina} unidade(s).")
                            print("| Indique a quantidade de bebidas que serão adicionadas:")
                            bebidas_para_adicionar = input("> ")
                            if bebidas_para_adicionar.isdigit():
                                bebida_na_maquina = bebida_na_maquina + int(bebidas_para_adicionar)
                                break
                            else:
                                print("\n[!] Insira um valor numérico! [!]")
                    elif atividade == '2' or atividade == 2:
                        while True:
                            print(f'\n| A quantidade atual do dinheiro na máquina é: R$ {dinheiro_na_maquina:.2f}')
                            print("| Quantidade de notas na máquina:")
                            print(f"| R$ 200\t-\t{n200reais} unidade(s)")
                            print(f"| R$ 100\t-\t{n100reais} unidade(s)")
                            print(f"| R$ 50 \t-\t{n50reais} unidade(s)")
                            print(f"| R$ 20 \t-\t{n20reais} unidade(s)")
                            print(f"| R$ 10 \t-\t{n10reais} unidade(s)")
                            print(f"| R$ 5  \t-\t{n5reais} unidade(s)")
                            print(f"| R$ 2  \t-\t{n2reais} unidade(s)")
                            print("| Quantidade de moedas na máquina:")
                            print(f"| R$ 1,00\t-\t{m1real} unidade(s)")
                            print(f"| R$ 0,50\t-\t{m50cents} unidade(s)")
                            print(f"| R$ 0,25\t-\t{m25cents} unidade(s)")
                            print(f"| R$ 0,10\t-\t{m10cents} unidade(s)")
                            print(f"| R$ 0,05\t-\t{m5cents} unidade(s)")
                            print(f"| R$ 0,01\t-\t{m1cents} unidade(s)")
                            
                            print('\n| Insira o dinheiro na máquina:')
                            print('| - Quantas notas de 200 reais você irá inserir?')
                            inserted_n200reais = input('> ')
                            print('| - Quantas notas de 100 reais você irá inserir?')
                            inserted_n100reais = input('> ')
                            print('| - Quantas notas de 50 reais você irá inserir?')
                            inserted_n50reais = input('> ')
                            print('| - Quantas notas de 20 reais você irá inserir?')
                            inserted_n20reais = input('> ')
                            print('| - Quantas notas de 10 reais você irá inserir?')
                            inserted_n10reais = input('> ')
                            print('| - Quantas notas de 5 reais você irá inserir?')
                            inserted_n5reais = input('> ')
                            print('| - Quantas notas de 2 reais você irá inserir?')
                            inserted_n2reais = input('> ')
                            
                            print('| - Quantas moedas de 1 real você irá inserir?')
                            inserted_m1real = input('> ')
                            print('| - Quantas moedas de 50 centavos você irá inserir?')
                            inserted_m50cents = input('> ')
                            print('| - Quantas moedas de 25 centavos você irá inserir?')
                            inserted_m25cents = input('> ')
                            print('| - Quantas moedas de 10 centavos você irá inserir?')
                            inserted_m10cents = input('> ')
                            print('| - Quantas moedas de 5 centavos você irá inserir?')
                            inserted_m5cents = input('> ')
                            print('| - Quantas moedas de 1 centavos você irá inserir?')
                            inserted_m1cents = input('> ')

                            if (inserted_n200reais.isdigit() and 
                                inserted_n100reais.isdigit() and 
                                inserted_n50reais.isdigit() and 
                                inserted_n20reais.isdigit() and 
                                inserted_n10reais.isdigit() and 
                                inserted_n5reais.isdigit() and 
                                inserted_n2reais.isdigit() and 
                                inserted_m1real.isdigit() and
                                inserted_m50cents.isdigit() and
                                inserted_m25cents.isdigit() and
                                inserted_m10cents.isdigit() and
                                inserted_m5cents.isdigit() and
                                inserted_m1cents.isdigit()):
                                
                                inserted_n200reais = int(inserted_n200reais)
                                inserted_n100reais = int(inserted_n100reais)
                                inserted_n50reais = int(inserted_n50reais)
                                inserted_n20reais = int(inserted_n20reais)
                                inserted_n10reais = int(inserted_n10reais)
                                inserted_n5reais = int(inserted_n5reais)
                                inserted_n2reais = int(inserted_n2reais)
                                inserted_m1real = int(inserted_m1real)
                                inserted_m50cents = int(inserted_m50cents)
                                inserted_m25cents = int(inserted_m25cents)
                                inserted_m10cents = int(inserted_m10cents)
                                inserted_m5cents = int(inserted_m5cents)
                                inserted_m1cents = int(inserted_m1cents)

                                n200reais = n200reais + inserted_n200reais
                                n100reais = n100reais + inserted_n100reais
                                n50reais = n50reais + inserted_n50reais
                                n20reais = n20reais + inserted_n20reais
                                n10reais = n10reais + inserted_n10reais
                                n5reais = n5reais + inserted_n5reais
                                n2reais = n2reais + inserted_n2reais

                                m1real = m1real + inserted_m1real
                                m50cents = m50cents + inserted_m50cents
                                m25cents = m25cents + inserted_m25cents
                                m10cents = m10cents + inserted_m10cents
                                m5cents = m5cents + inserted_m5cents
                                m1cents = m1cents + inserted_m1cents

                                dinheiro_na_maquina = (
                                    (inserted_n200reais * 200) + 
                                    (inserted_n100reais * 100) +
                                    (inserted_n50reais * 50) +
                                    (inserted_n20reais * 20) +
                                    (inserted_n10reais * 10) +
                                    (inserted_n5reais * 5) +
                                    (inserted_n2reais * 2) +
                                    (inserted_m1real * 1) +
                                    (inserted_m50cents * 0.5) +
                                    (inserted_m25cents * 0.25) +
                                    (inserted_m10cents * 0.1) +
                                    (inserted_m5cents * 0.05) +
                                    (inserted_m1cents * 0.01)
                                )
                                break
                            else:
                                print("\n[!] Valores inseridos incorretamente - Insira novamente! [!]")

            elif user == "c" or user == "C":
                while True:
                    print('\n| Selecione sua bebida: [0 - Sair | 1 - Refrigerante]')
                    bebida_selected = input('> ')
                    if bebida_selected == '0' or bebida_selected == 0:
                        break
                    if bebida_selected == '1' or bebida_selected == 1:
                        if bebida_na_maquina <= 0:
                            print("\n[!] Sem bebida na máquina! [!]")
                            break
                        else:
                            while True:
                                print('\n| Insira o dinheiro na máquina para coletar sua bebida')
                                print(f'- O valor da bebida é R$ {preco_bebida:.2}')
                                print('- Quantas notas de 200 reais você irá inserir?')
                                inserted_n200reais = input('> ')
                                print('- Quantas notas de 100 reais você irá inserir?')
                                inserted_n100reais = input('> ')
                                print('- Quantas notas de 50 reais você irá inserir?')
                                inserted_n50reais = input('> ')
                                print('- Quantas notas de 20 reais você irá inserir?')
                                inserted_n20reais = input('> ')
                                print('- Quantas notas de 10 reais você irá inserir?')
                                inserted_n10reais = input('> ')
                                print('- Quantas notas de 5 reais você irá inserir?')
                                inserted_n5reais = input('> ')
                                print('- Quantas notas de 2 reais você irá inserir?')
                                inserted_n2reais = input('> ')
                                
                                print('- Quantas moedas de 1 real você irá inserir?')
                                inserted_m1real = input('> ')
                                print('- Quantas moedas de 50 centavos você irá inserir?')
                                inserted_m50cents = input('> ')
                                print('- Quantas moedas de 25 centavos você irá inserir?')
                                inserted_m25cents = input('> ')
                                print('- Quantas moedas de 10 centavos você irá inserir?')
                                inserted_m10cents = input('> ')
                                print('- Quantas moedas de 5 centavos você irá inserir?')
                                inserted_m5cents = input('> ')
                                print('- Quantas moedas de 1 centavos você irá inserir?')
                                inserted_m1cents = input('> ')

                                if (inserted_n200reais.isdigit() and 
                                    inserted_n100reais.isdigit() and 
                                    inserted_n50reais.isdigit() and 
                                    inserted_n20reais.isdigit() and 
                                    inserted_n10reais.isdigit() and 
                                    inserted_n5reais.isdigit() and 
                                    inserted_n2reais.isdigit() and 
                                    inserted_m1real.isdigit() and
                                    inserted_m50cents.isdigit() and
                                    inserted_m25cents.isdigit() and
                                    inserted_m10cents.isdigit() and
                                    inserted_m5cents.isdigit() and
                                    inserted_m1cents.isdigit()):
                                    
                                    inserted_n200reais = int(inserted_n200reais)
                                    inserted_n100reais = int(inserted_n100reais)
                                    inserted_n50reais = int(inserted_n50reais)
                                    inserted_n20reais = int(inserted_n20reais)
                                    inserted_n10reais = int(inserted_n10reais)
                                    inserted_n5reais = int(inserted_n5reais)
                                    inserted_n2reais = int(inserted_n2reais)
                                    inserted_m1real = int(inserted_m1real)
                                    inserted_m50cents = int(inserted_m50cents)
                                    inserted_m25cents = int(inserted_m25cents)
                                    inserted_m10cents = int(inserted_m10cents)
                                    inserted_m5cents = int(inserted_m5cents)
                                    inserted_m1cents = int(inserted_m1cents)

                                    n200reais = n200reais + inserted_n200reais
                                    n100reais = n100reais + inserted_n100reais
                                    n50reais = n50reais + inserted_n50reais
                                    n20reais = n20reais + inserted_n20reais
                                    n10reais = n10reais + inserted_n10reais
                                    n5reais = n5reais + inserted_n5reais
                                    n2reais = n2reais + inserted_n2reais

                                    m1real = m1real + inserted_m1real
                                    m50cents = m50cents + inserted_m50cents
                                    m25cents = m25cents + inserted_m25cents
                                    m10cents = m10cents + inserted_m10cents
                                    m5cents = m5cents + inserted_m5cents
                                    m1cents = m1cents + inserted_m1cents

                                    dinheiro_do_consumidor = (
                                        (inserted_n200reais * 200) + 
                                        (inserted_n100reais * 100) +
                                        (inserted_n50reais * 50) +
                                        (inserted_n20reais * 20) +
                                        (inserted_n10reais * 10) +
                                        (inserted_n5reais * 5) +
                                        (inserted_n2reais * 2) +
                                        (inserted_m1real * 1) +
                                        (inserted_m50cents * 0.5) +
                                        (inserted_m25cents * 0.25) +
                                        (inserted_m10cents * 0.1) +
                                        (inserted_m5cents * 0.05) +
                                        (inserted_m1cents * 0.01)
                                    )

                                    if not (inserted_n200reais == 0 and 
                                        inserted_n100reais == 0 and 
                                        inserted_n50reais == 0 and 
                                        inserted_n20reais == 0 and 
                                        inserted_n10reais == 0 and 
                                        inserted_n5reais == 0 and 
                                        inserted_n2reais == 0 and 
                                        inserted_m1real == 0 and
                                        inserted_m50cents == 0 and
                                        inserted_m25cents == 0 and
                                        inserted_m10cents == 0 and
                                        inserted_m5cents == 0 and
                                        inserted_m1cents == 0):

                                        troco = dinheiro_do_consumidor - preco_bebida
                                        troco_real = troco
                                        if troco > 0:
                                            contador_troco = 0  
                                            contador_devolver = 0
                                            contador_dinheiro = 0
                                            while contador_dinheiro < len(tipo_de_dinheiro) and troco > 0:
                                                if (n200reais == 0 and 
                                                    n100reais == 0 and 
                                                    n50reais == 0 and 
                                                    n20reais == 0 and 
                                                    n10reais == 0 and 
                                                    n5reais == 0 and 
                                                    n2reais == 0 and 
                                                    m1real == 0 and
                                                    m50cents == 0 and
                                                    m25cents == 0 and
                                                    m10cents == 0 and
                                                    m5cents == 0 and
                                                    m1cents == 0):
                                                    print('Sem troco!')
                                                    contador_dinheiro = len(tipo_de_dinheiro)
                                                    break
                                                if contador_troco < len(tipo_de_dinheiro):
                                                    if not troco >= tipo_de_dinheiro[contador_troco]:
                                                        contador_troco = contador_troco + 1
                                                    while troco >= tipo_de_dinheiro[contador_troco]:
                                                        if (tipo_de_dinheiro[contador_troco] == 200 and n200reais > 0):
                                                            n200reais = n200reais - 1
                                                            devolver_dinheiro.append(tipo_de_dinheiro[contador_troco])
                                                            troco -= tipo_de_dinheiro[contador_troco]
                                                        elif (tipo_de_dinheiro[contador_troco] == 100 and n100reais > 0):
                                                            n100reais = n100reais - 1
                                                            devolver_dinheiro.append(tipo_de_dinheiro[contador_troco])
                                                            troco -= tipo_de_dinheiro[contador_troco]
                                                        elif (tipo_de_dinheiro[contador_troco] == 50 and n50reais > 0):
                                                            n50reais = n50reais - 1
                                                            devolver_dinheiro.append(tipo_de_dinheiro[contador_troco])
                                                            troco -= tipo_de_dinheiro[contador_troco]
                                                        elif (tipo_de_dinheiro[contador_troco] == 20 and n20reais > 0):
                                                            n20reais = n20reais - 1
                                                            devolver_dinheiro.append(tipo_de_dinheiro[contador_troco])
                                                            troco -= tipo_de_dinheiro[contador_troco]
                                                        elif (tipo_de_dinheiro[contador_troco] == 10 and n10reais > 0):
                                                            n10reais = n10reais - 1
                                                            devolver_dinheiro.append(tipo_de_dinheiro[contador_troco])
                                                            troco -= tipo_de_dinheiro[contador_troco]
                                                        elif (tipo_de_dinheiro[contador_troco] == 5 and n5reais > 0):
                                                            n5reais = n5reais - 1
                                                            devolver_dinheiro.append(tipo_de_dinheiro[contador_troco])
                                                            troco -= tipo_de_dinheiro[contador_troco]
                                                        elif (tipo_de_dinheiro[contador_troco] == 2 and n2reais > 0):
                                                            n2reais = n2reais - 1
                                                            devolver_dinheiro.append(tipo_de_dinheiro[contador_troco])
                                                            troco -= tipo_de_dinheiro[contador_troco]
                                                        elif (tipo_de_dinheiro[contador_troco] == 1 and m1real > 0):
                                                            m1real = m1real - 1
                                                            devolver_dinheiro.append(tipo_de_dinheiro[contador_troco])
                                                            troco -= tipo_de_dinheiro[contador_troco]
                                                        elif (tipo_de_dinheiro[contador_troco] == 0.5 and m50cents > 0):
                                                            m50cents = m50cents - 1
                                                            devolver_dinheiro.append(tipo_de_dinheiro[contador_troco])
                                                            troco -= tipo_de_dinheiro[contador_troco]
                                                        elif (tipo_de_dinheiro[contador_troco] == 0.25 and m25cents > 0):
                                                            m25cents = m25cents - 1
                                                            devolver_dinheiro.append(tipo_de_dinheiro[contador_troco])
                                                            troco -= tipo_de_dinheiro[contador_troco]
                                                        elif (tipo_de_dinheiro[contador_troco] == 0.1 and m10cents > 0):
                                                            m10cents = m10cents - 1
                                                            devolver_dinheiro.append(tipo_de_dinheiro[contador_troco])
                                                            troco -= tipo_de_dinheiro[contador_troco]
                                                        elif (tipo_de_dinheiro[contador_troco] == 0.05 and m5cents > 0):
                                                            m5cents = m5cents - 1
                                                            devolver_dinheiro.append(tipo_de_dinheiro[contador_troco])
                                                            troco -= tipo_de_dinheiro[contador_troco]
                                                        elif (tipo_de_dinheiro[contador_troco] == 0.01 and m1cents > 0):
                                                            m1cents = m1cents - 1
                                                            devolver_dinheiro.append(tipo_de_dinheiro[contador_troco])
                                                            troco -= tipo_de_dinheiro[contador_troco]
                                                        else:
                                                            break
                                                        contador_troco = contador_troco + 1
                                                        if contador_troco == len(tipo_de_dinheiro):
                                                            break
                                                if contador_troco == len(tipo_de_dinheiro) and troco > 0:
                                                    break
                                            contador_devolver = 0
                                            while contador_devolver < len(devolver_dinheiro):
                                                dinheiro_a_devolver = dinheiro_a_devolver + devolver_dinheiro[contador_devolver]
                                                contador_devolver = contador_devolver + 1
                                            faltante = troco_real - dinheiro_a_devolver 
                                            if faltante > 0:
                                                print(f"\n| Infelizmente não foi possível devolver todo o troco. \n[!] Faltou R$ {faltante:.2f} de troco. [!]")
                                            print(f"\n| Devolvendo R$ {float(dinheiro_a_devolver):.2f} de troco.")
                                            bebida_na_maquina = bebida_na_maquina - 1 
                                            print(f"| Entregando a bebida! Restam {bebida_na_maquina} bebida(s)!")
                                            dinheiro_de_troco = []
                                            dinheiro_a_devolver = 0
                                            break
                                        else:
                                            n200reais = n200reais - inserted_n200reais
                                            n100reais = n100reais - inserted_n100reais
                                            n50reais = n50reais - inserted_n50reais
                                            n20reais = n20reais - inserted_n20reais
                                            n10reais = n10reais - inserted_n10reais
                                            n5reais = n5reais - inserted_n5reais
                                            n2reais = n2reais - inserted_n2reais
                                            m1real = m1real - inserted_m1real
                                            m50cents = m50cents - inserted_m50cents
                                            m25cents = m25cents - inserted_m25cents
                                            m10cents = m10cents - inserted_m10cents
                                            m5cents = m5cents - inserted_m5cents
                                            m1cents = m1cents - inserted_m1cents
                                            print('| Devolvendo dinheiro inserido!')
                                            print('[!] Valores inseridos incorretamente - Insira novamente! [!]')