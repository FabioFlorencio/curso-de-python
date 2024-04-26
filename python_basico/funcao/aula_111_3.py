

'''

    Aula 111 - (Parte 1) *args para quantidade de argumentos não nomeados variáveis

'''
# args é uma convenção comum para se referir a uma sequência de argumentos
# Dessa forma seria uma forma de não declarar vários argumentos

def soma(*args):
    total = 0 
    for i,numero in enumerate(args):
        print(i,numero)            



soma(2,4,6,7,8,3)        