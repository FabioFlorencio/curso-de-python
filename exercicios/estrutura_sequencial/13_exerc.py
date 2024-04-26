'''

    13.Tendo como dados de entrada a altura e o sexo de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
        (h = altura)
        . Para homens: (72.7*h) - 58
        a. Para mulheres: (62.1*h) - 44.7 
        b. Peça o peso da pessoa e informe se ela está dentro, acima ou abaixo do peso.

'''

valida_genero = False

alt = float(input(f'Informe sua altura: '))
genero = input(f'Informe o seu sexo(Homem | Mulher): ')


if valida_genero := (genero == 'Homem') or (genero == 'Mulher'):
    if genero == 'Homem':
        peso_ideal = (72.7 * alt) - 58    
    else:     
        peso_ideal = (62.1 * alt) - 44.7

    msg = 'Seu peso ideal é %.2f Kg' %peso_ideal
    print(msg)
else:
    print('Você não escolheu as opções informadas! Tente novamente!')    
    

    