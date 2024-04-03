'''
    11.Faça um Programa que peça 2 números inteiros e um número real. 
        Calcule e mostre:
        a. o produto do dobro do primeiro com metade do segundo .
        b. a soma do triplo do primeiro com o terceiro.
        c. o terceiro elevado ao cubo.

'''

i = 0
numeros_int = []

while i < 2:
    num = int(input(f'Digite o {i+1}º inteiro número: '))    
    numeros_int.append(num)
    i+= 1

num3 = float(input(f'Digite um número real: '))

string_result = 'Resultado'

result_a = (numeros_int[0] * 2 ) * numeros_int[1] / 2
result_b = pow(numeros_int[0],3) + num3
result_c = num3 ** 3

print('%s 1: %d'%(string_result,result_a))
print('%s 2: %.2f'%(string_result,result_b))
print('%s 3: %.2f'%(string_result, result_c))


