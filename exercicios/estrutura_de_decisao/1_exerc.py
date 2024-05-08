# 1 - Faça um Programa que peça dois números e imprima o maior deles.

num_1 = input(f'Digite um número:')
num_2 = input(f'Digite outro número:')

maior_numero = f'Maior número é {num_1}' if num_1 > num_2 else f'Maior número é {num_2}'

print(maior_numero)