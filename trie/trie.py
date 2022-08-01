
INICIO_LETRAS_ASCII = 65
TAMANHO_ALFABETO = 26


class Node:

    def __init__(self, chave=None):
        """
        Chave pode ser None ou um 
        caractere (string), 'filhos' é uma lista de Nodes 
        """
        self.chave = chave
        self.filhos = [None]*TAMANHO_ALFABETO
        self.contagem = 0
   
    def __str__(self) -> str:

        def to_str_rec(node, nivel):
            chave_str = node.chave if node.chave else "*"
            string = nivel*"\t" + chave_str + "\n"
            for filho in node.filhos:
                if filho:
                    string +=  to_str_rec(filho, nivel+1)
            return string

        return to_str_rec(self, nivel=0)



arvore1 = Node(chave=None)

arvore2 = Node(chave=None)

arvore1.filhos.append("A")



def adicionar(node:Node, palavra:str) -> Node:

    if not palavra:  # se palavra é uma string vazia ("")
        # quando a palavra é vazia, então terminou de adicionar
        node.contagem += 1
        return node

    primeiro_caracter = palavra[0].upper() #pega caracter em letra maiuscula
    primeiro_caracter_int = ord(primeiro_caracter)
    indice = primeiro_caracter_int - INICIO_LETRAS_ASCII

    if indice < 0 or indice > 25:
        node = adicionar(node, palavra[1:])
        return node

    filho = node.filhos[indice]

    if filho:
        filho = adicionar(filho, palavra[1:])
        return filho
    

    #else  (posicao no vetor é nula)
    novo_filho = Node(primeiro_caracter)  # criando novo filho
    node.filhos[indice] = novo_filho
    novo_filho = adicionar(novo_filho, palavra[1:]) # adiciona para baixo na arvore do novo filho
    
    return node


def busca_string(raiz:Node, palavra:str):
    """
    Retorna a contagem de vezes se existe a  palavra,
    ou 0 caso não encontre
    """

    if not palavra:
        return raiz.contagem

    primeiro_caracter = palavra[0].upper() #pega caracter em letra maiuscula
    primeiro_caracter_int = ord(primeiro_caracter)
    indice = primeiro_caracter_int - INICIO_LETRAS_ASCII

    if indice < 0 or indice > 25:
        return busca_string(node, palavra[1:])

    filho = raiz.filhos[indice]

    if not filho:
        return 0

    #else (filho existe)
    return busca_string(filho, palavra[1:])

    



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
adicionar(node, "casa!")

print(node)

# assert busca_string(node, "")
assert busca_string(node, "roupeiro") == 0
assert busca_string(node, "roupa") == 1
assert busca_string(node, "roma") == 1

node1 = Node()

assert busca_string(node, "k") == 0
assert busca_string(node1, "k") == 0

adicionar(node, "roma")

assert busca_string(node, "roma") == 2
assert busca_string(node, "rom") == 0
print(busca_string(node, "roma"))