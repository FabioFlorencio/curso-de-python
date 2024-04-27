'''
    4 - Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
'''

vogais = ('a','e','i','o','u')


def verificar_letra(letra): 
    valida_resp = False
    for vogal in vogais:
        if letra == vogal:
            valida_resp = True  

    resp = f'A letra digitada é vogal:{letra}' if valida_resp else f'A letra digitada é consoante:{letra}'

    return resp

letra = input(f'Digite uma letra:')

print(verificar_letra(letra))
    



