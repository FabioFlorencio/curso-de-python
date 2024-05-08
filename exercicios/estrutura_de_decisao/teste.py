def obter_dia_semana(entrada):
    dia_semana = {
        "1": "Domingo",
        "2": "Segunda-feira",
        "3": "Terça-feira",
        "4": "Quarta-feira",
        "5": "Quinta-feira",
        "6": "Sexta-feira",
        "7": "Sábado"
    }

    try:
        if isinstance(entrada, (float, int)):  # Checa se a entrada é float ou int
            entrada = str(int(entrada))  # Converte para string e, se for float, trunca para int
        elif isinstance(entrada, str):
            entrada = entrada.lower()  # Convertendo entrada para minúsculas
        
        # Convertendo valores do dicionário para minúsculas para comparação
        dia_semana_lower = {k: v.lower() for k, v in dia_semana.items()}
        
        if entrada in dia_semana_lower.values():
            for key, value in dia_semana.items():
                if value.lower() == entrada:
                    return f"O dia correspondente à {entrada.capitalize()} é o {key}."
        else:
            return "Entrada inválida. Por favor, insira um número inteiro de 1 a 7 ou o nome de um dia da semana 666."

    except Exception as e:
        return f"Ocorreu um erro: {e}"

# Exemplos de uso:
entrada = input("Digite um número de 1 a 7 ou o nome de um dia da semana: ")

print(obter_dia_semana(entrada))
