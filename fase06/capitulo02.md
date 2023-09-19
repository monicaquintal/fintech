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

- exemplo: trecho de código que imprime os números do 1 ao 10.

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

- exemplo: trecho de código que imprime os números do 1 ao 10.

~~~java
int numero2 = 0;

do {
  numero2 = numero2 + 1;
  System.out.println(numero2);
} while (numero2 < 10);
~~~

> há situações em que não é possível prever a quantidade de iterações; nesses casos, as duas estruturas podem ser utilizadas.

- exemplo 2:

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




















--- 

[Voltar ao início!](https://github.com/monicaquintal/fintech)