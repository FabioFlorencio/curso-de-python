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
    msg = ""
    media_notas = sum(notas_parcias) / len(notas_parcias)

    if media_notas >= 6 and media_notas <= 7.5:
        conceito = "A"
        msg = f'Notas:\t  {notas_parcias}.\nA média é: {media_notas:>2}.\nConceito: {conceito:>2}\nSituação:{conceito_nota[conceito]:>10}'        
        

    return msg


notas_parcias = []
i = 0
c = 2

while i < c:
    try:
        num = int(input(f'Digite o {i+1}° número:'))
        notas_parcias.append(num)
        i+= 1
    except ValueError:
        notas_parcias.clear()
        i = 0
        print('Você não digitou um número! Tente novamente!')   



teste = calcular_media_notas(notas_parcias)

print(teste)





