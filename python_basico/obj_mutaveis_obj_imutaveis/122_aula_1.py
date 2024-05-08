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

print('Sem alterção no dicionário d1:',id(d1))
print('Sem alterção no dicionário d2:',id(d2))

d1['c1'] = 1000
d2['l1'][1] = 99999

print('Dados mutáveis, mesmo sendo alterado, permanece no mesmo local de memória: ',id(d1))
print('Dados mutáveis, mesmo sendo alterado, permanece no mesmo local de memória: ',id(d2))
print()

x = 5 

print(f'Dado imutável: não muda local de memória!, {x=}\n Local de memória: {id(x)}')

# a ponta para memória
a = x
# novo objeto
x = 10

print(f'Dado imutável: Quando você atribui um valor, ele gera um novo objeto, mantendo o valor anterior: {x=}\n Local de memória:{id(x)}')

print(f'Eu falei que não aceito atribuição no mesmo local de memória! Não divído local de memória com ninguém! {a=} \n Local de memória: {id(a)}')

