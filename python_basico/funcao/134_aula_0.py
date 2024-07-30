'''
    Aula 134 -   Funções lambda complexas (para entendimento)

'''

# *args recebe qualquer argumento não nomeado
def executa(funcao, *args):
    return funcao(*args)


duplica = executa(lambda m: lambda n: n * m, 2)


print(executa(lambda x,y: x + y, 2, 3))  
print(executa(lambda *args: sum(args), 1,2,3,4))
print(duplica(3))
