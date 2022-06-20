
#!/usr/bin/python
# source: https://dev.to/chroline/visualizing-algorithm-runtimes-in-python-f92
from setup import *


# Busca binária em lista ordenada
def busca_binaria(lista, valor):
    inicio = 0
    fim = len(lista)-1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if valor < lista[meio]:
            fim = meio - 1
        elif valor > lista[meio]:
            inicio = meio + 1
        else:
            return True
    else:
        return False

ns = np.linspace(10, 10000, 100, dtype=int)
ts = [timeit.timeit('busca_binaria(lista, 0)', 
                    setup='lista=list(range({}))'.format(n),
                    globals=globals(),
                    number=1000)
      for n in ns]

plt.plot(ns, ts, 'or')

degree = 4
coeffs = np.polyfit(ns, ts, degree)
p = np.poly1d(coeffs)
plt.plot(ns, [p(n) for n in ns], '-b')

plt.show()