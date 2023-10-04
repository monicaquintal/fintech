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








--- 

[Voltar ao início!](https://github.com/monicaquintal/fintech)