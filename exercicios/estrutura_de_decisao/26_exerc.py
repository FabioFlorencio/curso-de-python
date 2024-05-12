'''
    Um posto está vendendo combustíveis com a seguinte tabela de descontos:
    Álcool:
        até 20 litros, desconto de 3% por litro
        acima de 20 litros, desconto de 5% por litro
    Gasolina:
        até 20 litros, desconto de 4% por litro
        acima de 20 litros, desconto de 6% por litro 

    Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível
    (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a 
    ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

    *Sugestão seria utilizar esse exercício com dicionário*

'''
# álcool
# gasolina
# preco gas = R 2,50
# preco alc = R 1,90
# tipo_combus
# tot a ser pago



def calcular_desc(qtd_litros, tipo_comb):
    
    combus_alc = "Ácool"
    combus_gas = "Gasolina"

    PERC_ALC_3 = 3
    PERC_ALC_5 = 5
    PERC_GAS_4 = 4
    PERC_GAS_6 = 6

    valida_comb = combus_alc if combus_alc.lower() == tipo_comb.lower() else combus_gas

    if tipo_comb.lower() == combus_alc.lower():                
        perc_desc = PERC_ALC_3 if qtd_litros <= 20 else PERC_ALC_5                  
    else:
        perc_desc = PERC_GAS_4 if qtd_litros <= 20 else PERC_GAS_6

    return     
           
                     