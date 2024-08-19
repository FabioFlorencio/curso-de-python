"""
São métodos que são chamados na própria classe, em vez de em instâncias individuais da classe.

O primeiro parâmetro de um método de classe é sempre cls, que é uma referência à classe, e
não à instância. Para definir um método de classe, você usa o decorador @classmethod.

Métodos de classe são usados quando você quer que um comportamento seja relacionado à própria
classe em si, e não às instâncias dela. Eles podem ser usados, por exemplo, para criar fábricas 
de objetos ou manter um estado global relacionado à classe.

"""


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_sem_nome(cls, nome, idade):
        # cls() -> cria uma nova instância da classe
        # cls.idade-> seria usado para acessar um atributo da classe, caso existisse.
        return cls(nome, idade)

# Criando uma nova instância da classe Pessoa usando o método de classe
nova_pessoa = Pessoa.criar_sem_nome("João", 30)

print(nova_pessoa.nome)  # Saída: João
print(nova_pessoa.idade)  # Saída: 30
