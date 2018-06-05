lista = [7,6,2,3,6,7]

fila = []
fila.append(0)

while fila:
    atual = fila.pop()

    maior_indice = -1
    maior_valor = -1
    for f in range(len(lista)):
        if (f != atual):
            aux = lista[atual] & lista[f]
            if (aux > maior_valor):
                maior_indice = f
                maior_valor = aux

    if(maior_indice != -1):
        fila.append(maior_indice)

