"""
São métodos que são chamados na própria classe, em vez de em instâncias individuais da classe.

O primeiro parâmetro de um método de classe é sempre cls, que é uma referência à classe, e
não à instância. Para definir um método de classe, você usa o decorador @classmethod.

Métodos de classe são usados quando você quer que um comportamento seja relacionado à própria
classe em si, e não às instâncias dela. Eles podem ser usados, por exemplo, para criar fábricas 
de objetos ou manter um estado global relacionado à classe.

"""


class Pessoa:
    populacao = 0

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        Pessoa.populacao += 1

    @classmethod
    def populacao_atual(cls):
        return f"População atual: {cls.populacao}"

# Criando instâncias
p1 = Pessoa("João", 30)
p2 = Pessoa("Maria", 25)

# Chamando o método de classe
print(Pessoa.populacao_atual())  # Saída: População atual: 2
