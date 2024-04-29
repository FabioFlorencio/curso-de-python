'''
    7 - Faça um Programa que leia três números e mostre o maior e o menor deles.

'''

numeros = []
numero_maior = numero_menor = float('-inf') # inicialize com o menor valor possível
qtd_numeros = 3

for i in range(qtd_numeros): 
    numeros.append(float(input(f'Digite o {i+1}° número:')))
       
    if i == 0:
        numero_maior = numeros[i]       
        numero_menor = numeros[i]
    elif numeros[i] >= numero_maior:    
        numero_maior = numeros[i]
    elif numeros[i] < numeros[i]:
        numero_menor = numeros[i]

        
    




print(f'\nO maior número é {numero_maior}')            
print(f'O menor número é {numero_menor}')






    











    


    



    



