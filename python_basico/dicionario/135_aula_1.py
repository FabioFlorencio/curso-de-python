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

dados_pessoa = {
    'idade' : 16,
    'altura' : 1.75
}

print(pessoa, dados_pessoa,'\n')

# desempacotar para juntar dicionários e incluindo novos valores
pessoas_completa = {**pessoa,**dados_pessoa, 'chave': 1}

print('Juntando dicionários',pessoas_completa)








