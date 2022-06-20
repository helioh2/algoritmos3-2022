#!/usr/bin/python
# source: https://dev.to/chroline/visualizing-algorithm-runtimes-in-python-f92
from setup import *


lst = list(range(1_000_000))
ns = np.linspace(0, len(lst), 1000, endpoint=False, dtype=int)
ts = [timeit.timeit('_ = lst[{}]'.format(n),
                    globals=globals(),
                    number=10000)
        for n in ns]

plt.plot(ns, ts,'or')

degree = 4
coeffs = np.polyfit(ns, ts, degree)
p = np.poly1d(coeffs)
plt.plot(ns, [p(n)for n in ns],'-b')


plt.show()