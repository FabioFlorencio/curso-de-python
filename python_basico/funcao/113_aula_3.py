# Exercícios com funções

# Crie uma função que multiplica todos os argumentos não nomeados recebidos
# Retorne o total para uma variável e mostre o valor da variável

# Crie uma função fala se um número é par ou ímpar
# Retorne se o número é par ou ímpar


def valida_par_impar(numero):

    result = f'{numero} é par' if numero % 2 == 0 else f'{numero} é impar'
    return result


resp = valida_par_impar(7)
print(resp)







