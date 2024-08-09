"""
    Aula 174 - Combinations, Permutations e Product - Itertools
    Combinations, Permutations e Product - Itertools
    Combinação - Faz combinação - iterável + tamanho do grupo
    Permutação - Ordem importa
    Produto - Ordem importa e repete valores únicos

    Combinatiosn precisa de dois parâmetros
"""

from itertools import combinations

pessoas = ['João','Joana','Luiz','Leticia']

print(combinations(pessoas,2))
print(list(combinations(pessoas, 2)))


lista = [x for x in combinations(pessoas,3)]

print('\n',*lista,sep='\n')

