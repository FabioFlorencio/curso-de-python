'''
    Manipulando chaves e valores em dicionários em Python

'''

# dicionário  vazio
pessoa = {}

# exemplo de incluir uma chave dinâmica
chave = 'nome'

pessoa[chave] = 'Fábio'
pessoa['sobrenome'] = 'Florêncio'

print(pessoa[chave])
print(pessoa)

# apagar uma chave
del pessoa['sobrenome']

print(pessoa)