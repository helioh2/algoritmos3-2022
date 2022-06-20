#!/usr/bin/python
# source: https://dev.to/chroline/visualizing-algorithm-runtimes-in-python-f92
from setup import *


# y = log x
# vertically stretched 1000x
ns = range(1, 100)
ts = [math.log(n, 2) * 1000 for n in ns]
degree = 4
coeffs = np.polyfit(ns, ts, degree)
p = np.poly1d(coeffs)
plt.plot(ns, ts,'or')
plt.plot(ns, [p(n)for n in ns],'-b');

# y = x^2
ns = range(1, 100)
ts = [(n*n) for n in ns]
degree = 4
coeffs = np.polyfit(ns, ts, degree)
p = np.poly1d(coeffs)
plt.plot(ns, ts,'or')
plt.plot(ns, [p(n)for n in ns],'-b')


# y = 2^x
# vertically stretched 20x
# horizontally compressed 1x
ns = range(1, 10)
ts = [math.pow(2, n)*20 for n in ns]
degree = 4
coeffs = np.polyfit(ns, ts, degree)
p = np.poly1d(coeffs)
plt.plot(ns, ts,'or')
plt.plot(ns, [p(n)for n in ns],'-b')


# y = x
# vertically stretched 20x
# horizontally compressed 1x
ns = range(1, 10)
ts = [n*20 for n in ns]
degree = 4
coeffs = np.polyfit(ns, ts, degree)
p = np.poly1d(coeffs)
plt.plot(ns, ts,'or')
plt.plot(ns, [p(n)for n in ns],'-b')

plt.show()