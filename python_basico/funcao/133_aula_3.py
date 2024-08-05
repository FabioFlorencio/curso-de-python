# Aula avulsa
# Funções Lambda

def soma(num1, mum2):
    return num1 + num2

num1 = num2 = 2

# A função lambda precisa ser atribuida a uma variável antes do uso
soma_lambda = lambda num1, num2: num1 + num2

print(soma_lambda(num1, num2))
print(soma_lambda(5, num2))

