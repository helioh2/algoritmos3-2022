
def busca_sequencial(lista: list, valor: int) -> int:
    """
    Faz a busca pelo valor numa lista, retornando a posição do valor na lista
    ou -1 se não estiver na lista.
    
    List, Int -> Int[-1,n-1], onde n é o tamanho da lista
    """
    n = len(lista)   # tamanho da lista
    for i in range(0, n):  # iteração sobre os índices: 0, 1, 2,..., n-1
        if lista[i] == valor:
            return i
    # else
    return -1
    

#Exemplos:
print( busca_sequencial([4,8,15,16,23,42], 16) )
print( busca_sequencial([], 16) )
print( busca_sequencial([4,8,15,16,23,42], 18) )



def dobro(x):
    return 2*x

print(dobro(2))

def par_ou_impar(x):
    if x % 2 == 0:
        print("blabla")
        return "par"
    else:
        return "impar"













































