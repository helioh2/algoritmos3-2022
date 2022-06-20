
#!/usr/bin/python
# source: https://dev.to/chroline/visualizing-algorithm-runtimes-in-python-f92
from setup import *

def f(l:list, val): # l is a python list with n items
  d = {}
  for i in range(len(l)):
    d[l[i]] = i
  return d[val]

ns = range(5, 2000)
ts = [timeit.timeit('f(lst, {})'.format(n-1),
                    setup='lst=list(range({})); random.shuffle(lst)'.format(n),
                    globals=globals(),
                    number=1)
         for n in ns]
plt.plot(ns, ts, 'or');

degree = 4
coeffs = np.polyfit(ns, ts, degree)
p = np.poly1d(coeffs)
plt.plot(ns, [p(n) for n in ns], '-b')

plt.show()