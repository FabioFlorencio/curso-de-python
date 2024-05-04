# 🧠 Exercícios de Python 🐍

## Exercício retirado da 🏘️[comunidade python Brasil](https://wiki.python.org.br/EstruturaDeDecisao)

### 🚦 Lista de Estrutura de decisão

- `1️` - Faça um Programa que peça dois números e imprima o maior deles.
- `2` - Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo
- `3` - Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
- `4` - Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
  - Nesse exemplo foi usado o método `casefold` | não diferencia entre maiúsculas e minúsculas.
- `5` - Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média    alcançada por aluno e apresentar:
  - A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
  - A mensagem "Reprovado", se a média for menor do que sete;
  - A mensagem "Aprovado com Distinção", se a média for igual a dez.
- `6️` - Faça um Programa que leia três números e mostre o maior deles.
  - Nesse exemplo foi usado o `float('-inf') # Inicialize com o menor valor possível`
  - Nesse exemplo foi usado o `ternário`
- `7️` - Faça um Programa que leia três números e mostre o maior e o menor deles.
  - Nesse exemplo foi usado o `float('-inf') # Inicialize com o menor valor possível`
  - Nesse exemplo foi usado o `max() e min()` | Retorna o maior e o menor valor
- `8️` - Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
- `9️` - Faça um Programa que leia três números e mostre-os em ordem decrescente.
- `10` - Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
- `11` - As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
  - Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
  
    | Salários                                |    Aumento     | 
    |:----------------------------------------|:--------------:|
    | Salários até R$ 280,00                  |     de 20%     |   
    | Salários entre R$ 280,00 e R$ 700,00    |     de 15%     |
    | Salários entre R$ 280,00 e R$ 700,00    |     de 15%     |
    | Salários entre R$ 700,00 e R$ 1500,00   |     de 10%     |
    | Salários de R$ 1500,00 em diante        |     de 5%      |

  - Após o aumento ser realizado, informe na tela:
  - O salário antes do reajuste;
  - O percentual de aumento aplicado;
  - O valor do aumento;
  - O novo salário, após o aumento.
    -  Nesse exemplo foi usado `desempacotamento em chamada de função` e `função format` 
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
  
- `13` - Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
- `1️⃣4️⃣` Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:

  
  | 📊 Média de aproveitamento  | 📝 Conceito  |
  |:----------------------------|:-------------:|
  | Entre 9.0 e 10.0            |       A       |
  | Entre 7.5 e 9.0             |       B       |
  | Entre 6.0 e 7.5             |       C       |
  | Entre 4.0 e 6.0             |       D       |
  | Entre 4.0 e 0               |       E       |

- O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.
   
- 1️⃣5️⃣ Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
  - Dicas:
  - Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
  - Triângulo Equilátero: três lados iguais;
  - Triângulo Isósceles: quaisquer dois lados iguais;
  - Triângulo Escaleno: três lados diferentes; 
- 1️⃣6️⃣ Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
- 1️⃣7️⃣ Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.
- 1️⃣8️⃣ Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
- 1️⃣9️⃣ Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
  
`Observando os termos no plural a colocação do "e", da vírgula entre outros.`


#### Exemplo:

|   Número   | Centenas | Dezenas | Unidades |
|:----------:|:--------:|:-------:|:--------:|
|    326     |    3     |    2    |    6     |

---

|                |Testar com|          |
|:---------------|:--------:|:--------:|
|      326       |   300    |   100    |
|      320       |   310    |   305    |          
|      301       |   101    |   311    |          
|      111       |    25    |    20    |          
|      10        |    21    |    11    |          
|       1        |    7     |    16    |          

- 2️⃣0️ Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
A mensagem "Aprovado com Distinção", se a média for igual a 10.
- 2️⃣1️⃣ Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
  - A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
  - A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
  - A mensagem "Aprovado com Distinção", se a média for igual a 10.
- 2️⃣2️⃣ Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo (resto da divisão).
- 2️⃣3️⃣ Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.
- 2️⃣4️⃣ Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
  
    | Número|              | 
    |:----------|:---------|
    |    par    |  ímpar   |
    | positivo  | negativo |
    | inteiro   | decimal  |

- 2️⃣5️⃣ Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. 
  
  |      As perguntas são:       |
  |:----------------------------:|
  | "Telefonou para a vítima?"   |
  | "Esteve no local do crime?"  |
  | "Mora perto da vítima?"      |
  | "Devia para a vítima?"       |
  | "Já trabalhou com a vítima?" |

  -  O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a:
  
  |   Questões   |   classificação   |   
  |:------------:|:-----------------:|
  |      2       |   Suspeita        |
  | entre 3 e 4  |   Cúmplice        |
  |      5       |   Assassino       |

  `Caso contrário, ele será classificado como "Inocente"`
  
- 2️⃣6️⃣ Um posto está vendendo combustíveis com a seguinte tabela de descontos:
  
  |   Combustível   |    Litros       |   Desconto     |       Litros         |   Desconto     |
  |:---------------:|:---------------:|:--------------:|:--------------------:|:--------------:|
  |     Álcool      |  até 20 litros  |  3% por litro  |  acima de 20 litros  |  5% por litro  |
  |    Gasolina     |  até 20 litros  |  4% por litro  |  acima de 20 litros  |  6% por litro  |

  
  - Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
  
- 2️⃣7️⃣ Uma fruteira está vendendo frutas com a seguinte tabela de preços:
  
|  Até 5 kg              | Acima de 5 kg             |  
|-----------------------:|--------------------------:|
|Morango R$ 2,50 por Kg  |R$ 2,20 por Kg             |
|Maça R$ 1,80 por Kg     |R$ 1,50 por Kg             |

- 2️⃣8️⃣ O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
  
| Até 5 kg                            |       Acima de 5 kg         | 
|------------------------------------:|:---------------------------:|
|File Duplo             R$ 4,90 por Kg|     R$ 5,80 por Kg          |
|Alcatra                R$ 5,90 por Kg|     R$ 6,80 por Kg          |
|Picanha                R$ 6,90 por Kg|     R$ 7,80 por Kg          |

  - Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.



