import time
import random
from bubble_sort import *


#Teste de desempenho do Bubble sort para lista fora de ordem

lista_aleatoria = list(range(10000))
random.shuffle(lista_aleatoria)

tempo_inicial = time.time()

bubble_sort(lista_aleatoria)

tempo_final = time.time()

print("Tempo de execucao", tempo_final - tempo_inicial)


