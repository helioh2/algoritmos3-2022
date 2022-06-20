import time
import random
from merge_sort import *


#Teste de desempenho do Bubble sort para lista fora de ordem

lista1 = list(range(10000))
#random.shuffle(lista_aleatoria)

tempo_inicial = time.time()

merge_sort(lista1)

tempo_final = time.time()

print("Tempo de execucao", tempo_final - tempo_inicial)


