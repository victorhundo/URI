testes = int(input())
for teste in range(testes):
    pacotes = int(input())
    peso = [0]
    valor = [0]
    for pacote in range(pacotes):
        entrada = input().split()
        valor.append(int(entrada[0]))
        peso.append(int(entrada[1]))


    M = [[0 for x in range(51)] for y in range(pacotes + 1)]

    for Y in range(1, pacotes + 1):
        for X in range(1,51):
            sobra =  X - peso[Y]
            if (sobra >= 0):
                sobra_valor = M[Y-1][sobra]
                M[Y][X] = max(sobra_valor + valor[Y], M[Y-1][X])
            else:
                M[Y][X] = M[Y-1][X]


    solucao = []
    peso_total = 0
    aux = 50
    for Y in range(pacotes,0,-1):
        if (M[Y][aux] != M[Y-1][aux]):
            solucao.append(Y)
            peso_total += peso[Y]
            aux = aux - peso[Y]


    sobra = pacotes - len(solucao)
    brinquedos = M[pacotes][50]
    saida = "{} brinquedos\nPeso: {} kg\nsobra(m) {} pacote(s)\n"
    print(saida.format(brinquedos, peso_total,sobra))
        
