'''
    171 - Exercícios | somando duas listas
    Usa a função zip do módulo itertools para combinar elementos de duas listas e parar na lista com menos elementos.

    zip só une as listas até o tamanho da menor lista, por padrâo.

'''




lista_a = [1,2,3,4,5,6,7]
lista_b = [1,2,3,4]
lista_soma = []

lista_soma = [ x + y for x,y in zip(lista_a, lista_b)]

print(lista_soma)