"""
Um atributo de classe é compartilhado por todas as instâncias da classe. Ele é definido diretamente na classe
e não em métodos como __init__.
 Usamos atributos de classe quando queremos compartilhar uma variável comum entre todas as instâncias da classe.

"""


class Pessoa:
    especie = "Humano"  # Atributo de classe

    def __init__(self, nome, idade):
        self.nome = nome  # Atributo de instância
        self.idade = idade  # Atributo de instância

# Criando instâncias da classe
p1 = Pessoa("João", 30)
p2 = Pessoa("Maria", 25)

# Acessando o atributo de classe
print(p1.especie)  # Saída: Humano
print(p2.especie)  # Saída: Humano

# Modificando o atributo de classe
Pessoa.especie = "Ser Humano"

# Todas as instâncias refletem a mudança
print(p1.especie)  # Saída: Ser Humano
print(p2.especie)  # Saída: Ser Humano
