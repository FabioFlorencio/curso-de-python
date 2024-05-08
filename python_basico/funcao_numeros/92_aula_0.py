'''

    Aula 92 - Imprecisão dos números de ponto flutuante + round e decimal.Decimal


'''

num_1 = 0.1
num_2 = 0.7

num_3 = num_1 + num_2
# peguei uma valor que gera uma dizima para compreender a função round
res = 23/9

print(num_3)
print(f'Vamos arrendondar o resultado: {num_3:.2f}')
print(f'Vamos arrendondar o resultado usando a função round: {round(res, 3)}')
print(f'Vamos arrendondar o resultado usando a função round: {round(23/9, 3)}')
