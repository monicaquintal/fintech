<div id="fase05" align="center">
<h1>FASE 5 - OOP</h1>
<h2>Capítulo 03: Pensando software de maneira diferente.</h2>
</div>

<div align="center">
<h2>1. PENSANDO SOFTWARE DE MANEIRA DIFERENTE</h2>
</div>

## 1.1 Introdução

- linguagem Java, linguagem de programação orientada a objetos que será utilizada no desenvolvimento do sistema Fintech.

## 1.2 Linguagem de programação

- consiste em um conjunto limitado de instruções (vocabulário), associado a um conjunto de regras (sintaxe), que define como as instruções podem ser associadas, ou seja, como se pode compor os programas para a resolução de um determinado problema.

### Entendendo o processo

- em meados dos anos 1970, o formato que dominava a programação dos sistemas era chamado de programação estruturada, tendo como base os controles: sequência, condição e repetição, e a subprogramação (ou modularização) utilizando sub-rotinas e funções.
  - nesta categoria encaixam-se as linguagens de programação mais antigas, surgidas em meados dos anos 1960, como Fortran, Cobol, Pascal, C.
- entre as décadas de 1960 e 1980, ocorreu o aparecimento de uma grande quantidade de linguagens.
  - com o aumento da produção de sistemas e necessidade de reaproveitamento de códigos, ocorria desgaste técnico e baixa produtividade no desenvolvimento e peso financeiro às empresas, considerando que atualizações no sistema deveriam ser realizadas em todas as partes em que o código era replicado.
  - o modelo de programação orientada a objetos (POO), com conceitos de objetos da vida real e a criação de moldes para esses objetos, favoreceu toda uma nova linha de sistemas otimizados, reaproveitáveis e de fácil atualização.
  - novas linguagens de programação baseadas nesse paradigma: Delphi, C++, Java, PHP, Ruby etc.

## 1.3 Java

- primeira versão da linguagem Java surgiu em 1995, criada por um time de desenvolvedores da Sun Microsystem, liderado por James Gosling. 
  - a ideia inicial era desenvolver uma linguagem para controlar pequenos dispositivos, como televisores, videocassetes e aparelhos de TV a cabo. 
- se tornou popular pelo uso da internet, e hoje roda em muitos equipamentos e dispositivos: computadores, servidores, celulares, videogames, chips de cartões etc.
- características:
  - `simples:` a sintaxe é uma versão limpa daquela das linguagens da época, como C++. Não há a necessidade de arquivos de cabeçalho ou trabalhar com ponteiros (alocar memória da máquina para armazenar informações).
  - `robusto`: a plataforma Java foi concebida para desenvolver programas confiáveis em vários aspectos. Existe uma verificação preliminar de possíveis problemas, que em outras linguagens só seriam descobertos em tempo de execução.
  - `seguro`: muito utilizada em ambientes de rede/distribuído. 
  - `alto desempenho`: código Java é convertido em bytecodes, que são interpretados em um ambiente de execução do Java para executá-los. Se for necessário mais desempenho, esse ambiente de execução transforma os bytecodes em código de máquina nativo para a CPU específica, ganhando assim desempenho.
- outras duas características determinantes para o sucesso da plataforma Java são a `portabilidade` e a `orientação a objetos`.

### 1.3.1 Portabilidade

- portabilidade do código é a capacidade de ser utilizado em qualquer plataforma/sistema operacional (Windows, Linux, Mac OS) e hardware.
  - ***a linguagem Java é utilizada independentemente da plataforma***!
- `compilação`: 
  - significa transformar o código-fonte (mais fácil para os desenvolvedores) em código de máquina (utilizado pelo computador).
  - linguagens como C e Pascal são compiladas para determinado sistema operacional e arquitetura de hardware. Se for necessário executar em outro ambiente, compilar o programa especificamente para esse ambiente.
  - na linguagem Java, existe uma máquina virtual (`JVM` - Java Virtual Machine), que é capaz de interpretar/executar os arquivos Java compilados.
  - `linguagem Java é Compilada e Interpretada`: os arquivos de código-fonte Java com extensão “.java” são compilados para ***bytecodes*** (arquivos de extensão “.class”). Os bytecodes são interpretados pela JVM, iniciando a execução do software. Para cada plataforma (sistema operacional + hardware), existe uma Máquina Virtual Java, tornando as aplicações Java portáveis.
  - uma vez compilado, podemos executar o programa Java independentemente da plataforma utilizada.

## 1.4 Orientação a objetos

- programação orientada a objetos é um padrão de desenvolvimento que focaliza a construção e interação entre objetos. 
- a essência consiste em tratar os dados e os procedimentos que atuam sobre os dados como um objeto: uma entidade independente com uma identidade e características próprias.

- um `objeto` é gerado a partir de um molde (ou classe), seguindo os princípios do mundo real. Um objeto representa uma entidade que pode ser física, conceitual ou de software:
  - ***Física***: quando representa um modelo físico, como um carro, caminhão, óculos, prédio etc.
  - ***Conceitual***: quando representam formas abstratas ou não palpáveis, como a matemática, um processo químico, o sentimento etc.
  - ***De software***: quando representam objetos de software, como um botão, usuário, arquivo etc.

> Um objeto é uma entidade com fronteira e identidade bem definidas que encapsulam o estado e o comportamento.

- `estado`:
  - representado pelos atributos do objeto; representam as características do objeto em determinado instante.
  - estado normalmente é alterado ao longo do tempo.
  - representam as informações que o objeto possui.

- `comportamento`:
  - é representado pelos métodos que determinam como o objeto age ou reage a uma requisição (chamada) de outro objeto.
  - definem as operações que o objeto pode realizar. 

> A programação orientada a objetos é uma sequência de instruções enviadas ao computador que utiliza e manipula objetos em seu funcionamento!

### 1.5.1 Princípios de orientação a objetos

- são quatro princípios:

1. `Abstração`: 
  - entendimento e análise das necessidades do sistema, abstraindo do mundo real. 

2. `Encapsulamento`: 
  - programar por partes, o mais isolado possível, encapsulando-as. 
  - objetiva tornar o software mais flexível, fácil de modificar e evoluir. 
  - as classes devem proteger as suas informações e comportamentos, ou seja, devem possuir proteção no acesso a seus atributos e métodos.
  - a classe esconde a implementação das outras classes e faz com que estes interajam somente através das interfaces disponíveis.

3. `Hierarquia` (herança):
  - mecanismo pelo qual uma classe pode estender (herdar) de outra classe para receber seus comportamentos (métodos) e estados (atributos).
  - possibilita a criação de novas classes a partir de uma já existente.
  - aplicada como forma de reutilizar os atributos e métodos de classes já definidos, permitindo derivar uma nova classe mais especializada a partir de outra classe genérica existente.
  - **vantagem**: reaproveitamento de código.
  - aplicar herança envolve basicamente dois elementos: uma superclasse ou classe pai e uma subclasse ou classe filha.
    - ***Superclasse*** (ou classe ancestral ou classe pai): apresenta as características genéricas de um conjunto de objetos.
    - ***Subclasse*** (ou classe descendente ou classe filha): estende a superclasse para receber as suas características (herdam). 
  - importante:
    - organização das classes deve ser realizada hierarquicamente.
    - duas perguntas são básicas para essa organização: `IS-A (É-UMA) e HAS-A (TEM-UMA)`. 
    - é necessário perguntar se uma classe É-UMA parte hierárquica de outra classe ou se contém outra classe.

4. `Modularização`:
  - processo de dividir um todo em partes bem definidas, que podem ser construídas e examinadas separadamente e que consigam interagir entre si. A
  - criação de componentes modulares, que podem ser reutilizados para diversos sistemas.

---

## FAST TEST

### 1. Escolha a alternativa que apresenta apenas linguagens de programação orientadas a objetos.
> Java, C++, PHP eRuby.

### 2. Qual das alternativas apresenta corretamente o conceito de Modularização?
> É o processo de dividir um todo em partes bem definidas, que podem ser construídas e examinadas separadamente e que consigam interagir entre si.

### 3. Analise o conceito a seguir: É a capacidade de ser utilizado em qualquer plataforma, neste caso, sistema operacional (Windows, Linux, Mac OS) e hardware. Ou seja, pode ser utilizado independentemente da plataforma. Selecione a alternativa que representa esse conceito.
> Portabilidade do código.

### 4. A linguagem Java tornou-se popular pelo uso da internet e hoje roda em muitos equipamentos e dispositivos: computadores, servidores, celulares, videogames, chips de cartões etc. Em relação à linguagem Java é correto o que se afirma em:
> Os arquivos de código-fonte Java com extensão “.java” são compilados para bytecodes, também conhecidos como arquivos de extensão “.class”.

--- 

[Voltar ao início!](https://github.com/monicaquintal/fintech)