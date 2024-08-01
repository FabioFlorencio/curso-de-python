'''
    Aula 167. Decoradores com parâmetros

    Material de apoio
    aula 114/115 - Higher Order Functions
    aula 116 - Closure e funções que retornam outras funções

    Video de apoio
    https://www.youtube.com/watch?v=P0aW1czXHio
    https://www.youtube.com/watch?v=vEDdPnbrf_0



'''

# utilize debugger para compreender o funcionamento de decorators

# func recebe a função soma
def decoradora(func):
    print('Decoradora 1')

    def aninhada(*args, **kwargs):
        print('Aninhada')
        # func -> corresponde a função soma
        res = func(*args, **kwargs)    
        return res + 20
    return aninhada

# @decoradora atribui uma nova funcionalidade para uma função. Nesse exemplo função soma
# @decorators por padrão recebe como parâmetro uma outra função
# @decorators por padrão tem que ter uma função que chama outra função, ou seja, uma função dentro da outra função.
@decoradora
def soma(x,y):
    return x + y


resultado = soma(10,5)

print(resultado)