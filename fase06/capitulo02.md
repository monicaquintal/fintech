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
- obs: para verificar se as strings são diferentes, não precisamos de um método específico; **adicionar na comparação o operador de negação (!)**.
- exemplo:

~~~java
String nome = "FIAP";
String nome2 = new String("FIAP");

if (nome.equals(nome2)) {
  System.out.println("As Strings são diferentes."); 
} else {
  System.out.println("As Strings são iguais.");
}
// retorna: "As Strings são iguais."
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
// retorna: "As Strings são iguais."
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
// retorna: "A String começa com FIAP."
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
// retorna: "A String termina com gia."
~~~

### c) `Método length`:
- permite recuperar a quantidade de caracteres. 
- na string, o length é um método, logo, deve terminar com abre e fecha parênteses:

~~~java
String facu = "FIAP – A melhor faculdade de tecnologia.";
int caracteres = facu.length();

System.out.println("A string possui " + caracteres + "caracteres.");
// retorna: "A string possui 39 caracteres."
~~~

### d) `Método charAt`:
- permite recuperar um caractere específico de uma string dada a sua posição.
- parecida com um vetor, onde podemos recuperar um elemento por meio do seu índice (o primeiro caractere da string está na posição zero (0)).
- o método recebe a posição do caractere que será recuperado.

~~~java
String facu = "FIAP – A melhor faculdade de tecnologia.";
char caracter = facu.charAt(1);

System.out.println("O segundo caractereda string é" + caracter);
// retorna: "O segundo caractereda string é I".
~~~

### e) `Método indexOf`:
- permite localizar a primeira ocorrência de um caractere ou palavra em uma string. 
- caso não seja localizado, o ***valor -1*** é retornado.
- lembrando que o índice da string começa no zero, e os espaços também são considerados!
- exemplo, buscando a primeira ocorrência do caractere ‘a’:

~~~java
String facu = "FIAP – A melhor faculdade de tecnologia.";
int posição = facu.indexOf("a");

System.out.println("O índice do caractere 'a' na string é" + posição);
// retorna: "O índice do caractere 'a' na string é 17".
~~~

- o método indexOf também pode ser utilizado para ***procurar por uma sequência de caracteres***:
  - caso a palavra não seja encontrada, o valor -1 também será retornado. 

~~~java
String facu = "FIAP – A melhor Faculdade de tecnologia.";
int posição = facu.indexOf("Faculdade");

System.out.println("O índice da palavra \"Faculdade\" na string é" + posição);
// retorna: "O índice da palvra "Faculdade" na string é 16."
~~~

### f) `Método lastIndexOf`:
- parecido com o indexOf, retorna o índice da última ocorrência de um caractere ou palavra em uma string.

~~~java
String facu = "FIAP - A Melhor Faculdade de Tecnologia";
int posicao = facu.lastIndexOf('a');
System.out.println("O índice do último caractere\'a\' na string é " + posicao);

// retorna: "O índice do último caractere 'a' na string é 38."
~~~

- para procurar por uma palavra, passá-la como parâmetro.

### g) `Método substring`:
- permite criar uma string a partir de um trecho de outra string.
- recebe como parâmetro a posição inicial (inclusive) e a posição final (exclusive) do conjunto de caracteres a serem copiados da string original: o caractere da posição inicial será copiado para a nova string,e o caractere da última posição não será copiado.

~~~java
String facu = "FIAP - A Melhor Faculdade de Tecnologia";
String nova = facu.substring(16, 25);
System.out.println("A nova string é: " + nova);

// retorna: "A nova string é: Faculdade"
~~~

- é possível utilizar métodos vistos anteriormente em conjunto com substring. 
- exemplo: método indexOf para retornar o índice da primeira ocorrência e criar uma nova string.

~~~java
String facu = "FIAP – A Melhor Faculdade de Tecnologia";
String nova = facu.substring(facu.indexOf('M'), 25);
System.out.println("A nova string é: " + nova);

// retorna: "A nova string é: Melhor Faculdade"
~~~

- o método substring também aceita apenas a posição inicial do conjunto de caracteres, e a nova string será criada da posição inicial informada até o fim da string original.

### h) `Método toUpperCase toLowerCase`:
- para transformar os caracteres de uma string para maiúsculo, utilizar o método toUpperCase, e para minúsculo, o método toLowerCase.
- considerando que uma string é imutável, quando utilizamos esses métodos, uma nova string será criada com a alteração solicitada (devemos sempre atribuir a uma nova variável).

~~~java
String facu = "FIAP – A Melhor Faculdade de Tecnologia";
String nova = facu.toUpperCase();
System.out.println("A nova string é: " + nova);

// retorna: "A nova string é: FIAP - A MELHOR FACULDADE DE TECNOLOGIA"
~~~

### i) `Método replace`:
- permite substituir caracteres ou palavras de uma string original.
- esse método recebe como parâmetros o caractere ou a palavra a ser substituída e a letra ou a palavra para substituir. 
- esse método também cria uma nova string com a alteração.

~~~java
String facu = "FIAP – A Melhor Faculdade de Tecnologia";
String nova = facu.replace('a', 'x');
System.out.println("A nova string é: " + nova);

// retorna: "A nova string é: FIAP – A Melhor Fxculdxde de Tecnologix"
~~~

- é possível também substituir uma palavra em uma string.

### j) `Método split`:
- separa o valor de uma string em várias strings separadas por um delimitador, que deve ser informado ao método.

~~~java
String facu = "FIAP – A Melhor Faculdade de Tecnologia";
String[] palavras = facu.split(" ");
for (String p : palavras) {
  System.out.println(p);
}

/*
 * Este exemplo separa a string em várias 
 * palavras, separadas por um espaço. 
 * O resultado é armazenado em um vetor de strings.
 * retorna:
 * FIAP 
 * – 
 * A 
 * Melhor 
 * Faculdade 
 * de 
 * Tecnologia
 */
~~~

- além do espaço, podemos usar qualquer outro caractere ou palavra
 como delimitador.

<details>
<summary>Cálculo dos dígitos de controle do CPF</summary>

São válidos os seguintes aspectos:
- O CPF possui 11 dígitos; os dois últimos números são dígitos de controle.
- O primeiro dígito de controle é calculado com base nos 9 primeiros dígitos.
- O segundo dígito de controle é calculado com base nos 9 primeiros dígitos e no primeiro dígito de controle.
- A Região Fiscal onde é emitido o CPF (definida pelo nono dígito) tem a seguinte abrangência:
  - 1 (DF-GO-MS-MT-TO),
  - 2 (AC-AM-AP-PA-RO-RR),
  - 3 (CE-MA-PI),
  - 4 (AL-PB-PE-RN),
  - 5 (BA-SE),
  - 6 (MG),
  - 7 (ES-RJ),
  - 8 (SP),
  - 9 (PR-SC) e
  - 0 (RS).

- Solução:
  - Considere a representação do CPF em forma de letras: 
    - ABC.DEF.GHI-JK,
    - onde cada uma das letras representa um dígito do CPF.
  - O dígito de controle J é calculado pela seguinte expressão:
    - Soma = 10 * A + 9 * B + 8 * C + 7 * D + 6 * E + 5 * F + 4 * G + 3 * H + 2 * I
    - Resto = resto(Soma,11), ou seja, resto da divisão de “Soma” por 11.
      - Se resto <= 1 então J = 0.
      - SenãoJ = 11 – Resto.
  - Uma vez calculado o dígito J (primeiro dígito de controle), calcular o dígito de controle K (segundo dígito de controle). 
    - operação muito semelhante àanterior, como segue:
    - Soma = 11 * A + 10 * B + 9 * C + 8 * D + 7 * E + 6 * F + 5 * G + 4 * H + 3 * I + 2 * J
    - Resto = resto(Soma,11), ou seja, resto da divisão de “Soma” por 11.
      - Se resto <= 1 então K = 0.
      - Senão K = 11 – Resto.
  - O processo de desenvolvimento desse algoritmo consiste, primeiramente, na leitura de um número representando os 9 primeiros dígitos do CPF para o cálculo dos dígitos de controle.
  - Depois, o algoritmo deverá calcular cada dígito de verificação, concatenando-os à sequência original de 9 dígitos. 
  - Notar que com ambos os dígitos de controle calculados e feita a concatenação, a variável CPF, que contém o CPF, passa a ter 11 posições.
  </details>

---

<div align="center">
<h2>2. COLLECTIONS FRAMEWORK (COLEÇÕES)</h2>
</div>

- são estruturas de dados utilizadas para armazenar e organizar objetos de maneira eficiente e prática. 
- podem ser usadas para representar estruturas, como vetores, listas, pilhas, filas, mapas, conjuntos e outras estruturas de dados. 
- são muito comuns nas aplicações Java para o acesso ao banco de dados, principalmente no resultado de buscas.
- Coleções são definidas por meio de interfaces. As interfaces determinam o que a estrutura deve oferecerde funcionalidades, ou seja, fornece um contrato para que a classe concreta as implemente.

### Categorias:
- no Java, as Coleções podem ser classificadas em duas categorias: as que implementam a interface Collection e as que implementam a interface Map.
- as `principais subinterfaces de Collection` são:
  - ***List***: representa uma lista de objetos, a implementação mais utilizada é o ***ArrayList***.
  - ***Set***: representa um conjunto de objetos únicos, e os objetos não se repetem; a implementação mais usada é a ***HashSet***.
- a `Interface Map` representa uma tabela Hash, que armazena valores compostos de [chave, valor]. A principal subinterface é:
  - ***SortedMap***: representa um mapa ordenado, a implementação mais utilizada é o ***HashMap***.

- A interface Collection, que é base para todas as Coleções, exceto Mapas, define um conjunto de métodos comuns a todas as outras estruturas que estão abaixo dela: list, set e queue.
- Os principais métodos da interface Collection são:

<div align="center">

Método | Descrição
-------|---------------
add | Adiciona um objeto à coleção
clear | Remove todos os objetos da lista
contains | Verifica se a coléção contém o objeto determinado
isEmpty | Verifica se a coleção está vazia
remove | Remove um objeto da coleção
size | Retorna a quantidade de objetos na coleção
toArray | Retorna um array contendo os elementos da coleção

</div>

## 2.1 Interface List

- representa uma sequência de elementos ordenados e pode conter elementos repetidos: os elementos de uma lista estão dispostos pela ordem de inserção. 
- para criar uma lista, não precisamos passar o tamanho dela, como temos que fazer no array; a lista se adapta quando inserimos um elemento, possibilitando adicionar ou remover quantos elementos forem necessários. 
- também podemos manipular a lista, ordenando-a ou buscando um elemento pelo seu valor.
- há diversas implementações disponíveis, sendo a ArrayLista mais utilizada.
- principais métodos de uma lista:

<div align="center">

Método | Descrição
-------|------------
add | Insere um objeto no final da lista
get | Retorna o objeto localizado numa determinada posição
remove | Remove um objeto localizado numa determinada posição
set | Coloca um objeto numa determinada posição (substitui objetos)
indexOf | Retorna a posição de um objeto na lista
lastIndexOf | Retorna a última posição de um objeto na lista
subList | Retorna parte de uma lista

</div>

- a `ArrayList` armazena seus elementos em um array interno para gerar uma lista, que cresce ou diminui dinamicamente no momento que um elemento é inserido ou excluído da lista. 
- apesar do nome, ArrayList é uma implementação da interface List da API de Collections do Java; essa classe somente utiliza um array para armazenar os valores, porém não podemos acessar diretamente esse array, pois é um atributo encapsulado. 
- para criar uma ArrayList, basta chamar o seu construtor:

~~~java
Array lista = new ArrayList();
lista.add("LIP");
lista.add("Web");
lista.add("Algoritmos");
lista.set(1, "Algoritmos"); 
listra.remove(1);

System.out.println(lista.get(1));

for (int i = 0; i < lista.size(); i++) {
  System.out.println(lista.get(i));
}
~~~

## 2.2 Interface Set

- define uma coleção que não pode conter valores duplicados. 
- corresponde à abstração de um conjunto que funciona de forma análoga aos conjuntos da matemática.
- nem sempre a ordem de inserção dos elementos será a ordem dos elementos dispostos na coleção: pode variar de implementação para implementação.
- a interface contém somente os métodos herdados da interface Collection:

<div align="center">

Método | Descrição
-------|---------------
add | Adiciona um objeto no Set
clear | Remove todos os objetos do Set
contains | Verifica se o Set possui um objeto determinado
isEmpty | Verifica se o Set está vazio
remove | Remove um objeto do Set
size | Retorna a quantidade de objetos no Set
toArray | Retorna um array contendo os objetos do Set

</div>

- uma das principais implementações de Set é a `classe HashSet`, que armazena seus elementos em uma tabela hash.

~~~java
HashSet cursos = new HashSet<>();

cursos.add("Java");
cursos.add("J.NET");
cursos.add("Android");
cursos.add("Java"); // repetido, não será adicionado ao hashset
~~~

- a grande vantagem do Set é a performance nas operações de busca (método contains) em relação à List.

## 2.3 Map

- um mapa é composto de um par de chaves e valor. 
  - chaves não podem conter valores iguais, porém o valor, sim.
- a principal implementação de Map é a classe HashMap.

<div align="center">

Método | Descrição
-------|---------------
clear | Remove todos os mapeamentos
containsKey | Verifica se uma chave já está presente no mapeamento
containsValue | Verifica se um valor já está presente no mapeamento
get | Retorna o valor associado a uma chave determinada
isEmpty | Verifica se o mapeamento está vazio
ketSet | Retorna um Set contendo as chaves
put | Adiciona um mapeamento
remove | Remove um mapeamento
size | Retorna o número de mapeamentos
values | Retorna o número de mapeamentos

</div>

## 2.4 Generics

- A partir do Java 5, podemos utilizar o recurso de Generics para restringir os tipos de dados aceitos por referência genérica; somente será permitido inserir na lista o tipo determinado no Generics, e não qualquer objeto.
- O Generics permite a verificação do tipo em tempo de compilação e deixa o código mais limpo, pois não é necessário realizar um cast.
- sintaxe:

~~~java
ArrayList<Tipo> lista = new ArrayList<Tipo>();
ArrayList<Cliente> listaCliente = new ArrayList<Cliente>();
~~~

- Podemos utilizar o operador for-each para percorrer a lista.
- Toda a API de Collections permite a utilização de Generics por oferecer maior segurança na manipulação dos tipos e não há necessidade de cast.

> O Generic não permite tipos primitivos!

---

## FAST TEST

### 1. Ao utilizarmos Strings, em Java, temos métodos auxiliares que possibilitam realizar certas verificações de verdadeiro ou falso para algumas comparações. Escolha a alternativa que representa alguns desses métodos.
> startsWith(), endsWith() e equalsIgnoreCase().

### 2. Em Java, assim como em outras linguagens de programação, existem as estruturas de repetição. Escolha a alternativa que melhor descreve a função dessas estruturas.
> As estruturas de repetição têm a função de executar uma ou mais vezes um bloco de código.

### 3. O laço FOR pode, normalmente, ser utilizado para percorrer uma array através de um índice. Escolha a opção que representa uma alternativa válida para o uso do laço FOR na linguagem Java.
> for (&lt;tipo&gt; &lt;variável&gt; : &lt;array&gt;) { &lt;instruções&gt; }

### 4. Array é uma das estruturas de dados mais utilizadas em programação de sistemas em Java. Escolha a alternativa que representa a inicialização de uma array e o uso de um valor na quarta posição.
> String[] amigos = { “José”, “Carla”, “Flávio”, “Ana” }; String amigo4 = amigos[3];

### 5. Há um método existente na classe String, em Java, responsável por transformar uma cadeia de caracteres em uma array, qual é esse método?
> split().

### 6. Em Java, além das arrays, podemos utilizar algumas outras classes mais eficientes e práticas na criação de estruturas de dados usadas para armazenar e organizar objetos. Qual das opções representa algumas das classes disponíveis para uso na criação dessas estruturas?
> ArrayList, Set e Map.

### 7. Escolha a alternativa que representa o conceito correto para o método indexOf() utilizado na classe String em Java.
> O método é utilizado para encontrar a primeira ocorrência de um caractere.

### 8. Qual é o termo utilizado para uma array que armazena outras arrays?
> Array multidimensional.

### 9. No ambiente de desenvolvimento em Java, assim como em outras linguagens modernas, existe a figura do Generics. Escolha a definição verdadeira para essa entidade.
> São marcações de código que permitem a verificação do tipo em tempo de compilação, dando clareza de leitura ao código-fonte.

--- 

[Voltar ao início!](https://github.com/monicaquintal/fintech)