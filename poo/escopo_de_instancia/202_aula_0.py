# Aula 202 - Escopo de classe e de métodos da classe

class Animal:
    def __init__(self, nome):
        self.nome = nome


    def comendo(self, alimento):        
        return f'{self.nome} está comendo {alimento}'
    

    # Método está chamando outro método
    def executar(self, *args, **kwargs):
        return self.comendo(*args, **kwargs)

    

    
leao = Animal(nome='Leão')

print(leao.comendo('Maça'))

print(leao.executar("Feijoada"))
