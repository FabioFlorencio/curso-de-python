'''
    Faça um Programa que peça dois números e imprima a soma.

'''

numeros = []   
i = 0

while i < 2:
    try:
        num = int(input('Digite um número:'))
        numeros.append(num)
        i+= 1        
    except ValueError:
        i = 0              
        numeros.clear()
        print('Você não digitou um número inteiro! Tente novamente!')

print(sum(numeros))        


