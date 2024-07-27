"""
    Estudo avulso sobre list sorted
    As listas em Python possuem um método embutido list.sort() que modifica a lista em si. Há também a 
    função embutida sorted() que constrói uma nova lista ordenada à partir de um iterável.

    Outra diferença é que o método list.sort() é aplicável apenas às listas. Em contrapartida, a 
    função sorted() aceita qualquer iterável.    

    fonte:https://docs.python.org/pt-br/dev/howto/sorting.html 

"""




numeros = [3, 1, 4, 1, 5, 9, 2, 6, 5]

print('id - 1 ',id(numeros))
numeros.sort()

print('id - 2 ',id(numeros))

# Ordena a lista em ordem crescente
numeros_crescente = sorted(numeros)

# Ordena a lista em ordem decrescente
numeros_ordenados_decrescente = sorted(numeros, reverse=True)

print('Lista crescente',numeros_crescente)
print('Lista decrescente',numeros_ordenados_decrescente)
print(sorted(numeros))
print()

print(numeros)