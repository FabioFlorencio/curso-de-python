def calcular_ir(base_calc):
    ALIQ_7 = 7
    ALIQ_15 = 15
    ALIQ_22 = 22.5
    ALIQ_27 = 27.5

    REND_ISENTO = (0, 21453.24)
    REND_MIN_7_PERC = (21453.25, 32151.48)
    REND_MAX_7_PERC = (32151.49, 42869.16)
    REND_MIN_15_PERC = (42869.17, 53565.72)
    REND_MAX_15_PERC = (53565.73, float('inf'))

    if base_calc > REND_ISENTO[1]:
        if base_calc > REND_MAX_15_PERC[0]:
            deducao = (base_calc / 100) * ALIQ_27            
        else:
            if REND_MIN_7_PERC[0] <= base_calc <= REND_MAX_7_PERC[1]:
                deducao = (base_calc / 100) * ALIQ_7
                print('Rendimento 7')
            elif REND_MIN_15_PERC[0] <= base_calc <= REND_MAX_15_PERC[1]:
                deducao = (base_calc / 100) * ALIQ_15
                print('Rendimento 15')                
            else:                        
                deducao = (base_calc / 100) * ALIQ_22
                print('Rendimento 22')                       
    else:
        print('Isento.')
        deducao = 0

    return deducao

base_calc = 22000

print(calcular_ir(base_calc))
