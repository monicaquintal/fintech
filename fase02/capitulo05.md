<div id="fase02" align="center">
<h1>FASE 2 - PROTOTYPING</h1>
<h2>Capítulo 05: Entendendo o ponto de vista do usuário. 👤</h2>
</div>

<div align="center">

## UML

</div>

## O que é `UML`?

- Linguagem de modelagem unificada.
- é uma linguagem visual para modelagem de sistemas.
- o aprendizado em UML começa com um diagrama essencial: o `Diagrama de Casos de Uso`:
  - utilizado para documentar o sistema sob o ponto de vista do usuário, formalizando o que ele pode ou não fazer. 

## `Modelo de Caso de Uso`

- possui três objetivos: 
  - descrever as necessidades do cliente.
  - definir a base do sistema a ser implementado.
  - estabelecer um conjunto de requisitos que serão validados quando o projeto for construído.
- é composto pelo Diagrama de Caso de Uso e suas documentações (descrições textuais).
- a técnica de modelagem de caso de uso que representam graficamente os Requisitos Funcionais do sistema são os Diagramas de Caso de Uso.

<br>
<div align="center">
<img src="../assets/imagens-fase02/objetivos-caso-de-uso.png" width="50%"><br>
<em>Objetivos do modelo de caso de uso.</em>
</div>

- o modelo de caso de uso é elaborado durante as reuniões entre a equipe de desenvolvimento do sistema e as partes interessadas(stakeholders).
- tem como ***objetivo*** especificar os requisitos.
- composto do Diagrama de Caso de Uso e da descrição dos casos de uso (usualmente, uma descrição textual).
- a técnica de modelagem de caso de uso é a representação gráfica utilizada para descrever os requisitos de um sistema (conhecida como Diagrama de Caso de Uso).

## Conceito do modelo de caso de uso

- representação das funcionalidades externamente perceptíveis do sistema e dos elementos externos que trocam informações com ele.
- descreve os requisitos funcionais de um sistema sob o ponto de vista do usuário.
- a construção desse modelo associa:
  - funcionalidades do sistema (casos de uso),
  - seu ambiente operacional (atores) e
  - relacionamento entre eles (comunicação entre os atores e os casos de uso).
- ***objetivos***: especificar,construir e documentar o comportamento de cada parte que o sistema deve possuir.

## Elementos do modelo de caso de uso

- a construção desse modelo implicaa definição de diversos elementos relevantes ao sistema que será desenvolvido: cenário, caso de uso, ator, fronteira e os relacionamentos.

<br>
<div align="center">
<img src="../assets/imagens-fase02/elementos-caso-de-uso.png" width="50%"><br>
<em>Elementos de caso de uso.</em>
</div>

### 1. Cenário:

- um cenário é a descrição de uma das maneiras pelas quais um caso de uso pode ser executado ou realizado, também conhecido como ***instância de um caso de uso***.
- representa uma sequência de passos que descrevem uma interação entre um usuário e um sistema, detalhando o caminho do ponto inicial até o ponto final de um fluxo de eventos.
- fluxos:
  - pode envolver o Fluxo Principal e os Fluxos Alternativos ou de Exceção em qualquer combinação. Contudo, ***sempre começa pelo Fluxo Principal***!
  - fluxos alternativos são as “opções” de ações que um ator pode realizar.
  - fluxos de exceção são indicações de como um dos atores (cliente ou sistema) reagirá caso encontre uma situação excepcional.
