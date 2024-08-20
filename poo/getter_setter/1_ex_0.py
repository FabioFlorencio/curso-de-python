"""
Em Python, o uso de getters e setters pode ser simplificado com o decorador @property, tornando o 
código mais "pythônico".

obs. Que não está sendo usado get e set na assinatura do método. Em python utiliza o @decorador
para essa finalidade.cs
"""


class Pessoa:
    def __init__(self, nome):
        self._nome = nome

    # Getter com @property
    @property
    def nome(self):
        return self._nome

    # Setter usando @nome.setter
    @nome.setter
    def nome(self, nome):
        if isinstance(nome, str):
            self._nome = nome
        else:
            raise ValueError("Nome deve ser uma string")

p = Pessoa("Ana")
print(p.nome)  # Agora, o acesso é direto, como se fosse um atributo normal

p.nome = "Maria"  # Modificando usando o setter implícito
print(p.nome)
