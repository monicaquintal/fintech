<div id="fase03" align="center">
<h1>FASE 3 - MODELING</h1>
<h2>Capítulo 02: Onde guardar as informações geradas? 🤨</h2>
</div>

<div align="center">
<h2>Definição de dado e banco de dados</h2>
</div>

## 1. O que é um dado e o que é informação?

### Dado:

- é a menor unidade de armazenamento dentro da estrutura de um BD; é aquilo que está efetivamente armazenado.
- definição de uma entidade que nomeia ou classifica algo (exemplos: nome, sobrenome, telefone).
- é utilizado para se referir ao que realmente está armazenado (exemplos: endereço - logradouro, número, complemento).

### Informação:

- conjunto de dados (exemplo: um endereço é composto por logradouro, bairro, número e CEP).
- significado daquilo que temos armazenado no BD.

> Ou seja, `dado` é aquilo que é guardado por meio de uma estrutura de armazenamento e informação, extraído de uma estrutura de armazenamento. A `informação` sempre tem um significado para o usuário, podendo ser constituída por vários dados!

## 2. O que é um banco de dados?

- estrutura de armazenamento organizada, lógica e coerente.
- coleção de dados persistentes usada pelos sistemas de aplicação de uma determinada empresa.
- são utilizados principalmente por empresas que necessitam manter muitos dados sobre sua operação.
- uma coleção de dados representa dados armazenados e inter-relacionados que atendem às necessidades de vários usuários dentro das organizações.
- `dados persistentes`:
  - são aqueles que, uma vez aceitos por um Sistema Gerenciador de Banco de Dados (SGBD) para a entrada no banco de dados, somente poderão ser removidos por uma requisição explícita ao SGBD.
  - portanto, dados persistentes são aqueles que podem ser armazenados por um longo espaço de tempo.


## 3. Propriedades do banco de dados


- Coleção lógica e coerente de dados (dados dispostos de forma desordenada não podem ser referenciados como banco de dados).
- Projetado, construído e populado com dados para um propósito específico.
- Possui um conjunto predefinido de usuários e aplicações. 
- Representa algum aspecto do mundo real, porção da realidade, chamado de “minimundo”; qualquer alteração efetuada no minimundo é automaticamente refletida no banco de dados!

> Um banco de dados tem alguma fonte da qual o dado é derivado, algum grau de interação com eventos do mundo real e um público que está ativamente interessado em seu conteúdo!

<div align="center">
<h2>Sistema Gerenciador de Banco de Dados (SGBD)</h2>
<h3>(ou DataBase Management System - DBMS)</h3>
</div>

- sistema de software genérico para manipular bancos de dados.
- possui recursos específicos para facilitar o processo de definição, construção, manipulação e compartilhamento das informações dos bancos de dados e o desenvolvimento de programas e aplicativos.
- tem como principal objetivo propiciar um ambiente tanto conveniente quanto eficiente para a recuperação e armazenamento das informações do banco de dados.
- exemplos: Oracle, Sybase, DB2, Informix, SQL Server, MySQL, PostgreSQL, InterBase, Caché e outros.
- o SGBD é um software que facilita alguns processos associados aos bancos de dados:
  - ***definição***: refere-se à especificação de tipos, estruturas e restrições associados aos dados que serão armazenados. 
  - ***construção***: processo de armazenar os dados em algum meio controlado pelo SGBD.
  - ***manipulação***: inclusão de funções, como consulta ao BD para recuperação de dados específicos, atualização do banco de dados e geração de relatórios com base nos dados.
  - ***compartilhamento***: permite que diversos usuários e programas acessem-no simultaneamente.

<div align="center">
<h2>Sistema de banco de dados</h2>
</div>

- é um conjunto formado por um banco de dados (coleção de dados persistentes) e as aplicações (SGBD) que o manipulam.
- é um sistema de manutenção de registros por computador, envolvendo quatro componentes principais:
  - dados.
  - hardware e software.
  - usuário.
- são projetados para gerir grandes volumes de informações, que implicam definição das estruturas de armazenamento e dos mecanismos para a manipulação dessas informações.
- devem garantir a segurança das informações armazenadas contra eventuais problemas com o sistema, além de impedir tentativas de acesso não autorizadas.

<div align="center">
<h2>Componentes e características de um Sistema de Banco de Dados</h2>
</div>

## 1. Os componentes de um sistema de banco de dados

- o SGBD permite que um banco de dados tenha a característica `MULTIUSUÁRIO` (vários usuários podem acessá-lo ao mesmo tempo).
- de modo geral, os dados de um banco de dados estarão integrados e compartilhados.
  - integrado: unificação de vários arquivos, eliminação de redundância. Exemplos: dados do aluno e boletim do aluno.
  - compartilhado: vários usuários podem ter acesso aos mesmos dados, possivelmente ao mesmo tempo. Exemplo: consulta da ficha cadastral.

## 2. Características de um sistema de banco de dados

- `Autodescrição de um banco de dados`:
  - em seu sistema, há o banco de dados e uma definição completa de sua estrutura e restrições (metadados).
  - os ***METADADOS*** são armazenadas em uma espécie de catálogo que contéma estrutura de cada arquivo, tipo e formato de armazenamento e um conjunto de restrições sobre os dados.

- `Independência de dados do programa:`
  - a estrutura dos arquivos de dados é armazenada no catálogo do SGBD, separadamente dos programas de acesso. 
  - caso alguma descrição do catálogo seja alterada, nenhum programa associado ao SGBD precisa ser modificado, porque, automaticamente, as alterações são refletidas e acessadas pelos programas de SGBD.

- `Suporte a várias visões dos dados:`
  - normalmente um BD possui muitos usuários, com necessidades diferentes, que se refletem em visões diferentes dos dados. 
  - essas visões podem ser subconjuntos dos dados armazenados ou informações derivadas das informações armazenadas. P
  - para o usuário final, não há a necessidade de conhecer a origem da informação (armazenada ou derivada). 
  - o SGBD precisa fornecer funcionalidades que permitam a criação dessas visões!

- `Compartilhamento de dados e processamento de transação multiusuário:`
  - SGBD deve permitir que múltiplos usuários acessem o banco de dados ao mesmo tempo. 
  - para isso, o SGBD precisa de um software para controle de concorrência. 
  - isso posto, é possível garantir que vários usuários possam realizar alterações simultaneamente de uma forma controlada e que essas transações concorrentes operem de maneira correta e eficiente.

## 3. Tipos de usuários de um sistema de banco de dados

- `Programadores de Aplicações:` 
  - responsáveis pela escrita de programas de aplicações de banco de dados em alguma linguagem de programação. 
  - esses programas acessam o banco de dados emitindo uma requisição apropriada (instrução SQL).

- `Usuários Finais:`
  - um usuário pode acessar o banco de dados por meio de uma aplicação desenvolvida pelos programadores de aplicações.

- `Administrador de Banco de Dados (DBA – Data Base Administrator) e Administrador de Dados (DA – Data Administrator):`
  - decidem os dados que devem ser armazenados e estabelecem normas para manter e tratar esses dados.

## 4. Benefícios de um sistema de banco de dados

- Os dados podem ser compartilhados.
- A redundância pode ser reduzida.
  - evitando, assim, desperdício de espaço em disco devido à repetição da informação em vários lugares, dificuldade para atualização das informações repetidas em lugares diferentes e a inconsistência em função da falha durante a atualização das informações repetida.
- A inconsistência pode ser evitada.
- Suporte a transações.
  - transação é uma unidade lógica de trabalho de banco de dados, envolvendo diversas operações de banco de dados. Ex: transferência de dinheiro entre contas.
- A integridade pode ser mantida.
- Segurança.

--- 

## FAST TEST

### 1. Podemos definir dados como: 
> Entidade que nomeia ou classifica algo.

### 2. Escolha a alternativa que descreve um conjunto de dados integrado.
> Relatório de vendas de uma empresa.

### 3. Podemos definir que uma informação é:
> Conjunto de dados que trazem significado.

### 4. Podemos afirmar que um banco de dados é:
> Coleção lógica e coerente de dados utilizados em sistemas.

---

[Voltar ao início!](https://github.com/monicaquintal/fintech)