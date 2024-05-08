# Tipo list - mutável, ou seja, pode ser alterada
# Uma lista pode ter uma outra lista dentra da mesma
# Uma lista pode ser acessada por indice
# Uma lista começa por indice zero
# Uma lista pode trabalhar com indice negativo


#         |------------------------- Ìndice 0 ou -5
#         |     |------------------- Ìndice 1 ou -4
#         |     |     |------------- Ìndice 2 ou -3
#         |     |     |     |------- Ìndice 3 ou -2
#         |     |     |     |    |-- Ìndice 4 ou -1               
#         |     |     |     |    |
lista = [123, True,  1.2, 'Fá',  []]

print(lista)
print('Acessar ìndice da lista, posição 0:',lista[0])
print('Acessar ìndice da lista, posição 1:',lista[1])
print('Acessar ìndice da lista, posição 2:',lista[2])
print('Acessar ìndice da lista, posição 3:',lista[3])
print('Acessar ìndice da lista, posição 4:',lista[4])

# Verifica um tipo de dado de uma lista

print('Verifica o tipo de dado de um indice',type(lista[1]))

# Usando a função upper
lista[3] = lista[3].upper()

print('Usando a função upper case: ',lista[3].upper())

print(lista)

