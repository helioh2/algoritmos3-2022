

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

        if self.conteudo != outro.conteudo:
            return False

        #else
        return self.esq == outro.esq and self.dir == outro.dir



#Exemplos de Node:
arvore_um_elemento = Node(30, cor=Cor.PRETO)
arvore_dois_elementos_pendendo_esquerda = Node(30, Cor.PRETO,
                                            Node(20, cor=Cor.VERMELHO))

arvore_dois_elementos_pendendo_direita = Node(50, Cor.PRETO,
                                               Node(30, cor=Cor.VERMELHO))

arvore_tres_elementos = Node(30, Cor.PRETO,
                                Node(20, cor=Cor.PRETO),
                                Node(50, cor=Cor.PRETO))



def adicionar_rec(raiz:Node, elemento):
    """
    Adiciona um nó na árvore. Se a árvore for VAZIA (None),
    retorna um nó contendo o elemento
    """
    if raiz == None:
        return Node(elemento)  # novo nó folha

    if elemento <= raiz.conteudo:
        raiz.esq = adicionar_rec(raiz.esq, elemento)

    elif elemento > raiz.conteudo:
        raiz.dir = adicionar_rec(raiz.dir, elemento)


    ## CHECAGENS E AJUSTES

    

    return raiz


def adicionar(raiz:Node, elemento):
    raiz = adicionar_rec(raiz, elemento)
    #AJUSTAR raiz
    raiz.cor = Cor.PRETO
    return raiz
    



assert adicionar(arvore_um_elemento, 20)