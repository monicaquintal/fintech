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
  - **fluxo principal** trata-se do caminho perfeiro, onde o ator consegue obter exatamente o resultado esperado.
  - **fluxos alternativos** são as “opções” de ações que um ator pode realizar.
  - **fluxos de exceção** são indicações de como um dos atores (cliente ou sistema) reagirá caso encontre uma situação excepcional.
- exemplo:

Item | Valor
------|-------------
Caso de Uso | UC01 - Comprar cerveja
Sumário | Permite que o usuário efetue a compra de cerveja
Ator | Cliente
Precondição | Ter estoque disponível
Pós-condição | Registrar a compra e o pagamento
Fluxo principal | FP01 - O cliente seleciona a cerveja que deseja comprar. FP02 - O cliente informa a quantidade desejada. FP03 - O sistema verifica se há estoque disponível. FP04 - O sistema calcula o valor total da compra.
Fluxo(s) alternativo(s) | FAO01 - O cliente pode alterar a quantidade desejada. O sistgema retorna ao FP03.
Fluxo(s) de exceção | FE01 - O sistema exibe a mensagem "cerveja indisponível". Encerra o caso de uso.

### 2. Caso de Uso:

- o caso de uso especifica uma sequência de ações realizadas pelo sistema que produzem um resultado perceptível e de valor para o ator.
- caso de serviço interrompido: é uma história que descreve um serviço interrompido.
- portanto, caso de uso descreve uma sequência completa de interações, ou seja, como se relacionarão as funcionalidades umas com as outras e como serão utilizadas pelo usuário (ator) durante o funcionamento do sistema.
  - para descrever essa interação, utiliza-se uma metodologia que serve para padronizar a descrição da funcionalidade.
  - o desenvolvedor utilizará o caso de uso para implementar o sistema, ou o analista validará o desenvolvimento ou fará os testes, e entenderão a funcionalidade de uma maneira única!
- o caso de uso não representa um passo ou uma etapa em uma funcionalidade do sistema; é a especificação detalhada de uma das funcionalidades!
- ***como identificá-los***:
  - O que o ator pode fazer ao utilizar o sistema?
  - O ator precisa registrar, consultar, alterar ou excluir dados ou informações do sistema?
  - O ator será notificado sobre eventos do sistema?
  - O ator precisa informar o sistema sobre algum evento?
  - Há comunicação com outros dispositivos?
  - Há comunicação com outros sistemas?

### 3. Ator:

- corresponde a um papel representado por algo ou alguém, sendo qualquer elemento externo ao sistema (humano, hardware, dispositivo ou sistema externo que interage com o sistema em questão).
- é quem interagirá (trocará informações) com o sistema.
- sua representação é feita por um boneco e um rótulo com o nome.
  - quando o ator é humano: identificar com o nome do papel que executa, como funcionário, usuário, cliente ou atendente.
  - para representar um sistema, um módulo ou componente de outro sistema (externo ao que está sendo documentado; a equipe desconhece seu escopo e é alheia a qualquer responsabilidade), utiliza-se um ator sistêmico.
    - o sistema documentado é usuário desse sistema externo ou serve a ele, e o sistema externo torna-se, portanto, usuário dele.
    - no diagrama, deve possuir seu nome de fato (se o ator é o sistema “legado”, esse deve ser o seu nome).
- interage com o sistema, dando estímulos necessários para que ocorra troca de informações com as funcionalidades.
- externo ao sistema, ficam fora da fronteira.
- ***como identificar os atores:***
  - Quem usa o sistema?
  - Quem inicializa o sistema?
  - Quem fornece os dados?
  - Quem remove os dados?
  - Quem usa as informações?

### 4. Fronteira:

- delimita o limite do nosso sistema, compreendendo todos os seus casos de uso.
- constitui-se dos casos de uso que compõem o sistema, ou seja, é o limite do sistema.
- representada por um retângulo.
- a sigla UC no canto superior do retângulo identifica que cada um deles é um caso de uso (user case) diferente.

### 5. Relacionamento:

- a estruturação do modelo de caso de uso envolve a utilização dos seguintes tipos de relacionamento:
  - comunicação: indica qual caso de uso o ator vai interagir (linha sólida).
  - inclusão: apenas casos de uso (linha tracejada, a ponta da seta aponta o caso de uso incluido), relação de obrigação.
  - extensão: apenas em casos de uso, indica condição (linha tracejada, apontada para o caso de uso que solicita a extensão).
  - generalização: ocorre somente entre atores OU entre casos de uso. Associa características semelhantes, e permite concentrar-se às diferenças.
- no modelo de caso de uso, pode haver relacionamentos entre:
  - o ator e o caso de uso;
  - atores (um ator e outro ator);
  - casos de uso (um caso de uso e outro caso de uso).
<br>

***a. Associação por comunicação:*** 
<br>

- o relacionamento mais utilizado de um ator para com um caso de uso é a associação por comunicação (o ator executa a funcionalidade especificada no caso de uso).
- também conhecido como associação por comunicação.
- indica com qual caso de uso um determinado ator troca informações. 
- um ator pode interagir com mais de um caso de uso do sistema.
- é representada por uma linha sólida:
  - se a linha sólida contém a cabeça de flecha: somente o elemento que está no fim da flecha pode iniciar a comunicação.
  - caso a linha sólida não tenha a cabeça de flecha, então, quaisquer dos dois elementos, o caso de uso ou o ator, podem iniciar a interação.
<br>

***b. Associação por inclusão:*** 
<br>

- conecta o caso de uso base ao caso de uso incluído.
- esse tipo de relacionamento existe somente entre casos de uso.
- identifica um processo obrigatório (o caso de uso incluído será executado sempre que o caso de uso base for executado).
- o caso de uso base pode ter sua execução dependente do resultado do caso de uso incluído.