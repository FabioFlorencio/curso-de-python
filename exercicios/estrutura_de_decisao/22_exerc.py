'''
    22 - Faça um Programa que peça um número inteiro e determine se ele é par ou impar. 
    Dica: utilize o operador módulo (resto da divisão).

'''

valida = True


def par_impar(num):

    
    if num % 2 == 0:
        msg_validacao = "O número {} é número par!"
    else:
        msg_validacao = "O número {} é número impar!"

    return num, msg_validacao

while valida:
    try:
        num = int(input('Digite um número:'))
        valida = False                
    except ValueError:
        print('Você digitou um valor incorreto! Tente novamente!') 


numero,resp = par_impar(num)            

print(resp.format(numero))
   


