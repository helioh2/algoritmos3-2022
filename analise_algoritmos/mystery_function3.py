
#!/usr/bin/python
# source: https://dev.to/chroline/visualizing-algorithm-runtimes-in-python-f92
from setup import *

def h(n):
   if n <= 1:
       return n
   else:
       return h(n-1) + h(n-2)

ns = range(5, 30)
ts = [timeit.timeit('h({})'.format(n),
                    globals=globals(),
                    number=1)
         for n in ns]
plt.plot(ns, ts, 'or')

plt.show()