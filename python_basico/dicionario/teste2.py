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

# Mudando a chave 'rua' para 'logradouro' no primeiro endereço
endereco = pessoa['endereços'][0]
endereco['logradouro'] = endereco.pop('rua')

print(pessoa)
print()

pessoa['endereços'][0]['logradouro'] = 'TI'

print(pessoa)
