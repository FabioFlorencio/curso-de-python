'''
    Aula - 85 - for in com tipo list    

'''
import numpy as np

for letra in 'abc':
    print(letra,end=" ")

print()    

lista = ['Maria','Helena','Luiz']    

for nome in lista:
    print(nome, type(nome))

lista[:] = 'Fábio' , 'João'

lista_numeros = np.arange(10)
lista_numeros[:] = 84


print()
print(lista)
print(type(lista))
print(lista_numeros)



