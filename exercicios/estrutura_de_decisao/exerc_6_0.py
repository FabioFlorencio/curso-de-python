'''
    6 - Faça um Programa que leia três números e mostre o maior deles.

'''

numeros = []
qtd_numeros = 3
maior_numero = 0

for i in range(qtd_numeros):
    numeros.append(float(input(f'Digite o {i+1}° número: ')))    
    maior_numero = numeros[i] if numeros[i] > maior_numero else maior_numero


print(f'Maior número é: {maior_numero}')    



    


    



    



