# Aula 214 -  Encapsulamento (modificadores de acesso: public, _protected, __private)
# Encapsulamento (modificadores de acesso: public, protected, private)
# Python NÃO TEM modificadores de acesso
# Mas podemos seguir as seguintes convenções
#   (Sem underline) = public
#       pode ser usado em qualquer lugar
#   (um underline) = protected
#       DEVE ser usado SOMENTE dentro classe ou suas subclasses
#   (dois underlines) = private
#       "name mangling" (desfiguração de nomes) em Python
#       só DEVE ser usado na classe em que foi declarado.
# 
# 
# self.metodo_publico() = método publico
# self._metodo_protected() = método protegido
# self.__metodo_private() = método private


class Foo:
    def __init__(self):
        self.public = "isso é público"
        self._protected = 'isso é protegido'
        self.__exemplo = 'Isso é private'

    def metodo_pub(self):   
        print('método pub') 
        return 'metodo_pub'

    def metodo_publico(self):
        self.metodo_pub()
        self.__metodo_privado()
        self._metodo_protected()
        return 'método_publico'
    
    def _metodo_protected(self):
        print('_método_protected')
        return '_metodo_protected'
    
    def __metodo_privado(self):
        print('__método_private')
        return '__metodo_private'
    
    

    
f = Foo()    

print(f.public)
print()
print(f.metodo_publico())
print()
print('NÃO DEVE ser usado fora da classe ou suas subclasses',f._metodo_protected())
# vai gerar um erro, devido é um método privado
# print(f.__metodo_privado())




