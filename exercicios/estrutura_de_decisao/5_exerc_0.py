'''
    5 - Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
        A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
        A mensagem "Reprovado", se a média for menor do que sete;
        A mensagem "Aprovado com Distinção", se a média for igual a dez.

'''

notas_parciais = []
qtd_notas = 2
media_nota = 0
msg = ""

for i in range(qtd_notas):
    notas_parciais.append(float(input(f'Digite a {i+1}° nota: ')))        
    media_nota+= notas_parciais[i] / qtd_notas


def avaliar_aprovacao(media_nota,msg):        
    if media_nota >= 7:        
        msg+= "Aprovado"   

        if media_nota == 10:
            msg+= " com Distinção"                 
    else:
        msg = "Reprovado"
               

    return f'O aluno foi {msg}, com média {media_nota:.2f} .' 


print(avaliar_aprovacao(media_nota,msg))

    



    



