'''

4 - Faça um Programa que peça as 4 notas bimestrais e mostre a média.

Outra forma de ser feito esse algoritimo

'''

vetor_notas = []
somar_notas = 0
media_notas = 0

for i in range(4): 
    notas = float(input("Digite o valor da nota:"))
    vetor_notas.append(notas)
    somar_notas+= vetor_notas[i]

media_notas += somar_notas / len(vetor_notas)    


for i in range(len(vetor_notas)):
    print(f"Todas as notas: {vetor_notas[i]}")


print(f"\nSoma de todas as notas: {somar_notas}")    
print(f"Média das notas: {media_notas}")

