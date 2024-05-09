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


# usando list comprehension
# observe que no final do for não vai dois pontos
lista1 = [1 for numero in range(10)]
print(lista1)

# dentro de list permiti criar itens
# é necessário criar uma variável para receber os números gerados pelo iterável
lista2 = [numero for numero in range(10)]
print(lista2)
print(numero)

numero = 11

print(numero)


