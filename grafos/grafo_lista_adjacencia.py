
##### experimentando ##############

#Ex grafo com lista de adjacencia usando dicionario
grafo = {
    1: {2,3},
    2: set(),
    3: {1,2}
}


## Usando dicionario
grafo = {
    "A": {"B","C"},
    "B": set(),
    "C": {"A","B"}
}

print("B" in grafo["A"])



### Usando lista de vertices e de arestas
grafo1_vertices = ["A","B","C"]   # 0, 1, 2
grafo1_arestas = [["B","C"], [], ["A","B"]]

# quero saber se existe vértice entre 1 e 2
index_do_A = grafo1_vertices.index("A")  # -> 0
print("B" in grafo1_arestas[index_do_A])



######### criando uma classe ##############

class GrafoListaAdjacencia:

    def __init__(self, vertices, arestas):
        self.grafo = dict()
        
        for aresta in arestas:
            vertice1 = aresta[0]
            vertice2 = aresta[1]
            if vertice1 in self.grafo.keys():
                self.grafo[vertice1].add(vertice2)
            else:
                self.grafo[vertice1] = set([vertice2])

            
vertices = ["A", "B", "C"]
N = len(vertices)
arestas = [("A","B"), ("A","C"), ("C","A"), ("C", "B")]

grafo1 = GrafoListaAdjacencia(vertices, arestas)

print(grafo1.grafo)