'''
    (Parte 1) Métodos úteis nos dicionários Python (dict)
    # métodos úteis dos dicionários em python
    # len - quantas chaves
    # keys - iterável com as chaves
    # values - iterável com os valores
    # items - iterável com chaves e valores
    # setdefault - adiciona valor se a chave não existe
    # copy - retorna uma cópia rasa (Shallow copy)
    # get - obtém uma chave
    # pop - Apaga um item com a chave especifica (del)
    # popitem - Apaga o último item adicionado
    # update - Atualiza um dicionário com outro

'''

pessoa = {
    'nome': 'Fábio',
    'sobrenome': 'Miranda',
    'idade': 18,
    'altura': 1.75
}

# len para dicionário

print(f'Quantas chaves tem no dicionário:{pessoa.__len__()}')

# outra forma

print(f'Quantas chaves tem no dicionário:{len(pessoa)}')