import random
import time

def bubble_sort(lista):
    elementos = len(lista)-1
    ordenado = False
    while not ordenado:
        ordenado = True
        for i in range(elementos):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1],lista[i]
                ordenado = False     
    return lista

# print(bubble_sort([15,3,8,9]))

# ## TESTE DE DESEMPENHO:

# # definir entrada:
# lista = list(range(1000)) ## lista com valores de 0 a 99999 (ex: [0,1,2,3,...99999])
# random.shuffle(lista)

# # gravar o tempo inicial (antes do algoritmo executar)
# tempo_inicial = time.time()

# # executar o algoritmo
# result = bubble_sort(lista)

# # gravar o tempo final (depois do algoritmo executar)
# tempo_final = time.time()

# # calcular o tempo total
# tempo_total = tempo_final - tempo_inicial
# print(tempo_total)