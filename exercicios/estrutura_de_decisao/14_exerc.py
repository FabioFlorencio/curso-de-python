"""

    14 - Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre,
    e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:

"""

def calcular_media_notas(notas_parcias):

    conceito_nota = {
    'A' : 'APROVADO',
    'B' : 'APROVADO',
    'C' : 'APROVADO',
    'D' : 'REPROVADO',
    'E' : 'REPROVADO'
}
    
    media_notas = sum(notas_parcias) / len(notas_parcias)

    if media_notas > 9:
        conceito = "A"
    elif media_notas > 7.5:    
        conceito = "B"
    elif media_notas > 6:    
        conceito = "C" 
    elif media_notas > 4:   
        conceito = "D"
    else:
        conceito = "E"    
           
    return notas_parcias, media_notas, conceito, conceito_nota[conceito]    


notas_parcias = []
i = 0
c = 2

while i < c:
    try:
        num = float(input(f'Digite o {i+1}° número:'))
        notas_parcias.append(num)
        i+= 1
    except ValueError:
        notas_parcias.clear()
        i = 0
        print('Você não digitou um número! Tente novamente!')   


result = calcular_media_notas(notas_parcias)

msg = '''
Notas:\t  {}.
A média é: {:.2f}.
Conceito: {:>2}.
Situação:{:>10}
'''

print(msg.format(*result))





