'''
Crie uma lista de dicionários para armazenar comentários e emoções conforme a tabela abaixo:
Faça uma rotina para totalizar a quantidade de comentários negativos e comentários positivos
Calcule e mostre na tela a proporção de cada sentimento em relação ao total de comentários
Faça uma rotina para mostrar apenas os comentários positivos
Adicione uma chave em cada dicionário chamado sentimento_valor que conterá 0 se o sentimento for negativo ou 1 se o sentimento for positivo

#! Autor         Comentário                                 Sentimento 

#! João        Estou tão feliz hoje!                         Positivo 
#! Maria       Este filme é tão triste.                      Negativo 
#! Carlos      Que dia chuvoso entediante...                 Positivo 
#! Ana         Adorei a nova música da banda!                Negativo 
#! Roberto     Eureka, consegui resolver este problema       Positivo 

'''

import numpy as np
                                                                                          
comentarios = [
                        {'Autor':'João','Comentário':'Estou tão feliz hoje!','Sentimento':'Positivo'},
                        {'Autor':'Maria','Comentário':'Este filme é tão triste.','Sentimento':'Negativo'},
                        {'Autor':'Carlos','Comentário':'Que dia chuvoso entediante...','Sentimento':'Positivo'},
                        {'Autor':'Ana','Comentário':'Adorei a nova música da banda!','Sentimento':'Negativo'},
                        {'Autor':'Roberto','Comentário':'Eureka, consegui resolver este problema','Sentimento':'Positivo'}
                    ]


def calc_sentimentos(comentarios):
    cont_sent_neg = 0
    cont_sent_pos = 0

    for comentario in comentarios:
        if comentario['Sentimento'] == 'Positivo':
            cont_sent_neg+= 1
        else:
            cont_sent_pos+= 1 

    return cont_sent_neg, cont_sent_pos


tot_sent_neg, tot_sent_pos = calc_sentimentos(comentarios)    



def comentarios_pos(comentarios):
    guarda_sent_pos = ""

    for comentario in comentarios:
        if comentario['Sentimento'] == 'Positivo':
            print(f'{comentario['Comentário']}')
    return guarda_sent_pos


tot_sentimento_positivo = comentarios_pos(comentarios)

print(tot_sentimento_positivo)


for comentario in comentarios:
    comentario["Sentimento_valor"] = 1 if comentario["Sentimento"] == "Positivo" else 0


print(comentarios)    
print(comentarios_pos(comentarios))
