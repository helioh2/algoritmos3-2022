import random
import matplotlib.pyplot as plt
import numpy as np

from hash_encadeamento import TabelaHash, inserir

# An "interface" to matplotlib.axes.Axes.hist() method

def random_hash_table(m, n):
    tabela = TabelaHash(m=m)
    for i in range(n):
        inserir(random.randrange(1000000), tabela)
    
    return tabela
    

tabela = random_hash_table(m=13, n=10000000)
dados = [len(tabela.vetor[i]) for i in range(len(tabela.vetor))]

plt.hist(dados, bins=len(tabela.vetor))
plt.show() 