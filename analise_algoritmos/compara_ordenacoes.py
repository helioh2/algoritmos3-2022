
import random
import time
from bubble_sort import bubble_sort
from merge_sort import merge_sort


# TESTE DE DESEMPENHO (COMPARAÇÃO ENTRE bubble e merge sort):

# definir entrada:
lista = list(range(1000)) ## lista com valores de 0 a 99999 (ex: [0,1,2,3,...99999])
random.shuffle(lista)

#---------------------------
# MEDIDA DE TEMPO PARA O BUBBLE SORT

# gravar o tempo inicial (antes do algoritmo executar)
tempo_inicial_bubble = time.time()

# executar o algoritmo
result = bubble_sort(lista)

# gravar o tempo final (depois do algoritmo executar)
tempo_final_bubble = time.time()

# calcular o tempo total
tempo_total_bubble= tempo_final_bubble - tempo_inicial_bubble
# print(tempo_total)

# ----------------------------
# MEDIDA DE TEMPO PARA O MERGE SORT

# gravar o tempo inicial (antes do algoritmo executar)
tempo_inicial_merge = time.time()

# executar o algoritmo
merge_sort(lista)

# gravar o tempo final (depois do algoritmo executar)
tempo_final_merge = time.time()

# calcular o tempo total
tempo_total_merge= tempo_final_merge - tempo_inicial_merge
# print(tempo_total)

### RESULTADO DA COMPARAÇÃO
print("Tempo total bubble:", tempo_total_bubble)
print("Tempo total merge:", tempo_total_merge)
print("Quantas vezes merge é mais rapido que bubble:", 
        tempo_total_bubble / tempo_total_merge)