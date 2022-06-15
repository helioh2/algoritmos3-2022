
def busca_sequencial(lista: list, valor: int) -> int:
    """
    Faz a busca pelo valor numa lista ordenada, retornando a posição do valor na lista
    ou -1 se não estiver na lista.
    
    List, Int -> Int[-1,n-1], onde n é o tamanho da lista
    """
    n = len(lista)       
    for i in range(0, n):  
        if lista[i] == valor: 
            return i   
    return -1
    

def dobro(x):
    return 2*x

print(dobro(2))

assert dobro(2) == 4
assert dobro(-2) == -4
assert dobro(0) == 0
assert dobro(2.5) == 5.0
assert dobro("scss") == "scssscss"


def par_ou_impar(x: int) -> str:
    if x % 2 == 0:
        print("blabla")
        return "par"
    else:
        return "impar"


assert par_ou_impar(2) == "par"
assert par_ou_impar(3) == "impar"
assert par_ou_impar(0) == "par"












































