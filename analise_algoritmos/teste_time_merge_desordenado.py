from merge_sort import merge_sort
import random, time

#definir entrada:
lista = list(range(10000)) ## lista com valores de 0 a 9999 (ex: [0,1,2,3,...9999])
random.shuffle(lista)

# gravar o tempo inicial (antes do algoritmo executar)
tempo_inicial = time.time()

# executar o algoritmo
merge_sort(lista)

# gravar o tempo final (depois do algoritmo executar)
tempo_final = time.time()

# calcular o tempo total
tempo_total = tempo_final - tempo_inicial
print(tempo_total)