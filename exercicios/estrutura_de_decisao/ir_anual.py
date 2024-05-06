# LINGUAGEM PYTHON

def calcular_ir(base_calc):

    ALIQ_7_PERC = 7
    ALIQ_15_PERC = 15
    ALIQ_22_PERC = 22.5
    ALIQ_27_PERC = 27.5

    ISENTO = 0
    REND_ISENTO = 21453.24
    REND_MAX_7 = 32151.48
    REND_MAX_15 = 42869.16
    REND_MAX_22 = 53565.72

    REND_ACIMA = REND_MAX_22

    if base_calc >= REND_ISENTO:          
        if base_calc <= REND_MAX_7: # de 21.453.24 a 32.151.48             
            aliq_p_calc = ALIQ_7_PERC                                              
        elif base_calc <= REND_MAX_15: # de 32.151.49 a 42.869.16             
            aliq_p_calc = ALIQ_15_PERC                                  
        elif base_calc <= REND_MAX_22: # de 42.869.17 a 53.565.72                
            aliq_p_calc = ALIQ_22_PERC                                                         
        else: # acima de R$ 53.565.72                                                     
            aliq_p_calc = ALIQ_27_PERC                       
    else: # Isento        
        deducao = 0
        aliq_p_calc = ISENTO   

    deducao = (base_calc / 100) * aliq_p_calc

    return deducao, aliq_p_calc 


base_calc =  53565.73
result_deducao = calcular_ir(base_calc)
msg = 'Dedução de R${:.2f} com base da aliquota {:.1f}' 

print(msg.format(*result_deducao))

