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

# seria uma forma desempacotar um dicionário existente em novo dicionário
# nesse exemplo mostra como alterar o preço
# caso não compreenda esse exemplo veja o arquivo anterior
novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    for produto in produtos
]

print(*novos_produtos, sep='\n')            