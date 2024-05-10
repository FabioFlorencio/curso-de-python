'''
    Aula 139 - List comprehension com mais de um for

'''

lista = []

for l in range(3):
    for c in range(3):
        lista.append((l,c))

print(lista)  

# gera uma matriz usando comprehension
lista1 = [
    [x,y]
    for x in range(2)
    for y in range(2)   
]


print(*lista1, sep='\n')