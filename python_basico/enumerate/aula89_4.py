'''
    Aula 89 - enumerate para enumerar valores de iteráveis (pegar índices)
    enumerate utiliza o método iterator
    enumerate -> cria indice para lista
    Enumerate retorna uma tupla "Desempacota a lista"
    
'''

lista = ['Fábio', 'Francisca', 'Vitória']
lista.append('José')


for indice, nome in enumerate(lista):
    print(indice, nome)
    print(type(indice))

print()    

# retorna uma tupla
for indice, nome in enumerate(lista):    
    print(indice, nome)

print()    

for tupla_enumerada in enumerate(lista):
    print(tupla_enumerada)
    for valor in tupla_enumerada:
        print(valor)

print()

for tupla_enumerada in enumerate(lista):
    print(tupla_enumerada)   

print()

for i,nome in enumerate(lista):
    print(lista[i])

        