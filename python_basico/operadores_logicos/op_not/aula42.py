'''
    aula 42 - Operador lógico "not"
    Operador lógico "not"
    Usado para inverter expressões
    not True = False
    not False = True

'''

senha = input('Senha:') 


# 
if not senha:
    print('Você não digitou nada!')
else:
    print('Você digitou alguma coisa!')    

print(bool(not senha))
print('Teste:',bool(senha))    

print()

nova_senha = input('Senha: ')

if not nova_senha:
    print('Você não digitou nada!')
else:
    print('Vc digitou alguma coisa!')    

print(bool(nova_senha))
print('Teste-1:',bool(nova_senha))

print('Outros testes')
print('È verdadeiro ou falso?',not True)
print('È verdadeiro ou falso?',not False)
print('È verdadeiro ou falso?',not 1)
print('È verdadeiro ou falso?',not 0)
