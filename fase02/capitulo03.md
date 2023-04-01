<div id="fase02" align="center">
<h1>FASE 2 - PROTOTYPING</h1>
<h2>Capítulo 03: Andar em círculos não é necessariamente ruim... 🎡</h2>
</div>

## Situação-problema:

<em>"Imagine que todos os alunos do FIAP ON estejam cadastrados em um único arquivo de texto, no formato csv (valores separados por vírgula) e que, munido dessa lista, você deve disparar um e-mail para todos os alunos menores de idade. 

Depois de ficar muito bravo com quem decidiu colocar os dados em um arquivo de texto, você precisa cumprir a sua tarefa. O que fazer? Talvez verificar linha por linha o conteúdo desse arquivo?</em>

Em um cálculo rápido, se o arquivo tiver 10.000 linhas,você precisará de 10.000 ifs para verificar se cada aluno em cada uma das linhas é maior ou menor de idade, como no exemplo:

~~~
se <condição para a 1ª linha> então
  //o que ocorrerá se o aluno for menor
fim_se
se <condição para a 2ª linha> então
  //o que ocorrerá se o aluno for menor
fim_se
se <condição para a 2ª linha> então
  //o que ocorrerá se o aluno for menor
fim_se
...
se <condição para a 10.000ª linha> então
  //o que ocorrerá se o aluno for menor
fim_se
~~~

Além de ser contraproducente fazer a digitação manual de cada um desses blocos, o programa fica mais suscetível a falhas por conta do desenvolvedor e menos passível de manutenção.

## O que é um Loop?

É uma estrutura que permite indicar a repetição de uma tarefa em um determinado número de vezes. Assim, conseguimos fazer com que o programa repita a tarefa de verificar a idade para cada uma das linhas do arquivo:

### Aplicando na situação-problema:

~~~
para linha de 1 até 10000 passo 1 faça
  se <condição para linha> então
    //o que acontecerá se o aluno for menor
  fim_se
fim_para
~~~

Há dois tipos de laços de repetição presentes na maior parte das linguagens de programação: o laço enquanto (while) e o laço para (for). Apesar de poderem ser usados nas mesmas situações, os laços com frequência possuem funcionamentos e objetivos diferentes.

## Enquanto (while)

O loop `while` é utilizado em situações em que não temos um número definido de repetições, nem mesmo um limite para isso. Temos apenas uma condição que permite ao loop continuar ou parar. Dessa forma, ele é um `laço de repetição baseado em condição`.

### Exemplo:

<em>"Que tal prendermos o usuário em uma armadilha? Faremos um algoritmo para que ele seja obrigado a provar que é um verdadeiro nerd ao responder: “Qual é a resposta para a vida, o universo e tudo mais?”, e o programa não encerrará até que ele dê a resposta correta (que, segundo O guia do mochileiro das galáxias, é “42”). O que queremos é repetir uma pergunta ao usuário enquantoele não acertar a resposta." </em>

1. Algoritmo:

~~~
Variáveis:
  resposta: alfanumérico
Início
  resposta = “0”
  Enquanto (resposta != “42”) faça
    Escreva “Qual é a resposta para a vida, o universo e tudo mais?”
    Leia resposta
  Fim_enquanto
  Escreva “Parabéns, você acertou!”
Fim
~~~

2. O script com a codificação python pode ser conferido [aqui](./scripts/scripts-cap03/exemplo_while.py).

### Observação importante:

> Muitos autores caracterizam o laço de repetição while como “potencialmente infinito”, pois,se não nos atentarmos à condição criada, o programa ficará preso para sempre nesse ciclo.

Haverá cenários em que o programador desejará criar um loop infinito de forma proposital, como em uma thread que verifica se existem novas mensagens em uma comunicação por sockets.

### `Variável controladora`

Trata-se de uma variável que será usada como condição do nosso loop, sendo incrementada a cada volta realizada!

***Exemplo:***

"Executar uma repetição de 10 voltas:"

1. Algoritmo:

~~~
Variáveis:
    i: inteiro
Início
  i = 0
  Enquanto (i<10) faça
    Escreva “Mais uma mensagem, com i valendo: ”, i
    i = i + 1
  Fim_enquanto
Fim
~~~

A cada volta, podemos fazer o incremento da variável i (i = i + 1), aumentando o seu valor para que, eventualmente, atinja o limite estipulado na condição do laço (i < 10).

2. Codificação em Python [aqui](./scripts/scripts-cap03/exemplo_while_2.py).

> Algumas linguagens de programação suportam notações como "`i++`" ou "`i+=1`" para a operação de incremento na variável contadora.

---

## Para (for)

Usada quando estamos diante de um problema que exige um ***número determinado de repetições***.

Determinamos um ponto inicial e um ponto final para a repetição, e a própria estrutura se encarregará de controlar o número de voltas.

1. Pseoducódigo:

~~~
para <contadora> de <valor inicial> até <valor final> passo <incremento> faça
  //instruções que serão repetidas
fim_para
~~~

### Importante:

Para uma repetição de 10 vezes em linguagem Python, podemos fazer uso de uma função chamada `range()` , que **definirá um intervalo de valores para a nossa variável contadora assumir**. Exemplo:

~~~python 
# a variável contadora deverá assumir valores no intervalo entre 0 e 9
# “para a variável x no intervalo entre 0 e 9, faça:”
for x in range(10):
  #para cada um desses valores, vamos printar o valor da variável
  print(x)
~~~

É possível **alterar a função range**, com a inclusão de outro argumento. Se escrevermos range(1,15), por exemplo, o valor inicial da variável será 1 e o valor final da variável contadora será 14.

~~~python
# a variável contadora deverá assumir valores no intervalo entre 1 e 14
for x in range(1,15):
    # para cada um desses valores, vamos printar o valor da variável
    print(x)
~~~

Podemos, ainda, **controlar o incremento** da variável contadora, incluindo mais um argumento na função range. Se escrevermos range(1,10,2), avariável assumirá o valor inicial como sendo 1, o valor final como sendo 9, e a cada volta ela somará 2. Portanto terá os valores: 1, 3, 5, 7 e 9.

~~~python
# a variável contadora deverá assumir valores no intervalo entre 1 e 9 com incremento 2
for x in range(1,10,2):
  # para cada um desses valores, vamos printar o valor da variável
  print(x)
~~~

Os exemplos podem ser verificados [aqui](./scripts/scripts-cap03/exemplo_for.py).

---

<div align="center">

## Praticando

</div>

