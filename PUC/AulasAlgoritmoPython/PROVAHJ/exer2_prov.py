def verificaVogais():
    listaNomes = ['eduardo', 'dudu', 'edu', 'du']
    v = -1

    a = 0
    e = 0
    i = 0
    o = 0
    u = 0

    while v < len(listaNomes):
        v += 1
        for listaNomes in listaNomes[v]:
            if listaNomes == 'a':
                a += 1
            elif listaNomes == 'e':
                e += 1
            elif listaNomes == 'i':
                i += 1
            elif listaNomes == 'o':
                o += 1
            elif listaNomes == 'u':
                u += 1
    print("qt a: ", a)
    print("qt e: ", e)
    print("qt i: ", i)
    print("qt o: ", o)
    print("qt u: ", u)
verificaVogais()