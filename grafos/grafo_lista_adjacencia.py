
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

    def __init__(self, vertices=None, arestas=None, empty_value=0):

        self.grafo = dict()
        self.vertices = vertices if vertices else []

        for vertice in vertices:
            self.grafo[hash(vertice)] = set()
        
        if arestas:
            for aresta in arestas:
                vertice1 = hash(aresta[0])
                vertice2 = aresta[1]
                self.grafo[vertice1].add(vertice2)

        self.empty_value = empty_value
    
    def get_vizinhanca(self, vertice):
        if vertice in self.vertices:
            return self.grafo[hash(vertice)]
        return None

    def existe_aresta(self, vertice1, vertice2):
        if vertice1 in self.vertices and vertice2 in self.vertices:
            return vertice2 in self.grafo[hash(vertice1)]
        return False

    def print_busca_profundidade_rec(self, v_atual, visitados):

        visitados.append(v_atual)

        print(v_atual)   # ação que estou fazendo no nó

        vizinhos = self.get_vizinhanca(v_atual)

        for vizinho in vizinhos:
            if vizinho not in visitados:
                self.print_busca_profundidade_rec(vizinho, visitados)
        
    def print_busca_profundidade(self, v0):

        self.print_busca_profundidade_rec(v0, visitados=[])

    def __str__(self) -> str:
        string = ""
        for vertice in self.vertices:
            string += str(vertice) + ": "
            for adjacente in self.grafo[hash(vertice)]:
                string += str(adjacente) + ", "
            string = string[:-2] + "\n"
        return string 



"""
def template_busca_profundidade_rec(self, v_atual, visitados):

    visitados.append(v_atual)

    # ação que estou fazendo no nó

    vizinhos = self.get_vizinhanca(v_atual)

    for vizinho in vizinhos:
        if vizinho not in visitados:
            self.print_busca_profundidade_rec(vizinho, visitados)
            ## ação a fazer com o vizinho
            
    
def print_busca_profundidade(self, v0):

    self.print_busca_profundidade_rec(v0, visitados=[])
"""


vertices = ["A", "B", "C"]
N = len(vertices)
arestas = [("A","B"), ("A","C"), ("C","A"), ("C", "B")]

grafo1 = GrafoListaAdjacencia(vertices, arestas, empty_value="")

print(grafo1.grafo)
print(grafo1.get_vizinhanca("E"))
print(grafo1.get_vizinhanca("C"))
print(grafo1.get_vizinhanca("B"))

assert grafo1.existe_aresta("A", "B")
assert not grafo1.existe_aresta("B", "C")

grafo1.print_busca_profundidade("A")
print()
grafo1.print_busca_profundidade("B")
print()
grafo1.print_busca_profundidade("C")


def aplica_dobro_busca_profundidade(grafo, v0):

    def aplica_dobro_busca_profundidade_rec(grafo, v_atual, visitados):

        visitados.append(v_atual)

        v_atual.n = v_atual.n*2

        vizinhos = grafo.get_vizinhanca(v_atual)

        for vizinho in vizinhos:
            if vizinho not in visitados:
                aplica_dobro_busca_profundidade_rec(grafo, vizinho, visitados)

    aplica_dobro_busca_profundidade_rec(grafo, v0, visitados=[])





class Numero:

    def __init__(self, n):
        self.n = n

    def __str__(self) -> str:
        return str(self.n)

    def __radd__(self, outro):
        if type(outro) == int:
            return Numero(self.n + outro)
        return Numero(self.n + outro.n)

numero0 = Numero(0)
numero1 = Numero(1)
numero2 = Numero(2)
numero3 = Numero(3)

grafo_numeros_mutaveis = GrafoListaAdjacencia([numero1, numero2, numero3],
                    [(numero1, numero2), (numero1, numero3), (numero3,numero1), (numero3, numero2)])

print(grafo_numeros_mutaveis)

aplica_dobro_busca_profundidade(grafo_numeros_mutaveis, numero1)

print(grafo_numeros_mutaveis)

grafo_numeros_mutaveis.print_busca_profundidade(numero1)
