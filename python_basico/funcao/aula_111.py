'''

    Aula 111 - (Parte 1) *args para quantidade de argumentos não nomeados variáveis

'''

def soma(*args):
    total = 0 
    for numero in args:
        print('Total', total, numero)
        total = total + numero
    print(total)    

soma(2,4,6,7,8,3)        