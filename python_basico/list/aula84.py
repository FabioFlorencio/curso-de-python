
'''
Aula - 84 - Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor da memória (Mutável)
= - método id serve para obter o endereço de memória de um objeto.
'''
lista_a = ['Fábio', 'Maria',1, True, 1.2]
lista_b = lista_a

# método id -> serve para obter o endereço de memória de um objeto.
# nesse exemplo as listas A e B estão apontando para mesmo local de memória
# Caso seja alterado algum valor em qualquer lista vai afetar em todas.

print(f'Mesmo local de memória {id(lista_a)} lista A:',lista_a)
print(f'Mesmo local de memória {id(lista_b)} lista B:',lista_b)

print(id(lista_a))
print(id(lista_b))

lista_b[0] = 'Teste'

print(lista_a)
print(lista_b)

# Dessa forma gera um novo local de memória para lista B usando o método copy()

lista_b = lista_a.copy()

print(id(lista_a))
print(id(lista_b))
