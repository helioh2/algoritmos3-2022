from ssl import ALERT_DESCRIPTION_UNKNOWN_PSK_IDENTITY


def fat_rec(n):
    if n <= 1:
        return 1
    else:
        return n*fat_rec(n-1)


fat_rec(5)

funcao = lambda x: x*2

print(funcao(5))

def funcao2(fun, x):
    res = fun(x)
    res += 2
    return res

import math
print(funcao2(math.factorial, 5))