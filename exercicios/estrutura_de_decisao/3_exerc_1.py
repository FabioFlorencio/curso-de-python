'''
    3 - Faça um Programa que verifique se uma letra digitada é "F" ou "M".
    Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
'''

sexo = str(input(f'Digite seu gênero: F - Feminino, M - Masculino, Sexo Inválido: '))

generos = ('m','f')

def escolher_genero(sexo,generos):    

    if sexo.casefold() in generos:
        resp_genero = sexo
    elif sexo.casefold() in generos:
        resp_genero = sexo
    else: 
        resp_genero = 'Sexo inválido!'

    return resp_genero


print(escolher_genero(sexo,generos))
