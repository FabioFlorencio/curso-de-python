'''
    171 - Exercícios | somando duas listas
    Usa a função zip do módulo itertools para combinar elementos de duas listas e parar na lista com menos elementos.

    zip só une as listas até o tamanho da menor lista, por padrâo.
    Se lista_a tiver mais elementos que lista_b, como é o caso aqui, zip_longest continuará a somar os elementos restantes
    de lista_b com 0.
    fillvalue=0 preenche a lista mais curta com 0 para continuar a operação até que a lista mais longa termine.
'''


from itertools import zip_longest

lista_a = [11,21,3,4,55,66,77]
lista_b = [1,2,3,4]
lista_soma = []

lista_soma = [x + y for x,y in zip_longest(lista_a, lista_b, fillvalue= 0)]

print(lista_soma)