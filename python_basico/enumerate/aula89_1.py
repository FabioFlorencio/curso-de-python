'''
    Aula 89 - enumerate para enumerar valores de iteráveis (pegar índices)
    enumerate utiliza o método iterator
    enumerate -> cria indice para lista
    Enumerate retorna uma tupla "Desempacota a lista"

'''

lista = ['Fábio', 'Francisca', 'Vitória']
lista.append('José')

# criando um interator por vez

for item in enumerate(lista):
    print(item)

# transforma em list
print(list(enumerate(lista)))

for item in enumerate(lista):
    print(item)    
 