# Aula 215 - Relação entre classes: associação, agregação e composição
# Relações entre classes: associação, agregação e composição
# Associação é um tipo de relação onde os objetos estão ligados dentro do sistema


class Escritor:
    def __init__(self, nome):
        self.nome = nome
        self._ferramenta = None

    # getter
    @property
    def ferramenta(self):
        return self._ferramenta
    
    #setter
    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self._ferramenta = ferramenta


class FerramentasDeEscrever:
    def __init__(self, nome='Caneta sem marca'):
        self.nome = nome

    def escrever(self):               
        return f'{self.nome} está escrevendo'
    

escritor = Escritor('Fábio')
caneta = FerramentasDeEscrever()
maquina_de_escrever = FerramentasDeEscrever('Máquina de escrever')

# linkar objetos
escritor.ferramenta = caneta

print(caneta.escrever())
print(escritor.ferramenta.escrever())

escritor.ferramenta = maquina_de_escrever

print(escritor.ferramenta.escrever())