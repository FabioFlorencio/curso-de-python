# Aula 209 - Métodos de classe (@classmethod) + factories methods (métodos fábrica)
# São métodos onde "self" será "cls", ou seja,
# ao invés de receber a instância no primeiro parâmetro, receberemos a própria classe.

class Pessoa:
    # atributo da classe, permiti acesso direto
    ano = 2024

    # método de instância
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # método de instância
    def metodo_de_classe(self):
        print('Método da intância:')

    # método da classe
    @classmethod
    def criar_com_50_anos(cls, nome):    
        return cls(nome, 50)
    
    @classmethod
    def criar_sem_nome(cls, nome,idade):
        return cls(nome , idade)
    
    

p1 = Pessoa('João', 34)
p2 = Pessoa.criar_com_50_anos('Helena')
p3 = Pessoa.criar_sem_nome('Jones',60)

print(Pessoa.ano, end='\n\n')
print('Nome:', p2.nome , ' idade:', p2.idade )
print('Nome:', p1.nome , ' idade:', p1.idade )
print('P3:', p3.nome , ' idade:', p3.idade)
p1.metodo_de_classe()
Pessoa.metodo_de_classe(p2)


