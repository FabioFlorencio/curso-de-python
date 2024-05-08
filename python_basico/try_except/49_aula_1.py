
numero_str = input('vou dobrar o número que você digitar:')

try:
    print('STR', numero_str)
    # caso não seja uma string vai pular a instrução.
    numero_float = float(numero_str)
    print('FLOAT:', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2}')
except:
    print('Isso não é um número')