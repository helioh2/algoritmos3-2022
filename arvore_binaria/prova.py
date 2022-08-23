



def altura(raiz):

    if raiz is None:
        return 0

    altura_esq = altura(raiz.esq)
    altura_dir = altura(raiz.dir)
    return 1 + max(altura_esq, altura_dir)



def eh_balanceada(raiz):

    diferenca_altura = altura(raiz.esq) - altura(raiz.dir)
    if diferenca_altura > 1 or diferenca_altura < -1:
        return False

    if not eh_balanceada(raiz.esq):
        return False

    if not eh_balanceada(raiz.dir):
        return False

    return True



def calcula_hash(chave, m):
    return chave % m


def insere(chave, tabela):
    indice = calcula_hash(chave, tabela.m)
    tabela.vetor[indice].append(chave)

    return tabela
