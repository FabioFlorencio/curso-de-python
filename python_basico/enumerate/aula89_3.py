'''
    Aula 89 - enumerate para enumerar valores de iteráveis (pegar índices)
    enumerate utiliza o método iterator
    enumerate -> cria indice para lista

'''

lista = ['Fábio', 'Francisca', 'Vitória']
lista.append('José')


for item in lista:
    print(item)

nova_lista = tuple(lista)    

for item in nova_lista:
    print(item)

# Enumerate retorna uma tupla    
for item in enumerate(lista):
    print(type(lista))
    print(type(item))
    indice, nome = item
    print(indice, nome)
    print(type(item),end="\n\n")

# item[2] = 'teste'

#lista.append("jones")

