a
def calcular_ir(base_calc,aliq_p_calc):

    ALIQ_7_perc = 7
    ALIQ_15_perc = 15
    ALIQ_22_perc = 22.5
    ALIQ_27_perc = 27.5

    ISENTO = 0
    REND_ISENTO = 21453.24
    REND_MIN_7_PERC = REND_ISENTO
    REND_MAX_7_PERC = 32151.48

    REND_MIN_15_PERC = 32151.49
    REND_MAX_15_PERC = 42869.16

    REND_MIN_22_PERC = 42869.17
    REND_MAX_22_PERC = 53565.72

    REND_ACIMA = REND_MAX_22_PERC

    # Isento
    if base_calc > REND_ISENTO: 
        # Rendimento acima de R$ 53.565.72
        if base_calc > REND_ACIMA: 
            deducao = (base_calc / 100) * ALIQ_27_perc
            aliq_p_calc = ALIQ_27_perc                        
        else:
            # Rendimento entre 21.453.24 a 32.151.48
            if base_calc >= REND_MIN_7_PERC and base_calc <= REND_MAX_7_PERC:
                deducao = (base_calc / 100) * ALIQ_7_perc
                aliq_p_calc = ALIQ_7_perc
            # Rendimento entre 32.151.49 a 42.869.16   
            elif base_calc >= REND_MIN_15_PERC and base_calc <= REND_MAX_15_PERC:
                deducao = (base_calc / 100) * ALIQ_15_perc
                aliq_p_calc = ALIQ_15_perc  
            # Rendimento 42.869.17 a 53.565.72                                 
            else:                        
                deducao = (base_calc / 100) * ALIQ_22_perc
                aliq_p_calc = ALIQ_22_perc                       
    else:
        deducao = 0
        aliq_p_calc = ISENTO   

    return deducao, aliq_p_calc 


base_calc = 21453.24
aliq_p_calc = 0
result_deducao,aliq_p_calc = calcular_ir(base_calc,aliq_p_calc)         

print('Dedução de R$%.2f com base da aliquota %.1f%%' %(result_deducao,aliq_p_calc))
