'''
    Aula 148 - yield from em generator functions
    Uso de Yield from
'''

def gen1():
    yield 1
    yield 2
    yield 3
    print('fim do g1')

def gen2():
    yield from gen1()
    yield 4
    yield 5
    yield 6

g = gen2()

for x in g:
    print(x)

