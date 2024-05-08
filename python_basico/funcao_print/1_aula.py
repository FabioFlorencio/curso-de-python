
# No print tem argumentos não nomeados
# Por padrão o print já quebra uma linha
# Pode se utilizar aspas simples, aspas duplas ou até caracter como separador

#     |-------------------- Argumento não nomeado
#     |   |---------------- Argumento não nomeado
#     |   |   |------------ Argumento nomeado
#     |   |   |   |-------- Coloca o hifen entre os números
print(10,12,14,sep= "-", end="\n\n##")
print(56,78, sep="**\n\n")
print(20,30, sep="|", end="##")