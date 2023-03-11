<div id="fase01" align="center">
<h1>FASE 1 - DEVELOPMENT ENVIRONMENT</h1>
<h2>Capítulo 07: Técnicas nunca são demais...</h2>
</div>
<br>

<div align="center">

## Planejamento do Sprint

</div>

`Sprint`: 
- ciclo determinado por um timebox representando uma iteração para a construção do produto definido. 
- as histórias que o compõem são definidas pelo PO e as atividades e prazo são responsabilidade do time.
- cada Sprint é um timebox que dura de ***1 a 4 semanas*** e sempre deve entregar valor ao cliente. 
- um Sprint deve ter, no máximo, 1 mês de duração.
- a data final é definitiva.

***Orientação inicial para `definir o tamanho`***:
- um time começando a executar projetos com Scrum deve usar Sprint de 2 semanas para que as adaptações sejam mais rápidas.
- os primeiros Sprints de um projeto novo devem ser mais curtos, de até 2 semanas, para minimizar os riscos e adaptar o time.
- Product Backlog tem muitas mudanças de priorização pelo Product Owner que podem indicar indecisões ou incertezas. Neste caso, recomenda-se usar Sprints mais curtos para minimizar riscos.
- Sprints de 3 ou 4 semanas para reduzir o ritmo de entregas e permitir mais experimentação ou prototipagem.

> Antes de iniciar o Sprint, o time e o PO devem definir uma META específica que esteja alinhada à meta do release e atenda às expectativas do cliente. O Scrum Master deve garantir que nenhuma mudança possa afetar a meta do Sprint.

***O Sprint Planning é a segunda parte da reunião de planejamento e realiza-se antes da execução de cada Sprint.***

Tamanho do Sprint | Timebox da Reunião 
------------------|-------------------
4 semanas | 8 horas
3 semanas | 6 horas
2 semanas | 4 horas

<em>A Sprint Planning também é uma reunião do tipo timebox, definido no Scrum Guide®, que deve ter tempo de duração fixo, conforme quadro acima.</em>

### Etapas do planejamento do Sprint

1. Primeira atividade: definir a meta do Sprint!
2. Após definir a meta, escolher os itens mais importantes do Product Backlog.
3. Avaliar cada item do Product Backlog e verificar a possibilidade de entrega dentro do prazo: baseada na capacidade do time (velocidade) e no conhecimento.
- Para cada item do Product Backlog, decompor em atividades e fazer a estimativa de tempo (em horas) ou esforço (em story points) para fazer tudo o que é necessário para concluir cada atividade do Sprint.
- O resultado final deste trabalho é chamado de `Sprint Backlog`!

### Resumindo...

- Time: definir a meta do Sprint.
- PO: definir as histórias do Sprint.
- Time: decompor em atividades e estimar a duração.
- Time: montar Sprint Backlog.

---

## `Sprint Backlog`

- Contém as atividades necessárias para completar as histórias selecionadas do Product Backlog e atingir a meta do Sprint.
- As atividades devem ser estimadas em horas ou em pontos.
- Normalmente, o Sprint Backlog utiliza o `quadro Kanban`, organizado em colunas.
  - colunas mais comuns: A Fazer(To Do); Fazendo (Doing)e Feito (Done).
  - apriorização é feita colocando as atividades de cima para baixo, inserindo cores, etc.

> Novas atividades podem ser adicionadas ao Sprint Backlog durante o Sprint, desde que não afetem o timebox definido e não ameaçem a entrega da meta do Sprint (mas novas histórias, não!).

### Conceito de Ready (DoR, Definition of Ready)

- verificar se a história está clara e se todos os membros do time têm compreensão.
- cada organização e/ou cada time define quais são os requisitos necessários para considerar que a história está OK.
- normalmente é realizado por meio de checklist sobre cada história.
- pode ser revisado na Retrospectiva.

### Reunião de Refinamento

- busca melhorar a definição das histórias do Product Backlog, para que esteja em um nível de maturidade melhor antes da próxima reunião de planejamento do Sprint (revisar os itens do Product Backlog para esclarecer todos os pontos e dúvidas do time).
- realizada dois a três dias antes do final do Sprint e antes da próxima reunião de planejamento do Sprint.
- liderada pelo PO e com participação de 10% a 50% do time.
- duração de 1 a 2h para cada Sprint.
- não são obrigatórias no SCRUM.

### Conceito de Pronto (DoD,Definition of Done)

- estabelecido pela organização ou time SCRUM, e deve ser atendido minimamente por todos os times.
- objetivo: maior transparência ao processo de formalização de que um Sprint está concluído, e garante a qualidade dos itens desenvolvidos.
- checklist.
- aplicado antes de liberar o incremento do Sprint para a revisão do PO e stakeholders na reunião de Revisão.

> A ***diferença entre DoR e DoD*** é que o DoR é aplicado antes de o Sprint iniciar, e o DoD é aplicado antes de o Sprint terminar!!!

---

## SABE QUANDO O CLIENTE PERGUNTA SE ESTÁ PRONTO? COMO VOCÊ SABE O QUE É PRONTO?

### Testes de aceitação
- não é uma atividade do framework Scrum, mas auxilia na validação das funcionalidades construídas, aumentando a qualidade do produto!
- escritos pelo PO com auxílio do SM.
- deve fazer parte do processo de elaboração do produto.
- também pode ser utilizado o BDD [Behavior Driven Development](https://www.agilealliance.org/glossary/bdd/) para auxiliar na elaboração dos testes; o BDD consiste em ter as visões técnicas e de negócio juntas, permitindo identificar os comportamentos esperados do produto em linguagem o mais natural possível.

### Execução do Sprint

- O Sprint Backlog é um artefato que deve ser atualizado diariamente.
- No final do dia, as atividades a concluir devem ter seus esforços atualizados, para que o time avalie quanto ainda falta do trabalho a ser realizado, gerando o ***Sprint Burndown***.

***Importante:***
- `um Sprint só pode ser cancelado em casos extremos`, em que o PO percebe mudanças relevantes que ocorreram e afetaram a relevância de valor de negócio da meta do Sprint!!! Apenas o PO tem autoridade para cancelar Sprint.
- a `Reunião Diária`:
  - curta duração.
  - geralmente no início do dia de trabalho.
  - comumente realizada em pé.
  - 15 minutos.
  - **Questionamentos:** O que foi realizado desde a última reunião? O que vai realizar até a próxima reunião? Quais são os impedimentos em suas tarefas?
  - problemas/dúvidas são slassificados como impedimentos e passados ao SM.
  - faz parte do ciclo de inspeção e adaptação prevista nos pilares do Scrum.

---

## Burndown Chart

- ferramenta de medição visual, que permite a visualização do andamento do trabalho com base na programação realizada.
- mostra o trabalho realizado por dia contra a taxa projetada de conclusão para a versão atual do projeto. 
- pode acompanhar a evolução do projeto, do release ou do Sprint.
- é um gráfico que contém as informações do Total de Pontos a Serem Executados X Quantidade de Sprints, sendo a linha de velocidade opcional.
- normalmente, o Sprint Burndown representa Esforço X Duração (+ comum) ou Número de Atividades X Duração.
- o gráfico deve ser atualizado ao final do dia, de acordo com a evolução do quadro Kanban.

--- 

## Revisão do Sprint

- todos podem participar.
- objetivo: avaliação do resultado do Sprint, feita pelo PO e convidados (stakeholders).
- como resultado, deve ser apresentado o produto funcionando, conforme as especificações.
- é um timebox:
  - 4 horas para Sprint de 4 semanas.
  - 3 horas para Sprint de 3 semanas.
  - 2 horas para Sprint de 2 semanas.

### Resultados da Revisão

Além da avaliação, são realizados:

- Retornar as funcionalidades não terminadas ao Product Backlog e repriorizá-las.
- Remover do Product Backlog as funcionalidades finalizadas.
- Trabalhar com o Scrum Master para reformular a equipe, caso necessário.
- Repriorização do Product Backlog.
- Solicitar fechamento de um Release com as funcionalidades demonstradas, sozinhas ou com o incremento de Sprints anteriores.
- Autorizar ou não o próximo Sprint.
- Acrescentar ao Product Backlog novos itens com base no feedback obtido durante a Revisão.

### Retrospectiva

- participação do time Scrum e Scrum Master como facilitador.
- reflexões:
  - O que correu bem durante o Sprint?
  - O que não correu bem durante o Sprint?
  - Quais melhorias poderiam ser feitas para o próximo Sprint?
- timebox:
  - 3 horas para Sprint de 4 semanas.
  - 2 horas para Sprint de 3 semanas.
  - 1,5 hora para Sprintde 2 semanas.

--- 

## Dicas

- em um cenário de vários times trabalhando ao mesmo tempo, cada time terá seu Scrum Master e seu Product Owner.
- problemas comuns:
  - Conflitos de liderança.
  - Falhas de comunicação.
  - Planejamento descentralizado.
  - Duplicação de esforço e retrabalho.
  - Problemas com a integração dos produtos.
  - Dependências entre as atividades.
  - Difícil controle de mudanças.
- para evitá-los:
  - Dividir o escopo do projeto em incrementos mais independentes possíveis entre si, limitando as dependências entre os times;
  - Criar papéis para a centralização de decisões no nível do Scrum Master e do Product Owner;
  - Criar um Product Backlog único e compartilhado entre todos os times;
  - Criar pontos de controle para a unificação de releases e publicação de uma nova versão;
  - Fazer reuniões diárias conjuntas;
  - Criar uma reunião de Scrum de Scrums para o acompanhamento das atividades, verificação de dependências e centralização das mudanças.

--- 

## Importante

1. Para mais detalhes sobre SCRUM, acessar [este link](www.scrum.org).

2. Algumas ferramentas gratuitas:
- [ScrumHalf](http://myscrumhalf.com/?lang=pt): facilita o uso do Scrum; tem quadro Kanban virtual e propicia a colaboração e acompanhamento da equipe. Simples de dar manutenção e priorizar o Product Backlog, gera o Burn Down Chart, entre outros.
- [Trello](https://trello.com/): automatiza o quadro Kanban.

---

## FAST TEST

### 1. A reunião diária tem o objetivo de melhorar a comunicação do time e permitir-lhe tomar ações corretivas na execução dos trabalhos. Selecione a alternativa INCORRETA sobre a reunião diária:

> A reunião diária precisa obrigatoriamente ser feita de pé, para manter todos em estadp de alerta e com atenção focada na resposta das 3 perguntas essenciais.

### 2. A Revisão do Sprint (Sprint Review) tem como principal objetivo a avaliação d resultado da Sprint pelo Product Owner e Stakeholders. Selecione a alternativa INCORRETA sobre a Revisão do Sprint:

> O Sprint Review não é obrigatório no framework SCRUM, e pode ser ignorado se ao fim so Sprint o time não for lançar algo em produção.

### 3. O conceito de Ready (DoR - Definition of Ready) auxilia o time a verificar se uma história selecionada para um Sprint tem informações suficientes para começar a ser construída. Selecione a alternativa INCORRETA sobre DoR:

> Cada membro do time, de acordo com suas capacidades pessoais, define os requisitos necessários que devem compor o DoR de suas gtarefas.

### 4. O Planejamento do Sprint é a reunião onde se define o que será trabalhado pelo time durante o Sprint. Selecione a alternativa que contém apenas afirmações verdadeiras sobre o Planejamento do SPrint.

> A primeira atividade da reunião é definir a meta do Sprint; o time todo define sua capacidade para o Sprint, ou seja, quantos itens do Product Backlog irá se comprometer a desenvolver e entregar.

### 5. Um Sprint é um ciclo determinado por um timebox, e representa uma iteração para construção de um produto. Selecione a alternativa que contém apenas informações verdadeiras sobre o Sprint.

> Sprints precisam de uma meta definida para começarem; ao final do sprint, o time deve apresentar o que foi desenvolvido na reunião de Sprint Review.

---

[Voltar ao início!](https://github.com/monicaquintal/fintech)