'''
    Aula 139 - List comprehension com mais de um for

'''

lista = []

for l in range(3):
    for c in range(3):
        lista.append((l,c))

print(lista)  

# gera uma matriz usando comprehension
teste1 = [
    [x for y in range(3)] 
    for x in range(3)  
]


print(*teste1, sep='\n')