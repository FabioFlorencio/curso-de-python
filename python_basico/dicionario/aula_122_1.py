'''
    aula 122 - Shallow Copy vs Deep Copy em dados mutáveis Python

    copy - retorna uma cópia rasa (shallow copy)
    Em uma cópia rasa(shaloww copy), tudo que for imutável vai ser copiado para outro dicionário
'''

d1 = {
    'c1':1,
    'c2':2,
    'l1':  [0,1,2]
}

# Em uma cópia rasa(shaloww copy), tudo que for imutável vai ser copiado para outro dicionário
# cria uma cópia de d1
d2 = d1.copy()

print(id(d2))

d2['c1'] = 1000
d2['l1'][1] = 99999

print(d1)
print(d2)