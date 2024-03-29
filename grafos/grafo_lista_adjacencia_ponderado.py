
from queue import PriorityQueue


class GrafoPonderado:

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
                    vertice1 = aresta[0]
                    vertice2 = aresta[1]
                    peso = aresta[2]
                    self.grafo[hash(vertice1)].add((vertice2, peso))
                    self.grafo[hash(vertice2)].add((vertice1, peso))

        self.empty_value = empty_value


    def get_vizinhanca(self, vertice):
        if vertice in self.vertices:
            return self.grafo[hash(vertice)]
        return None

    def existe_aresta(self, vertice1, vertice2):
        if vertice1 in self.vertices and vertice2 in self.vertices:
            return vertice2 in [v for v, _ in self.grafo[hash(vertice1)]]
        return False

    

    def dikjstra(self, v0):
        """
        Encontrar as menores distâncias entre o vertice v0 e todos os outros vértices do grafo
        """

        visitados = set()

        fila = PriorityQueue()
        fila.put((0, v0))

        distancia = {v: float('inf') for v in self.vertices}
        distancia[v0] = 0

        pai = {v: None for v in self.vertices}

        while not fila.empty():

            peso_atual, v_atual = fila.get()

            visitados.add(v_atual)

            for vizinho, peso in self.get_vizinhanca(v_atual):

                if vizinho not in visitados:
                    
                    custo_novo = peso_atual + peso
                    custo_antigo = distancia[vizinho]

                    if custo_novo < custo_antigo:
                        distancia[vizinho] = custo_novo
                        pai[vizinho] = v_atual
                        fila.put((custo_novo, vizinho))

        return distancia, pai

    def prims_mst(self):

        visitados = set()

        # Árvore resultante
        result = {v:set() for v in self.vertices}
        
        visitados.add(self.vertices[0])

        # Enquanto existem nós não visitados:
        while len(visitados) < len(self.vertices):

            minimo = float('inf')  # +infinito
            inicial = self.vertices[0]
            final = self.vertices[0]

            # Itera sobre cada vértice que já foi visitado
            for v_atual in visitados:
                for vizinho, peso in self.get_vizinhanca(v_atual):
                    if vizinho not in visitados and peso < minimo:
                        # Define o novo mínimo, o vértice inicial e o vértice final
                        minimo = peso
                        inicial, final = v_atual, vizinho
            
            # Adicionando vértice final aos visitados
            visitados.add(final)         
            
            if minimo != float('inf'):
                result[inicial].add((final, minimo))
                result[final].add((inicial, minimo))

        return result



    def __str__(self) -> str:
        string = ""
        for vertice in self.vertices:
            string += str(vertice) + ": ["
            if not self.grafo[hash(vertice)]:
                string += "]\n"
                continue
            for adjacente, peso in self.grafo[hash(vertice)]:
                string += "(" + str(adjacente) + "," + str(peso) +"), "
            string = string[:-2] + "]\n"
        return string 



#EXEMPLO:
vertices = ["A", "B", "C"]
N = len(vertices)
arestas = [("A","B",10), ("A","C",20), ("C","A",20), ("C", "B", 15)]

grafo1 = GrafoPonderado(vertices=vertices, arestas=arestas)
print(grafo1)
print(grafo1.dikjstra("A"))


## Grafo da página: https://stackabuse.com/courses/graphs-in-python-theory-and-implementation/lessons/dijkstras-algorithm/
vertices = list(range(0,9))
arestas = [(0,1,4), (0,6,7), (1,2,9), (1,6,11), (1,7,20), (2,3,6), (2,4,2),
            (3,5,5), (3,4,10), (4,7,1), (4,8,5), (4,5,15), (6,7,1),
             (7,8,3), (8,5,12)]

grafo_grande = GrafoPonderado(vertices=vertices, arestas=arestas)

print(grafo_grande.dikjstra(0))  # verificar porque achou caminho 22 para o 5


print(grafo_grande.prims_mst())