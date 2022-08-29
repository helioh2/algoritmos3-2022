
##### experimentando ##############

#Ex grafo com lista de adjacencia usando dicionario
from queue import Queue


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

    def __init__(self, dict_=None, vertices=None, arestas=None, empty_value=0):

        self.grafo = dict()

        if dict_: #constroi objeto com base em lista de adjacencias pronta na forma de dict
            self.vertices = dict_.keys()
            for vertice, adjacentes in dict_.items():
                self.grafo[hash(vertice)] = set(adjacentes)

        else:
            
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


    def print_busca_profundidade_iterativa(self, v0):

        pilha = [v0]
        visitados = []

        while pilha:   # enquanto a pilha não é vazia
            atual = pilha.pop(-1)   # removendo o último elemento da lista (pilha) e retornando
            
            if atual not in visitados:

                visitados.append(atual)

                print(atual)  ## ou qualquer outra ação

                vizinhos = sorted([vizinho for vizinho in self.get_vizinhanca(atual) if vizinho not in visitados])

                pilha = pilha + list(reversed(vizinhos))  # coloca todos os vizinhos não visitados no topo


    def print_busca_largura_iterativa(self, v0):

        fila = Queue()
        fila.put(v0)

        visitados = []

        while not fila.empty():
            atual = fila.get()

            if atual not in visitados:
                visitados.append(atual)

                print(atual)  ## ou qualquer outra ação

                vizinhos = [vizinho for vizinho in self.get_vizinhanca(atual) if vizinho not in visitados]

                for vizinho in vizinhos:
                    fila.put(vizinho)


    def vertices_sem_entrada(self):
        res = []
        for v in self.vertices:
            for v2 in self.vertices:
                if v == v2:
                    continue
                if v in self.grafo[hash(v2)]:  # se vertice v está na lista de adjacencia do v2
                    break   # então o vertice tem entrada
            else:  # se não dar break
                res.append(v)   # adiciona como resultado (vertice sem entrada)
        return res


    def ordenacao_topologica(self):

        sequencia = []
        visitados=[]

        def ordenacao_topologica_rec(self, v_atual, visitados=[]):
            
            visitados.append(v_atual)

            ## faz nada

            vizinhos = self.get_vizinhanca(v_atual)

            for vizinho in vizinhos:
                if vizinho not in visitados:
                    ordenacao_topologica_rec(self, vizinho, visitados)
            
            ## insere na sequencia
            sequencia.append(v_atual)


        for vertice in self.vertices_sem_entrada():
            if not vertice in visitados:
                ordenacao_topologica_rec(self, vertice, visitados)

        return list(reversed(sequencia))
            


    def __str__(self) -> str:
        string = ""
        for vertice in self.vertices:
            string += str(vertice) + ": ["
            if not self.grafo[hash(vertice)]:
                string += "]\n"
                continue
            for adjacente in self.grafo[hash(vertice)]:
                string += str(adjacente) + ", "
            string = string[:-2] + "]\n"
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

grafo1 = GrafoListaAdjacencia(vertices=vertices, arestas=arestas, empty_value="")

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



class Numero:   # wrapper

    def __init__(self, n):
        self.n = n

    def __str__(self) -> str:
        return str(self.n)

    


numero0 = Numero(0)
numero1 = Numero(1)
numero2 = Numero(2)
numero3 = Numero(3)

grafo_numeros_mutaveis = GrafoListaAdjacencia(vertices=[numero1, numero2, numero3],
                    arestas=[(numero1, numero2), (numero1, numero3), (numero3,numero1), (numero3, numero2)])

print(grafo_numeros_mutaveis)
print()
aplica_dobro_busca_profundidade(grafo_numeros_mutaveis, numero1)

print(grafo_numeros_mutaveis)
print()
# grafo_numeros_mutaveis.print_busca_profundidade_iterativa(numero1)


print()
grafo1.print_busca_profundidade_iterativa("A")
print()
grafo1.print_busca_largura_iterativa("A")
print()
grafo_aciclico = GrafoListaAdjacencia(
    dict_= {
        7: [11,8],
        5: [11],
        3: [8, 10],
        11: [2, 9, 10],
        8: [9],
        2: [],
        9: [],
        10: []
    }
)

grafo_aciclico.print_busca_profundidade_iterativa(7)
print()
grafo_aciclico.print_busca_largura_iterativa(7)

# print(grafo_aciclico)

print(list(grafo_aciclico.ordenacao_topologica()))