'''
    Aula 89 - enumerate para enumerar valores de iteráveis (pegar índices)
    enumerate utiliza o método iterator
    enumerate -> cria indice para lista
    Enumerate retorna uma tupla "Desempacota a lista"

'''

lista = ['Fábio', 'Francisca', 'Vitória']
lista.append('José')


for item in lista:
    print(item)

nova_tupla = tuple(lista)    

for item in nova_tupla:
    print(item)

# Enumerate retorna uma tupla    
for item in enumerate(lista):    
    print(type(item))
    # item repassa o indice e o valor para (indice e nome)
    indice, nome = item
    print(indice, nome)
    print(type(item),end="\n\n")

# item[2] = 'teste'

#lista.append("jones")

