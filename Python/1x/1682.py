##
## INCOMPLETE - Wrong answer (100%) !!
##
      
while True:
    limite = int(input())

    if(limite == 0):
        print()
        break
    else:
        genoma = ""
        sub = ""
        adj1 = ""
        adj2 = ""
        pilha = ['N']
        while (len(genoma) != limite):
            atual = pilha.pop()
            if (atual == 'N'): proximos = ['P','O']
            elif (atual == 'O'): proximos = ['P','N']
            else: proximos = ['N']

            if (atual == 'N' and len(genoma) != 0):
                adj2 = adj1
                adj1 = sub
                sub = ""

            genoma += atual
            sub += atual
            for proximo in proximos:
                if (atual == 'N'):
                    if (sub + 'P' != adj1 and sub + '
                if (sub + proximo != adj1 and sub + proximo != adj2):
                    pilha.append(proximo)

        print(genoma)
