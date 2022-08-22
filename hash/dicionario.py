

"""
chave   ->   valor
0       ->    12
1       ->    30
2       ->    56
3       ->    23
"""
x = [12,30,56,23]
x[2]   # 56


## MAPA ASSOCIATIVA (HASH MAP) OU DICIONÁRIO

"""
   chave     ->  valor
"9090909090" ->  objeto Pessoa("Joao", "9090909090", "joao@uol.com")
"1898989890" ->  objeto Pessoa("Maria", "1898989890", "maria@uol.com")
"""

from Pessoa import Pessoa


pessoas = {}
pessoas = dict()

pessoas["9090909090"] = Pessoa("Joao", "9090909090", "joao@uol.com")
pessoas["1898989890"] = Pessoa("Maria", "1898989890", "maria@uol.com")
pessoas["5665566565"] = Pessoa("Jose", "1212121212", "jose@uol.com")

from pprint import pprint
pprint(pessoas)


## ACESSO:
print(pessoas["5665566565"])   # O(1) --> constantes


###
capitais = {}
capitais["Paraná"] = "Curitiba"
capitais["Santa Catarina"] = "Florianopolis"

print(capitais)

print(capitais["Paraná"])


### SET (CONJUNTO)

conjunto1 = set()

conjunto1.add("arroz")
conjunto1.add("feijao")
conjunto1.add("macarrao")
conjunto1.add("arroz")

print(conjunto1)


print("arroz" in conjunto1)
print("carne" not in conjunto1)

conjunto2 = {"macarrao", "carne"}
conjunto3 = conjunto1.union(conjunto2)
conjunto4 = conjunto1.intersection(conjunto2)
print(conjunto3)
print(conjunto4)

