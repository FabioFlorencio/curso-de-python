'''
    Faça um Programa que peça dois números e imprima a soma.

'''

i = 0
soma = 0

while i < 2:
    num = int(input(f'Digite o {i}º número:'))
    soma+= num
    i+= 1   

print(f'A soma dos número é: {soma}')    