# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor da variável

# Crie uma função fala se um número é par ou ímpar
# Retorne se o número é par ou ímpar


def multiplicar(*args):
    n1,n2,n3 = args
    tot = n1 * n2 * n3
    return tot


mult = multiplicar(2,4,6)

print(mult)










