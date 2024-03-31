'''
    Aula 53 -  Flags, is, is not e None
    Flag (bandeira) - Marcar um local
    is e is not
'''

def buscar_valor(chave, dicionario):
    if chave in dicionario:
        return dicionario[chave]
    else:
        return None

meu_dicionario = {'a': 1, 'b': 2, 'c': 3}

valor_encontrado = buscar_valor('d', meu_dicionario)

if valor_encontrado is None:
    print("O valor não foi encontrado no dicionário.")
else:
    print("O valor encontrado é:", valor_encontrado)
