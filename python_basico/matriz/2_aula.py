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

# usando append em uma matriz

carros.append(["Cor","Prata"])

linha = 0
pos = 0
elemento = "teste"  

carros[linha].insert(pos,elemento)

for l,c in carros:
    print(f'Linha:{l}\v\t\t Coluna:{c}')
    
