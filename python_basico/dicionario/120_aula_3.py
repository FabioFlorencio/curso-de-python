'''
    Aula 120 - Manipulando chaves e valores em dicionários em Python
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
print('Por padrão retorna None caso não seja passado um parâmetro:',pessoa.get('sobrenome'))
print(pessoa.get('sobrenome', 'Não existe'))