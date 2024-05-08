''''
    for + Range
    range -> range(start, stop, step)

    Quando se passa somente um valor em Range está determinando o 'stop'
'''

numeros_1 = range(10)
numeros_2 = range(5,10)
numeros_3 = range(5,10,2)


for numero in numeros_1:
    print(numero,end=" ")

print('\n')    

for numero in numeros_2:
    print(numero, end=' ')    

print('\n')    

for numero in numeros_3:
    print(numero,end =" ")





