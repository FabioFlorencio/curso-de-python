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

# desempocotar para juntar dicionários
pessoas_completa = {**pessoa,**dados_pessoa}

# Nesse caso recebe somente argumentos nomeados
def mostra_argumentos_nomedos(*args, **kwargs):    
    print(kwargs)


mostra_argumentos_nomedos(nome='Joana', qlq=123)










