import random
import time

def merge_sort(lista):
    if len(lista) > 1:
        meio = len(lista) // 2
        esquerda = lista[:meio]
        direita = lista[meio:]

        # Chamada recursiva em cada metade
        merge_sort(esquerda)
        merge_sort(direita)

        # Dois contadores para atravessar as duas metades
        i = 0
        j = 0
        
        # Iterador para a lista principal
        k = 0
        
        while i < len(esquerda) and j < len(direita):
            if esquerda[i] <= direita[j]:
              # O valor da esquerda foi usado
              lista[k] = esquerda[i]
              i += 1
            else:
                lista[k] = direita[j]
                j += 1
            # Vai para a próxima posição
            k += 1

        # Para todos os valores restantes:
        while i < len(esquerda):
            lista[k] = esquerda[i]
            i += 1
            k += 1

        while j < len(direita):
            lista[k] = direita[j]
            j += 1
            k += 1

# lista = [54,26,93,17,77,31,44,55,20]
# merge_sort(lista)
# print(lista)


