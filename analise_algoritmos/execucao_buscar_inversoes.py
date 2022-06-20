
#!/usr/bin/python
# source: https://dev.to/chroline/visualizing-algorithm-runtimes-in-python-f92
from setup import *


# Busca quantidade de inversões
def conta_inversoes(lista):
    n = len(lista)
    cont = 0
    for i in range(0, n-1):
        for j in range(i+1, n):
            if lista[i] > lista[j]:
                cont += 1
    return cont



ns = np.linspace(10, 1000, 100, dtype=int)
ts = [timeit.timeit('conta_inversoes(lst)', 
                    setup='lst=list(range({}))'.format(n),
                    globals=globals(),
                    number=100)
      for n in ns]

plt.plot(ns, ts, 'or')

degree = 4
coeffs = np.polyfit(ns, ts, degree)
p = np.poly1d(coeffs)
plt.plot(ns, [p(n) for n in ns], '-b')

plt.show()