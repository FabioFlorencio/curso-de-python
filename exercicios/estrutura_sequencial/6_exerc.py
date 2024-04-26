'''
    Faça um Programa que peça o raio de um círculo, calcule e mostre
    sua área.

'''

import math

raio = float(input(f'Digite o raio de um círculo: '))
area = math.pi * pow(raio,2)

print(f'A área do círculo é: {area:.2f}')
