<div id="fase05" align="center">
<h1>FASE 5 - OOP</h1>
<h2>Capítulo 04: Diagramando as estruturas!</h2>
</div>

<div align="center">
<h2>1. DIAGRAMANDO AS ESTRUTURAS!</h2>
</div>

## 1.1 Introdução

- `diagrama de classes`:
  - mostra a estrutura estática do modelo, onde os elementos são representados por classes, com sua estrutura interna e seus relacionamentos. 
  - também é útil na revisão do que é armazenado no sistema e nas estruturas de armazenamento.

---

## 1.2 Conceito de classe

- representada por uma ‘caixa’ com no máximo três compartimentos exibidos:
  - no primeiro compartimento, é exibido o `nome da classe`. Por convenção, no singular e com as palavras começando por maiúsculas.
  - no segundo compartimento, são declarados os `atributos` (informações/dados que um objeto armazena). 
  - no terceiro compartimento, são declaradas as `operações`/métodos (ações que um objeto sabe realizar, funções que uma instância de uma classe pode executar).
- segundo a documentação da UML pelo OMG, uma classe descreve um conjunto de objetos que compartilham as mesmas especificações de atributos, operações, restrições e semântica.
- finalidade de uma classe: classificar objetos e especificar os recursos que caracterizam a estrutura e o comportamento desses objetos.
- os valores dos atributos podem variar entre um objeto e outro, podendo identificá-los individualmente, enquanto ***métodos são idênticos para todos os objetos de uma classe específica***.

### Visibilidades:

- visibilidades são representadas pelos símbolos `–`, `+`, `#` e `~` antes de um atributo ou uma operação. 

<div align="center">

Símbolo | Tipo de visibilidade | Significado
---------|---------------------|----------
&#43; | Visibilidade pública | Atributo/método é visível por outras classes.
&#43; | Visibilidade privada | Visível somente pela própria classe.
&#35; | Visibilidade protegida | Visível para as classes derivadas (indica que as classes abaixo dela, ou seja, herança, podem ter acesso).
&#126; | Visibilidade pacote| Visível pelas classes envolvidas dentro do mesmo pacote.

</div>

- classes podem ser concretas ou abstratas:
  - `classes concretas` são aquelas que geram instâncias, ou seja, constroem objetos.
  - `classes abstratas` não geram instâncias, portanto não constroem objetos.

### 1.2.1 Conceito de tipos de classe

- em um diagrama de classe, as classes podem ser apresentadas em três tipos ou camadas, que estão relacionados com o seu objetivo na modelagem do sistema. 
- são eles: Fronteira, Controle e Entidade.

### 1.2.2 Fronteira

- `classes de fronteira` devem apenas servir como um ponto de captação de informações a partir do ambiente; ou de apresentação de informações que o sistema (modelo) processou. 
- portanto, não devemos atribuir a essas classes responsabilidades relativas à lógica do negócio.
- trata da comunicação do sistema com os atores. 
- pode ser representada por telas, sensores e interface de impressão.
- é responsável por apresentar os resultados de uma interação dos objetos. 
- muitas vezes necessita interagir com outra classe do tipo "Controle".
- pode ser utilizado o modelo expandido com o estereótipo ou o modelo simplificado, que é representado por um círculo com uma barra na frente.

<div align="center">
<img src="../assets/imagens-fase05/notacao-classe-fronteira.png" width="40%"/><br/>
<em>Notação para a classe de fronteira.</em>
</div>

### 1.2.3 Controle

- é o meio de comunicação entre objetos de fronteira e de entidade. 
- age como controlador dos outros objetos para a realização de um caso de uso.
- objetos desta classe interpretam os eventos ocorridos sobre os objetos da classe “fronteira” (movimentos do mouse, pressionamento de botões, entre outros) e os retransmitem aos objetos de classes de entidades que compõe o sistema.
- responsabilidades de uma classe de controle:
  - coordenar a realização de um caso de uso do sistema.
  - servir como canal de comunicação entre objetos de fronteira e de entidade.
  - comunicar-se com outros controladores, quando necessário.
  - mapear ações do usuário (ou atores de forma geral) para atualizações ou mensagens a serem enviadas a objetos de entidade.
  - estar apto a manipular exceções provenientes das classes de entidade.

<div align="center">
<img src="../assets/imagens-fase05/notacao-classe-controle.png" width="40%"/><br/>
<em>Notação para a classe de controle.</em>
</div>

### 1.2.4 Entidade

- classes de entidade são aquelas que representam os conceitos de domínio que o sistema deve processar. 
- representam as informações e as regras de negócio que direcionam a manipulação destas informações.
- representa o conceito do domínio do negócio. 
- representa as informações persistentes, portanto, é responsável pelos objetos persistentes.

<div align="center">
<img src="../assets/imagens-fase05/notacao-classe-entidade.png" width="40%"/><br/>
<em>Notação para a classe de entidade.</em>
</div>

---

## 1.3 Diagrama de classe

- diagrama mais importante e mais utilizado da UML. 
- representa as classes que fazem parte do sistema, ou seja, a estrutura lógica. 
- é um diagrama com visão estática, serve como base de construção para outros diagramas *da maioria dos outros diagramas da UML (como o Diagrama de Sequência e o de Máquina de Estados).

### 1.3.1 Perspectivas de abstração do diagrama de classe

- é possível ter até três perspectivas de abstração do diagrama de classes:

1. ***`Diagrama de classe de análise`***:

- representa as classes com as informações do que o sistema deve fazer em relação à solução do problema.
- ou seja, representa as classes no domínio do negócio.
- representa um modelo conceitual para elementos que tem responsabilidades e comportamento no sistema (por isso são mantidas em alto nível).
- construído durante a fase de análise e utiliza o Diagrama de Caso de Uso para identificação de classes.
- descreve as classes do mundo real e suas relações. 
- não leva em consideração as restrições inerentes à tecnologia que será utilizada na construção do sistema. 
- as informações das classes de análise surgem a partir do enunciado do problema e é independente da linguagem de programação!!!

> A construção de um único diagrama de classe para todo o sistema pode resultar em um diagrama bastante complexo. Uma alternativa é criar uma visão de classes participantes (VCP) para cada caso de uso, um diagrama de classe cujas instâncias (objetos) participam de apenas um caso de uso.

- nesse diagrama não é obrigatório demonstrar as classes de controle e a fronteira.
- também não possui todas as operações, estas podem surgir em conjunto com o desenvolvimento do Diagrama de Sequência.

> O objetivo da VCP (visão de classes participantes) é auxiliar no desenvolvimento de diagramas de classes complexos, mas também pode ser utilizada para representar um estudo sobre determinada funcionalidade em relação às classes envolvidas.

<div align="center">
<img src="../assets/imagens-fase05/exemplo1-classe-de-analise.png" width="70%"/><br/>
<em>Exemplo de Diagrama de Caso de Uso para controle de chamados e soluções.</em>
</div>
<br>
<div align="center">
<img src="../assets/imagens-fase05/exemplo2-classe-de-analise.png" width="70%"/><br/>
<em>Exemplo de VCP para o caso de uso “Registrar Abertura do Chamado”.</em>
</div>

- na fase de análise, quando um diagrama de caso de uso é desenvolvido, é possível observar a fronteira através da interação de um caso. Ou seja, **cada interação do ator com um caso de uso pode ser representada por uma fronteira**.
- para cada caso de uso é representada uma classe de controle que gerencia o fluxo do processo da funcionalidade do sistema, conforme o objetivo determinado no fluxo principal do caso de uso.
- no exemplo acima, há o ator Atendente que “Registra Abertura do Chamado” e terá uma tela de acesso para interação, portanto será necessário criar uma classe de fronteira que é a tela de acesso da funcionalidade do sistema e a classe de controle para gerenciar o fluxo do processo de “Registar Abertura do Chamado”. 

<div align="center">
<img src="../assets/imagens-fase05/exemplo3-classe-de-analise.png" width="70%"/><br/>
<em>Exemplo de Diagrama de Classe de Análise para “Sistema de Controle de Pedido”.</em>
</div>

- o exemplo acima não apresenta as classes de fronteira e de controle, pois podemos optar por não as exibir, para facilitar e simplificar o entendimento.

2. ***`Diagrama de classe de projeto ou especificação`***:

- representa as classes do funcionamento do sistema.
- é construído na fase de projeto do desenvolvimento do sistema,
- **objetivo**: complementar o Diagrama de Classe de Análise. 
- nesta fase, normalmente identificamos a necessidade de criar outras classes, pois esse modelo relaciona a tecnologia utilizada e apresenta todas as camadas de funcionamento do sistema MVC (Model, View e Controller) ou, simplificadamente, a camada de modelo, fronteira e controle.

<div align="center">
<img src="../assets/imagens-fase05/exemplo1-classe-de-projeto.png" width="70%"/><br/>
<em>Exemplo de Diagrama de Classe de Projeto para “Sistema de Controle de Pedido”.</em>
</div>

3. ***`Diagrama de classe de implementação`***:

- representado com base em um padrão de desenvolvimento, conforme uma linguagem de programação orientada a objetos, como Java ou C#. 
- é o menos utilizado no mercado por analistas de sistemas, pois uma vez que já existe o Diagrama de Classe de Análise, não é necessário construir o Diagrama de Classe de Implementação.
- deve seguir o padrão de arquitetura que foi definido ao projeto sob a responsabilidade de um arquiteto de softwares na fase de implementação. 
- somente o Diagrama de Classe de Análise é de responsabilidade do analista de sistemas, com base no problema e nos requisitos necessários para desenvolvimento do sistema.

---

## 1.4 Relacionamentos

- relacionamento descreve como as classes interagem umas com as outras, sendo necessário para a implementação de um comportamento.
- classes costumam ter relacionamentos entre si (associações), que permitem que compartilhem informações entre elas e também colaborem para a execução dos processos executados pelo sistema. 
- uma associação (relacionamento) descreve um vínculo que ocorre entre os objetos de uma ou mais classes.
- relacionamentos são divididos em dois grandes grupos: 
  - associações e 
  - generalizações.

### 1.4.1 Associações

- relacionamento existente entre as classes. 
- possui vários tipos.

- associações possuem algumas `características importantes`: 
  - `multiplicidade`, 
  - `navegabilidade`, 
  - `papéis e nome da associação` e 
  - `direção de leitura`.

> A) Multiplicidade:

- deve-se especificar a multiplicidade entre as classes:
  - `multiplicidade`:
  - é a indicação de quantos objetos podem participar de um relacionamento.
  - multiplicidade das associações indica os números mínimo e máximo de objetos envolvidos em um relacionamento.
  - cada associação em um Diagrama de Classes possui duas multiplicidades, uma em cada extremo da linha de associação.

<div align="center">

Nome | Simbologia
-----|-----------
Apenas um | 1..1 (ou 1)
Zero ou Muitos | 0..* (ou *)
Um ou Muitos | 1..*
Zero ou Um | 0..1
Intervalo Específico | 1i..1s

</div>

> B) Navegabilidade: 

- associação também pode ter `navegabilidade`:
  - pode ser com ou sem setas. 
  - a seta representa qual a direção de leitura da troca de mensagens.
  - na representação sem a seta, não conseguimos identificar a navegabilidade da troca de mensagens, podendo ocorrer para os dois lados.
  - demonstra a direção em que os objetos são transmitidos entre as classes envolvidas.

> C) Papéis e nome da associação:

- os `papéis` indicam qual é a função da classe no contexto do relacionamento.
- `nome da associação`:
  - deve ser utilizado quando não for de fácil interpretação a leitura do relacionamento.
  - ajuda a evitar que existam interpretações equivocadas, principalmente quando ocorrem associações múltiplas (uma mesma classe pode ter mais de uma associação com outra classe).
  - nome da associação normalmente é um verbo e está relacionado ao tipo de relacionamento entre as classes.
  - possui uma seta que representa a direção da leitura do relacionamento.
  - é preferível não nomear associações a usar nomes vagos ou óbvios demais. O mesmo vale para os papéis: em situações que o significado da associação for intuitivo, a utilização só serve para ‘carregar’ o diagrama.

<div align="center">
<img src="../assets/imagens-fase05/exemplo-nomes-e-papeis.png" width="70%"/><br/>
<em>Exemplo de utilização de nome de associação e papéis, sendo que o nome da associação é "Contrata", representando que a Organização contrata Indivíduo.</em>
</div>

### 1.4.2 Associação simples (ou associação binária, entre duas classes)

- representa a conexão entre as classes, isso define que os objetos se relacionam uns com os outros, eles usam os objetos.
- é o relacionamento mais comum.

<div align="center">
<img src="../assets/imagens-fase05/exemplo-associacao-simples.png" width="70%"/><br/>
<em>Exemplo de associação normal ou simples, onde a classe Imóvel pode se relacionar ou não a uma Locação, enquanto Locação obrigatoriamente tem que se relacionar ao imóvel para que o objeto Locação seja construído com todas as características pertinentes ao domínio de negócio (enquanto existir um objeto da classe Locação, deve haver um objeto da classe Imóvel). A navegabilidade para o Imóvel demonstra em que sentido ocorre a troca de mensagens, a Locação usa um Imóvel para ser construído, mas um Imóvel pode ser locado em nenhuma ou em muitas Locações.</em>
</div>

### 1.4.3 Associação por composição

- associações por composição e agregação sempre estão relacionadas a um contexto em que a informação pertence ao negócio.
- a composição é um caso especial de associação.
- definido como um relacionamento todo-parte, ou seja, propagam o comportamento, no sentido de que um comportamento que se aplica a uma classe se aplicará a suas partes, já que uma classe faz parte de outra.
- o objeto parte de uma Composição depende do objeto todo, ou seja, as partes “vivem” e “morrem” como um todo. Neste caso, o objeto parte é essencial para a existência do objeto todo.

<div align="center">
<img src="../assets/imagens-fase05/exemplo-associacao-composicao.png" width="70%"/><br/>
<em>Exemplo de Associação por Composição, onde "a parte" é representada pela classe Item, e "o todo" é a Nota Fiscal. Ao eliminar a classe NotaFiscal, todos os Itens relacionados à Nota Fiscal também serão eliminados, ou seja, "morreram" com a Nota Fiscal. A leitura é um Item formal (<strong>notação de losango fechado</strong>) de uma Nota Fiscal e uma Nota Fiscal tem no mínimo um Item, mas pode ter vários Itens.</em>
</div>

### 1.4.4 Associação por agregação

- é um relacionamento do tipo todo-parte.
- a informação contida no objeto parte é complementar ao objeto todo, não é essencial para constituir a informação relacionada ao conceito do negócio do objeto todo.
- o símbolo da agregação é um **pequeno losango sem preenchimento**, também ao lado do objeto-todo.
- importante:
  - associação de agregação pode ser substituída por uma associação simples, dependendo da visão de quem faz a modelagem.
  - PORÉM, a função principal de uma associação do tipo agregação é identificar a obrigatoriedade de uma complementação das informações de um objeto-todo por seus objetos-parte, quando este for consultado. Já em uma associação simples, essa obrigatoriedade não está explícita!
- em um exemplo de Associação por Agregação, um objeto "Desconto" (objeto-parte) só existirá se houver uma "Venda" (objeto-todo).O Desconto, como objeto-parte, é complementar à Venda e não essencial, portanto, se explica um caso de Agregação (losango sem preenchimento na Venda).

### 1.4.5 Classe associativa

- construídas quando existem Classes com multiplicidade, muitos para muitos nas extremidades, desde que tenham atributos próprios entre elas.
- classes associativas são necessárias nos casos em que existem atributos relacionados à associação que não podem ser armazenados por nenhuma das classes envolvidas.

<div align="center">
<img src="../assets/imagens-fase05/exemplo-classe-associativa.png" width="70%"/><br/>
<em>Exemplo de Classe associativa, em que muitas equipes têm muitos funcionários, mas que as equipes são formadas conforme o ingresso dos funcionários, que têm uma data início e uma data fim para participação na equipe. Portanto, a classe Ingresso representa as instâncias dos objetos que caracterizam a data início e a data fim da participação de Funcionáriosem muitas Equipes.</em>
</div>

### 1.4.6 Associação reflexiva

- tipo de associação que ocorre quando um objeto de uma classe se relaciona com outros da mesma classe: ocorre o autorrelacionamento, mas neste caso, cada objeto tem um papel.
- também conhecida como associação “unária”.

<div align="center">
<img src="../assets/imagens-fase05/exemplo-associacao-reflexiva.png" width="30%"/><br/>
<em>Exemplo de Associação Reflexiva.</em>
</div>

### 1.4.7 Associação n-ária

- utilizadas quando relacionam objetos de no mínimo três classes entre si.
- associação ternária é um caso mais comum de associação n-ária (n = 3).
- na notação da UML, as linhas de associação se interceptam em um losango.

<div align="center">
<img src="../assets/imagens-fase05/exemplo-associacao-ternaria.png" width="70%"/><br/>
<em>Exemplo de Associação Ternária, onde um Cliente pode fazer várias Viagens através de muitas Agências de Turismo, e a mesma Agência oferece muitas Viagens para muitos Clientes, muitas Viagens recebem muitos Clientes de muitas Agências. A associação é ternária, pois o contexto relaciona as três classes entre si.</em>
</div>

### 1.4.8 Associação qualificada

- utilizada na representação de 1..* (um para muitos) ou * (vários para vários).
- o identificador da associação qualificada determina como um determinado objeto no final da associação “n” é identificado, é um tipo de chave para separar todos os objetos na associação, pois este não pode se repetir.

<div align="center">
<img src="../assets/imagens-fase05/exemplo-associacao-qualificada.png" width="30%"/><br/>
<em>Exemplo de Associação QUalificada, onde um Cliente pode ter muitas Contas, mas o que o qualifica, ou seja, o que o identifica é o número da conta que não se repete para cada conta que o Cliente tem e, neste exemplo, uma Conta Corrente pode ter até dois clientes.</em>
</div>

### 1.4.9 Associação exclusiva

- a restrição {ou} representa que, em uma associação, é exclusiva quando pode ocorrer a instância de objetos de uma das classes do relacionamento da associação.

<div align="center">
<img src="../assets/imagens-fase05/exemplo-associacao-exclusiva.png" width="70%"/><br/>
<em>Exemplo de Associação Exclusiva, onde o Contrato de um estacionamento só pode ocorrer para um dos objetos ClienteAvulso ou ClienteMensalista.</em>
</div>

--- 

## 1.5 Interface

- Interface representa um conjunto de serviços, sendo que um serviço é alguma tarefa que uma classe realiza para outra.
- a interface não gera instâncias: quem deve implementar (realizar o que está determinado na interface) são as `classes concretas`.
  - a classe concreta relacionada à interface tem um tipo de relacionamento denominado `realização` (significa que a classe concreta deve implementar os serviços (assinaturas) definidos na interface).
  - portanto, a classe concreta realiza os métodos definidos pela interface.
- o uso de interface está relacionado ao diagrama de classe de projeto ou especificação, e quem define é o projetista ou arquiteto, pois impacta na implementação.
- alguns padrões de implementação usam a interface.
- as `notações para interface` são o estereótipo &lt;&lt;interface&gt;&gt;, o título em negrito da classe, os métodos aparecem em itálico ou simplesmente um pequeno círculo.
- `conceitos para o objetivo de interface`:
  - capturar semelhanças entre classes não relacionadas sem forçar relacionamento entre elas.
  - declarar operações que uma ou mais classes devem implementar.
  - revelar as operações de um objeto, sem revelar a sua classe.
  - facilitar o desacoplamento entre elementos de um sistema.

> Para simplificar o exemplo de interface, imagine uma pessoa que determina que você deve realizar uma tarefa, ela é a interface, e você realizando a tarefa é a classe concreta, que executa o serviço!

<div align="center">
<img src="../assets/imagens-fase05/exemplo-interface.png" width="70%"/><br/>
<em>Neste exemplo há duas Interfaces, onde a classe concreta ContaBancaria implementa os <strong>métodos assinatura (serviço)</strong> das interfaces Manipulável e Administrável. Há também o <strong>relacionamento de realização</strong>, que realização determina que, por exemplo, no caso da interface Manipulável, a classe ContaBancaria deve implementar os métodos criar(), bloquear() e desbloquear().</em>
<br>
<br>
<img src="../assets/imagens-fase05/exemplo-interface2.png" width="70%"/><br/>
<em>Neste exemplo, as classes Cliente, Funcionário e Fornecedor não são relacionadas entre si, mas executam os mesmos métodos de incluir() e excluir(). As três classes implementam os mesmos métodos, portanto são declaradas as operações que uma ou mais classes devem implementar.</em>
<br>
<br>
<img src="../assets/imagens-fase05/exemplo-interface3.png" width="70%"/><br/>
<em>Neste exemplo, os serviços de três classes diferentes são definidos na interface, o que para o sistema mantém uma obrigação de implementação por elas. Assim, uma única interface serve de mandante para várias classes concretas relacionadas a ela (conceito de reutilização).</em>
</div>

--- 

## 1.6 Realização

- é o relacionamento necessário para representar que uma classe concreta use a assinatura (serviço) de uma interface para a implementação de seus métodos.
- este tipo de relacionamento herda o comportamento de uma classe, mas não sua estrutura.
- a notação é uma seta fechada e pontilhada.

--- 

## 1.7 Dependência

- no diagrama de classe de análise é suficiente utilizar as associações e generalizações; já no diagrama de classe de especificação ou projeto, a dependência é mais bem definida por um projetista, pois ***a dependência influencia na implementação***.
- `dependência` significa que uma classe depende dos serviços de outra classe.

<div align="center">
<img src="../assets/imagens-fase05/exemplo-dependencia.png" width="30%"/><br/>
<em>Exemplo de Dependência com parâmetros, onde a classe A depende classes B e C, pois estas são usadas como parâmetros para as operações um e dois.</em>
<br>
<br>
<img src="../assets/imagens-fase05/exemplo-dependencia2.png" width="70%"/><br/>
<em>Outro exemplo de Dependência, em que é contextualizado através da seta pontilhada para as interfaces, o que representa a classe Cliente depende dos serviços criar(), bloquear() e desbloquear() da interface Manipulável, e o que representa a classe Gerente depende dos serviços creditar() e debitar() da interface Administrável.</em>
</div>

---

<div align="center">
<h2>2. Generalização (ou Herança).</h2>
</div>

- é o relacionamento de um objeto mais generalizado com um mais específico; o objeto generalizado é similar aos objetos específicos que recebem os atributos e/ou as operações de um objeto generalizado.
- a classe especializada é denominada **subclasse** e a classe generalizada é a **superclasse**.

<div align="center">
<img src="../assets/imagens-fase05/exemplo-generalizacao.png" width="30%"/><br/>
<em>Exemplo de Generalização, onde as subclasses são ClienteMaster e ClienteVisa, e a superclasse é Cliente.</em>
</div>

- notação para Generalização ou Herança:

<div align="center">
<img src="../assets/imagens-fase05/notacao-generalizacao.png" width="30%"/><br/>
<em>Representações alternativas para o relacionamento da generalização na UML, com uma seta e as subclasses relacionadas em uma linha ou uma seta para cada subclasse apontando para a superclasse.</em>
</div>

## 2.1 Hierarquia de generalização

- no relacionamento de hierarquia de generalização, as classes mais específicas podem ser construídas a partir de mais de uma classe generalizada hierarquicamente.
- uma classe é generalização de outra se toda instância desta última for também instância da primeira.

<div align="center">
<img src="../assets/imagens-fase05/exemplo-hierarquia-de-generalizacao.png" width="70%"/><br/>
<em>Exemplo de hierarquia de generalização ou herança, em que há uma hierarquia de quatro níveis: o Funcionário recebe "nome" da classe Pessoa, a classe Atendente tem "nome" e "códFuncionário" e "departamento". A classe OperadorTelemarketing tem "nome", "códFuncionário", "departamento", e ainda tem "nível", que é atributo próprio da classe.</em>
</div>

## 2.2 Generalização – restrições

- no diagrama de classe é possível contextualizar algumas restrições.
- são apresentadas entre chaves ( { } ). 
- as restrições estão relacionadas aos conceitos das informações que a classe representa e podem ser:
  - **sobreposta**: na hierarquia das classes, podem ser construídas classes que herdam de mais de uma subclasse, no nível vertical.
  - **disjunta**: as classes que são construídas podem herdar somente de um nível da superclasse na vertical.
  - **completa**: todas as subclasses possíveis já foram construídas na hierarquia horizontal, abaixo da superclasse.
  - **incompleta**: ainda é possível criar subclasses na horizontal, abaixo da superclasse.

<div align="center">
<img src="../assets/imagens-fase05/generalizacao-completa-disjunta.png" width="30%"/><br/>
<em>Exemplo de Generalização Completa e Disjunta, em que a classe Pessoa tem somente a representação de Homem e Mulher, não sendo possível criar mais subclasses na horizontal. Neste exemplo também é disjunta, o que significa que não é possível criar mais nenhum nível na vertical abaixo das classes Feminino ou Masculino.</em>
<br>
<br>
<img src="../assets/imagens-fase05/generalizacao-incompleta-sobreposta.png" width="30%"/><br/>
<em>Neste exemplo de Generalização Incompleta e Sobreposta, existem mais Atletas além de Nadador e Corredor, e a generalização é incompleta, pois é possível criar mais subclasses na horizontal, por exemplo, lutador de Jiu-jítsu, que é outro tipo de atleta. É sobreposta neste caso, pois é possível criar subclasses abaixo de Corredor e Nadador com suas especificidades, por exemplo, Nadador de cem metros nado livre.</em>
</div>

## 2.3 Classe abstrata

- classes que não geram instâncias diretas são denominadas classes abstratas.
- utilizadas para reaproveitar, organizar e simplificar uma hierarquia de generalização baseada em uma informação válida nessa hierarquia.
- as subclasses de uma classe abstrata também podem ser abstratas, mas a hierarquia deve terminar em uma ou mais classes concretas, que devem gerar a instância dos objetos.
- notação é o estereótipo com a palavra &lt;&lt;abstract&gt;&gt;, e o nome da classe fica em negrito.
- **objetivo**: reaproveitamento, a reutilização para uma implementação que possa facilitar a manutenção.
- classes abstratas também surgem no modelo do Diagrama de Classe de projeto ou especificação, pois podem impactar na implementação.

<div align="center">
<img src="../assets/imagens-fase05/exemplo-classe-abstrata.png" width="30%"/><br/>
<em>Exemplo de classe abstrata, que possui uma classe abstrata para Pessoa. As classes Professor e Alunosão instanciáveis e recebem da classe abstrata Pessoa os atributos cpf e nome, e a operação incluir().</em>
</div>

## 2.4 Técnicas para construir um diagrama de classe

- inicialmente devemos pensar:
  - qual é o negócio?
  - o Diagrama de Caso de Uso auxiliará na construção do Diagrama de Classe?
  - quais técnicas devo utilizar?
  - quais são os passos para construir o Diagrama de Classe?

- primeiro, são construídos o Diagrama de Classe de Análise, desenvolvido pelo analista de sistemas.
  - caso o projeto tenha o envolvimento de algum arquiteto de software, o Diagrama de Classe de Análise receberá as classes necessárias para o sistema funcionar e poderá ser construído o Diagrama de Classe de Projeto ou Especificação, conforme a tecnologia envolvida.

> O papel da análise do sistema é entender o que o sistema deve fazer para atender a uma determinada necessidade de negócio, e na fase de análise deve desenvolver o Diagrama de Classe de Análise ou Domínio para demonstrar quais são os objetos de negócio pertinentes ao sistema.

- é muito importante que você tenha o processo de negócio, as regras de negócio e o Diagrama de Casos de Uso.
- a UML não obriga a utilização de um diagrama para construção de outro, mas as metodologias e boas práticas sugerem que, para seguir um padrão, seja utilizado o Diagrama de Caso de Uso para fazer abstrações das classes.
- técnicas:

### 2.4.1 Análise do caso de uso






--- 

[Voltar ao início!](https://github.com/monicaquintal/fintech)