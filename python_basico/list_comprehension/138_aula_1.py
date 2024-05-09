'''

    Aula 138 - Filtro de dados em list comprehension (filter)

'''

produtos = [
    {'nome' : 'p1', 'preco': 20,},
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30,},
]

print(produtos)
print()

lista = [n for n in range(10) if n < 5]

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}     
    for produto in produtos
    if produto['preco'] * 1.05 > 10 
]

print(*novos_produtos, sep='\n')            