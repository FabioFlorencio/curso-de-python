'''
    Aula 35 - if, elif e else: entendendo o fluxo do interpretador em condicionais
    Nessa aula fala sobre elipses e pass

'''
condicao = False

if condicao:
    print(f'Este é o código do if. Essa variável é:{condicao=}')
elif condicao:
    # Usando elipses
    ...

if 10 == 9:
    print('Outro if.')
else:
    pass
    # print(f'Pulou o código usando ''pass''.')            
    # print(f'pula')


