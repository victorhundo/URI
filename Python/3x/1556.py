import collections
def bfs(palavra):
    fila = []
    fila.insert(0, (0,palavra[0]))
    

    while fila:
        atual = fila.pop()
        index = atual[0]
        path = atual[1]
        
        if ( (not path[1:] in saida) and path[1:] != ''):
            saida[path[1:]] = 0

        if (not path in saida):
            saida[path] = 0
            for i in range(index + 1, len(palavra)):
                fila.insert( 0, (i, path + palavra[i]))

while True:
    saida = {}
    
    try:
        palavra = input()
    except EOFError:
        break

    bfs(palavra)
    for i in sorted(saida):
        print(i)
    print()
