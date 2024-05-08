'''
    Aula 70 - Qual letra apareceu mais vezes na frase? (Iterando strings com while)
    String são iteravél
'''

frase = 'O python é uma linguagem de programação' \
        'multiparadigma. '\
        'python foi criado por Guido Van Rossum.'.lower()

# Conta quantas vezes a palavra python aparece        
print(frase.count('python'))
print(frase.count('a'))

