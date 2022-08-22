class Pessoa:

    def __init__(self, id, nome, email):
        self.id = id
        self.nome = nome
        self.email = email

    
    def __hash__(self) -> int:
        return hash(self.id)

    def __str__(self) -> str:
        return str(self.__dict__)


class TabelaHash:

    def __init__(self, m=17):
        self.m = m
        self.n = 0
        self.vetor = [[] for _ in range(m)]

    def __str__(self):
        string = ""
        for i in range(self.m):
            string += str(i) + "\t--->\t" 
            for item in self.vetor[i]:
                string += str(item) + ", "
            string += "\n"

        return string

    def table_iter(self):
        for bucket in self.vetor:
            for item in bucket:
                yield item

    def __iter__(self):
        return self.table_iter()


# operações

def nosso_hash(chave, m) -> int:
    return hash(chave) % m


def redimensionar(tabela: TabelaHash):
    tabela.m *= 2   ## TODO: pegar o numero primo mais proximo de m*2
    vetor_antigo = tabela.vetor  # ponteiro para o vetor antigo
    
    # resetando a tabela, com um novo m
    tabela.vetor = [[] for _ in range(tabela.m)]  #substituindo o vetor antigo pelo novo vetor vazio
    tabela.n = 0

    for bucket in vetor_antigo:
        for item in bucket:
            inserir(item, tabela)

    return tabela


def inserir(chave, tabela:TabelaHash) -> TabelaHash:
    indice = nosso_hash(chave, tabela.m)

    for item in tabela.vetor[indice]:
        if item == chave:
            return tabela

    #else
    tabela.vetor[indice].append(chave) ##inserir a chave
    tabela.n += 1

    # calculo do fator de carga
    fator_carga = tabela.n / tabela.m

    if fator_carga > tabela.fator_carga_maximo:
        tabela = redimensionar(tabela)

    return tabela


def busca(chave: object, tabela:TabelaHash) -> object:
    indice = nosso_hash(chave, tabela.m)

    for item in tabela.vetor[indice]:
        if item == chave:
            return item

    #else
    return None


def remover(chave: object, tabela:TabelaHash) -> object:
    indice = nosso_hash(chave, tabela.m)

    for i in range(len(tabela.vetor[indice])):
        item = tabela.vetor[indice][i]
        if item == chave:
            tabela.vetor[indice].pop(i)
            tabela.n -= 1
            return chave
    
    #else
    return None


#exemplos
tabela1 = TabelaHash(m=7)
# inserir(0, tabela1) 
# inserir(31, tabela1) 
# inserir(32, tabela1) 
# inserir(32, tabela1) 
# inserir(100, tabela1) 

pessoa1 = Pessoa(1, "Fulano", "fulano@bol.com.br")
pessoa2 = Pessoa(2, "Beltrano", "beltrano@gmail.com")
pessoa3 = Pessoa(33, "Jose", "jose@gmail.com")
pessoa4 = Pessoa(34, "Maria", "maria@gmail.com")

inserir(pessoa1, tabela1)
inserir(pessoa2, tabela1)
inserir(pessoa3, tabela1)
print(tabela1)
inserir(pessoa4, tabela1)

print(tabela1)
print(tabela1.n)


# print(busca(31, tabela1))
# print(busca(50, tabela1))


# remover(31, tabela1)

# print(tabela1)
# print(tabela1.n)

for item in tabela1:
    print(item)


def gen_cont(k):
    contador = 0
    for _ in range(k):
        contador += 1
        yield contador



cont = gen_cont(3)
print(next(cont))
print(next(cont))
print(next(cont))


# for x in gen_cont(5):
#     print(x)





