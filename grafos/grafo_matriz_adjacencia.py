##### experimentando ######

vertices = ["A", "B", "C"]
N = len(vertices)
arestas = [("A","B",10), ("A","C",20), ("C","A",20), ("C", "B",15)]

grafo = [[None for _ in range(N)] for _ in range(N)]  # matriz de adjacencia
print(grafo)

for aresta in arestas:
    vertice1 = aresta[0]
    vertice2 = aresta[1]
    linha = vertices.index(vertice1)
    coluna = vertices.index(vertice2)

    grafo[linha][coluna] = 1


print(grafo)

########## criando uma classe #############

class GrafoMatrizAdjacencia:

    def __init__(self, matriz=None, vertices=None, arestas=None):
        if matriz:
            self.matriz = matriz
            if vertices:
                self.vertices = vertices
            else:
                self.vertices = list(range(len(matriz)))
        
        else:
            self.vertices = vertices
            self.matriz = [
                            [0 for _ in range(len(self.vertices))] 
                                for _ in range(len(self.vertices))
                        ]

            print(self.matriz)

            for aresta in arestas:
                vertice1 = aresta[0]
                vertice2 = aresta[1]
                peso = aresta[2]
                linha = vertices.index(vertice1)
                coluna = vertices.index(vertice2)

                self.matriz[linha][coluna] = peso
                self.matriz[coluna][linha] = peso

    def get_vizinhanca(self, vertice):
        if vertice in self.vertices:
            index_vertice = self.vertices.index(vertice)
            for i in range(len(self.matriz)):
                yield (self.vertices[i], self.matriz[index_vertice][i]) 

    def existe_aresta(self, vertice1, vertice2):
        return self.matriz[vertice1][vertice2]


    def prims_mst(self):

        visitados = [False for v in range(len(self.vertices))]

        print(visitados)

        # Matriz representando a árvore resultante
        result = [[0 for coluna in range(len(self.vertices))] 
                    for linha in range(len(self.vertices))]
        
        indx = 0

        # Enquanto existem nós não visitados:
        while(False in visitados):

            minimo = float('inf')  # +infinito

            # Índice do nó inicial
            inicial = 0

            # Índice do nó final
            final = 0

            # Itera sobre cada vértice que já foi visitado (ver linha 99):
            for i in range(len(self.vertices)): # for (i=0; i < len(self.vertices); i++)
                if visitados[i]:
                    # Itera sobre cada vértice para capturar os vizinhos:
                    for j in range(len(self.vertices)):
                        # Se existe uma aresta entre o nó i e o nó j AND j já não foi visitado (para evitar ciclos)
                        if (not visitados[j] and self.matriz[i][j] > 0):  
                            # Se o peso da aresta é menor que o mínimo
                            if self.matriz[i][j] < minimo:
                                # Define o novo mínimo, o vértice inicial e o vértice final
                                minimo = self.matriz[i][j]
                                inicial, final = i, j
            
            # Adicionando vértice final aos visitados
            visitados[final] = True

            # Filling the MST Adjacency Matrix fields:
            result[inicial][final] = minimo
            
            if minimo == float('inf'):
                result[inicial][final] = 0

            print("(%d.) %d - %d: %d" % (indx, inicial, final, result[inicial][final]))
            indx += 1
            
            result[final][inicial] = result[inicial][final]

        # Imprimir a árvore
        for i in range(len(result)):
            for j in range(0+i, len(result)):
                if result[i][j] != 0:
                    print("%d - %d: %d" % (i, j, result[i][j]))

        return result

    def __str__(self):
        string = "\t"
        for vertice in self.vertices:
            string += str(vertice) + "\t"
        string += "\n"
        i = 0
        for linha in self.matriz:
            string += str(self.vertices[i]) + "\t"
            i += 1
            for coluna in linha:
                string += str(coluna) + "\t"
            string += "\n"
        return string
        

    def print_to_dot_file(self):
        file_ = open("grafo.dot", "w")
        file_.write("graph{\n")
        for i in range(len(self.vertices)):
            for j in range(i, len(self.vertices)):
                if self.matriz[i][j] > 0:
                    vertice1 = self.vertices[i]
                    vertice2 = self.vertices[j]
                    peso = self.matriz[i][j]
                    file_.write(f'{vertice1} -- {vertice2}[label="{peso}",weight="{peso}"];\n')
        file_.write("}")
        file_.close()

vertices = ["A", "B", "C"]
N = len(vertices)
arestas = [("A","B",10), ("A","C",20), ("C", "B",15)]

grafo2 = GrafoMatrizAdjacencia(vertices=vertices, arestas=arestas)
print(grafo2)
print (grafo2.prims_mst())

# arvore = GrafoMatrizAdjacencia(grafo2.prims_mst())
# print(arvore)
# arvore.print_to_dot_file()


vertices = list(range(0,9))
arestas = [(0,1,4), (0,6,7), (1,2,9), (1,6,11), (1,7,20), (2,3,6), (2,4,2),
            (3,5,5), (3,4,10), (4,7,1), (4,8,5), (4,5,15), (6,7,1),
             (7,8,3), (8,5,12)]

grafo_grande = GrafoMatrizAdjacencia(vertices=vertices, arestas=arestas)
print(grafo_grande.prims_mst())
