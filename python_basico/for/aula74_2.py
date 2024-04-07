'''
    Aula 74 - Como o for funciona por baixo dos panos? (next, iter, iterável e iterador)

    Iterável -> str, range, etc (__iter__)
    Iterável -> è um método que entrega uma coisa por vez
    Iterável -> Todo iterável tem um método iter
    next -> me entregue o próximo valor

    Obs. Quando se utiliza um for a primeira coisa que solicitada é o método iter

'''

# for letra in texto

texto = 'Fábio' # iterável
iteratador = iter(texto)

# Seria algo próximo que o python faz por baixo dos panos
# try except -> pode tratar uma exceção especifica

while True:
    try:
        letra = next(iteratador)
        print(letra)
    except StopIteration:    
        break

# Modo tradicional'

for letra in texto:
    print(letra)    