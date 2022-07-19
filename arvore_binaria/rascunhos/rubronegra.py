
import copy
from enum import Enum, auto

class Cor(Enum):
    VERMELHO = auto()
    PRETO = auto()

class Node:

    def __init__(self, conteudo, esq=None, dir=None, cor=Cor.VERMELHO):
        self.conteudo = conteudo
        self.esq = esq
        self.dir = dir
        self.cor = cor

    def __eq__(self, outro: object) -> bool:
        """
        Compara nó "self" com nó "outro"
        node1.__eq__(node2) <==> node1 == node2
        """
        if not outro:
            return False

        if self.conteudo != outro.conteudo or self.cor != outro.cor:
            return False

        #else
        return self.esq == outro.esq and self.dir == outro.dir



def eh_vermelho(node:Node):
    if node is not None:
        return node.cor == Cor.VERMELHO
    return False


def rotacao_esquerda(raiz:Node):

    filho_direita = raiz.dir
    neto_direita_esquerda = filho_direita.esq
    raiz.dir = neto_direita_esquerda
    filho_direita.esq = raiz
    filho_direita.cor, raiz.cor = raiz.cor, filho_direita.cor

    return filho_direita


def rotacao_direita(raiz:Node):

    filho_esquerda = raiz.esq
    neto_esquerda_direita = filho_esquerda.dir
    raiz.esq = neto_esquerda_direita
    filho_esquerda.dir = raiz
    filho_esquerda.cor, raiz.cor = raiz.cor, filho_esquerda.cor

    return filho_esquerda


def inverter_cores(node:Node):
    node.cor = Cor.VERMELHO if node.cor == Cor.PRETO else Cor.PRETO
    if node.esq:
        node.esq.cor = Cor.VERMELHO if node.esq.cor == Cor.PRETO else Cor.PRETO
    if node.dir:
        node.dir.cor = Cor.VERMELHO if node.dir.cor == Cor.PRETO else Cor.PRETO

    return node

def adiciona_rec(raiz:Node, elemento) -> Node:
    
    if not raiz:
        return Node(elemento) # por default, vermelho

    if elemento <= raiz.conteudo:
        raiz.esq = adiciona_rec(raiz.esq, elemento)
    else:
        raiz.dir = adiciona_rec(raiz.dir, elemento)

    if eh_vermelho(raiz.dir) and not eh_vermelho(raiz.esq):
        raiz = rotacao_esquerda(raiz)

    if eh_vermelho(raiz.esq) and eh_vermelho(raiz.esq.esq):
        raiz = rotacao_direita(raiz)

    if eh_vermelho(raiz.esq) and eh_vermelho(raiz.dir):
        raiz = inverter_cores(raiz)

    return raiz


def adiciona(raiz:Node, elemento) -> Node:
    raiz = adiciona_rec(raiz, elemento)
    raiz.cor = Cor.PRETO
    return raiz



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

assert adiciona(None, "B") == arvore_um_elemento

assert adiciona(copy.deepcopy(arvore_um_elemento), "A") == arvore_um_mais_um_esquerda

assert adiciona(copy.deepcopy(arvore_um_elemento), "C") == arvore_um_mais_um_direita

assert adiciona(arvore_um_mais_um_esquerda, "C") == arvore_um_mais_um_esquerda_mais_um_direita

assert adiciona(copy.deepcopy(arvore_quatro_elementos), "A") == arvore_quatro_elementos_adiciona_esquerda_esquerda

assert adiciona(copy.deepcopy(arvore_quatro_elementos), "C") == arvore_quatro_elementos_adiciona_esquerda_direita

assert adiciona(copy.deepcopy(arvore_um_mais_um_direita), "A") == arvore_um_mais_um_direita_mais_um_esquerda_na_esquerda

assert adiciona(copy.deepcopy(arvore_um_mais_um_esquerda2), "B") == arvore_um_mais_um_direita_mais_um_esquerda_na_esquerda



