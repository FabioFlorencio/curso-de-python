
# exemplo de retorno de dois parâmetros usando dicionário


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

print(f'Total de sentimento positivo:{tot_sent_pos}')
print(f'Total de sentimento negativo:{tot_sent_neg}')