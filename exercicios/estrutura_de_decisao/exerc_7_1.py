'''
    6 - Faça um Programa que leia três números e mostre o maior deles.

'''

numeros = []
qtd_numeros = 3


for i in range(qtd_numeros):
    numeros.append(float(input(f'Digite o {i+1}° número: ')))


def encontrar_maior_menor_numero(numeros):
    maior_numero = max(numeros)
    menor_numero = min(numeros)

    return maior_numero,menor_numero


result_maior,result_menor = encontrar_maior_menor_numero(numeros)

print(f'Maior número: {result_maior}')
print(f'Menor número: {result_menor}')




    


    



    



