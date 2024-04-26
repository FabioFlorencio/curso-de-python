# Exercícios com funções

# Crie uma função que multiplica todos os argumentos não nomeados recebidos
# Retorne o total para uma variável e mostre o valor da variável

# Crie uma função fala se um número é par ou ímpar
# Retorne se o número é par ou ímpar


def multiplicar(*args):
    total = 1
    for numero in args:
        total *= numero
    return total


def mult(*args):
    n1,n2,n3 = args
    total = n1 * n2 * n3
    return total

numeros = [1,2,3]

# argumentos não nomeados
result2 = mult(*numeros)
result1 = multiplicar(2,4,6)

print(result1)
print(result2)










