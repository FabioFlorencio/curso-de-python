'''
    Aula 89 - enumerate para enumerar valores de iteráveis (pegar índices)
    enumerate utiliza o método iterator
    enumerate -> cria indice para lista

'''

lista = ['Fábio', 'Francisca', 'Vitória']
lista.append('José')


for indice, nome in enumerate(lista):
    print(indice, nome)
    print(type(indice))

for indice, nome in range(lista):    
    print(indice, nome)

for tupla_enumerada in enumerate(lista):
    for valor in tupla_enumerada:
        print(valor)
        