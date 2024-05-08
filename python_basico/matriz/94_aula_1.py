'''
    Aula 94 - Listas dentro de listas(iteráveis dentro de iteráveis)

    lista de listas e seus índices

'''

salas = [    
    ['Maria', 'Helena'],
    ['Elaine'],
    ['Luiz', 'João', 'Eduarda',(0,10,20,30,40)]
]

print(salas[0][1])
print(salas[2][2])
print(salas[2][3][2])

# não vai funcionar devido que a coluna 3 não permiti atribuir valor em uma tupla por ser imutável.
# salas[2][3][1] = 50

salas[2][3] = list(salas[2][3])

print(salas)
