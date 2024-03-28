'''
    Aula 49 - Introdução ao try e except para capturar erros (exceptions)

    Introdução ao try/except
    try -> tentar executar o código
    except -> ocorreu algum erro ao tentar executar

'''

numero_str = input('Digite um número float ou uma string: ')

#numero_str = float(numero_str)

if numero_str.isdigit():
    print(f'O dobro de {numero_str} é {numero_str * 2}')
else:
    print(f'Isso não é um número inteiro!')    



