'''

    Aula 87 - Introdução ao desempacotamento + tuples (tuplas)

    Existe uma opção para pegar somente um valor especifico. Vai ser necessário criar uma variável
    de resto

    obs. quando não for utilizar uma variável pode se usar o underline para indicar o não uso dessa.

'''

# Dessa forma vai gerar erro, pois tem menos variaveis que valores
# nome1, nome2 = ['Fábio', 'Helena', 'Jones']
#print(nome1)

nome1, *resto = ['Maria', 'Helena', 'Luiz']

print(nome1)
print('Resto dos itens da lista:',resto)

# O uso do underline é uma convenção em python para indicar que não vai ser usada a variável
carro1, *_ = ['Volkswagem','Fiat','Ford']
print(carro1, _)

# Vai gerar um array vazio
_ ,_ ,cidade3, *_ = ['São Paulo', 'Rio de janeiro', 'Ceará']
print(cidade3, _)










