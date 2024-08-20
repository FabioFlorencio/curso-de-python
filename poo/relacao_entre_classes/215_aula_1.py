class Carro:
    def __init__(self, modelo):
        self.modelo = modelo

class Pessoa:
    def __init__(self, nome):
        self.nome = nome
        self.carro = None  # A pessoa pode ou não ter um carro

    def comprar_carro(self, carro):
        self.carro = carro

    def mostrar_carro(self):
        if self.carro:
            print(f"{self.nome} possui um carro: {self.carro.modelo}")
        else:
            print(f"{self.nome} não possui um carro")

# Criação de objetos
carro1 = Carro("Toyota Corolla")
carro2 = Carro("Fusca Volkswagem")
pessoa1 = Pessoa("João")
pessoa2 = Pessoa("Pedro")

# Associação: João compra um carro
# pessoa1.comprar_carro = carro1
pessoa1.comprar_carro(carro1)
pessoa1.mostrar_carro()
pessoa2.comprar_carro(carro2)
pessoa2.mostrar_carro()
