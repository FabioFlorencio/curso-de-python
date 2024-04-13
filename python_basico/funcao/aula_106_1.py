'''
    Aula 106 - Argumentos nomeados e argumentos posicionais (não nomeados) em funções

    Argumento nomeados e não nomeados em funções Python
    Argumento nomeado tem nome com sinal de igual
    Argumento não nomeado recebe apenas o argumento (valor)

    Por padrão, funções Python retornam None(nada).

'''

# definição
def soma(x ,y):
    print(x + y)

soma(1, 2)

# dessa forma permiti mandar parâmetro fora de ordem
soma(y=2, x=1)



