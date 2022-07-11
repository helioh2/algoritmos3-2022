
VAZIA = None  # null

class Node:  # nó

    def __init__(self, conteudo:int, esq=VAZIA, dir=VAZIA):
        self.conteudo = conteudo
        self.esq = esq
        self.dir = dir


    ## node1.__eq__(node2)  <==> node1 == node2
    def __eq__(self, outro: object) -> bool:
        if outro == VAZIA:
            return False

        if self.conteudo != outro.conteudo:
            return False

        #else
        return self.esq == outro.esq and self.dir == outro.dir

def str_arvore(raiz):
    string = "("

    string += str(raiz.conteudo) + " "

    if raiz.esq: # if raiz.esq != None
        string += str_arvore(raiz.esq) + " "

    if raiz.dir: # if raiz.esq != None
        string += str_arvore(raiz.dir) + " "

    string += ")"

    return string


def adicionar_na_arvore(raiz:Node, elemento:int) -> Node:
    """
    Adiciona um nó na árvore. Se a árvore for VAZIA (None),
    retorna um nó contendo o elemento
    """
    return Node(elemento)


#TESTES:
assert adicionar_na_arvore(VAZIA, 18) == Node(18)

assert adicionar_na_arvore(Node(18), 8) == Node(18, Node(8), VAZIA)


arvore_um_elemento = Node(8)  # nó folha
print(arvore_um_elemento.__dict__)

arvore_dois_elementos = Node(18, 
                                Node(8), 
                                VAZIA)

arvore_dois_elementos2 = Node(18, 
                                arvore_um_elemento, 
                                VAZIA)

arvore_tres_elementos = Node(18, 
                                Node(8), 
                                Node(30))

print(arvore_tres_elementos.conteudo)
print(arvore_tres_elementos.esq.conteudo)
print(arvore_tres_elementos.dir.conteudo)

from pprint import pprint
pprint(str_arvore(arvore_tres_elementos))




