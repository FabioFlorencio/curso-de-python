# Exercícios com funções

# Retire da lista os números, utilizando o desempacotamento
# Faça uma função para retornar a soma desses números

lista = ['Maria','Helena', 1, 2, 3,'Eduarda','Jones'] 

nome_1, nome_2, *_, nome_3, nome_4 = lista

def soma(*args):
    n1,n2,n3 = args 
    tot = n1 + n2 + n3
    return tot


result = soma(*_)

print(result)















