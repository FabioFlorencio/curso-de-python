'''
    Aula 133 -  Introdução à função lambda + list.sort e sorted
    

'''

lista_1 = [    
    {'nome': 'Daniel', 'sobrenome':'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
    {'nome': 'Alex', 'sobrenome': 'Souza'}
]
lista_2 = [    
    {'nome': 'Jones', 'sobrenome':'Silva'},
    {'nome': 'Lucas', 'sobrenome': 'Moreira'},
    {'nome': 'Ramon', 'sobrenome': 'Souza'},
    {'nome': 'Alex', 'sobrenome': 'Souza'}
]
def ordena(item):

    # Ordena pelo nome    
    return item['nome']


lista_1.sort(key=ordena)

for item in lista_1:
    print(item)

print()

lista_2.sort(key=lambda item: item['nome'])

for item in lista_2:
    print(item)


