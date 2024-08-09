'''
    171 - Exercícios | somando duas listas
    Usa a função zip do módulo itertools para combinar elementos de duas listas e parar na lista com menos elementos.

    A função zip, por padrão, já se comporta dessa maneira: ela combina os elementos das listas até que uma das listas se esgote, ou seja, até que a lista com menos elementos termine.

'''




lista_a = [1,2,3,4,5,6,7]
lista_b = [1,2,3,4]
lista_soma = []

lista_soma = [ x + y for x,y in zip(lista_a, lista_b)]

print(lista_soma)