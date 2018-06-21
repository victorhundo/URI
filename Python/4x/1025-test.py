class Node:
    def __init__(self, value):
        self.esquerda = None;
        self.direita = None;
        self.data = value;

class Arvore_Binaria:
    def __init__(self):
        self.raiz = None;

    def addNode(self, node, value):
        if(node==None):
            self.raiz = Node(value);
        else:
            if(value<node.data):
                if(node.esquerda==None):
                    node.esquerda = Node(value)
                else:
                    self.addNode(node.esquerda, value);
            else:
                if(node.direita==None):
                    node.direita = Node(value)
                else:
                    self.addNode(node.direita, value);

    def printInorder(self, node):
        if(node!=None):
            self.printInorder(node.esquerda)
            print(node.data)
            self.printInorder(node.direita)

    def busca(self,node,value,altura=1):
        if (node==None or value == node.data):
            return (node,altura)
        if (value < node.data):
            return self.busca(node.esquerda,value,altura + 1)
        else:
            return self.busca(node.direita,value,altura + 1)

caso = 0
while True:
    entrada = input().split()
    n = int(entrada[0])
    q = int(entrada[1])
    if (q == 0 and n == 0): break
    caso += 1
    array = []

    arvore = Arvore_Binaria()
    for i in range(n):
        elemento = int(input())
        array.append(elemento)
        arvore.addNode(arvore.raiz, elemento)

    print("CASE# {}:".format(caso))
    for i in range(q):
        consulta = int(input())
        resultado = arvore.busca(arvore.raiz, consulta)
        if (resultado[0].data):
            saida = "{} found at {}"
            print(saida.format(resultado[0].data, resultado[1]))
        else:
            saida = "{} not found"
            print(saida.format(consulta))
