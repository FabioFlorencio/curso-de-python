import re

# Texto inicial com 20 palavras e os caracteres especiais
texto = "Olá, este é um texto! Com $ caracteres? Diversos %"

# Substituições a serem feitas
substituicoes = {
    ',': '\\n',
    '!': '\\t',
    '$': '\\v',
    '?': '\\r',
    '%': '\\n'
}

# Função para aplicar as substituições
def substituir_caracteres(texto, substituicoes):
    # Monta o padrão de busca com os caracteres a substituir
    padrao = re.compile('|'.join(re.escape(ch) for ch in substituicoes.keys()))
    
    # Função de substituição
    def substituir(match):
        return substituicoes[match.group(0)]
    
    # Aplica a substituição no texto
    novo_texto = padrao.sub(substituir, texto)
    
    return novo_texto

# Aplica as substituições no texto
texto_alterado = substituir_caracteres(texto, substituicoes)

# Imprime o texto alterado
print(texto_alterado)
