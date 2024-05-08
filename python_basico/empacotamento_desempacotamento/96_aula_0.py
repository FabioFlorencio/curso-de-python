'''
    Aula 96 - Desempacotamento em chamadas de funções

'''

letras = 'ABCD'
lista = ['Maria','Helena', 1, 2, 3,'Eduarda','fim da lista']
tupla = 'Python', 'è', 'legal'

# desempacotamento
a,b, *_ ,e, f = lista

print('Desempacotamento de list: ',a,b,e,f)
print('Desempacotamento de list(meio da lista): ',_)
