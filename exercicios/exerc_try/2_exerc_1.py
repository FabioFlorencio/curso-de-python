'''
    Faça um Programa que peça um número e então mostre a
    mensagem do número informado foi [número].

'''

valida = True

while valida:
    try:
        num = int(input(f'Digite um número inteiro:'))        
        valida = False
        print(f'O número digitado é {num}!')
    except ValueError:
        print('Você não digitou um número inteiro!')    


