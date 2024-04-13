'''
    Aula 107 - Valores padrão para parâmetros em funções Python + NoneType e None

    Ao definir uma função, os parâmetros podem ter valores padrão. Caso o valor não seja enviado para o parâmetro, o valor padrão será usado.

'''

def soma(x , y, z = None):
    # caso não seja enviado algum valor por padrão será atribuido None
    if z is not None:
        print(f'{x=} {y=} {z=}')
    else:
        print(f'{x=} {y=} resultado:', x + y)


soma(1, 2)
soma(3, 5)
soma(100, 200)
soma(1,3,7)

