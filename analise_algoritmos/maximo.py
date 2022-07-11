

def maximo(vetor: list[float]) -> float:
    
    n = len(vetor)  # tamanho do vetor
    valor_maximo = None  # null

    for i in range(0, n): # até n, mas não inclui n
        if valor_maximo is None or vetor[i] > valor_maximo:
            valor_maximo = vetor[i]

    return valor_maximo


assert maximo([12,6,899,10,999,2]) == 999
assert maximo([]) is None




def fat_rec(n):
    if n <= 1: 
        return 1
    else: 
        return n * fat_rec(n-1)


def fat_it(n):
    result = 1
    for i in range(2, n+1):
        result = result * i
    return result

print(fat(5))