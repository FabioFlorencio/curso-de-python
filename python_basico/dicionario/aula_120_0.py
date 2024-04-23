'''
    Manipulando chaves e valores em dicionários em Python

'''

pessoa = {
    'nome': 'Fábio',
    'sobrenome': 'Florêncio',
    'idade': 18,
    'altura': 1.75,
    'endereços': [
        {'rua': 'tal tal','número': 123},
        {'rua': 'outra rua', 'número': 321}
    ]
}

# exemplo de incluir uma nova chave no dicionário
pessoa['Observação'] = ''

print(pessoa)