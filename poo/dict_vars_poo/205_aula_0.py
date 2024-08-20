# Aula 205 - __dict__e vars atributos de instância 
## __dict__ são dados internos da instância. É o local onde fica salvo os dados da sua classe
# __dict__: É um atributo especial em Python que armazena todos os atributos de instância de um objeto em um dicionário.
# __dict__: Mantém os valores que podem ser escritos dentro desse objeto.

class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade
    

p1 =Pessoa('Fábio', 42)
print(p1.__dict__)
print(vars(p1))


         