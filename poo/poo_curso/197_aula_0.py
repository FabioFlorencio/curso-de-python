# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de classe
# string = 'Luiz # str

# método é uma função dentro da classe

class Pessoa:
    ...

# novo objeto    
p1 = Pessoa()
# atributos
p1.nome = 'Fábio'
p1.sobrenome = 'Florêncio'

p2 = Pessoa() 
p2.nome = 'Francisca'
p2.sobrenome = 'Cassimiro'


print(p1)
print(p1.nome + " " + p1.sobrenome)
print(p2.nome + " " + p2.sobrenome)
