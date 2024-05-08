'''

    Aula 43 - Operadores in e not in

    Operadores in e not in
    in = está entre
    not in = não está entre
    Strings são iteráveis
    0 1 2 3 4 
    F á b i o
    -5 -4 -3 -2 -1
'''

nome = input('Digite seu nome: ')
encontar = input('Digite uma letra?')

if encontar in nome:
    print(f'{encontar} está em {nome}.')
else:
    print(f'{encontar} não está no nome {nome}.')    
