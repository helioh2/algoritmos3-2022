


class Node:

    def __init__(self, chave=None, filhos=[]):
        """
        Chave pode ser None ou um 
        caractere (string), 'filhos' é uma lista de Nodes 
        """
        self.chave = chave
        self.filhos = filhos


    def __str__(self) -> str:

        def to_str_rec(node, nivel):
            chave_str = node.chave if node.chave else "*"
            string = nivel*"\t" + chave_str + "\n"
            for filho in node.filhos:
                string +=  to_str_rec(filho, nivel+1)
            return string

        return to_str_rec(self, nivel=0)

    


### 
vazio = Node(chave=None)
um_elemento = Node(chave=None, filhos = [Node("O")])
tres_elementos = Node(chave=None, filhos = [Node("O"), Node("D", filhos=[Node("O")])])
print(tres_elementos)


def adicionar(node:Node, palavra:str) -> Node:

    if not palavra:  # se palavra é uma string vazia ("")
        return node

    primeiro_caracter = palavra[0]

    for filho in node.filhos:
        if primeiro_caracter == filho.chave: # encontrei o filho que tem o caracter
            filho = adicionar(filho, palavra[1:])
            return filho

    ##"else do for"
    novo_filho = Node(primeiro_caracter)  # criando novo filho
    node.filhos.append(novo_filho) # adiciona o novo filho na lista de filhos do nó atual
    novo_filho = adicionar(novo_filho, palavra[1:]) # adiciona para baixo na arvore do novo filho
    
    return node


node = Node()  #node vazio
adicionar(node, "o")
adicionar(node, "rato")
adicionar(node, "roeu")
adicionar(node, "a")
adicionar(node, "roupa")
adicionar(node, "do")
adicionar(node, "rei")
adicionar(node, "de")
adicionar(node, "roma")

print(node)