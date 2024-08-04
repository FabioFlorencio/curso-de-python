'''
    Aula 94 - Listas dentro de listas(iteráveis dentro de iteráveis)

    lista de listas e seus índices
    
'''

salas = [    
    ['Maria', 'Helena',],
    ['Elaine'],
    ['Luiz', 'João', 'Eduarda']
]

print(salas[0][1])
print(salas[2][2])
print()

salas[0][1] = 'tosco'

print(salas)

salas[0].insert(1,'Tosco')

print(salas)
