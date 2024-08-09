"""
    Aula 174 - Combinations, Permutations e Product - Itertools
    Combinations, Permutations e Product - Itertools
    Combinação - Faz combinação - iterável + tamanho do grupo
    Permutação - Ordem importa
    Produto - Ordem importa e repete valores únicos

    Combinatiosn precisa de dois parâmetros
"""

from itertools import combinations,permutations

pessoas = ['João','Joana','Luiz','Leticia']

lista_1 = [comb for comb in combinations(pessoas,2)]
lista_2 = [comb for comb in permutations(pessoas,2)]

print('Combinations: faz combinações a partir do índice')
print(*lista_1,sep='\n')
print('Permutations: faz todas as combinações possíveis dentro a lista sem repetir o conteúdo')
print()
print(*lista_2,sep='\n')