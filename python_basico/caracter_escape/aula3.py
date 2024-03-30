''' fonte curso em video - aula 86

    ^: Este é o operador de alinhamento, onde ^ indica alinhamento central.
    5: Este é o número que especifica a largura total do campo, ou seja, o número total de caracteres que a string formatada deve ocupar.
'''
#Matriz 3 x 3
matriz = [[0,0,0],[0,0,0],[0,0,0]]

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]:'))

print('-=' * 30)        

for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()






