'''
    Aula 89 - enumerate para enumerar valores de iteráveis (pegar índices)
    enumerate utiliza o método iterator
    Nesse exemplo não funciona o for devido que o método interator já foi usado

'''

lista = ['Fábio', 'Francisca', 'Vitória']
lista.append('José')

# criando um interator por vez

for item in enumerate(lista):
    print(item)

print()    

for item in enumerate(lista):
    print(item)    
 