
idade1 = 14
genero = "Homem"
valida_alistamento = False

if (valida_alistamento := (idade1 >= 16) & (genero == "Homem")):
    print("Vai ser analisado seu alistamento.")
    print('Retorne daqui 15 dias!')
else:
    print("Você não está apto ao alistamento.")


if valida_alistamento:
    print('Você foi convocado! Bem vindo ao exercito!')



