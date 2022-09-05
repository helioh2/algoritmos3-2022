from ast import operator
from copy import deepcopy
import math
import sys
# sys.setrecursionlimit(5000)

B = None

"""Exemplos de dados"""
tiles_resolvido = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, B)
)

tiles_embaralhado = (
    (5, 3, 2),
    (7, B, 4),
    (6, 1, 8)
)

tiles_solvable = (
    (1, 8, 2),
    (B, 4, 3),
    (7, 6, 5)
)

tiles_not_solvable = (
    (8, 1, 2),
    (B, 4, 3),
    (7, 6, 5)
)

tiles_easy = (
    (1, B, 3),
    (4, 2, 5),
    (7, 8, 6)
)

def is_resolvido(tiles):
    return hash(tiles) == hash(tiles_resolvido)


def procura_posicao_b(tiles):
    for i in range(3):
        for j in range(3):
            if tiles[i][j] is None:
                return (i, j)


def dentro(i, j):
    return 0 <= i < 3 and 0 <= j < 3


def novo_tiles_mudando_posicoes(tiles, posicao_b, nova_posicao_b):

    novo_tiles = ()
    i_nb, j_nb = nova_posicao_b
    valor_nova_posicao_b = tiles[i_nb][j_nb]
    for i in range(3):
        nova_linha = ()
        for j in range(3):
            if (i, j) == posicao_b:
                nova_linha += (valor_nova_posicao_b,)
            elif (i, j) == nova_posicao_b:
                nova_linha += (B,)
            else:
                nova_linha += (tiles[i][j],)
        novo_tiles += (nova_linha,)

    return novo_tiles




def proximos_apos_movimento(tiles):
    movimentos = [(-1,0), (1,0), (0,1), (0,-1)] #cima, baixo, direita, esquerda
    posicao_b = procura_posicao_b(tiles)

    for movimento in movimentos:
        nova_posicao_b = tuple(p1 + p2 for p1, p2 in zip(posicao_b, movimento))

        if not dentro(*nova_posicao_b):
            continue
        #else

        novo_tiles = novo_tiles_mudando_posicoes(tiles, posicao_b, nova_posicao_b)
        yield novo_tiles



def resolver(tiles, visitados=set(), cont=0):
    if is_resolvido(tiles):
        return tiles

    visitados.add(tiles)

    if len(visitados) >= math.factorial(9):
        return None

    print("qtd visitados:", len(visitados))
    print("chamadas:", cont)

    for proximo in proximos_apos_movimento(tiles):
        if proximo not in visitados:
            possivel_solucao = resolver(proximo, visitados, cont+1)
            if possivel_solucao:
                return possivel_solucao
    
    return None
    

assert resolver(tiles_solvable) == tiles_resolvido

print("terminado")
