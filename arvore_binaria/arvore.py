
VAZIA = None  # null

class Node:  # nó

    def __init__(self, conteudo, esq=VAZIA, dir=VAZIA):
        self.conteudo = conteudo
        self.esq = esq
        self.dir = dir
    
    def __eq__(self, outro: object) -> bool:
        """
        Compara nó "self" com nó "outro"
        node1.__eq__(node2) <==> node1 == node2
        """
        if outro == VAZIA:
            return False

        if self.conteudo != outro.conteudo:
            return False

        #else
        return self.esq == outro.esq and self.dir == outro.dir

def constroi_arvore_predefinida(tupla: tuple):

    def constroi_arvore_from_indice_tupla(tupla, indice):
        if indice >= len(tupla):
            return None
        return constroi_arvore_predefinida(tupla[indice])

    if len(tupla) == 0:
        return Node()

    return Node(tupla[0], 
                constroi_arvore_from_indice_tupla(tupla, 1),
                constroi_arvore_from_indice_tupla(tupla, 2)
                )



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
    if raiz == VAZIA:
        return Node(elemento)  # novo nó folha

    if elemento <= raiz.conteudo:
        nova_subarvore_esq = adicionar_na_arvore(raiz.esq, elemento)
        raiz.esq = nova_subarvore_esq
    elif elemento > raiz.conteudo:
        nova_subarvore_dir = adicionar_na_arvore(raiz.dir, elemento)
        raiz.dir = nova_subarvore_dir

    return raiz


#TESTES:
# Árvore vazia:
assert adicionar_na_arvore(VAZIA, 18) == Node(18)

# Inserir quando vai à esquerda da raiz
assert adicionar_na_arvore(Node(18), 8) == Node(18, Node(8), VAZIA)

# Inserir quando vai à direita da raiz
assert adicionar_na_arvore(Node(18), 36) == Node(18, VAZIA, Node(36))

# Inserir quando vai à direita da raiz
assert adicionar_na_arvore(Node(18, Node(8), VAZIA), 5) == Node(18, Node(8, Node(5), VAZIA), VAZIA)

# Inserir quando vai à direita da raiz
assert adicionar_na_arvore(Node(18, Node(8), VAZIA), 10) == Node(18, Node(8, VAZIA, Node(10)), VAZIA)


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



arvore_tupla1 = ("macarrao", 
                    ("feijao", ("arroz",), ("jujuba",)), 
                    ("patê", ("ovos",), ("salsicha",))
                )

arvore_teste = constroi_arvore_predefinida(arvore_tupla1)

