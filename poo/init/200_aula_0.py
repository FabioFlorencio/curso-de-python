# Aula 200 - Métodos em instâncias de classes Python

# usando um argumento nomeado
class Carro:
    def __init__(self, nome = 'Bala'):
        self.nome = nome

carro = Carro()

print(carro.nome)
