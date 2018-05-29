##
## INCOMPLETE - maximum recursion depth exceeded in comparison!!
##

nop = ['N','O','P']

def get_genoma(atual,limite, genoma="", sub="", adj=""):
    if (len(genoma) == limite):
        return genoma
    else:
        if (atual == 'N'): proximos = ['O','P']
        elif (atual == 'O'): proximos = ['N','P']
        else: proximos = ['N']

        if (atual == 'N' and len(genoma) != 1):
            adj = sub
            sub = ""
        
        genoma += atual
        sub += atual
        for proximo in proximos:
            if ( sub + proximo != adj):
                return get_genoma(proximo, limite, genoma,sub,adj)
        
while True:
    limite = int(input())

    if(limite == 0):
        print()
        break
    else:
        print(get_genoma('N',limite))
