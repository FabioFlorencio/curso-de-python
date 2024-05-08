'''
    Aula 121 - (Parte 1) Métodos úteis nos dicionários Python (dict)
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
    
}

# Retorna somente as chaves do dicionário
print('Retorna somente as chaves do dicionário:',pessoa.keys())
print('Retorna somente os valores do dicionário',pessoa.values())
print('Retorna somente os itens do dicionário',pessoa.items())

# transforma list usando o métod items()
teste = list(pessoa.items())

print(type(teste))
print('Transforma em list, mas os seus elementos são tuplas: ',teste)


print(teste)
print('Pula linha')


for chave in pessoa.keys():
    print(f'Chave:',chave)

print()

for valor in pessoa.values():
    print(f'Valor:',valor)
   
    

    