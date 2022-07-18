
from arvore import *


def encontra_e_remove_sucessor(raiz:Node) -> Node:
    """
    Encontra o sucessor do nó e remove ele da posição atual.
    Se não tem sucessor, retorna None
    """
    if raiz.dir == VAZIA: # quando não tem filho da direita, se sucessor
        return None

    if raiz.dir.esq == VAZIA:  # quando o sucessor é o filho da direita
        sucessor = raiz.dir
        raiz.dir = raiz.dir.dir
        return sucessor

    #else:
    anterior = None
    atual = raiz.dir

    while atual.esq != VAZIA:  
        #descendo à esquerda da subarvore direita até achar o sucessor
        anterior = atual
        atual = atual.esq

    anterior.esq = atual.dir  #removendo o atual de sua posicao 
    #(fazer o anterior apontar para a subarvore direita do atual)

    return atual


def remover(raiz:Node, elemento) -> Node:

    if raiz == VAZIA:
        return raiz

    #else
    if raiz.conteudo == elemento:  #achei o elemento a remover
        node_sucessor = encontra_e_remove_sucessor(raiz)

        if not node_sucessor: #se não existe sucessor
            return raiz.esq

        #else
        # setando os filhos esquerdo e direito do sucessor apontando p/ o esquerdo e direito da raiz
        # ou seja, substituindo a raiz pelo sucessor
        node_sucessor.esq = raiz.esq
        node_sucessor.dir = raiz.dir

        return node_sucessor

    # else
    if elemento <= raiz.conteudo:
        raiz.esq = remover(raiz.esq, elemento)
        # Procura e remove do lado esquerdo, e seta o ponteiro para a nova subárvore esquerda
    else:
        raiz.dir = remover(raiz.dir, elemento)
        # Procura e remove do lado direito, e seta o ponteiro para a nova subárvore direita

    return raiz


#TESTES:
arvore_um_elemento = Node(5)
arvore_dois_elementos_esquerda = Node(5, Node(2), VAZIA)
arvore_tres_elementos = Node(5, Node(2), Node(10))
arvore_quatro_elementos = Node(5, 
                                Node(2), 
                                Node(10, 
                                    Node(8), 
                                    VAZIA))
arvore_cinco_elementos = Node(5, 
                                Node(2), 
                                Node(10, 
                                    Node(8, 
                                        VAZIA, 
                                        Node(9)), 
                                    VAZIA))

# remoção de árvore vazia e árvore com um único elemento
assert remover(VAZIA, 5) == VAZIA
assert remover(arvore_um_elemento, 5) == VAZIA

# caso em que não tem sucessor
assert remover(arvore_dois_elementos_esquerda, 5) == Node(2)

# sucessor é o filho da direita
assert remover(arvore_tres_elementos, 5) == Node(10, Node(2), VAZIA)

# sucessor está mais profundo
assert remover(arvore_quatro_elementos, 5) == Node(8, Node(2), Node(10))

# sucessor que tem filho da direita
assert remover(arvore_cinco_elementos, 5) == Node(8, Node(2), Node(10, Node(9), VAZIA))