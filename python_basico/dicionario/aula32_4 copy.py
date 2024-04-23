'''

    Aula de mineração de dados
    Trata de dicionário
    Esse exemplo mostra uma opção de format nomeado

'''

dados_pessoa = {
    'nome': "Fábio",
    'idade': 41,
    'curso': 'Desenvolvimento de software multiplataforma'
}

texto = "Nome: {}, Idade: {}, curso: {}"

print(texto.format(dados_pessoa["nome"],dados_pessoa["idade"],dados_pessoa["curso"]))