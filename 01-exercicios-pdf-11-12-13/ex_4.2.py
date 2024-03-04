'''

4 - Faça um Programa que peça as 4 notas bimestrais e mostre a média.

Outra forma de ser feito esse algoritimo

'''

vetor_notas = []
somar_notas = 0
media_notas = 0

for i in range(4):
    notas = float(input(f"Digite a {i+1}º nota:"))        
    vetor_notas.append(notas)
    somar_notas+= notas

media_notas = somar_notas / len(vetor_notas)

print(f"Todas as notas: {vetor_notas}")   
print(f"Média das notas: {media_notas:.2f}") 
