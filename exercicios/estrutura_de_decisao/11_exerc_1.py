'''
    11 - As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o 
        programa que calculará os reajustes.
        Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, 
        baseado no salário atual:
        salários até R$ 280,00 (incluindo) : aumento de 20%
        salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
        salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
        salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
        o salário antes do reajuste;
        o percentual de aumento aplicado;
        o valor do aumento;
        o novo salário, após o aumento.

'''

def reajustar_salario(sal_ant):
    
    PERC_20 = 20
    PERC_15 = 15
    PERC_10 = 10
    PERC_5 = 5
    
    if sal_ant <= 280:
        perc_aumento = PERC_20
    elif sal_ant <= 700:
        perc_aumento = PERC_15
    elif sal_ant <= 1500:
        perc_aumento = PERC_10
    else:
        perc_aumento = PERC_5

    valor_aumento = (sal_ant / 100) * perc_aumento
    sal_atual = sal_ant + valor_aumento

    return sal_ant, sal_atual, perc_aumento, valor_aumento

# A função retorna uma tupla com os valores da função
result = reajustar_salario(2800)
msg = 'Salário antigo: R${:.2f} | Salário atual: R${:.2f} | percentual: {}% | valor do aumento:R${:.2f}'

print(msg.format(*result))






  



    


    



    



