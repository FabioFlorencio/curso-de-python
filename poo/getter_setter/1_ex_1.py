"""
Agora, vamos adicionar lógica para controlar o acesso e a modificação do atributo nome usando
getters e setters.

Obs. Nesse exemplo não está sendo usado @decocators para diferenciar o getters e setters.
Foi utlizado a assinatura do método(get/set)
"""


class Pessoa:
    def __init__(self, nome):
        self._nome = nome  # O atributo privado é indicado por "_"

    # Getter
    def get_nome(self):
        return self._nome

    # Setter
    def set_nome(self, nome):
        if isinstance(nome, str):  # Verificação se é uma string
            self._nome = nome
        else:
            raise ValueError("Nome deve ser uma string")

p = Pessoa("Ana")
print(p.get_nome())  # Usando o getter

p.set_nome("Maria")  # Usando o setter
print(p.get_nome())
