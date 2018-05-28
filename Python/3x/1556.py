##
## INCOMPLETE - Time limit exceeded!!
##

word = input()
visited = [False] * len(word) 
path = ""
output = []

# Retorna lista com indicies em ordem alfabetica
# da palavara a partir do indice u
def alpha_order(u,word):
    if (u != 0):  u += 1

    index_order = [0] * len(word[u:])
    aux = list(word)
    alpha = sorted(word[u:])
    
    for j in range(u):
        aux[j] = '-'
        
    for i in range(u, len(word)):
        j = i - u
        index = aux.index(alpha[j])
        index_order[j] = index
        aux[index] = '-'
        
    return index_order

# Retorna lista com todos os caminhos
# do vertice 'u' até o ultimo vertice
def bfs(u,visisted,path):
    visited[u] = True
    path += word[u]
    
    if (not output.count(path) > 0):
        output.append(path)
        print(path)

    children = alpha_order(u,word)        
    for i in children:
        if (visited[i] == False):
            bfs(i,visited,path)
                
    path = path[:-1]
    visited[u] = False


def main(word):
    for i in alpha_order(0,word):
        bfs(i,visited,path)

main(word)
