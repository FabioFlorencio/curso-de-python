from collections import Counter

# Texto com pelo menos 3 linhas, palavras separadas por vírgula
texto = """
python,java,c,python
python,ruby,java,c++
programming,language,coding,python
"""

# Convertendo o texto em uma lista de palavras
palavras = [palavra.strip() for linha in texto.split('\n') for palavra in linha.split(',')]

# Filtrando palavras vazias
palavras = [palavra for palavra in palavras if palavra]

# Contando a quantidade de palavras
quantidade_palavras = len(palavras)

# Criando um dicionário com a contagem de cada palavra
contagem_palavras = dict(Counter(palavras))

print("Texto:")
print(texto)
print("Quantidade de palavras:", quantidade_palavras)
print("Contagem de cada palavra:")
print(contagem_palavras)
