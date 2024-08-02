idade = 18
genero = "Homem"
valida_alistamento = False
msg_parts= []

if (valida_alistamento := (idade >= 16) & (genero.casefold() == "homem")):
    msg_parts.append("Vai ser analisado seu alistamento. Retorne daqui 15 dias!\n")    
else:
    msg_parts.append("Você não está apto ao alistamento.")    

if valida_alistamento:
    msg_parts.append('Você foi convocado! Bem vindo ao exercito!')    


msg = ''.join(msg_parts)
print(msg)



