'''
    6 - Faça um Programa que leia três números e mostre o maior deles.

'''

numeros = []
qtd_numeros = 3
maior_numero = float('-inf') # Inicialize com o menor valor possível

for i in range(qtd_numeros):
    numeros.append(float(input(f'Digite o {i+1}° número: ')))    
    if numeros[i] > maior_numero:
        maior_numero = numeros[i]
        


print(f'Maior número é: {maior_numero}')    



    


    



    



