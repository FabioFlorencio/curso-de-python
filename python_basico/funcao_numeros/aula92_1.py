'''

    Aula 92 - Imprecisão dos números de ponto flutuante + round e decimal.Decimal
    Exemplo usando o modulo decimal, seria uma alternativa quando precisa de uma
    precisão no número

'''

import decimal

num_1 = decimal.Decimal('0.1')
num_2 = decimal.Decimal('0.7')


print(round(num_1 + num_2, 3))
print(type(num_1))
print('Qual o maior valor 10 ou 2: ',max(10,2))
print('Qual o menor valor 10 ou 2: ',min(10,2))
print('Qual é a mádia: ',sum(10,2,5))


