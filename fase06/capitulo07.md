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

- todas as tabelas possuem a pseudocoluna ROWNUN, utilizada quando precisamos limitar a quantidade de linhas retornadas por meio de um comando SELECT.
- podemos usá-la, por exemplo, para recuperar certo número de linhas por vez para auxiliar a paginação em uma página WEB.
- exemplo: retornar as quatro primeiras linhas da tabela T_SIP_FUNCIONARIO.

~~~sql
-- Exemplo pseudocoluna ROWNUM
SELECT NR_MATRICULA,
       CD_DEPTO,
       DT_ADMISSAO,
       VL_SALARIO,
       (VL_SALARIO * 12) "SALÁRIO ANUAL"
  FROM T_SIP_FUNCIONARIO
  WHERE ROWNUM < 4;
~~~

- análise top-n (): análise que permite montar um ranking, de forma crescente ou decrescente.

~~~sql
  SELECT ROWNUM as RANK, 
         NM_FUNCIONARIO,
         VL_SALRIO
  FROM
    (
      SELECT NM_FUNCIONARIO,
             VL_SALARIO
        FROM T_SIP_FUNCIONARIO
      ORDER BY VL_SALARIO DESC
    ) 
  WHERE ROWNUM <= 3;
~~~

## 1.11 Pesquisa em múltiplas tabelas

### 1.11.1 NATURAL JOIN –Junção interna

- segue a padronização ANSI, e implica criar a junção interna entre duas tabelas.
- a junção é feita por meio de colunas com o mesmo nome nas duas tabelas.
- esse tipo de junção surgiu a partir da padronização ANSI 99.
- caso as colunas tenhamo mesmo nome, mas tipos de dados diferentes, será retornado um erro. 
- é ilustrada por meio da intersecção entre dois conjuntos.
- exemplo: recuperar todos os funcionários e respectivos departamentos nos quais trabalham.

~~~sql
--EXEMPLO - NATURAL JOIN
SELECT F.NR_MATRICULA "MATRICULA",
       CD_DEPTO "COD. DEPTO" ,
       D.NM_DEPTO "DEPARTAMENTO", 
       F.NM_FUNCIONARIO "FUNCIONARIO"
  FROM T_SIP_DEPARTAMENTO D 
  NATURAL JOIN T_SIP_FUNCIONARIO F;
~~~

> **NOTA**: não aplicar o qualificador na coluna “CD_DEPTO”, pois acarretará um erro. Quando utilizamos NATURAL JOIN, não podemos usar qualificadores para as colunas Chaves Primária/Estrangeira.

- há situações em que tabelas possuem campos com nomes iguais, mas conteúdos diferentes.
- nesses casos, podemos modificar a NATURAL JOIN adicionando a ***cláusula USING*** para especificar as colunas que devem ser usadas em uma junção.
- exemplo:

~~~sql
--EXEMPLO - NATURAL JOIN e cláusula USING
SELECT F.NR_MATRICULA "MATRICULA",
       CD_DEPTO "COD. DEPTO" ,
       D.NM_DEPTO "DEPARTAMENTO", 
       F.NM_FUNCIONARIO "FUNCIONARIO"
  FROM T_SIP_DEPARTAMENTO D 
  NATURAL JOIN T_SIP_FUNCIONARIO F
  USING (CD_DEPTO);
~~~

### 1.11.2 INNER JOIN – Junção interna

- segue o padrão ANSI e, na união de duas tabelas, serão exibidos todos os dados para os quais exista correspondência entre a Chave Primária e Chave Estrangeira.
- ou seja, INNER JOIN pode ser representado pela intersecção entre duas (ou mais) tabelas.
- exemplo: exibir funcionários e respectivos departamentos. 
  - a condição de junção é estabelecida na cláusula ON, em que comparamos a Chave Primária à Chave Estrangeira, com o objetivo de recuperar a intersecção entre as tabelas.

~~~sql
-- EXEMPLO - INNER JOIN – Padrão SQL/99
SELECT F.NR_MATRICULA "MATRICULA",
       F.CD_DEPTO "COD. DEPTO",
       D.NM_DEPTO "DEPARTAMENTO", 
       F.NM_FUNCIONARIO "FUNCIONARIO"
  FROM T_SIP_DEPARTAMENTO D INNER JOIN
    T_SIP_FUNCIONARIO F 
  ON ( D.CD_DEPTO = F.CD_DEPTO )
  ORDER BY D.NM_DEPTO;
~~~

- o mesmo exemplo pode ser reescrito de acordo com o padrão Oracle para equijunções (era utilizado antes da sua adequação ao SQL/99).
- a condição de junção é feita na cláusula WHERE, em que comparamos a Chave Primária à Estrangeira, para obter a intersecção entre as tabelas.

~~~sql
-- EXEMPLO - INNER JOIN – Padrão ORACLE
SELECT F.NR_MATRICULA "MATRICULA",
       F.CD_DEPTO "COD. DEPTO",
       D.NM_DEPTO "DEPARTAMENTO", 
       F.NM_FUNCIONARIO "FUNCIONARIO"
  FROM T_SIP_DEPARTAMENTO D,
    T_SIP_FUNCIONARIO F 
  WHERE D.CD_DEPTO = F.CD_DEPTO
  ORDER BY D.NM_DEPTO;
~~~

- a instrução INNER JOIN pode ser modificada, adicionando-se a ela a cláusula USING para especificar as colunas que devem ser usadas em uma junção.

~~~sql
SELECT F.NR_MATRICULA "MATRICULA",
       F.CD_DEPTO "COD. DEPTO",
       D.NM_DEPTO "DEPARTAMENTO", 
       F.NM_FUNCIONARIO "FUNCIONARIO"
  FROM T_SIP_DEPARTAMENTO D INNER JOIN
    T_SIP_FUNCIONARIO F 
  USING CD_DEPTO
  ORDER BY NM_DEPTO;
~~~

> NOTA: não utilizar apelido ou nome de tabelas nas colunas em que a referência for feita (Chave Primária/Chave Estrangeira)!!!

### 1.11.3 INNER JOIN com duas ou mais tabelas – Junção interna

- podemos combinar duas ou mais tabelas.
- a condição de junção é estabelecida na cláusula ON, em que comparamos a Chave Primária à Estrangeira, com o objetivo de recuperar a intersecção entre as tabelas (comparação aos pares).
- exemplo: serão recuperados todos os funcionários associados aos projetos que estão atuando (implantando) e ordenados por nome do funcionário.

~~~sql
-- EXEMPLO - INNER JOIN – Padrão SQL/99
  SELECT F.NR_MATRICULA "MATRICULA",
        F.NM_FUNCIONARIO "FUNCIONARIO",
        P.NM_PROJETO "PROJETO",
        I.DT_ENTRADA "ENTRADA",
        I.DT_SAIDA "SAIDA"
  FROM T_SIP_PROJETO P INNER JOIN 
        T_SIP_IMPLANTACAO I
        ON ( P.CD_PROJETO = I.CD_PROJETO )
        INNER JOIN T_SIP_FUNCIONARIO F 
        ON ( F.NR_MATRICULA = I.NR_MATRICULA )
  ORDER BY F.NM_FUNCIONARIO ;
~~~

- exemplo da sintaxe, utilizando a cláusula USING, para tabelas que possuem colunas com o mesmo nome:

~~~sql
-- EXEMPLO COM INNER JOIN - PADRÃO SQL/99
-- CLÁUSULA USING
SELECT NR_MATRICULA "MATRICULA",
       F.NM_FUNCIONARIO "FUNCIONARIO",
       P.NM_PROJETO "PROJETO",
       I.DT_ENTRADA "ENTRADA",
       I.DT_SAIDA "SAIDA"
  FROM T_SIP_PROJETO P INNER JOIN 
       T_SIP_IMPLANTACAO I
    USING ( CD_PROJETO )
    INNER JOIN T_SIP_FUNCIONARIO F 
    USING ( NR_MATRICULA )
ORDER BY F.NM_FUNCIONARIO ;
~~~

> NOTA: não aplicar o qualificador na coluna “NR_MATRICULA”, acarretará um erro. Quando utilizamos INNER JOIN com a cláusula USING, não podemos usar qualificadores para as colunas Chaves Primária/Estrangeira.

- exemplo anterior reescrito com o padrão Oracle:

~~~sql
-- EXEMPLO COM INNER JOIN - PADRÃO ORACLE (ANTES SQL/99)
SELECT F.NR_MATRICULA "MATRICULA",
       F.NM_FUNCIONARIO "FUNCIONARIO",
       P.NM_PROJETO "PROJETO",
       I.DT_ENTRADA "ENTRADA",
       I.DT_SAIDA "SAIDA"
  FROM T_SIP_PROJETO P,
       T_SIP_FUNCIONARIO F ,
       T_SIP_IMPLANTACAO I
  WHERE P.CD_PROJETO = I.CD_PROJETO AND
        F.NR_MATRICULA = I.NR_MATRICULA
ORDER BY F.NM_FUNCIONARIO ;
~~~

> DICA: no padrão SQL, a ordem em que colocamos as tabelas na cláusula FROM determina quais tabelas serão pesquisadas primeiro. Logo, se colocarmos as tabelas menores primeiro, a busca ficará mais rápida.Portanto, deixe as tabelas maiores, sempre que possível, para o final da cláusula!!!

### 1.11.4 Junções externas

- utilizada para recuperar as linhas de um EQUIJOIN, podendo, em alguma das tabelas, não existir linhas/registros correspondentes.
- a junção externa pode ser ***esquerda, direita ou completa***.
- junção externa é aquela que inclui linhas no resultado da busca, mesmo que não haja relação entre as duas tabelas que estão sendo combinadas.
- onde não houver informação, será recuperado NULL.
- há três formas de realizar uma junção externa:
  - `Left Outer Join`: 
    - junção externa à esquerda.
    - recupera todas as linhas do EQUIJOIN, além das que não possuem correspondentes na tabela à esquerda da operação.
  - `Right Outer Join`:
    - junção externa à direita.
    - recupera todas as linhas do EQUIJOIN, além das que não possuem correspondentes na tabela à direita da operação.
  - `Full Outer Join`:
    - junção completa.
    - recupera todas as linhas do EQUIJOIN, além das que não possuem correspondentes na tabela à direita e à esquerda da operação.

### 1.11.5 Left outer join

- todas as linhas da tabela à esquerda serão recuperadas, independentemente da existência de ocorrências relacionadas na tabela da direita, ou seja, entre a Chave Primária e a Chave Estrangeira.
- preserva as linhas se correspondência da primeira tabela (esquerda), juntando-as com uma linha nula na forma da segunda tabela (direita).
- a condição de junção é estabelecida na cláusula ON, onde comparamos a Chave Primária à Chave Estrangeira, com o objetivo de recuperar a intersecção ou não entre as tabelas.
- as linhas/registros recuperados são aqueles que atendem à intersecção dos conjuntos ou não.
- exemplo: nos projetos em que não há funcionários atuando em implantações, no momento da recuperação, os dados serão preenchidos com NULL.

~~~sql
-- EXEMPLO LEFT OUTER JOIN - PADRÃO SQL/99
SELECT P.CD_PROJETO "CÓDIGO" ,
       P.NM_PROJETO "PROJETO" ,
       P.DT_INICIO "DATA INÍCIO" ,
       I.NR_MATRICULA "MATRÍCULA FUNCIONÁRIO" ,
       I.DT_ENTRADA "ENTRADA" 
  FROM T_SIP_PROJETO P LEFT OUTER JOIN
      T_SIP_IMPLANTACAO I
    ON ( P.CD_PROJETO = I.CD_PROJETO );
~~~

- podemos recuperar somente os projetos que não possuem funcionários atuando em implantações.

~~~sql
-- EXEMPLO COM LEFT OUTER JOIN - PADRÃO SQL/99 -
-- COM VALIDAÇÃO DOS RESULTADOS NULOS
SELECT P.CD_PROJETO "CÓDIGO" ,
       P.NM_PROJETO "PROJETO" ,
       P.DT_INICIO "DATA INÍCIO" ,
       I.NR_MATRICULA "MATRÍCULA FUNCIONÁRIO" ,
       I.DT_ENTRADA "ENTRADA" 
  FROM T_SIP_PROJETO P LEFT OUTER JOIN
      T_SIP_IMPLANTACAO I
    ON ( P.CD_PROJETO = I.CD_PROJETO )
    WHERE I.CD_PROJETO IS NULL;
~~~

- exemplo da sintaxe, utilizando a cláusula USING, quando as colunas possuem o mesmo nome.

~~~sql
-- EXEMPLO COM LEFT OUTER JOIN - PADRÃO SQL/99 -
-- CLÁUSULA USING
SELECT P.CD_PROJETO "CÓDIGO" ,
       P.NM_PROJETO "PROJETO" ,
       P.DT_INICIO "DATA INÍCIO" ,
       I.NR_MATRICULA "MATRÍCULA FUNCIONÁRIO" ,
       I.DT_ENTRADA "ENTRADA" 
  FROM T_SIP_PROJETO P LEFT OUTER JOIN
      T_SIP_IMPLANTACAO I
    USING ( CD_PROJETO );
~~~

> NOTA: Não aplicar o qualificador na coluna “CD_PROJETO”, acarretará um erro. Quando utilizamos LEFT OUTER JOIN com a cláusula USING, não podemos usar qualificadores para colunas Chaves Primária/Estrangeira.

- exemplo da sintaxe aceita pelo Oracle:

~~~sql
-- EXEMPLO COM LEFT OUTER JOIN - PADRÃO ORACLE
-- OPERADOR ( + )
SELECT P.CD_PROJETO "CÓDIGO" ,
       P.NM_PROJETO "PROJETO" ,
       P.DT_INICIO "DATA INÍCIO" ,
       I.NR_MATRICULA "MATRÍCULA FUNCIONÁRIO" ,
       I.DT_ENTRADA "ENTRADA" 
  FROM T_SIP_PROJETO P,
      T_SIP_IMPLANTACAO I
    WHERE P.CD_PROJETO = I.CD_PROJETO (+);
~~~

> NOTA: o operador (+) deve ser inserido ao lado da coluna que poderá ter o valor nulo. Este operador só poderá ser colocado em um dos lados. Caso se coloque nos dois lados, será gerado um erro!

- podemos recuperar somente projetos que não possuem funcionários atuando em implantações. Para isso,deverá ser inserida a validação do NULO, na cláusula WHERE, nesta sintaxe:

~~~sql
-- EXEMPLO COM LEFT OUTER JOIN - PADRÃO ORACLE
-- OPERADOR ( + )
SELECT P.CD_PROJETO "CÓDIGO" ,
       P.NM_PROJETO "PROJETO" ,
       P.DT_INICIO "DATA INÍCIO" ,
       I.NR_MATRICULA "MATRÍCULA FUNCIONÁRIO" ,
       I.DT_ENTRADA "ENTRADA" 
  FROM T_SIP_PROJETO P,
      T_SIP_IMPLANTACAO I
    WHERE P.CD_PROJETO = I.CD_PROJETO (+)
          AND I.CD_PROJETO IS NULL;
~~~

### 1.11.6 RIGHT OUTER JOIN – Junções externas











--- 

[Voltar ao início!](https://github.com/monicaquintal/fintech)