'''
    Aula 41 - Operador Lógico "and"
    and, or, not
    and = todas as condições precisam ser verdadeiras
    0 0.0 '' False -> Essas comparações também são consideradas falsas

'''

entrada = input(f'[E]ntrar [S]air: ')
senha_digitada = input(f'Digite sua senha: ')

senha_permitida = '123456'

if (entrada == 'E' or entrada == 'e') and senha_digitada == '123456':
    print(f'Entrar')
else:
    print(f'Sair\n')

# Avaliação de curto circuito

print(0 or True)
print(0 or False or True)

# Nesse exemplo retorna 'abc'
print(0 or False or 0 or 'abc' or True)    

print()

# É uma forma de validar usando 'or' no input
senha = input('Senha: ') or 'Não digitou a senha!'
print(senha)

