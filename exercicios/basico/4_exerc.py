'''
    Faça um Programa que peça as 4 notas bimestrais e mostre a média.

'''

qtd_notas = 4 
notas = 0

for nota in range(qtd_notas):    
    notas+= float(input(f'Digite a {nota+1}° nota: '))
    media_notas = notas / qtd_notas

print(f'A média de notas é: {media_notas}')    


