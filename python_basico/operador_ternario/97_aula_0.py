'''
    Aula 97 - Operação ternária com Python (if e else de uma linha)

'''

valida_tern = 10 == 10

print('Valor' if True else 'Outro valor')
print('Verdadeiro' if valida_tern else 'Falso')


digito = 7
novo_digito = digito if digito <= 9 else 0


dig = 1
# Leia a sentença na sequência para facilitar o entendimento
# novo_dig é igual a zero | se dig for maior que 9 é 0 senão é dig
novo_dig = 0 if dig > 9 else dig



print(f'{novo_digito = }')
