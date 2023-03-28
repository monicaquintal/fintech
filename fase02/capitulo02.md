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