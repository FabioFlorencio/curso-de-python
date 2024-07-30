'''
    Aula 133 -  Introdução à função lambda + list.sort e sorted
    Nesse exemplo foi utilizado sorted

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
def exibir(lista):
    for item in lista:
        print(item)
    print()    

# sorted gera uma cópia rasa, caso seja necessário utilize deepcopy
l1 = sorted(lista_1, key=lambda item: item['nome'])
l2 = sorted(lista_2, key=lambda item: item['sobrenome'])

for item in lista_1:
    print(item)


exibir(l1)
exibir(l2)
