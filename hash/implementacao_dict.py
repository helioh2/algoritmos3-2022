
from hash_encadeamento import TabelaHash, inserir, busca


class ParChaveValor:

    def __init__(self, chave, valor):
        self.chave = chave
        self.valor = valor

    def __hash__(self) -> int:
        return hash(self.chave)

    def __eq__(self, outro: object) -> bool:
        return self.chave == outro.chave


class MyDict:

    def __init__(self):
        self.tabela = TabelaHash()

    def put(self, chave, valor):
        par = ParChaveValor(chave, valor)
        inserir(par, self.tabela)

    def get(self, chave):
        par = ParChaveValor(chave, None)
        par_encontrado = busca(par, self.tabela)
        return None if not par_encontrado else par_encontrado.valor

    def __str__(self) -> str:
        string = ""
        for par in self.tabela:
            string += str(par.chave) + "\t-->\t" + str(par.valor) + "\n"
        return string

    def __getitem__(self, chave):
        return self.get(chave)

    def __setitem__(self, chave, valor):
        self.put(chave, valor)


dict1 = MyDict()
dict1.put("Paraná", "Curitiba")
dict1.put("Santa Catarina", "Florianópolis")
dict1.put("Goiás", "Goiania")

dict1["Espírito Santo"] = "Vitória"

print(dict1)

print(dict1.get("Paraná"))
print(dict1["Espírito Santo"])