def binary_search(array,i,j,n):
    if (i <= j):
        mid = int((i + j)/2)
        if (array[i] == n):
            return (n,i + 1)
        if (array[mid] == n): 
            return (n,mid + 1)
        if (array[mid] < n):  
            return binary_search(array,mid + 1,j,n)
        else:
            return binary_search(array,i,mid - 1,n)
    else:
        return None


def busca(array,n):
    for i in range(len(array)):
        if (array[i] == n):
            return (n, i + 1)

caso = 0
while True:
    entrada = input().split()
    n = int(entrada[0])
    q = int(entrada[1])
    if (q == 0 and n == 0): break
    caso += 1
    array = []
    for i in range(n):
        elemento = int(input())
        array.append(elemento)

    print("CASE# {}:".format(caso))
    for i in range(q):
        consulta = int(input())
        resultado = busca(array, consulta)
        if (resultado):
            saida = "{} found at {}"
            print(saida.format(resultado[0], resultado[1]))
        else:
            saida = "{} not found"
            print(saida.format(consulta))

    
