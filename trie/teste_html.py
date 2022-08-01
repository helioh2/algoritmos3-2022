import time
import urllib.request

from trie import Node, adicionar, busca_string

fp = urllib.request.urlopen("https://pt.wikipedia.org/wiki/Jandaia_do_Sul")
mybytes = fp.read()

mystr = mybytes.decode("utf8")
fp.close()

print(mystr)

palavras = mystr.split()

trie = Node()

for palavra in palavras:
    adicionar(trie, palavra)



t_inicial = time.time()
print(busca_string(trie, "desenhistaliul"))
t_final = time.time()

print("tempo de busca com trie:", t_final-t_inicial )

def ignorar_caracteres_especiais(palavra):
    nova_palavra = ""
    for char in palavra:
        if ord(char) - 65 < 0 or ord(char) - 65 > 25:
            continue
        nova_palavra += char
    return nova_palavra 


def pesquisar_sequencial(palavra_a_pesquisar):
    for p in palavras:
        palavra_escaped = ignorar_caracteres_especiais(p).upper()
        if palavra_escaped == palavra_a_pesquisar:
            return True
    return False



t_inicial = time.time()
print(pesquisar_sequencial("desenhistaliul"))
t_final = time.time()

print("tempo de busca sem trie:", t_final-t_inicial )
