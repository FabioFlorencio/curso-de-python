'''
    Aula 136 - Introdução à List comprehension em Python

    Aula retirada do canal do youtube Otávio Miranda

'''

numeros = [1,2,3,4,5]
divisao = [numero / 2 for numero in numeros]
multiplicacao = [numero * 2 for numero in numeros]
quadrado = [numero ** 2 for numero in numeros]

print('Divisão:', divisao)
print('Multiplicação:', multiplicacao)
print('Quadrado:', quadrado)


