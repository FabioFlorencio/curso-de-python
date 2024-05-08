'''
    Aula 70 - Qual letra apareceu mais vezes na frase? (Iterando strings com while)

'''

frase = 'O Python é uma linguagem de programação ' \
        'multiparadigma. ' \
        'Python foi criado po Guido Van Rossum.'

i = 0

print(len(frase))


while i < len(frase):   
    letra_atual = frase[i]
    # Recebe o corte da palavra e verifica a qtd
    qtd_vezes_letra_apareceu = frase.count(letra_atual)
    print('Linha ',i    ,letra_atual, qtd_vezes_letra_apareceu)
    i += 1
