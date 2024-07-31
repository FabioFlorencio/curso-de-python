'''
    Aula 136 - Introdução à List comprehension em Python

    Aula retirada do canal do youtube Otávio Miranda
    https://www.youtube.com/watch?v=1YbTDczvqco&t=649s
    Exemplos list comprehension usando função

'''

numeros = [1,2,3,4,5,6,7,8,9,10]

novos_numeros = [numero for numero in numeros if numero > 5]
impares = [ numero for numero in numeros if numero % 2 != 0]
pares = [numero for numero in numeros if numero % 2 == 0]
outro_if_0 = [numero if numero != 6 else 600 for numero in numeros]
# São duas validações nesse exemplo
outro_if_1 = [numero if numero != 6 else 600 for numero in numeros if numero % 2 == 0]
outro_if_2 = [numero if numero != 6 else 600 for numero in pares]

print('Lista de números:',numeros)
print('Lista de novos números:',novos_numeros)
print('Números impares:',impares)
print('Números pares:',pares)
print('Outro if 0:', outro_if_0)
print('Outro if 1:', outro_if_1)
print('Outro if 2:', outro_if_2)


print()
print(id(numeros))
print(id(novos_numeros))