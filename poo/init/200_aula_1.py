# Aula 200 - Métodos em instâncias de classes Python

# usando um argumento nomeado
class Carro:
    def __init__(self, nome):
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} está acelerando ...')    


carro_1 = Carro('Fusca')

print(carro_1.nome)
carro_1.acelerar()

print() 

carro_2 = Carro(nome = 'Celta')

print(carro_2.nome)
carro_2.acelerar()


