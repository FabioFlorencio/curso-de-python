# Aula 198 - Classes são moldes para criar novos objetos

# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos

# método é uma função dentro da classe
# self referência o objeto que está sendo criado
# método init -> inicializa os atributos da classe, e é uma das primeiras coisas que são executadas quando você cria uma classe
# método init -> sempre retorna none
# self é algo parecido com o "this" do java
# self é usado para referenciar a própria instância
# self é o objeto da classe
# self é usado para usar os dados da instância
# self é usado por convenção, mas poderia ser outro nome

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

# novo objeto    
p1 = Pessoa('Fábio', 'Florêncio')

print(p1.nome + " " + p1.sobrenome)

p2 = Pessoa('Francisca', 'Cassimiro')

print(p2.nome + " " + p2.sobrenome)

