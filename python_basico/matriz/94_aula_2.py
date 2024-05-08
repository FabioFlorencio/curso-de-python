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
print(salas[1][0])
print(salas[2][1])

print()

for sala in salas:
    print(f'A sala é {sala}') 
    # sala se torna o control do for contando a qtd de itens de cada linha   
    for aluno in sala:
        print(aluno)

print()

for sala in salas:
    print(f'A sala é {sala}')
    for sala in salas:
        print(sala)
    print()    
