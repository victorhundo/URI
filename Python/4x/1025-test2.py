#USAR HASHMAP
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
