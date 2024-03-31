
# insert -> Adiciona um item no índice escolhido, conforme o parâmetro passado e realoca o elemento para próxima posição.     

lista = [10,20,30,40,'Fábio']

lista.append(50)

print('nova lista', lista)


# lista[0] = 1

#            |----------- Indica o índice
#            |
#            |   |------- O valor que será inserido na lista
lista.insert(0 , 4)


del lista[0]

print('Lista utilizando insert:',lista)



