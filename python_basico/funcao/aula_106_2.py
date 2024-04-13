'''
    Aula 106 - Argumentos nomeados e argumentos posicionais (não nomeados) em funções

    Argumento nomeados e não nomeados em funções Python
    Argumento nomeado tem nome com sinal de igual
    Argumento não nomeado recebe apenas o argumento (valor)

    Por padrão, funções Python retornam None(nada).

'''

# definição
def soma(x ,y, z):
    print(x + y + z)

soma(1, 2, 3)

# é possível misturar com parâmetro e sem
soma(10, y=1, z=6)
soma(11, z=2, y=5)

# Depois que é nomeado um parâmetro a próxima variável não aceita sem declaração
# Faço o teste
#soma(12,z=2,33)


