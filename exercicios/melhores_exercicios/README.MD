# 🧠 Exercícios de Python 🐍

## Exercício retirado da 🏘️[comunidade python Brasil](https://wiki.python.org.br/ListaDeExercicios)

### 🚦 Lista de Estrutura de decisão


- 4️⃣ Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
  - Nesse exemplo foi usado o método `casefold` | não diferencia entre maiúsculas e minúsculas.
- 5️⃣ Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média    alcançada por aluno e apresentar:
  - A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
  - A mensagem "Reprovado", se a média for menor do que sete;
  - A mensagem "Aprovado com Distinção", se a média for igual a dez.
- 6️⃣ Faça um Programa que leia três números e mostre o maior deles.
  - Nesse exemplo foi usado o `float('-inf') # Inicialize com o menor valor possível`
  - Nesse exemplo foi usado o `ternário`
- 7️⃣ Faça um Programa que leia três números e mostre o maior e o menor deles.
  - Nesse exemplo foi usado o `float('-inf') # Inicialize com o menor valor possível`
  - Nesse exemplo foi usado o `max() e min()` | Retorna o maior e o menor valor
- 1️⃣1️⃣ As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
  - Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
  - Salários até R$ 280,00 (incluindo) : aumento de 20%
  - Salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
  - Salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
  - Salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
  - O salário antes do reajuste;
  - O percentual de aumento aplicado;
  - O valor do aumento;
  - O novo salário, após o aumento.
- `12` - Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
  - Salário Bruto até 900 (inclusive) - isento
  - Salário Bruto até 1500 (inclusive) - desconto de 5%
  - Salário Bruto até 2500 (inclusive) - desconto de 10%
  - Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
  
  - | Salário Bruto: (5 * 220)  |   R$ 1100,00      |
    |:--------------------------|:------------------|
    |(-) IR (5%)                |    R$ 55,00       |
    |(-) INSS (10%)             |    R$ 110,00      |
    |FGTS (11%)                 |    R$ 121,00      |
    |Total de descontos         |    R$ 165,00      |
    |Salário Liquido            |    R$ 935,00      |

  - Nesse exemplo foi usado `desempacotamento em chamada de função`, `função format`, `parâmetro nomeado com índice` e `interpolação com espaçamento controlado` 
  
- `10` - Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.   