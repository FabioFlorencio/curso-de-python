'''
    Aula 146. Generator expression, Iterables e Iterators em Python
    Generator não gera indíce, não tem tamanho, diferentemente de list
    Generator "Seria uma função que pausa, que pode continuar quando for chamada."
    Generator usa os métodos(next, send, close, throw)
'''

def generator(n=0):
    yield 1 # pausa e retorna o valor
    yield 2 # pausa e retorna o valor
    return 'Acabou!'
    

# "Guarda o ponteiro"
gen = generator(n=0)    

print(gen.__iter__())
print(next(gen))

valida_gen = input("Quer chamar a função gen?")
if 'sim' in valida_gen.casefold():
    print(next(gen))
    gen.close()

valida_gen = input("Quer chamar a função gen?")
if 'sim' in valida_gen.casefold():
    gen = generator(n=0) 
    print(next(gen))


