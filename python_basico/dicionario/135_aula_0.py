"""
    Aula 135 - Empacotamento e desempacotamento de dicionários + *args e **kwargs
    kwargs = Argumentos nomeados
"""

# exemplo de desempacotamento
a, b = 1, 2

pessoa = {
    'nome' : 'Aline',
    'Sobrenome' : 'Souza'
}

a,b = pessoa

print(a,b)

a,b = pessoa.items()
print(a,b,'\n')

# Desempocotamento interno
(a1,b1), b = pessoa.items()
print(a1,b1, b)







