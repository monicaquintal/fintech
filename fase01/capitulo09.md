<div id="fase01" align="center">
<h1>FASE 1 - DEVELOPMENT ENVIRONMENT</h1>
<h2>Capítulo 09: Materializando o projeto.</h2>
</div>
<br>

<div align="center">

## Materializando o projeto 🧩

</div>

## Detalhando o escopo

***Backlog do Produto***: retratar os itens por meio de narrativas (histórias do usuário).

>“Como &#95;&#95;&#95;&#95;&#95; (papel), eu gostaria de / quero poder &#95;&#95;&#95;&#95;&#95; (funcionalidade ou necessidade) para &#95;&#95;&#95;&#95;&#95; (benefício)”.

Exemplos:

- Como usuário, quero poder cadastrar e atualizar meus dados pessoais para manter um histórico.
- Como usuário, quero poder informar meus recebimentos para realizar um acompanhamento adequado.
- Como usuário, quero poder registrar meus gastos para realizar um acompanhamento adequado.
- Como usuário, quero poder registrar os meus investimento spara planejar a vida financeira.
- Como desenvolvedor, preciso montar uma infraestrutura adequada para construir outras histórias.

História | Prioridade
---------|:-----------:
Como equipe de projetos, precisamos formalizar o projeto desenvolvendo seus primeiros artefatos | 1
Como desenvolvedor, preciso montar uma infraestrutura adequada para construir outras histórias | 2
Como usuário, quero poder cadastrar e atualizar meus dados pessoais para manter um histórico | 3
Como usuário, quero poder informar meus recebimentos para realizar um acompanhamento adequado | 4
Como usuário, quero poder registrar meus gastospara realizar um acompanhamento adequado | 5
Como usuário, quero poder registrar meus investimentospara planejar a vida financeira | 6

## Planejamento da primeira história de negócios (prioridade 1)

> Como equipe de projetos, precisamos formalizar o projeto desenvolvendo seus primeiros artefatos

- As atividades serão dispostas em ciclos de duas a quatro semanas (Sprints).
- Ao final de cada Sprint, a equipe (eu) deverá entregar algo para o cliente, representado pelo Dono do Produto (tutor).

### Neste primeiro ciclo:

- duração de quatro semanas.
- desenvolver o termo de abertura do projeto, essencial para formalizar o projeto e nosn apresentar como principal responsável por ele.
- definir qual equipamento será utilizado (estação de trabalho, notebook/laptop, etc).
- instalar os softwares necessários (como administrador).

Backlog do Sprint | _ 
-----------------|------
Meta do Sprint | Concluir a história de usuário “Como equipe de projetos, precisamos formalizar o projeto desenvolvendo seus primeiros artefatos”.

Atividade | Esforço (em horas)
----------|------------------
Desenvolver um termo de abertura do projeto | 4 horas
Definir e levantar a infra-estrutura física | 2 horas

## Planejando a primeira história técnica (prioridade 2):

> Como desenvolvedor, preciso montar uma infraestrutura adequada para construir outras histórias.

Para criação da infraestrutura de desenvolvimento, é possível separá-la do ambiente pessoal/de entretenimento, através da ***criação de uma máquina virtual*** (virtualização), que consiste em instalar um software que simula os comportamentos de um hardware (similar ao HW real existente), possibilitando instalar outro sistema operacional sobre esse hardware fictício, criando assim um ambiente isolado.

Embora seja altamente recomendada, essa atividade é considerada opcional. Para fazê-lo, é sugerido o uso do [Oracle Virtualbox](http://www.virtualbox.org/) ou do [Docker](http://www.docker.com/), ambos gratuitos e disponíveis para as três principais plataformas (Windows, MacOS X e Linux).

É recomendado também o download de um software processador de textos (Word).


Backlog do Sprint | _ 
-----------------|------
Meta do Sprint (1) | Concluir a história de usuário “Como equipe de projetos, precisamos formalizar o projeto desenvolvendo seus primeiros artefatos”.
Meta do Sprint (2) | Concluir a história de usuário "Como desenvolvedor, preciso montar uma infraestrutura adequada para construir outras histórias”.

Atividade | Esforço (em horas)
----------|------------------
Desenvolver um termo de abertura do projeto | 4 horas
Definir e levantar a infra-estrutura física | 2 horas
**OPCIONAL** Instalação de um ambiente de virtualização | 2 horas
Instalação ou atualização do sistema operacional | 4 horas
Instalação de um software processador de textos | 3 horas

## Lista de Softwares que serão utilizados

Software | Descrição
---------|-----------
[Eclipse](http://www.eclipse.org/) | IDE para desenvolvimento Java
[Apache Tomcat](http://tomcat.apache.org/) | Servidor Web do tipo WebContainer
[Oracle SQL Developer Data Modeler](http://www.oracle.com/technetwork/developer-tools/datamodeler/overview/index.html) | Ferramenta de Modelagem Relacional para o banco de dados Oracle
[Oracle SQL Developer](http://www.oracle.com/technetwork/developer-tools/sql-developer/downloads/index.html) | Cliente para o servidor de banco de dados Oracle
[Python](https://www.python.org) | Linguagem de Programação
[VS Code](https://code.visualstudio.com/) | Editor para desenvolvimento em várias linguagens
[Postman](https://www.postman.com/) | Plataforma para trabalhar com API
[NodeJS](https://nodejs.org/en/) | Ambiente de execução JS Server Side

Atualizando Backlog:

Atividade | Esforço (em horas)
----------|------------------
Desenvolver um termo de abertura do projeto | 4 horas
Definir e levantar a infra-estrutura física | 2 horas
**OPCIONAL** Instalação de um ambiente de virtualização | 2 horas
Instalação ou atualização do sistema operacional | 4 horas
Instalação de um software processador de textos | 3 horas
Instalação do Eclipse | 2 horas
Instalação do Apache Tomcat e integração com o Eclipse | 3 horas
Instalação do Oracle SQL Developer Data Modeler | 2 horas
Instalação do Oracle SQL Developer | 2 horas
Instalação do Python | 1 hora

## Organizando as atividades em um Kanban

- o quadro de tarefas (taskboard) é dividido em pelo menos três colunas: “a fazer”, “fazendo” e “feito”.
- os cartões, cada um representando uma atividade, migram de uma coluna para outra de acordo com seus progressos.
- qualquer membro da equipe pode mover os cartões das atividades pelas quais é responsável, sinalizando aos demais o seu progresso!

## Dicas

`Scrum of Scrums`:
- trabalhar com grandes times (pois no Scrum há limite de componentes:9 pessoas). 
- ou seja, criar tantos times de 9 pessoas quanto for necessário para atender à demanda do projeto.
- nesse cenário de vários times trabalhando ao mesmo tempo, ***cada time terá seu Scrum Master e seu Product Owner**.

Problemas comuns neste cenário:
- Conflitos de liderança.
- Falhas de comunicação.
- Planejamento descentralizado.
- Duplicação de esforço e retrabalho.
- Problemas com a integração dos produtos.
- Dependências entre as atividades.
- Difícil controle de mudanças.

Para solucionar esses problemas: **Nexus Guide**. 
- Dividir o escopo do projeto em incrementos mais independentes possíveis entre si, diminuindo as dependências entre os times.
- Criar papéis para a centralização de decisões no nível do Scrum Master e do Product Owner.
- Criar um Product Backlog único.
- Criar marcos (pontos de controle) para unificação de releases e publicação de uma nova versão.
- Fazer reuniões diárias conjuntas para que representantes de outros times possam participar, com o objetivo de compartilhar problemas, dependências e conhecimento.
- Criar uma reunião de Scrum de Scrums para o acompanhamento das atividades, verificação de dependências e centralização das mudanças.

> Para mais detalhes sobre escalar o Scrum, consultar o [Nexus Guide](www.scrum.org)!

Ferramentas:

- [ScrumHalf](http://myscrumhalf.com/?lang=pt)– brasileira. Facilita o uso do Scrum. Tem um quadro Kanban virtual e facilita a colaboração e o acompanhamento da equipe. É de fácil manutenção, prioriza o Product Backlog e gera o Burn Down Chart, entre outros.
- [Trello](https://trello.com/): não é uma ferramenta de Scrum, mas automatiza o quadro Kanban.

---

[Voltar ao início!](https://github.com/monicaquintal/fintech)