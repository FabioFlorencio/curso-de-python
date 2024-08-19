"""
Um atributo de instância é específico para cada instância de uma classe. Ele é geralmente 
definido dentro do método __init__ e armazena dados únicos para aquela instância.

Ele pertence apenas à instância específica da classe e não afeta as outras instâncias. Cada
instância tem sua própria cópia dos atributos de instância.

Usamos atributos de instância quando cada objeto deve manter seu próprio estado independente dos
outros objetos.
"""
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome  # Atributo de instância
        self.idade = idade  # Atributo de instância

# Criando instâncias da classe
p1 = Pessoa("João", 30)
p2 = Pessoa("Maria", 25)

# Acessando os atributos de instância
print(p1.nome)  # Saída: João
print(p2.nome)  # Saída: Maria

# Modificando o atributo de instância
p1.nome = "Carlos"

# A mudança afeta apenas a instância modificada
print(p1.nome)  # Saída: Carlos
print(p2.nome)  # Saída: Maria

