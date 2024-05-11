'''

    Aula 137 - Mapeamento de dados em list comprehension (map)

'''

produtos = [
    {'nome' : 'p1', 'preco': 20,},
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30,},
]

print(produtos)
print()

# produtos está sendo usado para gerar um novo dicionário
novos_produtos = [
    {'nome': produto['nome'], 'preco': produto['preco']}       
    for produto in produtos
]

print(*novos_produtos, sep='\n')            