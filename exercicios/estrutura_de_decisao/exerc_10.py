'''
    10 - Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
    Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
    
'''

turno = {
    'M': 'matutino',
    'V': 'Vespertino',
    'N': 'Noturno'
}


msg = input(f'Em que turno você estuda? Digite M - matutino ou V - Vespertino ou N - Noturno: ')
msg.casefold()

if msg in turno:
    print(turno[msg])

  



    


    



    



