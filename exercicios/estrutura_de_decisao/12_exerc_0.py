'''
    Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda,
    que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do
    Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto
    menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas
    trabalhadas no mês.
        Desconto do IR:
        Salário Bruto até 900 (inclusive) - isento
        Salário Bruto até 1500 (inclusive) - desconto de 5%
        Salário Bruto até 2500 (inclusive) - desconto de 10%
        Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o
        exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.

'''

def calc_sal(sal_bruto):

    ISENTO = 0
    ALIQ_PERC_5 = 5
    ALIQ_PERC_10 = 10
    ALIQ_PERC_20 = 20
    SIND_PERC_3 = 3
    FGTS_PERC_11 = 11
    INSS_PERC_10 = 10
    aliq_aplicada = 0

    if sal_bruto > 900:
        if sal_bruto < 1500:
            aliq_aplicada = ALIQ_PERC_5
        elif sal_bruto < 2500:
           aliq_aplicada = ALIQ_PERC_10
        else:
          aliq_aplicada = ALIQ_PERC_20
    else:
        aliq_aplicada = ISENTO        

    calc_imposto = (sal_bruto / 100) * aliq_aplicada
    calc_sind = (sal_bruto / 100) * SIND_PERC_3
    calc_fgts = (sal_bruto / 100 ) * FGTS_PERC_11  
    calc_inss = (sal_bruto / 100) * INSS_PERC_10         
    tot_desc = calc_imposto + calc_sind + calc_inss
    sal_liquido = sal_bruto - tot_desc

    return sal_bruto, sal_liquido, tot_desc, calc_imposto, calc_inss, calc_sind, calc_fgts
  
sal_bruto = 900         
result = calc_sal(sal_bruto)

# Conte o return para compreender o parâmetro nomeado com índice
msg ='''
Salário bruto:       R${0:>7.2f}
(-)IR (5%):          R${3:>7.2f}
(-)INSS (10%):       R${4:>7.2f}
(-)Sindicato:        R${5:>7.2f}
FGTS (11%):          R${6:>7.2f}
Total de descontos:  R${2:>7.2f}
Salário Liquido:     R${1:>7.2f}
''' 

print(msg.format(*result))




