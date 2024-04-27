'''
    3 - Faça um Programa que verifique se uma letra digitada é "F" ou "M".
    Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
'''

genero = str(input(f'Digite seu gênero: F - Feminino, M - Masculino, Sexo Inválido: '))


def escolher_genero(genero):    

    if genero.upper() == 'M' or genero.lower() == 'm':
        resp_genero = genero
    elif genero.upper == 'F' or genero.lower() == 'f':
        resp_genero = genero
    else: 
        resp_genero = 'Sexo inválido!'

    return resp_genero


print(escolher_genero(genero))
