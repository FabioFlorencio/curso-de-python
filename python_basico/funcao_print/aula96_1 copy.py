'''
    Aula 96 - Desempacotamento em chamadas de funções

'''

letras = 'ABCD'
lista = ['Maria','Helena', 1, 2, 3,'Eduarda','fim da lista']
tupla = 'Python', 'è', 'legal'
salas = [
    ['Maria', 'Helena'],
    ['Elaine'],
    ['Luiz','João','Eduarda']
]


# desempacotamento em chamadas

print(*lista)
print(*tupla)
print(*salas)
print('Mosta a lista conforme está distribuidos os itens.')
print(*salas, sep='\n')






