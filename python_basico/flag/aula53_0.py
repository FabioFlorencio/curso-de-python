'''
    Aula 53 -  Flags, is, is not e None
    Flag (bandeira) - Marcar um local
    is e is not
'''

condicao = True
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Faça algo')
else:
    print('Não faça algo')    

print(passou_no_if is None)    
print(passou_no_if is not None)