

class TabelaHash:

    def __init__(self, m=17):
        self.m = m
        self.n = 0
        self.vetor = [[] for _ in range(m)]

    def __str__(self):
        string = ""
        for i in range(len(self.vetor)):
            string += str(i) + "\t--->\t" + str(self.vetor[i]) + "\n"
        return string


# operações

def nosso_hash(chave, m) -> int:
    return hash(chave) % m


def inserir(chave, tabela:TabelaHash) -> TabelaHash:
    indice = nosso_hash(chave, tabela.m)
    tabela.vetor[indice].append(chave)
    return tabela


#exemplos
tabela1 = TabelaHash(m=31)
inserir(0, tabela1) 
inserir(31, tabela1) 
inserir(32, tabela1) 
inserir(100, tabela1) 
print(tabela1)

