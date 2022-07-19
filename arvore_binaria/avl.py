

class Node:  # nó

    def __init__(self, conteudo, esq=None, dir=None):
        self.conteudo = conteudo
        self.esq = esq
        self.dir = dir
        self.set_altura()

    def set_altura(self):
        self.altura = 0

        if self.esq is not None:
            if self.dir is not None:
                self.altura += 1 + max(self.esq.altura, self.dir.altura)
            else:
                self.altura += 1 + self.esq.altura
        elif self.dir is not None:
            self.altura += 1 + self.dir.altura
  
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


def fator_balanceamento(node:Node) -> int:

    if node is None:
        return 0

    altura_esq = 0 if node.esq is None else node.esq.altura
    altura_dir = 0 if node.dir is None else node.dir.altura

    return altura_esq - altura_dir


def rotacao_esquerda(raiz:Node) -> Node:
    filho_direita = raiz.dir
    filho_direita_esquerda = filho_direita.esq
    filho_direita.esq = raiz
    raiz.dir = filho_direita_esquerda

    return filho_direita


def rotacao_direita(raiz:Node) -> Node:
    filho_esquerda = raiz.esq
    filho_esquerda_direita = filho_esquerda.dir
    filho_esquerda.dir = raiz
    raiz.esq = filho_esquerda_direita

    return filho_esquerda


def adicionar(raiz:Node, elemento) -> Node:
    if raiz is None:
        return Node(elemento)  # novo nó folha

    if elemento <= raiz.conteudo:
        raiz.esq= adicionar(raiz.esq, elemento)
        raiz.altura = 1 + raiz.esq.altura  #atualização da altura de cada nó visitado
    elif elemento > raiz.conteudo:
        raiz.dir = adicionar(raiz.dir, elemento)
        raiz.altura = 1 + raiz.dir.altura #atualização da altura de cada nó visitado

    # balanceamento
    if fator_balanceamento(raiz) == 2:  # arvore pendendo para a esquerda
        if fator_balanceamento(raiz.esq) == -1: # subarvore esquerda pendendo para a direita
            raiz.esq = rotacao_esquerda(raiz.esq)
        
        raiz = rotacao_direita(raiz)
    
    elif fator_balanceamento(raiz) == -2: # arvore pendendo para a direita
        if fator_balanceamento(raiz.dir) == 1: # subarvore direita pendendo para a esquerda
            raiz.dir = rotacao_direita(raiz.dir)
        
        raiz = rotacao_esquerda(raiz)

    return raiz



caso_rot_direita = Node(65, 
                        Node(50,
                            Node(20),
                            Node(60)),
                        Node(91))

assert adicionar(caso_rot_direita, 10) == Node(50, 
                                                Node(20, 
                                                    Node(10),
                                                    None),
                                                Node(65,
                                                    Node(60),
                                                    Node(91))
                                                    )


caso_rot_esquerda = Node(50,
                            Node(30),
                            Node(80,
                                Node(65),
                                Node(90)))

assert adicionar(caso_rot_esquerda, 95) == Node(80,
                                                        Node(50,
                                                            Node(30),
                                                            Node(65)),
                                                        Node(90,
                                                            None,
                                                            Node(95)))                          


caso_rot_esquerda_direita =  Node(10,
                                    Node(5,
                                        Node(4),
                                        Node(6)),
                                    Node(11))


assert adicionar(caso_rot_esquerda_direita, 7) == Node(6,
                                                            Node(5,
                                                                Node(4),
                                                                None),
                                                            Node(10,
                                                                Node(7),
                                                                Node(11)))

        
caso_rot_direita_esquerda = Node(40,
                                Node(20),
                                Node(70,
                                    Node(53),
                                    Node(84)))

assert adicionar(caso_rot_direita_esquerda, 60) == Node(53,
                                                            Node(40,
                                                                Node(20),
                                                                None),
                                                            Node(70,
                                                                Node(60),
                                                                Node(84)))


