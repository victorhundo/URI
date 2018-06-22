from bisect import bisect_left

def busca(array,n):
    index = (bisect_left(array,n))
    if index < len(array) and array[index] == n:
       return index
    else:
        return None

def main(entrada):
    lista = []
    for i in range(entrada):
        caixa = input().split()
        inferior = int(caixa[0])
        superior = int(caixa[1])
        lista += list(range(inferior,superior + 1))

    lista.sort()
    consulta = int(input())
    saida = busca(lista,consulta)

    if (saida != None):
        somador = 0
        lista.remove(consulta)
        while busca(lista,consulta) != None:
            somador += 1
            lista.remove(consulta)
        msg = "{} found from {} to {}"
        print(msg.format(consulta,saida,saida + somador))
    else:
        msg = "{} not found"
        print(msg.format(consulta))

while True:
    try:
        n = input()
        if (n):
            main(int(n))
    except EOFError:
        break
        
