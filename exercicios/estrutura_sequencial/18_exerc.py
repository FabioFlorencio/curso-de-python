'''
    Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), 
    calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
'''


def calcular_tempo_download(tamanho_arquivo_mb, velocidade_link_mbps):
    # Converter o tamanho do arquivo de MB para Megabits (megabits)
    tamanho_arquivo_mbits = tamanho_arquivo_mb * 8
    
    # Calcular o tempo de download em segundos
    tempo_segundos = tamanho_arquivo_mbits / velocidade_link_mbps
    
    # Converter o tempo de download de segundos para minutos
    tempo_minutos = tempo_segundos / 60
    
    return tempo_minutos

def main():
    tamanho_arquivo_mb = float(input("Digite o tamanho do arquivo para download (em MB): "))
    velocidade_link_mbps = float(input("Digite a velocidade do link de Internet (em Mbps): "))
    
    tempo_minutos = calcular_tempo_download(tamanho_arquivo_mb, velocidade_link_mbps)
    
    print(f"O tempo aproximado de download do arquivo é de {tempo_minutos:.2f} minutos.")

if __name__ == "__main__":
    main()


