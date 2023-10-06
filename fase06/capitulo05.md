<div id="fase06" align="center">
<h1>FASE 6 - MODEL</h1>
<h2>Capítulo 05: Exceções à regra.</h2>
</div>

<div align="center">
<h2>1. EXCEÇÕES À REGRA</h2>
</div>

## 1.1 Introdução 

- capítulo dedicado a conceitos avançados de orientação a objetos e sua aplicabilidade em Java (possibilidade do polimorfismo, classes abstratas e o uso de exceções para tratar as falhas às quais todo software está sujeito).

## 1.2 Tratamento de exceções

- durante a execução de um programa, é possível que algumas exceções ou erros aconteçam.
- alguns dos problemas mais comuns: 
  - falha na aquisição de algum recurso, como abrir um arquivo, conectar com o banco de dados ou acessar um web service.
  - tentativa de realizar algo impossível, como a divisão de um número por zero, acessar uma posição que não existe em um array.
  - outras condições inválidas, como evocar um método de um objeto que não foi instanciado ou realizar um cast inválido.
- esses eventos não esperados geralmente interrompem o fluxo da execução do código.
- o tratamento de exceções permite verificar esses eventos (erros) e realizar uma ação sem prejudicar o fluxo do programa.
- em geral, o fluxo para o tratamento de exceções no Java ocorre em `três passos`:
  - ***uma exceção é lançada***: um comando do código dispara uma condição inesperada de erro.
  - ***a exceção é capturada***: em algum ponto do código, podemos adicionar um comando para capturar a possível exceção.
  - ***o tratamento de erro é realizado***: após a captura da exceção, o tratamento de erro adequado é executado.

> IMPORTANTE: Realizando o tratamento das exceções, o programa consegue continuar a execução normalmente. Exceções não capturadas provocam a finalização do programa.

## 1.3 Classificação

- uma exceção é um objeto do tipo Exception.
- no polimorfismo, um objeto desse tipo pode ser qualquer instância de uma subclasse de Exception.
- dentro da plataforma Java, podemos classificar as exceções em:
  - `Checked`: exceção que deve ser tratada ou relançada pelo desenvolvedor, geralmente herda da classe Exception. 
  - `Unchecked`: exceção que pode ser tratada ou relançada pelo programador. Essa exceção é gerada pelo código mal escrito. Caso a exceção não seja tratada, ela será automaticamente relançada. Geralmente, esse tipo de exceção herda de RuntimeException.
  - `Error`: erro crítico, utilizado pela JVM para indicar que existe um problema que não permite a continuação da execução do programa.

<div align="center">

Classe | Objetivo | Erro
-------|----------|--------------
Error | Erro que não pode ser tratado na aplicação. Lançado pela JVM indicando que o programa não pode continuar a execução. | OutOfMemoryError: indica que não há memória suficiente na máquina para continuar a execução do programa.
Exception | Exceção que deve ser tratada pelo desenvolvedor. | ArithmeticException: indica que houve alguma operação aritmética inválida, exemplo: divisão por zero.
RuntimeException | Exceção que pode ser tratada pelo desenvolvedor. | NullpointerException: indica que há uma tentativa de acessar algum método ou atributo de uma classe que não foi instanciada.

</div>

- além das exceções existentes na plataforma, podemos criar as nossas próprias exceções, sejam elas checked (filhas de exception) ou unchecked(filhas de RuntimeException).
- hierarquia de classes de exceções do Java:

<div align="center">
<img src="./assets/hierarquia-excecoes.png" width="50%"/><br/>
</div>

- a classe Throwable tem duas subclasses: Exception e Error:
  - Exception é a classe base para as subclasses de exceções checked e unchecked, exceções que devem ou podem ser tratadas. 
  - Error é a base para as classes de exceções que não podem ser tratadas.
- `exceções mais comuns em Java`:

1. ***ArithmeticException***:

- exceção unchecked.
- ocorre quando alguma operação aritmética é inválida; operação esta que não pode ser resolvida, como é o caso da divisão de um número por zero.

2. ***ArrayIndexOutOfBoundsException***:

- exceção do tipo unchecked (o desenvolvedor não é obrigado a tratar a exceção).
- acontece quando tentamos acessar uma posição inválida de uma matriz ou vetor (array). 
  - uma posição inválida é uma posição que não existe (negativa ou valor igual ou maior que o tamanho do vetor). 
  - lembre-se: o índice do vetor sempre começa em zero, ou seja, não existe posição negativa e o último elemento de um array está posicionado no tamanho do vetor menos um.

3. ***NullpointerException***:

- é uma exceção unchecked, mais conhecida e comum durante o desenvolvimento.
- ocorre na tentativa de acessar um objeto que ainda não foi instanciado.
- exemplo: quando tentamos acessar o método size() de um ArrayList que ainda não foi instanciado. 

4. ***FileNotFoundException***:

- exceção checked.
- precisamos tratar quando tentamos acessar um arquivo que não foi encontrado.

5. ***NumberFormatException***:

- não precisa ser tratada (unchecked).
- ocorre quando tentamos transformar uma string inválida em algum tipo numérico. 

## 1.4 Captura e tratamento de exceções

- para tratar as exceções (checked ou unchecked) em tempo de execução, elas devem ser capturadas e tratadas. 
- o Java possui duas estruturas importantes para o tratamento de exceções: `try-catch` e `try-catch-finally`.
- essas estruturas têm a finalidade de separar o código que executa as tarefas desejadas das rotinas de tratamento das exceções.

~~~java
try {
  //Código
} catch(Excecao) {
  //Tratamento da exceção
}
~~~

- o `bloco try` tem um código que pode gerar uma exceção, ou seja, esse trecho de código será monitorado pela JVM. 
  - se um erro for gerado, o fluxo da execução será desviado para o bloco catch, para o tratamento do erro.
  - o uso do try indica que o código está tentando realizar algo “perigoso”, passível de erro. 
- o `bloco catch` só é executado se uma exceção for gerada. 
  - caso nenhuma exceção seja lançada, a execução pula o bloco catch e continua normalmente. 
  - se uma exceção for lançada, o bloco try é finalizado e o fluxo de execução procura por um bloco catch adequado para tratar a exceção.
  - depois de executar o bloco catch, a execução do programa continua na primeira instrução após o último bloco catch.
  - podemos adicionar vários blocos catch para capturar diferentes tipos de exceções:

~~~java
try {
  // Código
  } catch (Excecao1) {
    // Tratamento da exceção 1
  } catch (Excecao2) {
    //Tratamento da exceção 2
  } catch (Excecao3) {
    //Tratamento da exceção 3
}
~~~

- os catches são testados de cima para baixo, um por um, até que o catch apropriado seja executado, por isso as exceções mais específicas devem ser colocadas nos primeiros catches, sempre obedecendo à ordem das exceções mais específicas para as mais genéricas.
- a `exceção Exception` é a mais genérica possível, pois todas as exceções (checked ou unchecked) são filhas dela. 
  - portanto, a captura dessa exceção deve ser colocada no último catch, pois ela captura qualquer tipo de exceção que for lançada.
  - se nenhum catch conseguir capturar a exceção lançada, ela não será tratada, como se não existisse o bloco try-catch.
  - exemplo:

~~~java
Scanner sc= new Scanner(System.in);
//Lê os dois números
int numero1 = sc.nextInt();
int numero2 = sc.nextInt();
//Realiza a divisão
int divisao = numero1/numero2;
//Exibe o resultado
System.out.println("O resultado é: "+ divisao);
sc.close();
~~~







--- 

[Voltar ao início!](https://github.com/monicaquintal/fintech)