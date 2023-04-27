<div id="fase02" align="center">
<h1>FASE 3 - MODELING</h1>
<h2>Capítulo 2: Onde guardar as informações geradas? 🤨</h2>
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

<div align="center">
<h2>Propriedades do banco de dados</h2>
</div>

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