

from hash_encadeamento import TabelaHash, inserir, busca

class MySet:

    def __init__(self):
        self.tabela = TabelaHash()

    def add(self, item):
        inserir(item, self.tabela)

    def contains(self, item):
        return busca(item, self.tabela) is not None

    def __str__(self):
        string = "["
        for item in self.tabela:
            string += str(item) + ", "
        string = string[:-2]
        string += "]"

        return string

    def __iter__(self):
        return self.tabela.__iter__()


set1 = MySet()
set1.add("arroz")
set1.add("arroz")
set1.add("feijao")
set1.add("macarrao")

print(set1)

print(set1.contains("feijao"))
print(set1.contains("carne"))


for item in set1:
    print(item)