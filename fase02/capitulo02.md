<div id="fase02" align="center">
<h1>FASE 2 - PROTOTYPING</h1>
<h2>Capítulo 02: Quando a máquina começa a tomar decisões. 🤔</h2>
</div>

<div align="center">

## Introdução! 

</div>

## Variável

### O que são variáveis?

São espaços utilizados na memória RAM para armazenar temporariamente alguma informação que os algoritmos utilizam.

São dados temporários, importantes para a solução.

### Tipos de variáveis:

Nos fluxogramas e pseudocódigos, a indicação do tipo de uma variável é feita no momento de sua criação, como ocorre na maior parte das linguagens de programação.

> Exemplo no script [tipos_variaveis.py](./scripts/scripts-cap02/tipos_variaveis.py)

<div align="center">

Tipos básicos | Descrição | Exemplos
--------------|-----------|------------
int | Número inteiro | 1, 20, 1000
float | Números reais (ponto flutuante) | 7.5, 2.07, 50.29
complex | Números complexos | 4j, 5+2j, 15j
bool | Valores lógicos | True, False, 1, 0
string (str) | Textos | "Bom dia", "x", "12", "f5"

</div>

### Importante:

1. O `comando type()` permite identificar o tipo de uma variável.

2. Para ***converter uma variável de um tipo para outro***, chamar o tipo para o qual gostaríamos de converter, como no exemplo:

~~~python
variavel_float = 5.2
print(variavel_float)
# resultado = 5.2

variavel_int = int(variavel_float)
print(variavel_int)
# resultado = 5
~~~

--- 

<div align="center">

## Desvio condicional

</div>

## O que é um Desvio Condicional? `if`

Estrutura que permite realizar um teste lógico e executar alguma ação, dependendo do resultado do teste. Ou seja, o algoritmo realizará um desvio na sua execução com base em uma condição!

1. `Desvio condicional simples`: apresenta um desvio apenas, se a condição testada for verdadeira; caso contrário, o programa segue o fluxo normal.

2. `Desvio condicional composto`: capaz de realizar uma ação para o caso de a condição ser verdadeira, e outra ação para o caso de a condição ser falsa.

3. `Desvio condicional encadeado`: dependendo do resultado de uma condição, permite a realização de um segundo teste.

## If simples em Python

### Exemplo:

"A FIAP está propondo a formação de um time de Esportes para representar a instituição e, para isso, realizará um campeonato interno no qual os alunos podem se inscrever. Porém, há uma condição: só podem ser inscritos alunos que são maiores de idade."

1. Algoritmo:

~~~
variáveis
  idade: inteiro
  rm: alfanumérico
início
  Escreva “Por favor, digite seu RM”
  Leia rm
  Escreva “Por favor, digite sua idade”
  Leia idade
  Se idade >=18 então
    Escreva “Sua participação foi autorizada, aluno de RM”, rm
      Escreva “Mais instruções serão enviadas ao seu e-mail cadastrado na FIAP!”
  Fim_se
Fim
~~~

2. Sintaxe da estrutura condicional simples em Python:

~~~python
if <condição>:
  <ação a ser realizada se a condição for verdadeira>
~~~

3. Estrutura condicional simples em Python: arquivo [exemplo_if_simples.py](./scripts/scripts-cap02/exemplo_if_simples.py).

Há ainda um segundo exemplo, que pode ser conferido [aqui](./scripts/scripts-cap02/exemplo_if_simples_2.py)

---

## If composto em Python

### Exemplo:

Considerando o exemplo anterior, podemos exibir também uma mensagem para os alunos menores de idade.

1. Algoritmo:

~~~
variáveis
  idade: inteiro
  rm: alfanumérico
início
  Escreva “Por favor, digite seu RM”
  Leia rm
  Escreva “Por favor, digite sua idade”
  Leia idade
  Se idade >=18 então
    Escreva “Sua participação foi autorizada, aluno de RM”, rm
      Escreva “Mais instruções serão enviadas ao seu e-mail cadastrado na FIAP!”
  Senão
    Escreva “Sua participação não foi autorizada por causa da sua idade”
  Fim_se
Fim
~~~

2. Sintaxe do desvio condicional composto em Python:

~~~python
if <condição>:
  <ação a ser realizada se a condição for verdadeira>
else:
  <ação a ser realizada se a condição for falsa>
~~~

3. Desvio condicional composto em Python: arquivo [exemplo_if_composto.py](./scripts/scripts-cap02/exemplo_if_composto.py).

---

## If encadeado em Python

Consiste na aplicação de um if dentro de outro.

### Exemplo:

Dado o elevado número de alunos com menos de 18 anos interessados em se inscrever no campeonato, a FIAP resolveu abrir vagas para aqueles que possuam autorização escrita dos responsáveis. Portanto:

1. Pseudocódigo:

~~~
variáveis
  idade: inteiro
  rm: alfanumérico
  autorizado: caractere
início
  Escreva “Por favor, digite seu nome”
  Leia rm
  Escreva “Por favor, digite sua idade”
  Leia idade
  Se idade >=18 então
    Escreva “Sua participação foi autorizada, aluno de RM”, rm
    Escreva “Mais instruções serão enviadas ao seu e-mail cadastrado na FIAP!”
  Senão
    Escreva “Você possui autorização dos responsáveis para participar? S – SIM ou N – NÃO”
      Leia autorizado
      Se autorizado = “S” então
        Escreva “Sua participação foi autorizada, aluno de RM”, rm
        Escreva “Mais instruções serão enviadas ao email dos seus responsáveis”
      Senão
        Escreva “Sua participação não foi autorizada por causa da sua idade”
      Fim_se
  Fim_se
Fim
~~~

2. O script contendo a codificação em Python, utilizando if encadeado, encontra-se no arquivo [exemplo_if_encadeado.py](./scripts/scripts-cap02/exemplo_if_encadeado.py).

---

## Python e o poder do `elif`

Utilizado caso seja necessário testar uma série de condições em sequência.

O elif serve como substituto do bloco else, quando queremos realizar uma nova verificação de condição dentro do senão. 

### Exemplo:

Uma operadora de celular concede bônus em consumo da franquia de internet, dependendo da pontuação dos clientes: 
- clientes que fizerem mais de 1000 pontos recebem 3GB adicionais em sua franquia.
- clientes que fizerem mais de 500 pontos recebem 1,5GB adicionais em sua franquia.
- clientes que fizerem mais de 200 pontos recebem 500MB adicionais em sua franquia. 
- Os demais não recebem nada.

A aplicação do elif na codificação Python pode ser verificada no arquivo [exemplo_elif.py](./scripts/scripts-cap02/exemplo_elif.py).

---


<div align="center">

## Operando a lógica

</div>

## Operador lógico `OR`

É a conexão entre dois testes lógicos, e retornará verdadeiro caso qualquer um dos testes seja verdadeiro.

<div align="center">

A | B | A or B
--|---|--------
False | False | False
False | True | True
True | False | True
True | True | True

</div>

## Operador lógico `AND`

É a conexão entre dois testes lógicos, e retornará verdadeiro apenas se ambos os testes retornarem verdadeiro!

<div align="center">

A | B | A and B
--|---|--------
False | False | False
False | True | False
True | False | False
True | True | True

</div>

## Importante:

O Python tem uma característica especial que não está presente na maior parte das outras linguagens de programação. Ele permite a avaliação de condições em cadeia. 

---

<div align="center">

## Hora da prática:

</div>

## Exemplo 1:

"O doutor Henry Jones Junior estabeleceu uma regra com seus alunos da disciplina de Arqueologia: todos os que obtiverem nota maior do que 8,5 na sua prova semestral serão convidados para uma visita de campo na América do Sul. Nosso programa deve solicitar o e-mail e a nota do aluno, exibindo a mensagem “ENVIANDO CONVITE” caso a nota do aluno satisfaça a condição proposta."

### Solução:

A resolução, utilizando if simples, pode ser conferida [aqui](./scripts/scripts-cap02/exemplo1.py).

## Exemplo 2:

"A loja virtual FIAP Wear, que vende roupas personalizadas da instituição, disponibilizou no mês do seu aniversário o cupom NIVER10,que concede 10% de desconto no valor total de uma compra feita no site. Caso o cliente digite o cupom corretamente, deverá ser informado do valor final da compra já com o desconto aplicado. Caso digite o cupom de maneira incorreta, deverá ser informado do valor da compra sem o desconto."

### Solução:

A resolução, utilizando if composto, pode ser conferida [aqui](./scripts/scripts-cap02/exemplo2.py).

## Exemplo 3:

Transporte-se no tempo e volte para a época de escola! Lembra do dia em que aprendeu a encontrar o valor de X nas equações de 2º grau? Aquelas que tinham uma carinha parecida com Ax² + Bx + C = 0? Vamos criar um programa no qual o usuário só tenha que escrever os valores de A, B e C, e o programa vai se encarregar de fazer os cálculos.

### Solução:

A resolução pode ser conferida [aqui](./scripts/scripts-cap02/exemplo1.py).

### Observação:

cada linguagem de programação possui sua função própria para realizar a operação de raiz quadrada. No caso do Python, precisamos importar a classe math, e depois usar a função math.sqrt. Para importar a classe math, escrevemos na primeira linha do nosso script: import math. Para calcular a raiz de algum valor depois de importarmos a classe math, devemos escrever math.sqrt(valor).

---

<div align="center">

## Hora de treinar:

</div>

## Exercício 1:

"Verificar se os batimentos cardíacos por minuto se encontram na faixa adequada. Para isso, você deve solicitar ao usuário que informe o seu número de BATIMENTOS POR MINUTO (BPM) e a IDADE. A partir disso,o script deve verificar e exibir uma mensagem informando se os batimentos do usuário encontram-se DENTRO da faixa adequada, ACIMA da faixa adequada ou ABAIXO da faixa adequada, de acordo com o site Tua Saúde.

<div align="center">

Idade | BPM
-------|-----
Até 2 anos | 120 a 140
De 8 a 17 anos | 80 a 100
Adulto sedentário | 70 a 80
Idoso | 50 a 60

</div>

Resolucão [aqui](./scripts/scripts-cap02/exercicio1.py).

## Exercício 2:

Uma agência de viagens está propondo uma estratégia para alavancar as vendas após os impactos da pandemia do coronavírus. A empresa ofertará descontos progressivos na compra de pacotes, dependendo do número de viajantes que estão no mesmo grupo e moram na mesma residência. Para ajudar a tornar esse projeto real, você deve criar um algoritmo que receba o VALOR BRUTO do pacote, a CATEGORIA DOS ASSENTOS no voo e a QUANTIDADE DE VIAJANTES que moram em uma mesma casa e calcule os descontos de acordo com a tabela abaixo:

<div align="center">

Categoria | Descontos
-------|-----
Econômica | 2 viajantes = 3%
&#32; | 3 viajantes = 4%
&#32; | 4 viajantes ou mais = 5%
Executiva | 2 viajantes = 5%
&#32; | 3 viajantes = 7%
&#32; | 4 viajantes ou mais = 8%
Primeira classe | 2 viajantes = 10%
&#32; | 3 viajantes = 15%
&#32; | 4 viajantes ou mais = 20%

</div>

O programa deverá exibir o valor BRUTO DA VIAGEM (o mesmo que foi digitado), o VALOR DO DESCONTO, o VALOR LÍQUIDO DA VIAGEM (valor bruto menos os descontos) e o VALOR MÉDIO POR VIAJANTE!

Resolucão [aqui](./scripts/scripts-cap02/exercicio2.py).

## Exercício 3:

Os colaboradores da sua equipe foram sorteados para ganhar um console de última geração, cada um, em razão do bom desempenho que tiveram nos últimos projetos. Por uma questão de logística, porém, a empresa pede que todos os cinco membros da equipe recebam o mesmo aparelho. Crie um algoritmo em que o usuário possa digitar o voto de cada um dos 5 membros da equipe e, ao final, exiba qual foi o console escolhido e com quantos votos. As opções são: PLAYSTATION, XBOX e NINTENDO.

Resolucão [aqui](./scripts/scripts-cap02/exercicio3.py).

---

<div align="center">

## FAST TEST

</div>

### QUESTÃO 1: Assinale a alternativa que apresenta corretamente a condicional da estrutura if para verificar se um número é ímpar no Python:
> if numero % 2 == 0:

### QUESTÃO 2: Selecione a alternativa que apresenta uma expressão que retorne True para uma nota válida. Considere como válidos os valores de 0 a 10, inclusive.
> nota >= 0 and nota <= 10

### QUESTÃO 3: No Python, podemos utilizar os operadores lógicos para combinar expressões e realizar os testes lógicos. Escolha a alternativa correta conforme as expressões lógicas a seguir:
> True or False = True.

### QUESTÃO 4: Pense em um código com estruturas condicionais para apresentar o resultado de uma partida ("Vitória do Time 1", "Vitória do Time 2" ou "Empate") a partir dos gols de cada time. Qual das alternativas apresenta a melhor solução?
> Utilização de estruturas com ifs encadeados.

---

[Voltar ao início!](https://github.com/monicaquintal/fintech)