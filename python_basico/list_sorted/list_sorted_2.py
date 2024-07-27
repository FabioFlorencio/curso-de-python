"""
    Estudo avulso sobre list sorted
    As listas em Python possuem um método embutido list.sort() que modifica a lista em si. Há também a 
    função embutida sorted() que constrói uma nova lista ordenada à partir de um iterável.

    Exemplo usando a função chave

    fonte:https://docs.python.org/pt-br/dev/howto/sorting.html 

"""


# Lista de tuplas (nome, idade)
pessoas = [("Ana", 28), ("Bruno", 35), ("Carla", 22), ("Diego", 30)]

# Ordena a lista pelo segundo elemento da tupla (idade)
pessoas_ordenadas_por_idade = sorted(pessoas, key=lambda pessoa: pessoa[1])

# ordena a lista de forma invertida
pessoas_ordenadas_invertida = sorted(pessoas, reverse=True, key=lambda pessoa: pessoa)

# ordena a lista de forma invertida usando o parâmetro idade
pessoas_ordenadas_reversa= sorted(pessoas, reverse=True, key=lambda pessoa: pessoa[1])

print(pessoas_ordenadas_por_idade)
print(pessoas_ordenadas_invertida)
print(pessoas_ordenadas_reversa)


