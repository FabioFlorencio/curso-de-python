'''
    aula 122 - Shallow Copy vs Deep Copy em dados mutáveis Python

    copy - retorna uma cópia rasa (shallow copy)
    Em uma cópia rasa(shaloww copy), tudo que for imutável vai ser copiado para outro dicionário
'''

# c1 = chave 1
# l1 = lista 1
# d1 = dicionário 1

import copy

d1 = {
    'c1':1,
    'c2':2,
    'l1':  [0,1,2]
}

# Em uma cópia rasa(shallow copy), tudo que for imutável vai ser copiado para outro dicionário
# cria uma cópia de d1 usando a biblioteca copy 
#d2 = copy.copy(d1)

# usando o método deepcopy
d2 = copy.deepcopy(d1)

print(id(d1))
print(id(d2))


# observe que deepycopy vai permitir alterar somente a lista de d2 

d2['c1'] = 1000
d2['l1'][1] = 99999

print(d1)
print(d2)