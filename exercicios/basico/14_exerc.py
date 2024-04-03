'''
    14.João Papo-de-Pescador, homem de bem, comprou um
    microcomputador para controlar o rendimento diário de seu trabalho.
    Toda vez que ele traz um peso de peixes maior que o estabelecido
    pelo regulamento de pesca do estado de São Paulo (50 quilos) deve
    pagar uma multa de R$ 4,00 por quilo excedente. João precisa que
    você faça um programa que leia a variável peso (peso de peixes) e
    verifique se há excesso. Se houver, gravar na variável excesso e na
    variável multa o valor da multa que João deverá pagar. Caso contrário
    mostrar tais variáveis com o conteúdo ZERO.

'''

valida_peso = False
LIMITE_PESO = 50
MULTA = 4.00

peso = float(input('Informe o peso do peixe:'))

if valida_peso:= peso > LIMITE_PESO:
    excesso_kg = (peso - LIMITE_PESO)
    calc_multa = excesso_kg * MULTA
    print('O valor que deve ser pago pelo excesso é R$%.2f' %calc_multa)    
else:
    print('O peso está dentro do estabelecido pelo estado de São Paulo.')


    
