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
    'sobrenome': 'Mendonça 1',
    'sobrenome': 'Mendonça 2',
    'sobrenome': 'Mendonça 3',
    
}

# Caso repita as chaves vai imprir somente a última chave

print(pessoa)