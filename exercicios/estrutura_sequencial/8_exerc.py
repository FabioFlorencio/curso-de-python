'''
    Faça um Programa que pergunte quanto você ganha por hora e o
    número de horas trabalhadas no mês. Calcule e mostre o total do seu
    salário no referido mês.

'''

valor_hora = float(input(f'Informe o valor por hora da sua mão de obra: '))
horas_mes = float(input(f'Informe a quantidade de horas trabalhadas por mês: '))

salario_mes = valor_hora * horas_mes

print(f'O seu salário é: {salario_mes}')