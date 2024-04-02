'''
    Aula 70 - Qual letra apareceu mais vezes na frase? (Iterando strings com while)

'''

frase = 'O Python é uma linguagem de programação ' \
        'multiparadigma. ' \
        'Python foi criado po Guido Van Rossum.'

i = 0
qtd_q_letra_apareceu = 0
letra_q_mais_apareceu =  ''


while i < len(frase):   
    letra_atual = frase[i]
    # Recebe o corte da palavra e verifica a qtd
    qtd_letra_atual = frase.count(letra_atual)

    if letra_atual == ' ':
        i +=1
        continue
    
    if qtd_q_letra_apareceu < qtd_letra_atual:
        qtd_q_letra_apareceu = qtd_letra_atual
        letra_q_mais_apareceu = letra_atual

    i += 1

print(f'A letra que mais apareceu foi {letra_q_mais_apareceu},')
print(f'A letra apareceu {qtd_q_letra_apareceu} vezes.')
