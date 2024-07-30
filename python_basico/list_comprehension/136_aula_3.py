'''
    Aula 136 - Introdução à List comprehension em Python

    Aula retirada do canal do youtube Otávio Miranda
    Exemplos list comprehension usando função

'''
def multiplicacao(x,y):
    return x * y

def divisao(x,y):
    return x / y

numeros = [1,2,3,4,5]
divisao = [multiplicacao(numero, 2 ) for numero in numeros]
multiplicacao = [divisao(numero, 2) for numero in numeros]


print('Divisão:', divisao)
print('Multiplicação:', multiplicacao)

# https://www.youtube.com/watch?v=1YbTDczvqco
# video 10:49

