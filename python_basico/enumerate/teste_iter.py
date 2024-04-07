# Verificando se uma lista é iterável
lista = [1, 2, 3]
if iter(lista):
    print("A lista é iterável")
else:
    print("A lista não é iterável")

# Verificando se uma tupla é iterável
tupla = (1, 2, 3)
if iter(tupla):
    print("A tupla é iterável")
else:
    print("A tupla não é iterável")

# Verificando se uma string é iterável
string = "Python"
if iter(string):
    print("A string é iterável")
else:
    print("A string não é iterável")

# Verificando se um número inteiro é iterável
inteiro = 123
if iter(inteiro):
    print("O número inteiro é iterável")
else:    
    print("O número inteiro não é iterável")
