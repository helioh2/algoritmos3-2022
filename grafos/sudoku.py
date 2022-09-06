

class Node:

    def __init__(self, posicao, cores=None):
        self.posicao = posicao
        self.cores = cores

    def __hash__(self):
        return hash(self.posicao)

N=9
vertice1 = Node((0,0), cores=list(range(1, N+1)))
print(vertice1.posicao)
print(hash(vertice1))


class Grafo:

    def __init__(self, vertices, arestas):
        pass


B = None
TAB_FACIL= [[2, 7, 4, B, 9, 1, B, B, 5],
            [1, B, B, 5, B, B, B, 9, B],
            [6, B, B, B, B, 3, 2, 8, B],
            [B, B, 1, 9, B, B, B, B, 8],
            [B, B, 5, 1, B, B, 6, B, B],
            [7, B, B, B, 8, B, B, B, 3],
            [4, B, 2, B, B, B, B, B, 9],
            [B, B, B, B, B, B, B, 7, B],
            [8, B, B, 3, 4, 9, B, B, B]]

vertices = {}
for i in range(9):
    for j in range(9):
        valor = TAB_FACIL[i][j]
        if valor:
            node = Node((i,j), [valor])
        else:
            node = Node((i,j), list(range(1, N+1)))
        vertices[(i,j)] = node

print(vertices)

arestas = []   #()

LINHAS = [[(l,c) for c in range(9)] for l in range(9)]  # ex: [(0,0), (0,1), (0,2)... (0,8)], [(1,0), (1,1),... (1,8)]
COLUNAS = [[(l,c) for l in range(9)] for c in range(9)]
CAIXAS = [[(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)],
          [(0,3),(0,4),(0,5),(1,3),(1,4),(1,5),(2,3),(2,4),(2,5)],
          [(0,6),(0,7),(0,8),(1,6),(1,7),(1,8),(2,6),(2,7),(2,8)],
          [(3,0),(3,1),(3,2),(4,0),(4,1),(4,2),(5,0),(5,1),(5,2)],
          [(3,3),(3,4),(3,5),(4,3),(4,4),(4,5),(5,3),(5,4),(5,5)],
          [(3,6),(3,7),(3,8),(4,6),(4,7),(4,8),(5,6),(5,7),(5,8)],
          [(6,0),(6,1),(6,2),(7,0),(7,1),(7,2),(8,0),(8,1),(8,2)],
          [(6,3),(6,4),(6,5),(7,3),(7,4),(7,5),(8,3),(8,4),(8,5)],
          [(6,6),(6,7),(6,8),(7,6),(7,7),(7,8),(8,6),(8,7),(8,8)]
           ]

UNIDADES = LINHAS + COLUNAS + CAIXAS

arestas = []

# iterar nas posições em cada unidade criando as arestas
# acesse o objeto Node de uma posição (i,j) usando -> vertices[(i,j)]