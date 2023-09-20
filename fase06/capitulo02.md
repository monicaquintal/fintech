<div id="fase06" align="center">
<h1>FASE 6 - MODEL</h1>
<h2>Capítulo 02: Lidando com vários dados... em Java!</h2>
</div>

<div align="center">
<h2>1. LIDANDO COM VÁRIOS DADOS...EM JAVA!</h2>
</div>

## 1.1 Introdução

- no Java, vetores e matrizes são chamados de `arrays`.
- as estruturas formadas pelos arrays têm uma desvantagem: precisam ser dimensionadas com um tamanho fixo assim que são declaradas para uso, mas isso nem sempre é possível – em algumas situações, precisamos de estruturas mais flexíveis. 
  - a resposta para essa necessidade são as `Coleções (Collections)`.

## 1.2 Estruturas de repetição (loops ou laços)

- loops permitem que um bloco de código seja executado repetidamente enquanto alguma condição permanecer verdadeira. 
- no Java, existem três estruturas de repetição: while, do-while e for.

### 1.2.1 `While`

- executa um bloco de código enquanto a condição for verdadeira. 
- IMPORTANTE: **o loop while nunca será executado se a condição resultar falsa desde o início!**
- estrutura básica do comando:

~~~
while (<condição>) {
  <instruções>
}
~~~

- [exemplo](./projects/capitulo02_fase06/src/capitulo02_fase06/Estruturas_de_repeticao.java): trecho de código que imprime os números do 1 ao 10.

~~~java
int numero = 0;
		
while (numero < 10) {
	numero = numero + 1;
	System.out.println(numero);
}
~~~

> A estrutura while faz e avalia a condição no início do laço.

### 1.2.2 `Do-While`

- este loop **primeiramente executará todo o bloco de código para depois testar a condição**, e assim verificar se repete novamente o bloco de código.
- sintaxe básica:

~~~
do {
  <instruções>
} while (<condição>);
~~~

- [exemplo](./projects/capitulo02_fase06/src/capitulo02_fase06/Estruturas_de_repeticao.java): trecho de código que imprime os números do 1 ao 10.

~~~java
int numero2 = 0;

do {
  numero2 = numero2 + 1;
  System.out.println(numero2);
} while (numero2 < 10);
~~~

> há situações em que não é possível prever a quantidade de iterações; nesses casos, as duas estruturas podem ser utilizadas.

- [exemplo 2](./projects/capitulo02_fase06/src/capitulo02_fase06/Exemplo_do_while.java):

~~~java
Scanner sc = new Scanner(System.in);

String opcao;
do {
  System.out.println("Digite um número: ");
  int n1 = sc.nextInt();
  System.out.println("Digite outro número: ");
  int n2 = sc.nextInt();
  int soma = n1 + n2;
  System.out.println("A soma é: "+ soma);
  System.out.println("Deseja somar outro número? (S/N)");
  opcao = sc.next();
} while (opcao.equals("S"));
// para verificar igualdade de strings, utilizar método equals em vez do operador ==.

sc.close();

/*
 * Java é case sensitive: 
 * devemos respeitar o uso de letras maiúsculas ou minúsculas
 * na grafia dos comandos.
 */
~~~

### 1.2.3 `For`

- seu uso é **indicado quando sabemos exatamente quantas vezes o loop deve ser realizado**.
- é uma estrutura de repetição que utiliza uma **variável responsável por controlar o número de iterações**. 
  - funciona como um contador de voltas que é incrementadoa cada iteração. 
- sintaxe básica:

~~~
for (<inicialização>; <condição lógica>; <incremento ou decremento>) {
  <instruções>
}
~~~

- [exemplo](./projects/capitulo02_fase06/src/capitulo02_fase06/Estruturas_de_repeticao.java): trecho de código que imprime os números do 1 ao 10.

~~~java
System.out.println("Utilizando FOR:");
for (int i = 0; i <= 10; i++) {
  System.out.println(i);
}
~~~

### 1.2.4 Exercícios

1. Elabore um programa para ler 20 valores inteiros fornecidos pelo usuário e calcular a soma deles. Apresente o resultado ao final.
2. Elabore um programa para fazer a tabuada de um número fornecido pelo usuário,variando de 0 a 12, e mostre o resultado a cada iteração.
3. Elabore um programa que calcule a sequência de Fibonacci até o 30º termo.A sequência obedece ao seguinte padrão: 1, 1, 2, 3, 5, ... n.
4. Elabore um programa que leia o nome e o salário de n pessoas, o usuário deverá informar se deseja continuar a iteração. Ao final, apresente a quantidade de pessoas informadas e a média entre os salários.

## 1.3 Arrays

- estrutura de dados que armazena uma coleção de itens do mesmo tipo, que pode ser um tipo primitivo ou um objeto.
- cada item no vetor possui seu próprio local numerado, chamado `índice`. 
  - o índice é utilizado para acessar um elemento no vetor e, assim, recuperar ou atribuir uma informação naquele índice.
  - em um array, o índice se inicia a partir do 0.
  - um array possui um comprimento fixo que não pode ser alterado. 
  - há a possibilidade de recuperar o tamanho do array por meio do `atributo length`.
- um array em Java é um objeto, logo devemos utilizar o `operador new` para criar um anova instância de um array.
- para declarar uma variável de modo a armazenar um array: especificar o tipo de array, acrescentar colchetes ([ ]) e definir o nome da variável, ou adicionar os colchetes depois do nome da variável.
- exemplo:

~~~java
int[] notas = new int[40];
int notas2 [] = new int [50];

notas[0] = 10;
/* Para atribuir valor em uma posição:
  * indicar o nome do vetor e 
  * inserir o índice nos colchetes. */
~~~

- no momento da declaração, definir entre colchetes o comprimento do array.
- um array de boolean é inicializado com false, e um array de objeto é inicializado com null.
- exemplo:

~~~java
notas[0] = 10;
~~~

- para recuperar o valor, indicar o nome e o índice do vetor:

~~~java
System.out.println(notas[0]);
~~~

- há **duas formas de declarar um vetor com suas posições preenchidas com valores predeterminados**:
  - a primeira consiste em atribuir uma lista de valores entre chaves { }, sendo cada valor separado por vírgula.
  - a outra forma tem o mesmo princípio, diferenciando-se pela adição do operador new na declaração.

~~~java
int notas[] = {10, 9, 8, 2};
// ou
int notas[] = new int{10, 9, 8, 2};

/* o resultado das declarações acima 
 * é igual ao resultado do código:
 */
int notas[] = new int[4];
notas[0] = 10;
notas[1] = 9;
notas[2] = 8;
notas[3] = 2;
~~~

- podemos criar arrays seja qual for o tipo de dado em Java: String, byte, char, int, long, double, float, boolean ou qualquer classe Java. 
- exemplos:

~~~java
byte bytes[] = new byte[4];
short shorts[] = new short[8];
double doubles[] = new double[7];
float floats[] = new float[3];
String strings[] = new String[10];
Carro carros[] = new Carro[15];
~~~

- para acessar todas as posições de um vetor, utilizamos loops: podemos fazer um loop para repetir uma determinada operação pela quantidade de vezes igual ao tamanho do vetor.

### [Exemplo 1](./projects/capitulo02_fase06/src/capitulo02_fase06/Exemplo_For.java):

- desenvolver um programa que precisa armazenar as notas de uma turma de 10 alunos e calcular a sua média. 
- primeiro, ler as notas dos 10 alunos utilizando um loop e armazenando cada uma em uma posição do array (vetor).
- depois, calcular a média e exibir para o usuário. 

~~~java
Scanner scanner = new Scanner(System.in);

float[] notas = new float[4];
float totalNotas = 0;

for (int i = 0; i < notas.length; i++) {
  System.out.println("Digite a nota do aluno: ");
  notas[i] = scanner.nextFloat();
  totalNotas = totalNotas + notas[i];
}
float mediaNotas = totalNotas / notas.length;
System.out.println("A média dos alunos é: "+ mediaNotas);
scanner.close();
~~~

### Exemplo 2:

- definido um array com 5 posições para armazenar as referências de objetos do tipo Carro.
- para popular o array de carros, primeiro instanciá-lo e depois armazenar a sua referência em uma posição do vetor.

~~~java
Carro[] carros = new Carro[5];

Carro carro = new Carro();
carro.setModelo("Gol");

carros[0] = carro;
~~~

- para recuperar o valor do modelo do carro que está armazenado na primeira posição do vetor:

~~~java
String modelo = carros[0].getModelo();System.out.println(modelo);
~~~

### 1.3.1 `For-each`:

- permite percorrer um vetor de primitivos ou referências com uma sintaxe mais simples.
- não necessita manter uma variável de controle para indicar a posição do elemento no vetor.
- sintaxe:

~~~
for (<tipo> <variável> : <array>){
  <instruções>
}
~~~

- temos:
  - primeiro parâmetro é o tipo do array; 
  - o segundo é um nome para a variável que vai receber cada um dos itens do vetor; 
  - e o último parâmetro, que está após os dois pontos (:), é o array que queremos percorrer.
- percorrendo o array do exemplo acima: 

~~~java
for (Carro carro: carros) {
  System.out.println(carro.getModelo());
}
~~~

### 1.3.2 `Matrizes` (ou arrays multidimensionais):

- são arrays de arrays. 
- ou seja, cada posição do array armazena outro array. Esses arrays também podem conter arrays e assim por diante, abrangendo quantas dimensões o desenvolvedor desejar.
- exemplo:
  - as notas dos alunos devem ser armazenadas por disciplina. 
  - o curso tem 9 disciplinas com 40 alunos cada.
  - criar um array com 9 posições e em cada posição armazenar um outro array com 40 elementos.

~~~java
float[][] notas = new float[9][40];
~~~

- o array de array denominado "notas" representa uma matriz de 9 linhas com 40 colunas.
- ou seja, uma matriz 9 x 40 que tem 360 posições, uma para cada aluno em 9 disciplinas. 
- para armazenar uma nota 10 para o primeiro aluno na primeira disciplina:

~~~java
notas[0][0] = 10f;
~~~

- para informar uma nota 9 ao segundo aluno da primeira disciplina, basta alterar o índice:

~~~java
notas[0][1] = 9f;
~~~

- portanto, arrays de arrays funcionam da mesma forma que arrays unidirecionais. 
- o primeiro índice de cada array começa em 0.
- é possível também criar um array de array de array, ou em quantas dimensões forem necessárias:

~~~java
float[][][] notas = new float[10][50][10];
~~~

### 1.3.3 Exercícios

1. Escreva um programa para preencher uma matriz unidimensional (vetor) com 15 posições de números inteiros e, em seguida,apresente os elementos.
2. Escreva um programa para preencher uma matriz unidimensional (vetor) que deverá receber as temperaturas ao longo do dia. A medição precisa ser registrada a cada uma hora. Ao final, exiba a temperatura média do dia.
3. Altere o programa anterior para registrar as temperaturas de cada dia do mês, neste caso, utilize uma matriz com 30 linhas e 24 colunas. Ao final, verifique qual foi a maior temperatura, a menor temperatura e a temperatura média.
4. Escreva um programa para armazenar em uma matriz as notas das 5 disciplinas dos 20 alunos de uma turma.

### 1.4 Strings

- são sequências de caracteres.
- **Java não tem um tipo de dado primitivo,como int ou double, para armazenar uma string.** Em vez disso, podemos utilizar a biblioteca-padrão Java,que contém uma classe predefinida, chamada String!

> Importante: **String** é a palavra reservada do Java e representa uma classe predefinida, e **string** refere-se a uma cadeia de caracteres, ou seja, um texto.

- objetos strings são imutáveis e seu conteúdo de caracteres não pode ser alterado após a sua inicialização.
- porém, é possível armazenar outra string no lugar da string original. 
- uma variável String deve ser declarada, instanciada e inicializada. 
- sintaxe:

~~~java
String nome;
~~~

- depois de declarar uma String, podemos instanciá-la como uma classe normal.
- sintaxe: 

~~~java
String nome = new String();
nome = "hello";
// OU
String nome = new String("hello");

/* 
 * É possível também atribuir um valor 
 * a uma variável String sem instanciá-la:
 */
String nome = "hello";
~~~

- dessa forma, a string será armazenada em um pool de strings, área utilizada pelo Java como cache.
- caso a variável String seja uma variável de instância, ou seja, um atributo de uma classe, ela precisa ser instanciada ou inicializada antes de ser utilizada, pois todos os atributos de referência são inicializados com null.
  - se invocarmos um método de uma variável vazia, vamos receber uma exceção (exception), chamada `NullPointerException`.
  - ou seja, um erro pode acontecer.
  - exemplo: método length() para recuperar a quantidade de caracteres da string nome sem instanciá-la:

~~~java
String nome = null;
System.out.println(nome.length());
~~~

- a variável nome não possui nenhum valor, é nula (null).
- quando o programa for executado, um erro vai ocorrer.
- para resolve-lo, instanciar ou inicializar uma variável String:

~~~java
String nome = new String();
System.out.println(nome.length());

// OU

String nome = "hello";
System.out.println(nome.length());
~~~

- ao declarar uma variável dentro de um método, é necessário inicializá-la antes de utilizá-la!

### 1.4.1 Caracteres de escape:

- são alguns caracteres precedidos da contrabarra, considerados sequência de escape e que têm um significado especial para o compilador.

<div align="center">

Sequência de escape | Descrição
--------------------|----------------
&#92;n | Nova linha.<br>Posiciona o cursor no início da próxima linha.
&#92;t | Tabulação horizontal.<br>Move o cursor para a próxima posição da tabulação horizontal.
&#92;&#92; | Barras invertidas.<br>Utilizadas para gerar um caractere de barra invertida (&#92;).
&#92;" | Aspas duplas.<br>Utilizadas para gerar um caractere de aspas duplas.
&#92;' | Aspas simples.<br>Utilizadas para gerar um caractere de aspas simples.

</div>

### 1.4.2 Somando strings (concatenação):

- concatenação de strings consiste em juntar duas ou mais strings para criar uma nova.
- a forma mais fácil de concatenar uma string é utilizar o operador de soma (+).
- além do operador + e +=, podemos concatenar strings utilizando o método concat:

~~~java
String nome = "FIAP";
String slogan = "A melhor faculdade de tecnologia";String faculdade = nome.concat("-").concat(slogan);
System.out.println(faculdade);
~~~

### 1.4.3 Comparação de strings:

- deve ser realizada por meio de métodos:
  - `equals(string)`: verifica a igualdade do valor das strings.
  - `equalsIgnoreCase(string)`: verifica a igualdade do valor das strings sem diferenciar as letras maiúsculas e minúsculas.

> IMPORTANTE: não utilizar o operador == para comparar strings, pois compara o endereço de memória em que a string está alocada em vez do valor armazenado na string.

~~~java
String nome = new String("FIAP");
String nome2 = new String("FIAP");

if (nome == nome2) {
  System.out.println("As Strings são iguais.");
} else {
  System.out.println("As Strings são diferentes.");
}

/*
 * Nesse caso, as duas variáveis têm o mesmo valor,
 * porém estão alocadas em endereços de memória
 * diferentes. 
 * O resultado será “As strings são diferentes”,
 * pois o operador == compara o endereço de
 * memória e não o valor!
 */
~~~

- porém, se inicializar as strings sem instanciá-las, os valores serão alocados em um pool de strings. 
- dessa forma, se os valores forem iguais, elas vão compartilhar o mesmo espaço de memória no pool, fazendo com que o operador == funcione!
- porém, se uma das duas variáveis for instanciada utilizando-se new, o operador == não vai funcionar.

> POR ISSO é recomendado sempre utilizar os métodos para realizar a comparação de strings, porque eles funcionam independentemente da forma que a variável foi inicializada!

### a) `Método equals`
- compara o conteúdo de duas strings, diferenciando os caracteres maiúsculos e minúsculos. 
- ou seja, a string “Fiap” é diferente de “fiap”.
- para verificar se as strings são diferentes, não precisamos de um método específico; **adicionar na comparação o operador de negação (!)**.
- exemplo:

~~~java
String nome = "FIAP";
String nome2 = new String("FIAP");

if (!nome.equals(nome2)) {
  System.out.println("As Strings são diferentes."); 
} else {
  System.out.println("As Strings são iguais.");
}
~~~

### b) `Método equalsIgnoreCase`
- compara o conteúdo de duas strings, mas não diferencia caracteres maiúsculos e minúsculos. 
- ou seja, nesse caso a string “Fiap” é igual à string “fiap”.

~~~java
String nome = "FIAP";
String nome2 = new String("fiap");

if (nome.equalsIgnoreCase(nome2)) {
  System.out.println("As Strings são iguais.");
} else {
  System.out.println("As Strings são diferentes.");
}
~~~

- podemos verificar se uma string começa com uma sequência de caracteres específica, utilizando o `método startsWith()`:
  - lembrar que esse método diferencia o case das letras.

~~~java
String facu = "FIAP – A melhor faculdade de tecnologia.";

if (facu.startsWith("FIAP")) {
  System.out.println("A String começa com FIAP.");
} else {
  System.out.println("A String não começa com FIAP.");
}
~~~

- para verificar se uma string termina com uma sequência de caracteres específica, utilizar o `método endsWith()`, que também recebe a palavra a ser procurada:
  - lembrar que esse método também diferencia o case das letras.

~~~java
String facu = "FIAP – A melhor faculdade de tecnologia.";

if (facu.endsWith("gia.")) {
  System.out.println("A String termina com gia."); 
} else {
  System.out.println("A String não termina com gia.");
}
~~~

### c) `Método length`:
- permite recuperar a quantidade de caracteres. 
- na string, o length é um método, logo, deve terminar com abre e fecha parênteses:

~~~java
String facu = "FIAP – A melhor faculdade de tecnologia.";
int caracteres = facu.length();

System.out.println("A string possui " + caracteres + "caracteres.");
~~~










--- 

[Voltar ao início!](https://github.com/monicaquintal/fintech)