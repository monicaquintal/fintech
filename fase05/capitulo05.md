<div id="fase05" align="center">
<h1>FASE 5 - OOP</h1>
<h2>Capítulo 05: Um pouco de Java nesta forma de pensar. 🤔</h2>
</div>

<div align="center">
<h2>1. UM POUCO DE JAVA NESTA FORMA DE PENSAR</h2>
</div>

## 1.1 Ambiente de desenvolvimento integrado

`IDE` (Integrated Development Environment ou Ambiente de Desenvolvimento Integrado):

- é um programa que visa maximizar a produtividade do desenvolvedor.
- possui várias funcionalidades que auxiliam no desenvolvimento, sendo as mais comuns:
  - editor: editor de código-fonte específico para cada linguagem de programação suportada pela IDE.
  - compilador: compila o código-fonte.
  - debugger (Depurador): executa o programa “passoa passo”, por meio do qual é possível verificar o que ocorre em cada linha do programa, auxiliando no entendimento do sistema e no processo de encontrar e corrigir problemas.
  - modelagem: criação de modelos de classes, objetos, interfaces, associações e interações de forma visual.
  - geração de código: a partir de templates de código comumente utilizados para solucionar problemas rotineiros.
  - deploy (Distribuição): auxilia no processo de gerar o arquivo final para a instalação do programa desenvolvido.
  - testes automatizados: realiza testes no programa de forma automatizada, baseados em scripts ou programas de testes previamente especificados, gerando relatórios que auxiliam na análise do impacto das alterações no código-fonte.
  - refactoring (Refatoração): melhoria constante do código-fonte do programa, seja na construção de código mais otimizado, mais limpo e/ou com melhor entendimento pelos envolvidos no desenvolvimento do software.
- há várias IDEs disponíveis no mercado, destinadas às linguagens de programação ou uma plataforma de desenvolvimento específica. Exemplos: Visual Studio, da Microsoft, Netbeans, da Oracle etc.
- para a plataforma Java existem várias IDEs,como Eclipse, NetBeans, JDeveloper e IntelliJ.

> Para o curso e desenvolvimento do sistema Fintech, vamos utilizar a IDE Eclipse.

## 1.2 Criando um projeto com Eclipse

### 1. menu File > New > Project.

### 2. escolher a primeira opção: Java Project e clicar em Next.

### 3. definir o nome do projeto. 

    - como sugestão, dar o nome de 01-OlaMundo e clicar em Finish.

### 4. antes de finalizar a criação do projeto, o eclipse pode abrir uma janela perguntando se você gostaria de mudar de perspectiva. 
    - o eclipse possui diferentes visões que são associadas ao tipo de projeto/atividade que está sendo executada. 
    - provavelmente, na primeira execução do eclipse ele estará na perspectiva de Java EE, e quando criarmos um Java Project, ele estará associado ao Java SE, por isso aparece o dialog perguntando se gostaria de mudar de perspectiva.
    - neste ponto, não faz diferença a perspectiva que escolher. A qualquer momento, é possível mudar de perspectiva através da opção Window > Open Perspective.

### 5. após escolher a perspectiva, o eclipse irá finalizar a criação do projeto e o resultado poderá ser visualizado na aba de Package Explorer,localizado na janela à esquerda no eclipse.
    - `pasta src` é onde devemos criar os arquivos Java. Abaixo desta pasta, estão localizadas as bibliotecas de classes básicas do Java (`JRE System Library`).

### 6. depois de definir a workspace e criar um projeto, está na hora de criar a nossa primeira classe Java.
    -  para isso, vamos primeiro definir o diretório em que ele será criado.
    - a hierarquia de diretórios para a organização dos arquivos de um programa em Java é denominada `Pacotes`.

> Devemos sempre criar uma estrutura de diretório (pacotes) para organizar os arquivos do sistema. Dessa forma, podemos agrupar as classes em coleções e separá-las das bibliotecas de classes fornecidas por outras empresas.

  - além de organizar, utilizar pacotes garante a singularidade dos nomes das classes.
  - em um sistema, não podemos ter classes com o mesmo nome dentro do mesmo pacote. 
  - porém, não há conflito se as classes estiverem em pacotes diferentes! 
  - para garantir um nome de pacote único, é recomendado utilizar o nome de domínio da internet da empresa (que é único) escrito ao contrário. E depois especificar melhor ainda os pacotes com nome do projeto, tipos de classes etc.
  - exemplo: para a faculdade FIAP, que possui o domínio fiap.com.br e está desenvolvendo um projeto para e-commerce, o pacote será definido como br.com.fiap.ecommerce.

### 7. criar um pacote para o projeto, chamado br.com.fiap.tds, para agrupar as classes do projeto do curso de TDS.
    - clicar com o botão direito do mouse no diretório src e escolher new > package.
    - definir o nome do pacote e finalizar o processo clicando no botão Finish.

### 8. verificar a estrutura que foi criada no disco rígido. 
    - para isso, navegar até a pasta do workspace no Windows Explorer.
    - podemos visualizar uma pasta que representa o Projeto “01-OlaMundo”. Dentro da pasta do projeto, temos a pasta src, com uma estrutura de diretórios do pacote criado. Assim, podemos perceber que cada pasta do pacote é separada pelo “.” (ponto).

### 9. criar a primeira classe Java: clicar com o botão direito do mouse no pacote e escolher New > Class.

### 10. definir o nome da classe: dar o nome de “OlaMundo”e finalizar o processo com o botão Finish.

### 11. o resultado pode ser visualizado na área central do eclipse, onde está localizado o editor de código-fonte.
    - a classe possui uma primeira instrução, que define o pacote da classe: package br.com.fiap.tds.
    - a definição de pacote sempre é feita na primeira linha do arquivo Java, em seguida, temos a definição da classe, conforme o código abaixo:

~~~java
package br.com.fiap.tds;

public class OlaMundo {

}
~~~

- após a `palavra-chave class`, vem o nome da classe. 
  - o nome do arquivo gerado é o mesmo da classe com a extensão .java. 
  - é importante, pois é obrigatório que o nome do arquivo seja o mesmo da classe pública.
  - nomes devem iniciar com uma letra, depois podem conter quaisquer combinações entre letras e dígitos.
  - ***padrão para atribuir nomes a classes*** é utilizar substantivos que iniciam com uma letra maiúscula. 
    - se o nome tiver mais de uma palavra, utilizar “notação camelo” ou “CamelCase”.

- as chaves delimitam os blocos em um programa.
  - neste caso, as chaves delimitam o início e o fim da classe OlaMundo.

> Dentro de uma workspace, definimos os projetos. Projetos podem ter vários pacotes, e estes, por sua vez, podem conter várias classes.

### 12. adicionar um código para executar o programa e exibir informações:

~~~java
package br.com.fiap.tds;

public class OlaMundo {
	public static void main (String[] args) {
		System.out.println("FIAP - Olá Mundo!");
	}	
}
~~~

- o código `public static void main(String[] args)` define o método main, o método principal do programa, por onde a aplicação é inicializada.- - as chaves de abertura e fechamento estão delimitando o início e o fim do método.
- para executar uma classe compilada, a máquina virtual do Java sempre inicia a execução pelo método main.
- a `instrução System.out.println()` exibe na console a informação que está entre os parênteses, neste caso “FIAP – Olá Mundo”. 

> Toda instrução deve terminar com ponto e vírgula (;).

- outro detalhe é o `asterisco antes do nome da classe na aba do editor`; ele indica que a classe não foi salva. 
  - utilizar o atalho CTRL + S ou o botão Save, na barra de ferramentas.

### 13. para executar o programa:

- utilizar o atalho F11 ou o botão “play” localizado na barra de ferramentas.
- há mais uma opção para executar a classe Java: clicar com o botão direito do mouse em cima da classe e escolher as opções: Run As > Java Application.

> O primeiro programa desenvolvido pode ser visualizado [aqui](../fase05/projects/olaMundo/src/br/com/fiap/tds/OlaMundo.java).

---

## 1.3 Fundamentos da programação Java

### 1.3.1 Tipos de dados e variáveis

- `variáveis`:
  - compostas pelo seu nome e o tipo de informação que irá armazenar. 
  - uma variável também pode armazenar um objeto.
  - para declará-la, primeiro é definido o tipo e depois o nome da variável, como:

~~~java
int idade;
double preco;
double taxa, salario;
~~~

- é possível declarar mais de uma variável do mesmo tipo de uma só vez, basta separar o nome das variáveis por vírgulas (,).
- **nomes das variáveis** podem começar com uma letra, um caractere de sublinhado (_) ou $.
  - depois do primeiro caractere, os nomes das variáveis podem conter qualquer combinação de letras ou números. A
  - evitar utilizar acentuação na declaração do nome das variáveis, evitar nomes muito longos.
  - por padrão, o nome da variável deve começar com um caractere em minúsculo e, se for composto por mais de uma palavra, a próxima palavra deve começar com caractere em maiúscula.

> a linguagem Java é `case sensitive`: as letras maiúsculas e minúsculas são diferentes. 

- na linguagem Java existem palavras que não podemos utilizar para nomear as variáveis, classes ou métodos.
  - são as `palavras reservadas`, que possuem significados dentro da programação.
  - abstract, asert, boolean, break, byte, case, catch, char, class, const, continue, default, do, double, else,enum, extends, final, finally, float, for, goto, if, implements, import, instanceof, int, interface, long, native, new, package, private, protected, public, return, short, static, strictfp, super, switch, synchronized, this, throw, throws, transient, try, void, volatile, while.

> `Java é uma linguagem fortemente tipada`, pois cada variável precisa ter um tipo declarado.

- há `oito tipos primitivos` para armazenamento de informações.
  - tipos primitivos não são objetos, são partes internas da linguagem Java, o que os tornam mais eficientes, pois armazenam somente o seu valor.

> A) quatro dos tipos primitivos são para armazenar `tipos numéricos inteiros, positivo ou negativo, sem a parte fracionária`.

<div align="center">

&#32; | Tipos de números inteiros do Java | &#32;
------|-----------------------------------|------
Tipo | Requisito de Armazenamento | Intervalo (inclusive)
int | 4 bytes | -2.147.483.648 a 2.147.483.647 (um pouco acima de 2 bilhões)
short | 2 bytes | -32.768 a 32.767
long | 8 bytes | -9.223.372.036.854.775.808 a 9.223.372.036.854.775.807
byte | 1 byte | -128 a 127

<div>

- a diferença entre os tipos é o tamanho do número que consegue armazenar, e consequentemente, a quantidade de memória necessária para isso. 
- na maioria das situações, o tipo int é o mais utilizado. 
- quando for necessário armazenar um número muito grande, recorrer ao tipo long.

> B) `valores de ponto flutuante` são os números que contêm parte fracionária, ou seja, os números decimais.

<div align="center">

&#32; | Tipos de ponto flutuante | &#32;
------|-----------------------------------|------
Tipo | Requisito de Armazenamento | Intervalo (inclusive)
float | 4 bytes | aprox. +/- 3.40282347E+38F (6-7 dígitos significativos)
short | 8 bytes | aprox. +/- 1.797693134862311570E+308 (15 dígitos decimais significativos)

<div>

- o tipo double é duas vezes mais preciso que o tipo float.

> C) `outros tipos primitivos`:

- tipo char:
  - utilizado para armazenar caracteres individuais, como letras, algarismos, sinais de pontuação, entre outros.

- tipo boolean:
  - possui somente dois valores, verdadeiro (true) ou falso (false). 
  - no Java não é possível converter números inteiros em valores booleanos.

> “E o conjunto de caracteres?”. Na linguagem Java, `String` é uma classe, ou seja, não é um valor primitivo. Dessa forma, ela possui métodos e atributos!

### 1.3.2 Atribuindo valores às variáveis








--- 

[Voltar ao início!](https://github.com/monicaquintal/fintech)