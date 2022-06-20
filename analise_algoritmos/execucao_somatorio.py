#!/usr/bin/python
# source: https://dev.to/chroline/visualizing-algorithm-runtimes-in-python-f92
from setup import *


ns = np.linspace(10, 10_000, 100, dtype=int)
ts = [timeit.timeit('sum(range({}))'.format(n), number=100)
      for n in ns]

degree = 4
coeffs = np.polyfit(ns, ts, degree)
p = np.poly1d(coeffs)
plt.plot(ns, ts,'or')
plt.plot(ns, [p(n)for n in ns],'-b')

plt.show()