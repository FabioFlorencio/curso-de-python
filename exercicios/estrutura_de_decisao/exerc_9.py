'''
    9 - Faça um Programa que leia três números e mostre-os em ordem decrescente. 
    
'''

precos_produtos = []

for i in range(3):
    precos_produtos.append(float(input(f'Digite o valor do {i+1} produto: ')))


print(f'O produto mais barato é R${min(precos_produtos)} .')


    


    



    



