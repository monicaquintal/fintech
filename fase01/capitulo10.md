<div id="fase01" align="center">
<h1>FASE 1 - DEVELOPMENT ENVIRONMENT</h1>
<h2>Capítulo 10: Vamos aprender a programar?</h2>
</div>
<br>

<div align="center">

## Algoritmo

</div>

- é uma sequência ordenada de instruções que visa resolver determinado problema.
- algoritmos e programas não são sinônimos.
- formas mais comuns de representação algorítmica na computação:
  - fluxogramas (diagramas de blocos).
  - pseudocódigos (através de texto, com uma linguagem que apresenta estrutura formasl).

<div align="center">

## Mão na massa

</div>

### Ambiente para programação:

É composto de ao menos duas partes: IDE e interpretador (ou compilador, dependendo da linguagem).

### Tipos de linguagem:

a. `Compilada`: o código é transformado em um arquivo executável que está em código de máquina e pode ser executado por ela. Ou seja, precisamos gerar um código de máquina para cada arquitetura em que quisermo rodar nosso software (Windows, MacOS, Linux).

b.`Interpretada`: o código original não é transformado em código de máquina; é interpretado, ou seja, qualquer máquina que tiver um interpretador instalado conseguirá rodar o código original!

## Etapa 1: Instalando o Python

No caso do Python, há duas versões da linguagem: Python 2.x e Python 3.x. Será utilizada a **versão 3**.

O download pode ser realizado [aqui](https://www.python.org).

## Etapa 2: Conhecendo alguns comandos

Toda linguagem de programação possui algumas `palavras reservadas`, que têm algum significado dentro daquela linguagem (podem ser comandos, por exemplo, que realizam tarefas específicas).

Outro conceito importante é o de `variável`, que comsiste em um espaço que um programa pode reservar na memória RAM do computador, para armazenar temporariamente alguns dados. O Python entende que uma palavra escrita do lado esquerdo do sinal de igual é uma variável, e cria automaticamente!

### Comando `print()`

Usado para exibir uma mensagem na tela do computador.

~~~python
print ("Olá, mundo!")
~~~

### Comando `input()`

Utilizado para para permitir que os usuários digitem informações dentro de variáveis.

Sintaxe:

~~~python
nome_variavel = input (“Mensagem de texto :”)
~~~

Exemplo:

~~~python
nome = input("Por favor, digite seu nome: ")
print(nome + "é um programador incrível!")
~~~

## Etapa 2: Instalando PyCharm

IDEs (Integrated Development Environment): 
- ferramentas usadas para escrever programas em uma linguagem de programação específica. 
- não contêm apenas os editores de texto, mas ferramentas que permitem verificar erros no código, executar o programa diretamente no interpretador ou compilador e, em alguns casos, montar interfaces gráficas.

### Criando o arquivo nome_sobrenome.py

~~~python
print("Esse programa exibirá seu nome completo. ")
nome = input("Por favor, digite seu primeiro nome: ")
sobrenome = input("Por favor, digite seu sobrenome: ")
nome_completo = nome + " " + sobrenome
print("Seu nome completo é: " + nome_completo)
~~~

> diretório PrimeiroProjeto, arquivo nome_sobrenome.py

<div align="center">

## Operadores

</div>

páginas
9/15
23/36