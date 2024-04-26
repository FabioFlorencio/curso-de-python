'''
    15.Faça um Programa que pergunte quanto você ganha por hora e o
    número de horas trabalhadas no mês. Calcule e mostre o total do seu
    salário no referido mês, sabendo-se que são descontados 11% para o
    Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um
    programa que nos dê:
    . salário bruto.
    a. quanto pagou ao INSS.
    b. quanto pagou ao sindicato.
    c. o salário líquido.
    d. calcule os descontos e o salário líquido, conforme a tabela abaixo:
'''

valor_hora = float(input(f'Informe o valor por hora da sua mão de obra: '))
horas_mes = float(input(f'Informe a quantidade de horas trabalhadas por mês:'))


sal_bruto = valor_hora * horas_mes
imposto_renda = (sal_bruto / 100) * 11
INSS = (sal_bruto / 100 ) * 8
imposto_sind = (sal_bruto / 100) * 5
tot_desc =  imposto_renda + imposto_sind + INSS 

print('\n+ Salário Bruto: \t R$%.2f' %(sal_bruto))
print('- IR (11%%) : \t\t R$%.2f' %(imposto_renda))
print('- INSS (8%%) : \t\t R$%.2f' %(INSS))
print('- Sindicato(5%%): \t R$%.2f' %(imposto_sind))
print('- Salário Liquido: \t R$%.2f' %(sal_bruto - tot_desc))