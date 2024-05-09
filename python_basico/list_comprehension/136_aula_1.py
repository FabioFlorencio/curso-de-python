'''
    Aula 136 - Introdução à List comprehension em Python

    List comprehension em python
    List comprehension é uma rápida para criar listas
    a partir de iteráveis

'''

# Em linguagens tradicioais, seria dessa forma a inclusão de itens em uma list vazia
lista = []
for numero in range(10):
    lista.append(numero)

print(lista)  
# list comprehension permiti fazer operações
# list comprehension permiti fazer ternário
# list comprehension permiti fazer um filtro entre outros possibilidades
lista = [numero * 2 for numero in range(10)]

print(lista)

# observe que no final do for não vai dois pontos
# outra forma de ser feito, caso não esteja compreendendo
lista1 = [
    num * 4 
    for num in range(10)
]

print(lista1)


