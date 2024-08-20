# Aula 214 -  Encapsulamento (modificadores de acesso: public, _protected, __private)
# 
# self.metodo_publico() = método publico
# self._metodo_protected() = método protegido
# self.__metodo_private() = método private


class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular  # Público
        self._saldo = saldo  # Protegido
        self.__senha = "senha123"  # Privado
    
    def depositar(self, valor):
        self._saldo += valor  # Método público

    def __verificar_saldo(self):
        return self._saldo  # Método privado

conta = ContaBancaria("Ana", 1000)

# Acesso a atributos públicos
print(conta.titular)  # Funciona
conta.depositar(500)

# Acesso a atributos protegidos (não recomendado)
print(conta._saldo)  # Funciona, mas não recomendado

# Acesso a atributos privados (não funciona)
# print(conta.__senha)  # Levantaria um erro

# Name mangling para acessar atributo privado (não recomendado)
print(conta._ContaBancaria__senha)  # Funciona, mas não é uma prática segura
