import numpy as np


numeros_alunos = int(input("Informe o número de alunos : "))
numeros_secoes = int(input("Informe o número de seções para avaliação: "))

while True:
    pesos = input("Informe os pesos das seções separados por vírgula (Exemplo: 2,3,5 = 10): ").split(',')
    pesos = np.array(pesos, dtype=float)
    if np.sum(pesos) == 10.0:
        break
    else:
        print("A soma dos pesos deve ser igual a 10.0. Tente novamente!.")

notas = []


for i in range(numeros_alunos):
    notas_dos_aluno = input(f"Notas do Aluno {i+1}: ").split(',')
    notas_dos_aluno = np.array(notas_dos_aluno, dtype=float)
    notas.append(notas_dos_aluno)

notas = np.array(notas)

pontuacoes_finais = np.dot(notas, pesos)


print("\nPontuações dos alunos:")
for i, pontuacao in enumerate(pontuacoes_finais):
    print(f"Aluno {i+1}: {pontuacao:.2f}")

