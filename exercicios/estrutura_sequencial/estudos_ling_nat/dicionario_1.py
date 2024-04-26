comentarios = [
    {"Autor": "João", "Comentário": "Estou tão feliz hoje!", "Sentimento": "Positivo"},
    {"Autor": "Maria", "Comentário": "Este filme é tão triste.", "Sentimento": "Negativo"},
    {"Autor": "Carlos", "Comentário": "Que dia chuvoso entediante...", "Sentimento": "Positivo"},
    {"Autor": "Ana", "Comentário": "Adorei a nova música da banda!", "Sentimento": "Negativo"},
    {"Autor": "Roberto", "Comentário": "Eureka, consegui resolver este problema", "Sentimento": "Positivo"}
]

def contar_comentarios(comentarios):
    tot_negativos = 0
    tot_positivos = 0
    
    for comentario in comentarios:
        if comentario["Sentimento"] == "Negativo":
            tot_negativos += 1
        elif comentario["Sentimento"] == "Positivo":
            tot_positivos += 1
            
    return tot_negativos, tot_positivos

# calcular e mostrar na tela a proporção de cada sentimento em relação ao total de comentários

def proporcao_de_sentimentos(comentarios):
    tot_negativos, tot_positivos = contar_comentarios(comentarios)
    tot_comentarios = len(comentarios)
    proporcao_negativos = tot_negativos / tot_comentarios
    proporcao_positivos = tot_positivos / tot_comentarios
    print("Proporção de comentários negativos:", proporcao_negativos)
    print("Proporção de comentários positivos:", proporcao_positivos)

# Mostra somente comentários positivos
def mostrar_comentarios_positivos(comentarios):
    for comentario in comentarios:
        if comentario["Sentimento"] == "Positivo":
            print(comentario["Comentário"])

            
for comentario in comentarios:
    comentario["sentimento_valor"] = comentario["Sentimento"] == "Positivo"


print("Quantidade de comentários negativos e positivos:", contar_comentarios(comentarios))
proporcao_de_sentimentos(comentarios)
print("\nComentários positivos:")
mostrar_comentarios_positivos(comentarios)
print()
print(comentarios)

