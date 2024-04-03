'''
    Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

'''

import math

rend_lata = 18 * 3

area_quadrada = float(input(f'Informe o tamanho da área que deseja pintar(m²) :'))
qtd_latas = math.ceil(area_quadrada / rend_lata)

preco_tot = qtd_latas * 80


print('\nVai ser necessário utilizar %d lata(s) de tinta' %(qtd_latas))
print('O preço total da(s) lata(s) de tinta é R$%.2f' %(preco_tot))









