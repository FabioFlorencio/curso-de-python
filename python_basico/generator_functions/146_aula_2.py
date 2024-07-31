'''
    Aula 146. Generator expression, Iterables e Iterators em Python
    Generator não gera indíce, não tem tamanho, diferentemente de list
    Generator "Seria uma função que pausa, que pode continuar quando for chamada."
    Generator usa os métodos(next, send, close, throw)
'''

# o debug para compreender o código

def generator(n=0, maximum=10):
    while True:
        yield n
        n+= 1

        if n > maximum:
            return

# recebe função gen        
gen = generator(n=5, maximum=8)        

for n in gen:
    print(n)