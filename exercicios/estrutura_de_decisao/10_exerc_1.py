'''
    10 - Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
    Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
    
'''

turno = {
    'M': 'matutino',
    'V': 'Vespertino',
    'N': 'Noturno'
}

valida = True

msg = input('Em que turno você estuda? Digite M - matutino ou V - Vespertino ou N - Noturno: ')

msg_t = msg.upper()

# a comparação é feita pela chave
if msg_t in turno:
    print(f'Bom {turno[msg_t]}!')
else:
    for value in turno.values():        
        if msg_t == value.upper():
            print(f'Bom {value.capitalize()}!') 
            valida = False
            

if not valida:
    print(f'2 - O que vc digitou não é valido! Tente de novamente!')


    

  



    


    



    



