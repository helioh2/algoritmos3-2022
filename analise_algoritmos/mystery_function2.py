
#!/usr/bin/python
# source: https://dev.to/chroline/visualizing-algorithm-runtimes-in-python-f92
from setup import *

def g(l): # l is a python list of integers of length n
  pairs = [ (i,j) for i in range(len(l)) for j in range(len(l)) if i < j ]
  result = []
  for (i,j) in pairs:
    if l[i] == l[j]:
      result.append((i,j))
  return result

ns = range(5, 200)
ts = [timeit.timeit('g(lst)',
                    setup='lst=list(range({}))'.format(n),
                    globals=globals(),
                    number=1)
         for n in ns]
plt.plot(ns, ts, 'or')

degree = 4
coeffs = np.polyfit(ns, ts, degree)
p = np.poly1d(coeffs)
plt.plot(ns, [p(n) for n in ns], '-b')

plt.show()