# Aula 204 - Atributos da classe

class Pessoa():
    # atributo do escopo da classe, esse valor será o mesmo em todas as intâncias da classe
    ano_atual = 2024

    #atributo da instância
    def __init__(self, nome, idade ):
        self.nome = nome
        self.idade = idade        

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade
    


p1 = Pessoa('Fabio', 30)
p2 = Pessoa('Francisca', 22)


print(Pessoa.ano_atual)
print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())



