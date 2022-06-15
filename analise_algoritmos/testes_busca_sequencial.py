
from busca_sequencial import *

#Exemplos:
# print( busca_sequencial([4,8,15,16,23,42], 16) ) #-> 3
# print( busca_sequencial([4,8,15,16,23,42], 42) ) #-> 5
# print( busca_sequencial([], 16) ) # -> -1
# print( busca_sequencial([4,8,15,16,23,42], 18) ) # -> -1

assert busca_sequencial([4,8,15,16,23,42], 16) == 3

# Valor não existente na lista
assert busca_sequencial([4,8,15,16,23,42], 18) == -1

# Lista vazia
assert busca_sequencial([], 16) == -1

# Valores limítrofes:
assert busca_sequencial([4,8,15,16,23,42], 4) == 0
assert busca_sequencial([4,8,15,16,23,42], 42) == 5
print("PARABENS!! TODOS OS TESTES PASSARAM.")