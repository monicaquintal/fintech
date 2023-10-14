<div id="fase06" align="center">
<h1>FASE 6 - MODEL</h1>
<h2>Capítulo 07: Consulte o oráculo.</h2>
</div>

<div align="center">
<h2>1. CONSULTE O ORÁCULO</h2>
</div>

- com o SQL, também podemos recuperar os dados armazenados e realizar operações com eles, utilizando o comando SELECT.
- essas operações permitem construir consultas capazes de responder às diversas demandas do negócio.

## 1.1 Recuperação de dados

- na linguagem SQL, as `consultas (queries)` são instruções que permitem recuperar os dados de tabelas de um BD, e pertencem à divisão DRS (Data Retrieve Statement) ou DQL (Data Query Language).
- são operações de recuperação de dados de tabelas:
  - SELECT simples.
  - SELECT com operadores.
  - SELECT a partir de junções.
  - SELECT a partir de agrupamentos.
- para recuperarmos os dados das tabelas, utilizamos o `comando SELECT`.

~~~sql
SELECT [ DISTINCT | ALL] { * | coluna  [, coluna, … ] }
  FROM tabela
  WHERE condição
  ORDER BY coluna [, coluna, ...]
~~~

- em que:
  - SELECT: especifica as colunas (campos) necessárias para a pesquisa.
  - DISTINCT: não mostra eventuais valores repetidos de colunas.
  - ALL: mostra todos os valores, mesmo que repetidos. É O PADRÃO, se o DISTINCT não for definido.
  - * (asterisco): indica que devem ser mostradas todas as colunas da tabela.
  - FROM: indica em que tabelas serão efetuadas essas pesquisas.
  - WHERE: condição para que se execute a pesquisa (filtra dados).
  - ORDER BY: especifica em que ordem deverá ser apresentada a pesquisa desejada e por qual campo estará ordenada (crescente ou decrescente).

> Para exemplificar o uso do SELECT, utilizaremos o Estudo de Caso: SIP - SISTEMA DE CONTROLE DE IMPLANTAÇÃO DE PROJETOS.

## 1.2 Exemplos de comando SELECT

- comando SELECT para recuperar registros ou linhas na tabela “FUNCIONARIO”: retornará todas as colunas (*) e todas as linhas (não há condições) da tabela “FUNCIONARIO”.

~~~sql
SELECT * FROM T_SIP_FUNCIONARIO;
~~~

> Não é uma boa prática utilizar a cláusula SELECT *, pois todas as colunas serão retornadas. É importante recuperar apenas as colunas realmente necessárias, ou seja, que serão utilizadas.

- neste exemplo, as colunas a serem retornadas são declaradas na cláusula SELECT:

~~~sql
SELECT NR_MATRICULA ,
  CD_DEPTO ,
  DT_ADMISSAO ,
  VL_SALARIO
  FROM T_SIP_FUNCIONARIO;
~~~

- no próximo exemplo, além de selecionar as colunas, acrescentaremos um filtro que recuperará apenas as linhas que satisfazem a condição:

~~~sql
SELECT NR_MATRICULA ,
  CD_DEPTO ,
  DT_ADMISSAO ,
  VL_SALARIO
FROM T_SIP_FUNCIONARIO
WHERE CD_DEPTO = 3;
~~~

- a instrução `SELECT DISTINCT` é usada para retornar valores distintos: o comando SELECT retornará apenas as colunas declaradas com valores distintos e todas as linhas da tabela “FUNCIONARIO”:

~~~sql
SELECT 	DISTINCT CD_DEPTO 
  FROM 	T_SIP_FUNCIONARIO;
~~~

- no exemplo a seguir, o comando SELECT retornará apenas colunas declaradas com valores distintos, considerando-se colunas declaradas cd_depto e dt_admissao, e todas as linhas da tabela “FUNCIONARIO”:

~~~sql
SELECT DISTINCT CD_DEPTO, DT_ADMISSAO 
  FROM T_SIP_FUNCIONARIO;
~~~

## 1.4 Operadores relacionais

- são utilizados para realizar comparações, por exemplo, entre valores e valores, campos e valores, ou campos e campos, além de serem usados também em estruturas de controle.

<div align="center">

Operador | Significado | Exemplo
----------|------------|---------------
= | Igual | codigo = 2
&lt; | Menor que | preco < 10
&lt;= | Menor ou igual a | preco <= 10
&gt; | Maior que | preco > 10
&gt;= | Maior ou igual a | preco >= 10
&lt;&gt; ou != | Diferente | codigo <> 2

</div>

- exemplo: recuperados funcionários com salário maior que R$ 1.500,50.

~~~sql
-- Exemplo de filtro com números
SELECT 	NR_MATRICULA ,
        NM_FUNCIONARIO,
        VL_SALARIO
  FROM 	T_SIP_FUNCIONARIO
  WHERE VL_SALARIO > 1500.50 ;
~~~

- exemplo: recupera funcionários com nome “ROSA MARIA”.

~~~sql
-- Exemplo de filtro com texto
SELECT 	NR_MATRICULA,
        NM_FUNCIONARIO 
  FROM T_SIP_FUNCIONARIO
  WHERE NM_FUNCIONARIO = 'ROSA MARIA';
~~~

- exemplo: recuperar funcionários admitidos a partir de 01/08/2010 (inclusive).

~~~sql
-- Exemplo de filtro com data
SELECT	NR_MATRICULA,
        NM_FUNCIONARIO,
        DT_ADMISSAO
  FROM	T_SIP_FUNCIONARIO
  WHERE DT_ADMISSAO >= TO_DATE ('01/08/2010','DD/MM/YYYY');
~~~

## 1.5 Operadores lógicos

- utilizados para filtrar linhas de uma base de dados, usando mais de uma condição.

<div align="center">

Operador | Descrição
---------|------------
AND | Retorna TRUE se ambas as condições forem verdadeiras
OR | Retorna TRUE se ao menos uma das condições for verdadeira
NOT | Retorna TRUE se a condição for falsa

</div>

- exemplo: recuperar todos os funcionários alocados no departamento de código igual a 3, admitidos a partir de 01/08/2010.

~~~sql
-- Exemplo OPERADOR LÓGICO AND
SELECT 	NR_MATRICULA,
        NM_FUNCIONARIO,
        CD_DEPTO,
        DT_ADMISSAO
  FROM T_SIP_FUNCIONARIO
  WHERE CD_DEPTO = 3 AND
        DT_ADMISSAO > TO_DATE('01/08/2010','DD/MM/YYYY');
~~~

- exemplo: recuperar funcionários alocados no departamento de código igual a quatro o uque possuem salário maior que R$ 3.000,00.

~~~sql
-- Exemplo OPERADOR LÓGICO OR
SELECT 	NR_MATRICULA,
        NM_FUNCIONARIO,
        CD_DEPTO,
        VL_SALARIO
  FROM T_SIP_FUNCIONARIO
  WHERE CD_DEPTO = 4 OR
        VL_SALARIO > 3000 ;
~~~

- exemplo: recuperar funcionários que não estão alocados no departamento de código igual a quatro:

~~~sql
-- Exemplo OPERADOR LÓGICO NOT
SELECT 	NR_MATRICULA,
        NM_FUNCIONARIO,
        CD_DEPTO,
        VL_SALARIO
  FROM T_SIP_FUNCIONARIO
  WHERE NOT CD_DEPTO = 4 ;
~~~

## 1.6 Operadores SQL 

- operadores SQL permitem limitar as linhas recuperadas com base na correspondência de padrão de strings, listas de valores, intervalos de valores e campos nulos.

<div align="center">

Operador | Descrição
--------|-------------------
BETWEEN... AND... | Entre dois valores (inclusive)
IN (lista) | Compara o valor de uma coluna com um conjunto de valores
Like *valor* | Compara cadeia de caracteres
IS NULL / IS NOT NULL | É um valor nulo / não nulo

</div>

### 1.6.1 Operador SQL BETWEEN

- utilizado para recuperar linhas cujo valor da coluna está em um intervalo especificado; inclui os valores das duas extremidades.
- exemplo: recuperar os funcionários com remuneração (salário) entre R$ 600,00 (inclusive) e R$ 1.200,00 (inclusive).

~~~sql
-- Exemplo SQL BETWEEN
SELECT 	NR_MATRICULA,
        NM_FUNCIONARIO,
        CD_DEPTO,
        VL_SALARIO
  FROM T_SIP_FUNCIONARIO
  WHERE VL_SALARIO BETWEEN 600 AND 1200 ;
~~~

- exemplo: recuperar funcionários admitidos entre 01/01/2011 (inclusive) e 31/12/2011 (inclusive).

~~~sql
-- Exemplo SQL BETWEEN
SELECT 	NR_MATRICULA,
        NM_FUNCIONARIO,
        CD_DEPTO,
        DT_ADMISSAO
  FROM T_SIP_FUNCIONARIO
  WHERE DT_ADMISSAO 
        BETWEEN 
          TO_DATE ('01/01/2011','DD/MM/YYYY') AND
          TO_DATE ('30/12/2011','DD/MM/YYYY');
~~~

- exemplo: recuperar todos os funcionários com nome entre a letra ‘J’ (inclusive) e as letras ‘RU’ (inclusive).

~~~sql
-- Exemplo SQL BETWEEN
SELECT 	NR_MATRICULA,
        NM_FUNCIONARIO,
        CD_DEPTO,
        DT_ADMISSAO
  FROM T_SIP_FUNCIONARIO
  WHERE NM_FUNCIONARIO BETWEEN 'J' AND 'RU';
~~~

### 1.6.2 Operador SQL IN()

- utilizado para recuperar linhas cujo valor da coluna está em uma lista.
- exemplo: recuperar todos os funcionários alocados nos departamentos um, dois ou três.

~~~sql
-- Exemplo SQL IN()
SELECT  NR_MATRICULA,
        NM_FUNCIONARIO ,
        CD_DEPTO 
  FROM T_SIP_FUNCIONARIO
  WHERE CD_DEPTO IN (1, 2, 3);
~~~

- exemplo: recuperar todos os funcionários admitidos nos anos de 2010 ou 2011.

~~~sql
-- Exemplo SQL IN()
SELECT 	NR_MATRICULA,
        DT_ADMISSAO,
        VL_SALARIO
  FROM T_SIP_FUNCIONARIO
  WHERE TO_CHAR(DT_ADMISSAO,'YYYY') IN ('2010','2011');
~~~

- a função TO_CHAR converte o conteúdo informado para uma string e tem a sintaxe: TO_CHAR (&lt;conteudo&gt;,&lt;formato&gt;).
- no exemplo acima, convertemos a data em string e capturamos apenas o ano com quatro dígitos, em função do formato especificado.
- outro exemplo: recuperar todos os funcionários que não estão alocados nos departamentos um, dois ou três.

~~~sql
-- Exemplo SQL NOT IN()
SELECT 	NR_MATRICULA,
        NM_FUNCIONARIO,
        CD_DEPTO 
  FROM T_SIP_FUNCIONARIO
  WHERE CD_DEPTO NOT IN (1, 2, 3);
~~~

### 1.6.3 Operador SQL IS NULL e IS NOT NULL

- são utilizados para recuperar linhas cujo valor da coluna é nulo ou não é nulo, respectivamente.
- utilizados para avaliar se uma coluna tem valor ou não, portanto, devem ser aplicados em situações nas quais há colunas opcionais.
- exemplo: recuperar funcionários que possuem data de nascimento informada (cadastrada).

~~~sql
-- Exemplo SQL IS NOT NULL
SELECT 	NR_MATRICULA,
        NM_FUNCIONARIO ,
        DT_NASCIMENTO 
  FROM T_SIP_FUNCIONARIO
  WHERE DT_NASCIMENTO IS NOT NULL;
~~~

- exemplo: recuperar funcionários que não possuem data de nascimento informada (cadastrada).

~~~sql
-- Exemplo SQL IS NULL
SELECT 	NR_MATRICULA,
        NM_FUNCIONARIO ,
        DT_NASCIMENTO 
  FROM T_SIP_FUNCIONARIO
  WHERE DT_NASCIMENTO IS NULL ;
~~~

### 1.6.4 Operador SQL LIKE

- utilizado para recuperar linhas quando se deseja procurar um padrão em uma string.
- os padrões são especificados usando uma combinação de caracteres normais e os dois caracteres curinga:
  - Sublinhado (_): corresponde a um caractere em uma posição específica.
  - Porcentagem (%): corresponde a qualquer número de caracteres a partir da posição especificada

<div align="center">

Expressão | Descrição
-----------|-----------------
LIKE 'A%' | Todas as palavras que iniciem com a letra A.
LIKE '%A' | Todas as palavras que terminem com a letra A.
LIKE '%A%' | Todas as palavras que contenham a letra A em qualquer posição.
LIKE 'A_' | String de dois caracteres que tenham a primeira letra A e o segundo caractere seja qualquer um.
LIKE '_A' | String de dois caracteres, onde o primeiro caractere é qualquer um, e a última letra é A.
LIKE '&lowbar;A&lowbar;' | String de três caracteres, onde a segunda letra é A, independente do primeiro e último caracteres.
LIKE '%A_' | Todas as palavras que tenham a letra A na penúltima posição e a última seja qualquer outro caractere.
LIKE '_A%' | Todos que tenham a letra A na segunda posição e o primeiro caractere seja qualquer um.

</div>

- exemplo: recuperar todos os departamentos cujo nome seja iniciado com as letras ‘FINA’.

~~~sql
-- Exemplo SQL LIKE
SELECT 	CD_DEPTO,
        NM_DEPTO
  FROM 	T_SIP_DEPARTAMENTO
  WHERE NM_DEPTO LIKE 'FINA%';
~~~

- exemplo: recuperar todos os departamentos que tenham como segundo caractere do nome a letra 'A'.

~~~sql
-- Exemplo SQL LIKE
SELECT 	CD_DEPTO,
        NM_DEPTO
  FROM	T_SIP_DEPARTAMENTO
  WHERE NM_DEPTO LIKE '_A%';
~~~

- exemplo: recuperar todos os departamentos que tenham como quarto e quinto caracteres do nome as letras 'UR', respectivamente.

~~~sql
-- Exemplo SQL LIKE
SELECT 	CD_DEPTO,
        NM_DEPTO
  FROM	T_SIP_DEPARTAMENTO
  WHERE NM_DEPTO LIKE '___UR%' ;
~~~

- exemplo: recuperar todos os departamentos que tenham as letras 'MER' em qualquer parte do nome.

~~~sql
-- Exemplo SQL LIKE
SELECT 	CD_DEPTO,
        NM_DEPTO
  FROM T_SIP_DEPARTAMENTO
  WHERE NM_DEPTO LIKE '%MER%';
~~~

## 1.7 Exemplo de consulta com vários operadores

- seste exemplo, serão recuperados todos os funcionários nascidos entre 01/01/1970 e 30/12/1996, admitidos a partir de 01/01/2009, com salário inferior a R$ 1.500,00, e que não estejam alocados no departamento de código igual a três.

~~~sql
-- Exemplo utilizando vários operadores
SELECT 	NR_MATRICULA,
        CD_DEPTO,
        NM_FUNCIONARIO,
        DT_NASCIMENTO,
        DT_ADMISSAO,
        VL_SALARIO
  FROM T_SIP_FUNCIONARIO
  WHERE DT_NASCIMENTO 
    BETWEEN 
      TO_DATE('01/01/1970','DD/MM/YYYY')
    AND
      TO_DATE('30/12/1996','DD/MM/YYYY')
    AND
      DT_ADMISSAO > TO_DATE('01/01/2009','DD/MM/YYYY')
    AND VL_SALARIO < 1500 
    AND NOT CD_DEPTO=3 ;
~~~

## 1.8 Cláusula ORDER BY

- utilizada para classificar (ordenar) as linhas recuperadas por uma consulta.
- podemos especificar uma ou mais colunas para ordenar os dados de uma tabela.
- exemplo: todos os departamentos cadastrados ordenados de forma ascendente (crescente), por nome do departamento.

~~~sql
-- Exemplo ORDER BY (ASC)
SELECT 	CD_DEPTO,
        NM_DEPTO
  FROM T_SIP_DEPARTAMENTO
  ORDER BY NM_DEPTO ;
~~~

- a ordenação é por `default ascendente`; o uso do **ASC** é opcional, mas se a ordenação for descendente, o **DESC** deve ser informado obrigatoriamente.
- exemplo: retornar departamentos cadastrados, ordenados de forma descendente (decrescente), por nome do departamento.

~~~sql
-- Exemplo ORDER BY (DESC)
SELECT 	CD_DEPTO,
        NM_DEPTO
  FROM T_SIP_DEPARTAMENTO
  ORDER BY NM_DEPTO DESC;
~~~

- as opções ASC e DESC podem ser combinadas, e a classificação é feita conforme a ordem das colunas especificadas na cláusula ORDER BY.
- exemplo: recuperar todos os funcionários cadastrados alocados nos departamentos de código superior a um, ordenados de forma ascendente (crescente), por código e nome do departamento, e ordenados de forma descendente (decrescente), por salário.

~~~sql
-- Exemplo ORDER BY (ASC e DESC)
SELECT 	NR_MATRICULA,
        CD_DEPTO,
        NM_FUNCIONARIO,
        VL_SALARIO
  FROM T_SIP_FUNCIONARIO
  WHERE CD_DEPTO > 1 
  ORDER BY CD_DEPTO ASC, VL_SALARIO DESC ;
~~~

- podemos ***substituir o nome das colunas declaradas na cláusula ORDER BY pelo número de ordem das colunas declaradas na cláusula SELECT***, conforme exemplo:

~~~sql
-- Exemplo ORDER BY (ASC e DESC)
SELECT 	NR_MATRICULA,
        CD_DEPTO,
        NM_FUNCIONARIO,
        VL_SALARIO
  FROM T_SIP_FUNCIONARIO
  WHERE CD_DEPTO > 1 
  ORDER BY 2 ASC, 3 DESC, 4 DESC;
~~~

## 1.9 Operador de concatenação (||)

- permite a concatenação de colunas ou string de caracteres com outras colunas.
- a coluna resultante de uma consultaem que utilizamos este operador é uma expressão de caracteres.
- exemplo: será apresentado o texto "O funcionário &lt;nome&gt; foi admitido em &lt;data admissão&gt;", em que &lt;nome&gt; e &lt;data admissão&gt; serão obtidosa partir da leitura das colunas da tabela "FUNCIONARIO".

~~~sql
-- EXIBIR O TEXTO: "O FUNCIONARIO <NOME> FOI ADMITIDO EM <DATA>"
SELECT NR_MATRICULA,
        'O FUNCIONARIO' || 
          NM_NOME || 
        ' FOI ADMITIDO EM ' || 
          DT_ADMISSAO
FROM T_SIP_FUNCIONARIO;
~~~

## 1.10 Pseudocoluna ROWNUM








--- 

[Voltar ao início!](https://github.com/monicaquintal/fintech)