'''

    Aula 31- Uma introdução às f-strings (formatação de strings)

'''

nome = 'Fábio'
altura = 100050.4
peso = 95
imc = peso / altura


#                              |------ Formata usando virgula
#                              |                                 
linha_1 = f'{nome} tem {altura:,.2f} de altura è pesa {peso} e seu IMC é {imc:.3f}' 

print(linha_1)
