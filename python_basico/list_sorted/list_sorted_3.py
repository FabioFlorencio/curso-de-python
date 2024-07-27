"""
    Estudo avulso sobre list sorted
    As listas em Python possuem um método embutido list.sort() que modifica a lista em si. Há também a 
    função embutida sorted() que constrói uma nova lista ordenada à partir de um iterável.

    Exemplo usando a função chave

    fonte:https://docs.python.org/pt-br/dev/howto/sorting.html 

"""

# Lista de strings
palavras = ["banana", "abacate", "laranja", "melancia", "uva"]

# Ordena a lista pelo tamanho das palavras
palavras_ordenadas_por_tamanho = sorted(palavras, key=len)

print(palavras_ordenadas_por_tamanho)

