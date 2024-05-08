'''
    Aula 117 - Exercício com funções

'''

def criar_multiplicador(multiplicador):    
    def multiplicador(numero):
        return numero * multiplicador
    return multiplicador

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(2))
print(triplicar(3))
print(quadruplicar(4))



