'''
4 - Faça um Programa que peça as 4 notas bimestrais e mostre a média.

Outra forma de ser feito esse algoritimo

'''
media = 0

for i in range(4):
    num = float(input(f"Digite o {i+1}º números: "))
    media+= num / 4

print(f"A média das notas são: {media}")