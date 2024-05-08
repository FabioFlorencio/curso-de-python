'''
    4 - Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
'''

vogais = ('a','e','i','o','u')
texto = 'A letra digitada é "{}" e é uma {}.'

def verificar_letra(letra):               
    resp = texto.format(letra,'vogal') if letra.casefold() in vogais else texto.format(letra,'consoante')
    return resp



letra = input(f'Digite uma letra:')

print(verificar_letra(letra))
    



