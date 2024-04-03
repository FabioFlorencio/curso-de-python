'''

    12.Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

'''

alt = input(f'Digite sua altura: ')
peso_ideal = (72.7 * float(alt)) - 58

print('Seu peso ideal é %.2f Kg' %(peso_ideal))