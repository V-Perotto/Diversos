def validaTelefone(telefone):
    if len(telefone) == 10:
        if telefone[0] == 7 or 8 or 9:
            ativador = True
        else:
            ativador = False
    else:
        ativador = False
    if ativador == True:
        ativado = 'YES'
    else:
        ativado = 'NO'

    return ativado