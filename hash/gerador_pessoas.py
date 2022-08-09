import names
from hash_encadeamento import Pessoa, TabelaHash, inserir
import uuid

N = 10000
tabela = TabelaHash()

for i in range(N):
    id = uuid.uuid4()
    nome = names.get_full_name()
    email = nome.split()[0] + "@gmail.com"

    pessoa = Pessoa(id, nome, email)
    inserir(pessoa, tabela)


print(tabela)
print(tabela.n/tabela.m)

# x = []
# for i in range(tabela.m):
#     x.append(len(tabela.vetor[i]))

tamanhos_buckets = [len(tabela.vetor[i]) for i in range(tabela.m)]
print(max(tamanhos_buckets))


import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

x = np.array(range(tabela.m))
y = np.array(tamanhos_buckets)

plt.title("Line graph")
plt.bar(x, y, color="red")

plt.show()