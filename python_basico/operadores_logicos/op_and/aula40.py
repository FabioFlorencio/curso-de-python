'''
    Aula 40 - Operador Lógico "and"
    and, or, not
    and = todas as condições precisam ser verdadeiras
    0 0.0 '' False -> Essas comparações também são consideradas falsas

'''

entrada = input(f'[E]ntrar [S]air: ')
senha_digitada = input(f'Digite sua senha: ')

senha_permitida = '123456'

if entrada == 'E' and senha_digitada == senha_permitida:
    print(f'Entrar')
else:
    print(f'Sair\n')

# Avaliação de curto circuito 
    
print(True and False and True)
# Nesse exemplo vai retornar '0'
print(True and 0 and True)
print(bool(0) and bool(0.0))

# 0 0.0 '' False -> Essas comparações também são consideradas falsas

print('È false?',bool(0))
print('È False?',bool(0.0))
print('È False?',bool(' '))
print('È False?',bool(''))



