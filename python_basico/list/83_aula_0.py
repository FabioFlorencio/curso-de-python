# list.extend -> serve para incluir mais de um elemento em uma lista, diferente do método append, que deve ser usaso para incluir somente um elemento, caso seja usado incorretamente, o método vai criar mais uma lista dentro o array

lista_a = [1,2,3]
lista_b = [4,5,6]
lista_c = lista_a + lista_b + [7,8,9]

print('Lista A:',lista_a)
print('Lista B',lista_b)
print('Lista C',lista_c)
print(len(lista_c))

lista_a.extend(lista_b)

lista_c.append('Fabio')

print('Usando o método extend na lista_a:', lista_a)
print(lista_c)
print(id(lista_a))
print(id(lista_b))
print(id(lista_c))
print(sum(lista_a))
