from bisect import bisect_left

def busca(array,n):
    index = (bisect_left(array,n))
    if index < len(array) and array[index] == n:
       return index
    else:
        return None

caso = 0
while True:
    entrada = input().split()
    n = int(entrada[0])
    q = int(entrada[1])
    if (q == 0 and n == 0): break
    caso += 1
    array = [0] * n
    for i in range(n):
        elemento = int(input())
        array[i] = elemento

    print("CASE# {}:".format(caso))
    array = sorted(array)
    for i in range(q):
        consulta = int(input())
        resultado = busca(array,consulta)
        if (resultado):
            saida = "{} found at {}"
            print(saida.format(consulta, resultado))
        else:
            saida = "{} not found"
            print(saida.format(consulta))
            

    
