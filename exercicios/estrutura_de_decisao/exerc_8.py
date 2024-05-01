'''
    8 - Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, 
    sabendo que a decisão é sempre pelo mais barato.

'''

precos_produtos = []

for i in range(3):
    precos_produtos.append(float(input(f'Digite o valor do {i+1} produto: ')))


print(f'O produto mais barato é R${min(precos_produtos)} .')


    


    



    



