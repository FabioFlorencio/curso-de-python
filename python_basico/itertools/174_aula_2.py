"""
    Aula 174 - Combinations, Permutations e Product - Itertools
    Combinations, Permutations e Product - Itertools
    Combinação - Faz combinação - iterável + tamanho do grupo
    Permutação - Ordem importa
    Produto - Ordem importa e repete valores únicos

    Combinatiosn precisa de dois parâmetros
"""

from itertools import combinations,product

camisetas = [
    ['preta','branca'],
    ['p','m','g'],
    ['masculino', 'feminino'],
    ['algodão','poliéster']
]


print(*list(product(*camisetas)),sep='\n')
