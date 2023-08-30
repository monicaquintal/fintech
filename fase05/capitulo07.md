<div id="fase05" align="center">
<h1>FASE 5 - OOP</h1>
<h2>Capítulo 07: Quando as partes conversam.</h2>
</div>

<div align="center">
<h2>1. QUANDO AS PARTES CONVERSAM</h2>
</div>

## 1.1 Diagrama de Interação

- o Diagrama de Sequência será importante para entender como os objetos vão interagir com a troca de mensagens.
- `Diagramas de Interação`:
  - objetivos: 
    - demonstrar a relação dos objetos em determinado processo.
    - demonstrar o comportamento interno do sistema, auxiliando no esclarecimento dos casos de uso pela representação do funcionamento do processo por meio da troca de mensagens entre os objetos,
  - na versão 2.5 da UML, estão no grupo dos Diagramas de Interação: Diagrama de Visão Geral de Interação, Diagrama de Tempo, Diagrama de Comunicação e o Diagrama de Sequência. 
  - até a versão 1.5 da UML, o Diagrama de Comunicação era conhecido como Diagrama de Colaboração.

> Um `Diagrama de Interação` mostra uma interação formada por um conjunto de objetos e seus relacionamentos, incluindo as mensagens que poderão ser trocadas entre eles.

> O objetivo do `Diagrama de Sequência` é apresentar as interações entre os objetos na ordem temporal em que elas acontecem.

- ***diferenças*** entre o Diagrama de Sequência e o Diagrama de Comunicação é:

<div align="center">

Diagrama de Comunicação | Diagrama de Sequência
------------------------|--------------------
- não existe a representação de tempo em que o objeto está sendo utilizado. | - é possível verificar claramente esse momento.
- não podemos demonstrar uma fragmentação do processo. | - é possível demonstrar uma fragmentação do processo.
- utilizado para modelar processos mais simples. | - o mercado utiliza muito mais o Diagrama de Sequência.

</div>

<div align="center">
<img src="../assets/imagens-fase05/diagrama-de-comunicacao1.png" width="50%" /><br />
<em>Diagrama de Comunicação – Processo Reservar Mesa.</em>
</div>

- no exemplo acima, o cliente informa a mesa e o CPF, e a classe de controle inicia o processo para que a reserva troque mensagens com o cliente e a mesa para criar uma reserva.

---

## 1.2 Conceito de mensagem

- representa a requisição de um objeto remetente a um objeto receptor para que este último execute alguma operação definida para sua classe.
- a mensagem deve conter informação suficiente para que a operação do objeto receptor possa ser executada.
- é um estímulo utilizado para demonstrar quando um método é solicitado para que realize a sua operação dentro do processo.

---

## 1.3 Diagrama de Sequência

### 1.3.1 Conceito

- Diagrama de Sequência representa a ordem lógica da troca de mensagens entre os objetos de um caso de uso.
- demonstra o processamento a partir de solicitações e de execuções dos métodos entre os objetos.
- é um diagrama comportamental que procura determinar a sequência de eventos que ocorrem em um processo.
- ***é desenvolvido por caso de uso***!
- faz o papel da documentação de caso de uso, que pode ser utilizada para conferir a ocorrência do processo existente no caso de uso.
- nos projetos com muitos casos de uso, podem ser desenvolvidos os Diagramas de Sequência dos processos que tenham maior complexidade.

> como boa prática para um projeto, é ideal que a modelagem de classes seja realizada em conjunto com o Diagrama de Sequência, pois um diagrama complementa o outro!

### 1.3.2 Notação

- exemplo:

<div align="center">
<img src="../assets/imagens-fase05/diagrama-de-sequencia1.png" width="50%" /><br />
<em>Diagrama de Comunicação – Processo Reservar Mesa.</em>
</div>







--- 

[Voltar ao início!](https://github.com/monicaquintal/fintech)