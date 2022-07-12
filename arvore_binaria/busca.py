from arvore import *

def contem(raiz:Node, elemento) -> bool:

    if raiz == VAZIA:
        return False

    if raiz.conteudo == elemento:  # ACHOOU
        return True

    if elemento <= raiz.conteudo:
        return contem(raiz.esq, elemento)

    if elemento > raiz.conteudo:
        return contem(raiz.dir, elemento)



arvore_tupla1 = ("macarrao", 
                    ("feijao", ("arroz",), ("jujuba",)), 
                    ("patê", ("ovos",), ("salsicha",))
                )

arvore_teste = constroi_arvore_predefinida(arvore_tupla1)

#Testes:
assert not contem(VAZIA, "macarrao")
assert contem(arvore_teste, "macarrao")  #raiz
assert contem(arvore_teste, "feijao")
assert contem(arvore_teste, "ovos")
assert contem(arvore_teste, "salsicha")
assert not contem(arvore_teste, "peixe")



arvore_teste2 = VAZIA

arvore_teste2 = adicionar_na_arvore(arvore_teste2, 50)
arvore_teste2 = adicionar_na_arvore(arvore_teste2, 25)
arvore_teste2 = adicionar_na_arvore(arvore_teste2, 75)
arvore_teste2 = adicionar_na_arvore(arvore_teste2, 10)
arvore_teste2 = adicionar_na_arvore(arvore_teste2, 35)
arvore_teste2 = adicionar_na_arvore(arvore_teste2, 30)
arvore_teste2 = adicionar_na_arvore(arvore_teste2, 60)
arvore_teste2 = adicionar_na_arvore(arvore_teste2, 90)

def print_in_ordem(raiz:Node):

    if raiz.esq != VAZIA:
        print_in_ordem(raiz.esq)

    print(raiz.conteudo)  #visita

    if raiz.dir != VAZIA:
        print_in_ordem(raiz.dir)


print_in_ordem(arvore_teste2)


def print_pre_ordem(raiz:Node):

    print(raiz.conteudo)  #visita

    if raiz.esq != VAZIA:
        print_pre_ordem(raiz.esq)

    if raiz.dir != VAZIA:
        print_pre_ordem(raiz.dir)

print()
print_pre_ordem(arvore_teste2)

def print_pos_ordem(raiz:Node):

    if raiz.esq != VAZIA:
        print_pos_ordem(raiz.esq)

    if raiz.dir != VAZIA:
        print_pos_ordem(raiz.dir)

    print(raiz.conteudo)  #visita

print()
print_pos_ordem(arvore_teste2)



def multiplica_por_dois(raiz:Node) -> Node:

    if raiz.esq != VAZIA:
        raiz.esq = multiplica_por_dois(raiz.esq)

    raiz.conteudo *= 2  #visita

    if raiz.dir != VAZIA:
        raiz.dir = multiplica_por_dois(raiz.dir)

    return raiz

print()
print_in_ordem(multiplica_por_dois(arvore_teste2))


def print_arvore_indentado(raiz:Node, nivel=0):

    #imprimir indentação
    print("\t"*nivel, end="")

    #imprimir conteudo
    print("("+str(raiz.conteudo))  #visita

    if raiz.esq != VAZIA:
        print_arvore_indentado(raiz.esq, nivel+1)

    if raiz.dir != VAZIA:
        print_arvore_indentado(raiz.dir, nivel+1)

    #imprimir indentação
    print("\t"*nivel, end="")
    print(")")


print_arvore_indentado(arvore_teste2)