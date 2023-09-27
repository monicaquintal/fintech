<div id="fase06" align="center">
<h1>FASE 6 - MODEL</h1>
<h2>Capítulo 04: ... e as estruturas do banco são finalmente criadas!</h2>
</div>

<div align="center">
<h2>1. ...E AS ESTRUTURAS DE DADOS SÃO FINALMENTE CRIADAS!</h2>
</div>

## 1.1 Introdução aos comandos da linguagem SQL

- a criação das estruturas do BD é uma atividade que requer atenção especial, pois essas estruturas serão responsáveis pelo armazenamento de dados, essencial para o funcionamento de um sistema.

## 1.2 SQL

- é uma linguagem de definição, manipulação e controle de banco de dados. 
- representa um conjunto de comandos responsáveis pela definição das tabelas, seleção e atualização dos dados em um SGBD.
- a linguagem SQL é padronizada e reconhecida pelo ANSI.
- possui uma sintaxe simples.
- agrupa os comandos de acordo com suas funcionalidades:

### a) DDL (Data Definition Language) – Linguagem de Definição de Dados:
- utilizada para definir tabelas e elementos associados à estrutura dos dados.
- exemplos: CREATE, DROP, ALTER, RENAME, TRUNCATE.

### b) DML (Data Manipulation Language) – Linguagem de Manipulação de Dados:
- utilizada para inserir, atualizar e excluir dados, ou seja, para modificar o conteúdo das tabelas.
- exemplos: INSERT, UPDATE, DELETE.

### c) DCL (Data Control Language) – Linguagem de Controle de Dados:
- utilizada para controlar autorização de acesso a dados e operações.
- exemplos: GRANT, REVOKE.

### d) DTL (Data Transaction Language) – Linguagem de Transação de Dados:
- utilizada para controlar as transações de banco de dados, permitindo o registro permanente das alterações ou desfazendo as alterações.
- exemplos: COMMIT, ROLLBACK, SAVEPOINT.

### e) DQL (Data Query Language) – Linguagem de Consulta de Dados:
- também chamada de DRS (Data Retrieve Statement).
- utilizada para especificar consultas.
- é composta de várias cláusulas e opções, o que possibilita a elaboração de consultas simples a complexas.
- exemplos: SELECT.

> Alguns SGBDs que utilizam SQL são: Apache Derby, Caché, DB2, Firebird, Informix, Interbase, SQL Server, MySQL, Oracle, PostgreSQL e Sybase.

## 1.3 Implementando um banco de dados

- a implementação de um BD é feita após a representação do modelo físico de dados, no qual devem ser aplicadas as boas práticas de modelagem relacional.
- comandos DDL para implementar as tabelas do banco de dados.
- importante: ***comandos SQL não são sensíveis a letras maiúsculas e minúsculas***.
- SGBDs utilizam ***terminadores para indicar a finalização de uma instrução***. 
  - no caso do Oracle, o terminador utilizado é o ponto e vírgula (;).

## 1.4 Comandos DDL para criação e manutenção de tabelas

- o comando que possibilita a implementação de tabelas com suas restrições é o **`CREATE TABLE`**. 
- sintaxe:

~~~sql
CREATE TABLE <nome-tabela> (
  <nome-coluna> <tipo-do-dado> [NOT NULL]
  PRIMARY KEY (nome-coluna-chave)
  FOREIGN KEY (nome-coluna-chave-estrangeira) 
REFERENCES <nome-tabela-pai> (nome-coluna-chave-primária)
);
~~~

- a alteração da estrutura de uma tabela é feita com o comando **`ALTER TABLE`**. 
  - permite acrescentar e eliminar colunas ou restrições e alterar o formato das colunas.
- sintaxe:

~~~sql
ALTER TABLE <nome-tabela>
DROP COLUMN <nome-coluna>
ADD <nome-coluna> <tipo-do-dado> [NOT NULL][NOT NULL WITH DEFAULT] 
RENAME <nome-coluna> <novo-nome-coluna>
MODIFY <nome-coluna> <tipo-do-dado> [NULL][NOT NULL];
~~~

- para exclusão de uma tabela, comando **`DROP TABLE`**.
  - após execução desse comando, estarão deletados todos os dados, estrutura e índices de acessos que estejam a ela associados.
- sintaxe:

~~~sql
DROP TABLE <nome-tabela>;
~~~

## 1.5 Convenções para nomenclatura de tabelas e campos

- busca padronizar a nomenclatura utilizada para os objetos de banco de dados, tornando o código mais compreensível e fácil de ler.
- utilizaremos a convenção baseada nas recomendações do padrão Oracle.

### 1.5.1 Nomenclatura de tabelas e campos

- o nome de uma tabela ou um campo deve possuir, no máximo, 30 caracteres.
- os caracteres permitidos para identificação de campos e tabelas são: letras, números, underline (_), cifrão ($) e cerquilha (#).
- para diferenciar os identificadores de campos e tabelas, recomenda-se:

<div align="center">

Tabela (Entidade) | Campos (Atributos)
------------------|---------------------
Singular | Singular
Primeiro caractere deve ser uma letra | Primeiro caractere deve ser uma letra
Letras maiúsculas | Letras minúsculas

</div>

- ***Tabela (entidade)***:
  - inicializar o nome com a letra "T".
  - utilizar 3 caracteres como prefixo para indicar a sigla do sistema.
  - nome atribuído à tabela.
  - utilizar o underline como separador.
  - nomes compostos separar com o underline.

- ***Campo (atributo)***:
  - utilizar 2 ou 3 caracteres como prefixo para indicar o significado da coluna.
  - utilizar underline como separador.
  - nome atribuído à coluna (sufixo).
  - nomes compostos separar com o underline.

- prefixos comuns para identificação de campos:

<div align="center">

Prefixo (2 caracteres) | Prefixo (3 caracteres) | Significado
-----------------------|-------------------------|-------------
nr | Num | Número (pode identificar exclusivamente)
cd | Cod | Código (identifica esclusivamente uma ocorrência)
id | idt | Identificador (identifica exclusivamente uma ocorrência)
ds | des | Descrição
nm | nom | Nome
dt | dat | Data
vl | val | Valor
qt | qtd | Quantidade
sq | seq | Número sequencial que identifica algo do mundo real
in | Ind | Indicador
st | sta | Status
ob | obs | Observação
tx | txt | Texto extenso

</div>

- `restrições (constraints)` são definidas nas tabelas. Como boa prática,para diferenciá-las de outros elementos, podemos seguir o padrão:

<div align="center">

Prefixo | Descrição
--------|------------
PK | Primary Key
FK | Foreign Key
UN | UNIQUE
CK | CHECK

</div>

## 1.6 Estudo de caso SIP 

> O estudo de caso SIP - SISTEMA DE CONTROLE DE IMPLANTAÇÃO DE PROJETOS será usado para demonstrar a utilização das instruções DDL, e para auxiliar no aprofundamento dos estudos sobre os comandos.

### 1.6.1 Regras de negócio do Projeto SIP

- RN01 – Um funcionário possui apenas um endereço residencial.
- RN02 – Um funcionário pode ter um ou mais dependentes (filhos, esposa ou marido).
- RN03 – Um funcionário tem apenas uma data de admissão.
- RN04 – Um funcionário deve pertencer a um único departamento.
- RN05 – Um funcionário possui um único número de matrícula.
- RN06 – Um funcionário pode participar da implantação de um ou mais projetos.
- RN07 – Um departamento pode locar vários funcionários.
- RN08 – Um projeto pode ser implantado por vários funcionários.
- RN09 – Cada dependente deve ter uma data de nascimento.
- RN10 – Cada dependente pertence a um único funcionário.
- RN11 – Um funcionário pode participar da implantação de um mesmo projeto várias vezes (pode participar da implantação de um projeto em diferentes momentos).
- RN12 – Não será considerada a hipótese de termos um casal trabalhando na mesma empresa (teriam dependentes comuns).








--- 

[Voltar ao início!](https://github.com/monicaquintal/fintech)