'''    
    Desafio 87 - Execício:

    a) Soma de todos os valores pares digitados.
    b) Soma dos valores da terceira coluna.
    c) O maior valor da segunda linha.
'''    

matriz = [[0,0,0],[0,0,0],[0,0,0]]

soma_pares = soma_terc_coluna = maior_valor_seg_linha = 0
v_col_fixo = linha_2 = 2

#matriz = [[]]

for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor: [{l},{c}:]'))        
        if matriz[l][c] % 2 == 0:   
            soma_pares+= matriz[l][c]
        if linha_2 == l:
            if maior_valor_seg_linha < matriz[l][c]:
                maior_valor_seg_linha = matriz[l][c]

for l in range(0,3):            
    soma_terc_coluna+= matriz[l][v_col_fixo]

print('-=' * 30)    

for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()  

print(f'Total valores de pares:{soma_pares}')
print(f'Maior valor da segunda linha:{maior_valor_seg_linha}')
print(f'Total valores da terceira coluna:{soma_terc_coluna}')













