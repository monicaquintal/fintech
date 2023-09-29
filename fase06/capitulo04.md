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

## 1.7 Passos para implementação de um modelo relacional

### a) Criar as tabelas contendo campos, tipos de dados e tamanho, utilizando o comando CREATE TABLE.
### b) Criar as Chaves Primárias e demais constraints (exceto Chaves Estrangeiras), usando o comando ALTER TABLE.
### c) Criar as Chaves Estrangeiras, utilizando o comando ALTER TABLE após todas as tabelas, respectivas Chaves Estrangeiras e demais constraints.

- vantagem: o código fica mais simples de ser lido e mantido.
- desvantagem: necessário observar a ordem de criação das tabelas, conforme a dependência que existe entre elas e os seus relacionamentos. 
  - o comando se torna mais complexo e mais difícil de ser mantido.

## 1.8 Impondo restrições

- restrições (`constraints`), são as regras aplicadas à estrutura de armazenamento. 
- elas evitam:
  - que uma tabela seja deletada se houver pendências,
  - que dados inválidos sejam inseridos em branco e
  - garante a integridade dos dados armazenados.
- constraint é parte opcional dos comandos CREATE TABLE e ALTER TABL.
- pode ser utilizada para impor regras a colunas e tabelas.
- no Oracle, há os seguintes tipos de constraint:
  - NOT NULL.
  - UNIQUE.
  - CHECK.
  - DEFAULT.
  - PRIMARY KEY.
  - FOREIGN KEY.

### 1.8.1 Restrição NOT NULL

- indica que o conteúdo de uma coluna não poderá ser nulo.
- diferentemente das outras restrições, só pode ser definida ao nível de coluna e implementada na criação da estrutura da coluna com o comando CREATE TABLE ou modificando-se a estrutura do campo com o comando ALTER TABLE.
- exemplo:

~~~sql
CREATE TABLE T_SIP_DEPARTAMENTO (
  nm_depto VARCHAR2(30) NOT NULL,
  ...
);
~~~

### 1.8.2 Restrição UNIQUE

- indica que não pode haver repetição no conteúdo da coluna.
- é diferente do conceito de Chave Primária (único e não nulo): quando indicamos que uma coluna deve conter valores únicos, mostramos que todos os valores não nulos devem ser exclusivos.
- exemplo:

~~~sql
CREATE TABLE T_SIP_DEPARTAMENTO (
  ...
  nm_depto VARCHAR2(30) UNIQUE,
  ...
);
~~~

### 1.8.3 Restrição CHECK

- pode ser utilizada para validar o valor que será atribuído a um campo.
- exemplo: definição de um domínio (definição de valores possíveis para o conteúdo de uma coluna de acordo com as Regras do Negócio).
- exemplo:

~~~sql
CREATE TABLE T_SIP_FUNCIONARIO (
  ...
  sexo char(1) CHECK (UPPER(SEXO)= 'M' OR UPPER(SEXO) = 'F' OR UPPER(SEXO) = 'O'),
  ...
);
~~~

- importante:
  - função UPPER (&lt;nome-campo&gt;) converte o conteúdo do campo para maiúsculas no momento da validação.
  - o operador lógico “OR” (ou) permite avaliar condições: retorna um valor verdadeiro, se uma das condições for satisfeita.
  - outros operadores lógicos:
    - AND (e): permite avaliar condições; retorna um valor verdadeiro se todas as condições envolvidas forem satisfeitas.
    - NOT (não): retorna um valor contrário à expressão avaliada.

- exemplo2:

~~~sql
CONSTRAINT CK_SPI_SALARIO CHECK (vl_salario >= 788);
~~~

### 1.8.4 Restrição Primary Key

- permite identificar um registro na tabela e garante que cada registro seja único no banco de dados.
- além de assegurar a unicidade, esse(s) atributo(s) será(rão) exportado(s) em caso de relacionamento, tornando-se, na outra tabela, a Chave Estrangeira!
- exemplo:

~~~sql
CREATE TABLE T_SIP_DEPARTAMENTO (
  ...
  cd_depto NUMBER(2) PRIMARY KEY,
  ...
);
~~~

- já ao nível de tabela, o campo é definido e a restrição pode ser imposta a qualquer momento.
- a restrição requer a indicação do nome do campo ao qual se aplicará:

~~~sql
CREATE TABLE T_SIP_DEPARTAMENTO (
  ...
  cd_depto number(2),
  ...
  PRIMARY KEY(cd_depto)
);
~~~

- nos exemplos anteriores, a restrição não foi identificada (não recebeu um nome).
- isso não é uma boa prática, pois o Oracle atribuirá um identificador, o que dificultará o trabalho nas situações em que seja necessário manipular a restrição.
- a nomeação explícita das restrições pode ser feita ao nível de coluna ou tabela e aplicada a qualquer tipo de restrição.

### 1.8.5 Restrição FOREIGN KEY

- estabelece o relacionamento entre duas tabelas.
- recebe o nome "Chave Estrangeira" porque a chave é originária de outro local:
  - é, necessariamente, uma Chave Primária em outra tabela que foi exportada para esta com o objetivo de estabelecer um relacionamento entre as duas informações.
- ***há uma exceção à regra***: em caso de autorrelacionamento, a Chave Estrangeira é exportada a partir da própria Chave Primária da tabela,relacionando assim, uma ocorrência (ou registro) com outro!
- exemplo:

~~~sql
CREATE TABLE T_SIP_FUNCIONARIO (
  ...
  CONSTRAINT fk_depto_func FOREIGN KEY (cod_depto) REFERENCES T_SIP_DEPARTAMENTO(cod_depto),
  ...
);
~~~

- sendo:
  - fk_depto_func: nome da restrição.
  - FOREIGN KEY (cod_depto): definição do campo cod_depto, da tabela que está sendo criada, como Chave Estrangeira.
  - REFERENCES T_SIP_DEPARTAMENTO(cod_depto): a instrução references estabelece a relação entre o campo que está sendo definido como Chave Estrangeira e a tabela pai. Os campos de origem e referenciado possuem o mesmo nome (cod_depto), mas isso não é obrigatório, os nomes podem ser diferentes.

### 1.8.6 Restrição DEFAULT

- atribui um conteúdo-padrão a uma coluna da tabela sempre que for incluída uma nova linha nela.
- exemplo:

~~~sql
CREATE TABLE T_SIP_PROJETO(
  ...
  dt_inicio DATE default SYSDATE
  ...
);

/* SYSDATE é uma função que retorna a data atual.
~~~

### 1.8.7 Recomendações para adição de constraints

- normalmente, utilizamos o comando “ALTER TABLE” para inserir restrições (constraints).
- é uma boa prática adicionar ou eliminar restrições, mas não modificar restrições.
- adicione uma restrição NOT NULL utilizando a cláusula MODIFY. 
- exemplo:

~~~sql
ALTER TABLE tb_Exemplo
MODIFY status CONSTRAINT nn_tb_Exemplo_status NOT NULL;
~~~

- é recomendado que se especifique sempre um nome significativo para as restrições (constraints) pois ,quando ocorrer um erro de restrições, ficará mais fácil identificar o problema ou mesmo sua manutenção quando necessário!

## 1.9 Comando ALTER TABLE

- permite alterar a estrutura de uma tabela, acrescentando ou modificando a estrutura das colunas e restrições de uma tabela.

~~~sql
ALTER TABLE <nome-tabela>
  DROP COLUMN <nome-coluna>
  ADD <nome-coluna> <tipo-do-dado> [NOT NULL][NOT NULL WITH DEFAULT] 
  RENAME <nome-coluna> <novo-nome-coluna>
  MODIFY <nome-coluna> <tipo-do-dado> [NULL][NOT NULL];
~~~

- a partir da sintaxe básica, observamos que é possível executar as seguintes ações:
  - DROP COLUMN – Permite eliminar colunas de uma tabela.
  - ADD – Permite adicionar colunas ou restrições a uma tabela existente.
  - RENAME – Permite renomear a própria tabela, colunas e constraints.
  - MODIFY – Permite modificar a estrutura das colunas, como um tipo de dado, tamanho ou restrições.

### 1.9.1 Adicionando elementos a uma tabela

- exemplo 1:

~~~sql
ALTER TABLE T_SIP_FUNCIONARIO
  ADD ds_email VARCHAR2(60);
~~~

> Importante: podemos inserir constraints no momento da adição de uma nova coluna.

- ao adicionar uma nova coluna à tabela, também podemos definir as restrições que se aplicam a ela:

~~~sql
ALTER TABLE T_SIP_FUNCIONARIO
  ADD ds_email VARCHAR2(60) NULL;
~~~

> Caso a tabela na qual foi inserida a nova coluna já possua linhas, a nova coluna terá inicialmente seu conteúdo nulo.

- exemplo 2:

~~~sql
ALTER TABLE T_SIP_FUNCIONARIO
  ADD CONSTRAINT CK_SIP_FUNC_SALARIO
  CHECK (VL_SALARIO >= 880 );
~~~

### 1.9.2 Modificando elementos de uma tabela

~~~sql
ALTER TABLE T_SIP_FUNCIONARIO
  MODIFY ds_email VARCHAR2(100) NOT NULL;
~~~

- podemos alterar uma coluna de não obrigatória (NULL) para obrigatória,(NOT NULL) considerando: ***a tabela deve estar vazia***.
  - caso a tabela tenha registros, é necessário haver valores para todos os registros na coluna a ser alterada.
- não há restrições para a alteração de obrigatório (NOT NULL) para não obrigatório (NULL).
- é possível aumentar ou reduzir o tamanho de colunas. 
  - porém, se a coluna for Chave Primária da tabela, primeiramente,deve-se alterar as tabelas que recebem o relacionamento antes de modificar a tabela propriamente dita.

> O novo tamanho da coluna não pode ser inferior ao comprimento dos dados já inseridos na tabela.

### 1.9.3 Eliminando elementos de uma tabela

- eliminando uma coluna:

~~~sql
ALTER TABLE T_SIP_FUNCIONARIO
  DROP COLUMN ds_email;
~~~

- eliminando a constraint Chave Primária:

~~~sql
ALTER TABLE T_SIP_DEPARTAMENTO
  DROP CONSTRAINT PK_SIP_DEPARTAMENTO CASCADE;
~~~

Importante:
- a opção CASCADE CONSTRAINT possibilita a eliminação de todas as restrições de integridade referencial que se referem às Chaves Primárias. 
- se essa cláusula for omitida e as restrições de integridade referencial existirem, ocorrerá um erro durante a execução do comando e a constraint não será descartada!

### 1.9.4 Alterando os nomes dos elementos de uma tabela

- exemplo 1: alterar o nome da tabela.

~~~sql
ALTER TABLE T_SIP_FUNCIONARIO
  RENAME TO T_SIP_FUNC;
~~~

- exemplo 2: alterar o nome da coluna.

~~~sql
ALTER TABLE T_SIP_FUNCIONARIO
  RENAME COLUMN nm_funcionario TO nm_func;
~~~

- exemplo 3: alterar o nome da constraint.

~~~sql
ALTER TABLE T_SIP_FUNCIONARIO
  RENAME CONSTRAINT CK_SIP_FUNC_SALARIO
  TO CK_SIP_FUNC_SAL;
~~~

### 1.9.5 Visualizando CONSTRAINTS de uma tabela

- exemplo para as tabelas a que tenhamos acesso:

~~~sql
-- VISUALIZAR CONSTRAINTS DE TODAS AS TABELAS A QUE
-- TENHA ACESSO
SELECT TABLE_NAME, CONSTRAINT_NAME,
  CONSTRAINT_TYPE, SEARCH_CONDITION
FROM ALL_CONSTRAINTS;
~~~

- é possível também consultar as restrições de uma tabela específica:

~~~sql
-- VISUALIZAR CONSTRAINTS DE UMA TABELA ESPECÍFICA
SELECT TABLE_NAME, CONSTRAINT_NAME,
  CONSTRAINT_TYPE, SEARCH_CONDITION
FROM ALL_CONSTRAINTS 
WHERE UPPER(TABLE_NAME) = 'T_SIP_FUNCIONARIO';
~~~

---

<div align="center">
<h2>2. DROP TABLE</h2>
</div>

- o comando DROP TABLE é uma instrução DDL utilizada para remover a definição de uma tabela.
- estrutura, dados e índices são eliminados permanentemente.
- sintaxe é simples, mas o resultado não pode ser desfeito!!!

~~~sql
DROP TABLE tabela;
~~~

- em caso de tabelas que possuam vínculos (que usem sua chave primária como chave estrangeira), a operação causará uma falha, a menos que sejam incluídas as palavras-chave CASCADE CONSTRAINTS (elimina os vínculos de integridade referencial com outras tabelas).

~~~sql
DROP TABLE tabela CASCADE CONSTRAINTS;
~~~

### 2.1 Implementando as tabelas do estudo de caso SIP

<details>
<summary>Criando algumas das tabelas do projeto.</summary>

~~~sql
-- TABELA DEPARTAMENTO
CREATE TABLE T_SIP_DEPARTAMENTO 
  ( 
    cd_depto NUMBER (2) NOT NULL , 
    nm_depto VARCHAR2 (30) NOT NULL 
  ) ;

-- CRIAÇÃO DA CHAVE PRIMÁRIA
ALTER TABLE T_SIP_DEPARTAMENTO 
ADD CONSTRAINT PK_SIP_DEPARTAMENTO PRIMARY KEY ( cd_depto );

-- CRIAÇÃO DA CONSTRAINT UNIQUE
ALTER TABLE T_SIP_DEPARTAMENTO 
ADD CONSTRAINT UN_SIP_DEPTO_NOME UNIQUE ( nm_depto ) ;

-- TABELA FUNCIONARIO
CREATE TABLE T_SIP_FUNCIONARIO 
  ( 
    nr_matricula NUMBER (6) NOT NULL , 
    cd_depto NUMBER (2) NOT NULL , 
    nm_funcionario VARCHAR2 (60) NOT NULL , 
    dt_nascimento DATE NULL , 
    dt_admissao DATE NOT NULL , 
    ds_endereco VARCHAR2 (80) NOT NULL , 
    vl_salario NUMBER (7,2) NOT NULL 
  );

-- CRIAÇÃO DA CHAVE PRIMÁRIA
ALTER TABLE T_SIP_FUNCIONARIO 
  ADD CONSTRAINT PK_SIP_FUNCIONARIO PRIMARY KEY ( nr_matricula ) ;

-- CRIAÇÃO DA CONSTRAINT CHECK PARA O SALÁRIO
ALTER TABLE T_SIP_FUNCIONARIO 
  ADD CONSTRAINT CK_SIP_FUNC_SALARIO CHECK ( vl_salario >= 788 ) ;

-- TABELA DEPENDENTE
CREATE TABLE T_SIP_DEPENDENTE 
  ( 
    cd_dependente NUMBER (3) NOT NULL , 
    nr_matricula NUMBER (6) NOT NULL , 
    nm_dependente VARCHAR2 (60) NOT NULL , 
    dt_nascimento DATE NOT NULL 
  ) ;

-- CRIAÇÃO DA CHAVE PRIMÁRIA
ALTER TABLE T_SIP_DEPENDENTE 
  ADD CONSTRAINT PK_SIP_DEPENDENTE 
PRIMARY KEY ( cd_dependente, nr_matricula ) ;
-- Observe que criamos uma Chave Primária composta pelos campos cd_dependente e nr_matricula

-- TABELA PROJETO
CREATE TABLE T_SIP_PROJETO 
  ( 
    cd_projeto NUMBER (4) NOT NULL , 
    nm_projeto VARCHAR2 (40) NOT NULL , 
    dt_inicio DATE NOT NULL , 
    dt_termino DATE 
  ) ;

-- CRIAÇÃO DA CHAVE PRIMÁRIA
ALTER TABLE T_SIP_PROJETO 
  ADD CONSTRAINT PK_SIP_PROJETO PRIMARY KEY ( cd_projeto ) ;

-- CRIAÇÃO DA CONSTRAINT UNIQUE
ALTER TABLE T_SIP_PROJETO 
  ADD CONSTRAINT UN_SIP_PROJETO_NOME UNIQUE ( nm_projeto ) ;

-- CRIAÇÃO DA CONSTRAINT CHECK PARA AS DATAS
ALTER TABLE T_SIP_PROJETO 
  ADD CONSTRAINT CK_SIP_PROJETO_DATE CHECK ( DT_TERMINO > DT_INICIO ) ;

-- TABELA IMPLANTACAO
CREATE TABLE T_SIP_IMPLANTACAO 
  ( 
    cd_implantacao NUMBER (6) NOT NULL , 
    cd_projeto NUMBER (4) NOT NULL , 
    nr_matricula NUMBER (6) NOT NULL , 
    dt_entrada DATE NOT NULL , 
    dt_saida DATE NULL 
  ) ;

-- CRIAÇÃO DA CHAVE PRIMÁRIA
ALTER TABLE T_SIP_IMPLANTACAO 
  ADD CONSTRAINT PK_SIP_IMPLANTACAO 
  PRIMARY KEY ( cd_implantacao, cd_projeto ) ;

-- CRIAÇÃO DA CONSTRAINT CHECK PARA AS DATAS
ALTER TABLE T_SIP_IMPLANTACAO 
  ADD CONSTRAINT CK_SIP_IMPLAT_DATE CHECK 
    ( DT_SAIDA > DT_ENTRADA ) ;
~~~

</details>

















--- 

[Voltar ao início!](https://github.com/monicaquintal/fintech)