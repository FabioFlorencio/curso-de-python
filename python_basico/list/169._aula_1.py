'''
    Aula 169 - O comando zip em Python é usado para agregar dois ou mais iteráveis (listas, tuplas, etc.) 
    Crie uma função zipper 
    Exercício - Unir listas
    O trabalho dessa função será unir duas
    lista na ordem.
    Use todos os valores da menor lista.
    ['Salvador', 'Ubatuba', 'Belo Horizonte']
    ['BA', 'SP', 'MG', 'RJ']
    Resultado
    [('Salvador', 'BA'),('Ubatuba','SP'), ('Belo Horizonte', 'MG')]

'''

from itertools import zip_longest

# zip_longest usa como referência a lista que tem maior conteúdo

l1 = ['Salvador','Ubatuba', 'Belo Horizonte']    
l2 = ['BA', 'SP', 'MG', 'RJ']

print(list(zip(l1,l2)))
print()
print('Lista com none:',list(zip_longest(l1,l2)),sep='\n')
print('Lista com none:',list(zip_longest(l1,l2, fillvalue= 'SEM CIDADE')))
