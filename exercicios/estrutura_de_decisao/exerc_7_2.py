'''
    7 - Faça um Programa que leia três números e mostre o maior deles.

'''

numeros = []
qtd_numeros = 3


for i in range(qtd_numeros):
    numeros.append(float(input(f'Digite o {i+1}° número: ')))


def encontrar_maior_menor_numero(numeros):
    maior_numero = max(numeros)
    menor_numero = min(numeros)

    return maior_numero,menor_numero



result = encontrar_maior_menor_numero(numeros)
# O retorno da função será uma tupla, será necessário desempacotar as variáveis
num_maior, num_menor= result

print('Maior número:',num_maior)
print('Meor número',num_menor)    



    


    



    



