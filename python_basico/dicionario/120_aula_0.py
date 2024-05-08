'''
    Manipulando chaves e valores em dicionários em Python

'''

pessoa = {
    'nome': 'Fábio',
    'sobrenome': 'Florêncio',
    'idade': 18,
    'altura': 1.75,
    'endereços': [
        {'rua': 'tal tal', 'número': 123},
        {'rua': 'outra rua', 'número': 321}
    ]
}

# Exemplo de incluir uma nova chave no dicionário
pessoa['Observação'] = ''

print(pessoa)
print()

# Modificando a rua do primeiro endereço
pessoa['endereços'][0]['rua'] = 'TI'
pessoa['endereços'][0]['número'] = 222


pessoa['endereços'][1]['número'] = 333

print(pessoa)
