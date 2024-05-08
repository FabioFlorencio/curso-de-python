def dia_da_semana(entrada):
    dia_semana = {
        "1": "Domingo",
        "2": "Segunda-feira",
        "3": "Terça-feira",
        "4": "Quarta-feira",
        "5": "Quinta-feira",
        "6": "Sexta-feira",
        "7": "Sábado"
    }

    valida = True

    if entrada.isdigit():        
        if entrada in dia_semana.keys():
            entrada = f'{dia_semana[entrada]}'        
        else:
            entrada = f'1 - O que vc digitou não é valido! Tente de novamente!'   
    else:
        for value in dia_semana.values():
            if entrada == value:
                entrada = f'{value.capitalize()}'
                valida = False

        if valida:
            entrada = f'2 - O que vc digitou não é valido! Tente de novamente!'
            
    return entrada    


entrada = input('Digite um número:')

print(dia_da_semana(entrada))