'''
    Aula 89 - enumerate para enumerar valores de iteráveis (pegar índices)
    enumerate utiliza o método iterator
    enumerate -> cria indice para lista
    Enumerate retorna uma tupla "Desempacota a lista"

'''

lista = ['Fábio', 'Francisca', 'Vitória']
lista.append('José')

# o start permite mudar o índice do enumerate
lista_enumerada = list(enumerate(lista, start=10))
print(lista_enumerada)

print(len(lista_enumerada))

print(enumerate(lista_enumerada, start=2))