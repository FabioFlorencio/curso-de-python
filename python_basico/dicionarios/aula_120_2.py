'''
    Manipulando chaves e valores em dicionários em Python

'''

# dicionário  vazio
pessoa = {}

# exemplo de incluir uma chave dinâmica
chave = 'nome'

pessoa[chave] = 'Fábio'
pessoa['sobrenome'] = 'Florêncio'

print(pessoa)

# apagar uma chave
del pessoa['sobrenome']

# verifica se tem o dados 'sobrenome' caso não tenha retorna None
# print(pessoa.get('sobrenome'))

if pessoa.get('sobrenome') is None:
    print('Não exite')
else:
    print(pessoa['sobrenome'])    

print(pessoa)