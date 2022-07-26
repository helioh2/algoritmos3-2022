

import copy
import enum


class Cor(enum.Enum):
    VERMELHO = 1
    PRETO = 2

class Node:  # nó

    def __init__(self, conteudo, cor=Cor.VERMELHO, esq=None, dir=None):
        self.conteudo = conteudo
        self.esq = esq
        self.dir = dir
        self.cor = cor
    
    def __eq__(self, outro: object) -> bool:
        """
        Compara nó "self" com nó "outro"
        node1.__eq__(node2) <==> node1 == node2
        """
        if outro == None:
            return False

        if self.conteudo != outro.conteudo or self.cor != outro.cor:
            return False

        #else
        return self.esq == outro.esq and self.dir == outro.dir



def eh_vermelho(node:Node) -> bool:

    if node is None:
        return False

    # if node is None:
    #     return False
    # elif node.cor == Cor.VERMELHO:
    #     return True

    return node.cor == Cor.VERMELHO

##Testes
assert not eh_vermelho(None)
assert eh_vermelho(Node(10, cor=Cor.VERMELHO))
assert not eh_vermelho(Node(10, cor=Cor.PRETO))


def rotacao_esquerda(raiz:Node) -> Node:
    filho_direita = raiz.dir
    filho_direita_esquerda = filho_direita.esq
    filho_direita.esq = raiz
    raiz.dir = filho_direita_esquerda
    raiz.cor, filho_direita.cor = filho_direita.cor, raiz.cor

    return filho_direita


def rotacao_direita(raiz:Node) -> Node:
    filho_esquerda = raiz.esq
    filho_esquerda_direita = filho_esquerda.dir
    filho_esquerda.dir = raiz
    raiz.esq = filho_esquerda_direita
    raiz.cor, filho_esquerda.cor = filho_esquerda.cor, raiz.cor

    return filho_esquerda


def inverte_cor(node:Node):
    if node is None:
        return None

    node.cor = Cor.PRETO if node.cor == Cor.VERMELHO else Cor.VERMELHO
    return node


assert inverte_cor(None) == None
assert inverte_cor(Node(10, cor=Cor.PRETO)) == Node(10, cor=Cor.VERMELHO)
assert inverte_cor(Node(10, cor=Cor.VERMELHO)) == Node(10, cor=Cor.PRETO)


def inverte_cores(node:Node) -> Node:

    node = inverte_cor(node)
    node.esq = inverte_cor(node.esq)
    node.dir = inverte_cor(node.dir)

    return node




def adicionar_rec(raiz:Node, elemento):
    """
    Adiciona um nó na árvore. Se a árvore for VAZIA (None),
    retorna um nó contendo o elemento
    """
    if raiz is None:
        return Node(elemento)  # novo nó folha

    if elemento <= raiz.conteudo:
        raiz.esq = adicionar_rec(raiz.esq, elemento)

    elif elemento > raiz.conteudo:
        raiz.dir = adicionar_rec(raiz.dir, elemento)


    ## CHECAGENS E AJUSTES

    if eh_vermelho(raiz.dir) and not eh_vermelho(raiz.esq):
        # quando filho da direita é vermelho e o da esquerda não é vermelho
        raiz = rotacao_esquerda(raiz)

    if eh_vermelho(raiz.esq) and eh_vermelho(raiz.esq.esq): 
        # quando filho da esquerda é vermelho e o filho da esquerda do filho da esquerda
        # é vermelho
        raiz = rotacao_direita(raiz)

    if eh_vermelho(raiz.esq) and eh_vermelho(raiz.dir):
        # quando os dois nós filhos são vermelhos
        raiz = inverte_cores(raiz)

    return raiz


def adicionar(raiz:Node, elemento):
    raiz = adicionar_rec(raiz, elemento)
    #AJUSTAR raiz
    raiz.cor = Cor.PRETO
    return raiz



#Exemplos de Node:
arvore_um_elemento = Node(30, cor=Cor.PRETO)
arvore_dois_elementos_pendendo_esquerda = Node(30, Cor.PRETO,
                                            Node(20, cor=Cor.VERMELHO))

arvore_dois_elementos_pendendo_direita = Node(50, Cor.PRETO,
                                               Node(30, cor=Cor.VERMELHO))

arvore_tres_elementos = Node(30, Cor.PRETO,
                                Node(20, cor=Cor.PRETO),
                                Node(50, cor=Cor.PRETO))




#TESTES
arvore_um_elemento = Node("B", cor=Cor.PRETO)

arvore_um_mais_um_esquerda = Node("B",
                                Node("A", cor=Cor.VERMELHO),
                                None,
                                Cor.PRETO)
                            
arvore_um_mais_um_direita = Node("C",
                                Node("B", cor=Cor.VERMELHO),
                                None,
                                Cor.PRETO)

arvore_um_mais_um_esquerda2 = Node("C",
                                Node("A", cor=Cor.VERMELHO),
                                None,
                                Cor.PRETO)


arvore_um_mais_um_direita_mais_um_esquerda_na_esquerda = Node("B",
                                                            Node("A", cor=Cor.PRETO),
                                                            Node("C", cor=Cor.PRETO),
                                                            Cor.PRETO)


arvore_um_mais_um_esquerda2_mais_um_direita_na_esquerda = arvore_um_mais_um_direita_mais_um_esquerda_na_esquerda

arvore_um_mais_um_esquerda_mais_um_direita = Node("B",
                                                Node("A", cor=Cor.PRETO),
                                                Node("C", cor=Cor.PRETO),
                                                Cor.PRETO)


arvore_quatro_elementos = Node("E", 
                            Node("B", cor=Cor.PRETO),
                            Node("S",
                                Node("R", cor=Cor.VERMELHO),
                                None,
                                cor=Cor.PRETO),
                            cor=Cor.PRETO)


arvore_quatro_elementos_adiciona_esquerda_esquerda = Node("E", 
                                                        Node("B",
                                                            Node("A", cor=Cor.VERMELHO),
                                                            None,
                                                            cor=Cor.PRETO,),
                                                        Node("S",
                                                            Node("R", cor=Cor.VERMELHO),
                                                            None,
                                                            cor=Cor.PRETO),
                                                        cor=Cor.PRETO)

arvore_quatro_elementos_adiciona_esquerda_direita = Node("E", 
                                                        Node("C",
                                                            Node("B", cor=Cor.VERMELHO),
                                                            None,
                                                            cor=Cor.PRETO,),
                                                        Node("S",
                                                            Node("R", cor=Cor.VERMELHO),
                                                            None,
                                                            cor=Cor.PRETO),
                                                        cor=Cor.PRETO)

#Testes

assert adicionar(None, "B") == arvore_um_elemento

assert adicionar(copy.deepcopy(arvore_um_elemento), "A") == arvore_um_mais_um_esquerda

assert adicionar(copy.deepcopy(arvore_um_elemento), "C") == arvore_um_mais_um_direita

assert adicionar(arvore_um_mais_um_esquerda, "C") == arvore_um_mais_um_esquerda_mais_um_direita

assert adicionar(copy.deepcopy(arvore_quatro_elementos), "A") == arvore_quatro_elementos_adiciona_esquerda_esquerda

assert adicionar(copy.deepcopy(arvore_quatro_elementos), "C") == arvore_quatro_elementos_adiciona_esquerda_direita

assert adicionar(copy.deepcopy(arvore_um_mais_um_direita), "A") == arvore_um_mais_um_direita_mais_um_esquerda_na_esquerda

assert adicionar(copy.deepcopy(arvore_um_mais_um_esquerda2), "B") == arvore_um_mais_um_direita_mais_um_esquerda_na_esquerda

