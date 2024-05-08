'''
    Aula 44 - Interpolação básica de strings
    Interpolação algo próximo de placeholders
    s - string
    d e i - int
    f - float
    x e X - Hexadecimal (ABCDEF0123456789)

'''

nome = 'Fábio'
preco = 1000.95897643

# Interpolação de uma única variável não precisa de parênteses
usando_interpolacao_1 = '%s, quanto que custa o valor do saber? ' %nome

# Interpolação usando mais de uma variável
usando_interpolacao_2 = '%s, o preço é R$%.2f' %(nome, preco)

print(usando_interpolacao_1)
print(usando_interpolacao_2)

print('O hexadecimal de %d é %x' % (15,15))
print('O hexadecimal de %d é %06x' % (15,15))
print('O hexadecimal de %d,%d,%i é %02x %02x %02x' % (255,70,30,255,70,30))
print('O hexadecimal de %d,%d,%i é %02X %02X %02X' % (255,70,30,255,70,30))


