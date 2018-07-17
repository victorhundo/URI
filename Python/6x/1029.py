testes = int(input())

for i in range(testes):
    n = int(input())
    valor = [0] * (n + 1)
    chamadas = [0] * (n + 1)
    for i in range(n + 1):
        if (i == 0):
            valor[i] = 0
            chamadas[i] = 0
        elif (i == 1):
            valor[i] = 1
            chamadas[i] = 0
        else:
            valor[i] = valor[i-1] + valor[i-2]
            chamadas[i] = chamadas[i-1] + chamadas[i-2] + 2

    msg = "fib({}) = {} calls = {}"
    print(msg.format(n,chamadas[n],valor[n]))
    
    
