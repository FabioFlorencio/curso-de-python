''''
    for + Range
    range -> range(start, stop, step)

    Quando se passa somente um valor em Range está determinando o 'stop'
'''


for numero in range(10):
    print(numero,end=" ")

print('\n')    

for numero in range(5,10):
    print(numero, end=' ')    

print('\n')    

for numero in range(5,10,2):
    print(numero,end =" ")

print('\n')    

for numero in range(-1, -10, -2):
    print(numero)

i = 0

for numero in range(0,22,2):
    print(2,'x', i,'=', numero)
    i+=1

indice = 0

print()

for numero in range(0,22,2):
    print(2,indice,sep=" x ", end=" = ")
    print(numero)
    indice+=1





