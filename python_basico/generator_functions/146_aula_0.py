'''
    Aula 146. Generator expression, Iterables e Iterators em Python
    Generator não gera indíce, não tem tamanho, diferentemente de list
    Generator "Seria uma função que pausa, que pode continuar quando for chamada."
'''


import sys

lista = [n for n in range(10)]
generator = (n for n in range(10))

print(lista)
print(generator)
print()

print(next(generator),sep='\n')
print(next(generator),sep='\n')
print()


for gen in generator:
    print(gen)

print()
print(sys.getsizeof(lista))
print(sys.getsizeof(generator))
