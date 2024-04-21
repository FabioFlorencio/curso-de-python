import numpy as np

dados_meteorologicos = [
    25, 26, 27, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12
    ]


temp_media_anual = np.mean(dados_meteorologicos)
temp_max = np.max(dados_meteorologicos)
temp_min = np.min(dados_meteorologicos)
desvio_padrao = np.std(dados_meteorologicos)


print(f"Temperatura média anual: {temp_media_anual}")
print(f'Temperatura máxima registrada: {temp_max}')
print(f'Temperatura mínima registrada: {temp_min}')
print(f'Desvio padrão da temperatura: {desvio_padrao:.4f}')

