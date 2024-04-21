'''

    Aula 88 - Tipo de tuple(tuplas)
    
    tipo tupla - Uma lista imutável
    Seria uma lista que não vai ser removido ou adicionado valor, que se mantém estática.
    Exemplo: lista de cidades, estados
    Obs. Tupla são mais eficientes e rápidas

    Nesse exemplo seria uma alternativa para alterar uma tupla

'''

tupla_carros = ("HRV","Golf","Argo")
lista_carros = list(tupla_carros)


lista_carros[2] = "Fusca"
lista_carros.append("Brasilia")
tupla_carros = tuple(lista_carros)



print(tupla_carros)
print(len(tupla_carros))





