

from typing import Set


class Trie:

    def __init__(self, chave:str=None, filhos:Set=None):
        self.chave = chave
        if not filhos:
            self.filhos = set()
        else:
            self.filhos = filhos

    def __str__(self) -> str:

        def to_str_rec(trie, nivel):
            chave_str = trie.chave if trie.chave else "*"
            string = nivel*"\t" + chave_str + "\n"
            for filho in trie.filhos:
                string +=  to_str_rec(filho, nivel+1)
            return string
        
        return to_str_rec(self, nivel=0)

       
def inserir_string(raiz:Trie, string:str) -> Trie:

    if not string:
        return raiz

    for filho in raiz.filhos:
        if filho.chave == string[0]:
            filho = inserir_string(filho, string[1:])
            return filho

    #else
    novo_filho = Trie(string[0])
    raiz.filhos.add(novo_filho)
    novo_filho = inserir_string(novo_filho, string[1:])
    
    return raiz


        
def busca_string(raiz:Trie, string:str) -> bool:
    
    if not string:
        return True

    if not raiz.chave or string[0] == raiz.chave:

        substring = string[1:] if raiz.chave else string

        if not raiz.filhos and len(string) == 1: # nó folha e último caractere == encontrou string 
            return True

        for filho in raiz.filhos:
            achou_filho = busca_string(filho, substring)
            if achou_filho:
                return achou_filho
        #else
        return False

    #else
    return False


trie = Trie()  #trie vazio
inserir_string(trie, "o")
inserir_string(trie, "rato")
inserir_string(trie, "roeu")
inserir_string(trie, "a")
inserir_string(trie, "roupa")
inserir_string(trie, "do")
inserir_string(trie, "rei")
inserir_string(trie, "de")
inserir_string(trie, "roma")

print(trie)

assert busca_string(trie, "rato")
assert not busca_string(trie, "ratol")
assert busca_string(trie, "")
assert busca_string(trie, "o")
