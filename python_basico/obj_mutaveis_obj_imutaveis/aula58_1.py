'''
    Aula 58 -  tipos built-in, documentação, tipo imutáveis


    Objetos imutáveis
    strings, tuplas, int, float, bool
'''
s = "Olá"
print(f'{s}{id(s):^27}')  # Identificador do objeto original

s += " mundo"          # Resultado: Olá mundo
print(s , id(s),'\n')  # Novo identificador, um novo objeto foi criado

# Objetos mutáveis

lista = [1, 2, 3]
print(id(lista))  # Identificador do objeto original

lista.append(4)
print(lista)      # Resultado: [1, 2, 3, 4]
print(id(lista))  # Mesmo identificador, o objeto original foi modificado


