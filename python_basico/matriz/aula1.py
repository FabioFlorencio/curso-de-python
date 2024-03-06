# cfb cursos 

carros=[
        #--coluna 0 | coluna 1   
        ["Modelo",      "HRV"],#------- Linha 0
        ["Fabricante","Honda"],#------- Linha 1
        ["Ano",        2016]#-------- Linha 2
    ]

print('Linha 0:','Coluna:0',carros[0][0])
print('Linha 0:','Coluna:1',carros[0][1])
print()
print('Linha 1:','Coluna:0',carros[1][0])
print('Linha 1:','Coluna:1',carros[1][1])
print()
print('Linha 2:','Coluna:0',carros[2][0])
print('Linha 2:','Coluna:1',carros[2][1])
print()

for l,c in carros:
    print(f'Linha:{l}\v\t\t Coluna:{c}')
    
