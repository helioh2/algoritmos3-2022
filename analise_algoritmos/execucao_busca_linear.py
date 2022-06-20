#!/usr/bin/python
# source: https://dev.to/chroline/visualizing-algorithm-runtimes-in-python-f92
from setup import *

## Função testada:
def busca_sequencial(lista, valor):
    n = len(lista)   # tamanho da lista
    for i in range(0, n):  # iteração sobre os índices: 0, 1, 2,..., n-1
        if lista[i] == valor:
            return i
    return -1


## Execução aleatória dos pontos vermelhos (quando valor está em lista)

ns = np.linspace(10, 10000, 100, dtype=int)

# red plots
ts = [timeit.timeit('busca_sequencial(lst, 0)', 
                    setup='lst=list(range({})); random.shuffle(lst)'.format(n),
                    globals=globals(),
                    number=100)
      for n in ns]
plt.plot(ns, ts, 'or')

# Plotagem dos pontos azuis
degree = 4
coeffs = np.polyfit(ns, ts, degree)
p = np.poly1d(coeffs)
plt.plot(ns, [p(n) for n in ns], '-r')



## Execução aleatória dos pontos azuis (quando valor está em lista)
# ts = [timeit.timeit('busca_sequencial(lst, -1)', 
#                     setup='lst=list(range({}))'.format(n),
#                     globals=globals(),
#                     number=100)
#       for n in ns]
# plt.plot(ns, ts, 'ob')

# # Plotagem dos pontos azuis
# degree = 4
# coeffs = np.polyfit(ns, ts, degree)
# p = np.poly1d(coeffs)
# plt.plot(ns, [p(n) for n in ns], '-b')

plt.show()