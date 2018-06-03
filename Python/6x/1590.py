##
##INCOMPLETE WA(30%)
##

def get_bin(num,base):
    return bin(num)[2:].zfill(base)

caso_teste = int(input())
for caso in range(caso_teste):
    entrada = input().split()
    n = int(entrada[0])
    k = int(entrada[1])
    s = input().split()
    numeros = [0] * n
    for i in range(n):
        numeros[i] = int(s[i])

    numeros.sort()
    numeros.reverse()
    base = (len(bin(numeros[0])[2:]))
    aux = []
    out = 2**base - 1
    match = False
    for i in range(base):
        if (len(aux) >= k):
            match = True
            break
        aux = []
        out = 2**base - 1
        for j in numeros:
           if (len(aux) >= k): break
           binario = get_bin(j,base)
           if (binario[i] == '1'):
               aux.append(j)
               out = out & j

    if (match):
        print(out)
    else:
        print(0)



##numeros = [8,4,2,1]
##numemros = [1073741823,1019123382, 1044628510,1038459169,1049709462,1026579533,1061136321,1015724753,1029527407,1069278663,1070298324,1046498410,1030597727,1021605793,1043562197,1040560634,1047315728,1056588290,1017168704,1037375714,1032740187,1035241580,1053557176,1014546164,1013591354,1018619308,1050210511,1066432361,1011488721,1057542356,1023197576,1064503458,1012382770,1062458598,0]
