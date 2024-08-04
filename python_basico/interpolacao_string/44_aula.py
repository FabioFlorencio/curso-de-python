# Definindo os valores

"""
{:<10}: Isso significa que o espaço reservado para o nome terá 10 caracteres de largura, e o nome será 
alinhado à esquerda dentro desse espaço.
{:>5}: Isso significa que o espaço reservado para a idade terá 5 caracteres de largura, e a idade será 
alinhada à direita dentro desse espaço.
{: .2f}: Isso significa que o espaço reservado para a altura será formatado como um número de ponto flutuante
com duas casas decimais.

"""
nome = "Alice"
idade = 25
altura = 1.65

# Interpolação com espaçamento controlado
mensagem = "Nome:{:<10}Idade:{:>10} Altura:{:>8.2f}".format(nome, idade, altura)
print(mensagem)
