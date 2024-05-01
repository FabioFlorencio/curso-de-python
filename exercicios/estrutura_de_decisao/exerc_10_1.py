'''
    10 - Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
    Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
    
'''

turno = {
    'M': 'matutino',
    'V': 'Vespertino',
    'N': 'Noturno'
}

msg = input('Em que turno você estuda? Digite M - matutino ou V - Vespertino ou N - Noturno: ')

msg_upper = msg.upper()

if msg_upper in turno:
    print(f'Bom {turno[msg_upper]}!')
else:
    for value in turno.values():
        if msg_upper == value.upper():
            print(f'Bom {value.capitalize()}!')
            break
    else:
        print('Valor Inválido!')

    

  



    


    



    



