<div id="fase06" align="center">
<h1>FASE 6 - MODEL</h1>
<h2>Capítulo 03: Tornando as coisas físicas. 💪</h2>
</div>

<div align="center">
<h2>1. TORNANDO AS COISAS FÍSICAS</h2>
</div>

## 1.1 Introdução à linguagem SQL

- Structured Query Language (Linguagem Estruturada para Consulta).
- é uma linguagem para definição, manipulação e controle de banco de dados. 
- representa um conjunto de comandos responsáveis pela definição das tabelas, bem como pela seleção e atualização dos dados em bancos de dados relacionais.
- as entidades responsáveis pela padronização do SQL são o [American National Standards Institute (ANSI)](www.ansi.org) e a [International Organization for Standardization (ISO)](www.iso.org).

## 1.2 Tipos de dados

- dados são armazenados nos campos de uma tabela e devem ser informados no momento da sua criação.
- uma tabela é uma estrutura lógica usada para armazenamento de dados em Bancos de Dados Relacionais, composta de linhas e colunas.
- linhas representam os registros; e as colunas, os campos.
- para garantir a integridade dos dados e operações, é necessário que estes sejam tipificados.
  - tipos de dados são estruturas que cada SGBD utiliza para definir como os dados serão armazenados internamente.
  - são padronizados pelo ANSI, porém cada SGBD pode usar uma nomenclatura própria.
  - a capacidade de armazenamento também pode variar nos diferentes SGBDs e de acordo com a versão de um mesmo SGBD. 

> Alguns exemplos de SGBD são: Oracle, SQL Server, PostgreSQL, entre outros. Estudaremos os tipos de dados utilizados pelo ***SGBD Oracle***.

## 1.3 Tipos de dados Oracle

- o Oracle é um SGBD Objeto-Relacionais que possui recursos para armazenamento e gerenciamento de dados.
- existem vários [tipos de dados](https://docs.oracle.com/en/database/oracle/oracle-database/21/sqlrf/Data-Types.html#GUID-1BABC478-FB47-4962-9B0C-8B8BD059E733) que podem ser usados para manipular os dados em um SGBD Oracle.

<div align="center">

Tipos de de dados | Descrição
---------------|--------------
VARCHAR2(tamanho) | Dados de caractere de comprimento variável, o tamanho deve ser especificado (mínimo 1 e máximo 4000 caracteres).
CHAR(tamanho) | Dados de caractere de comprimento fixo. O tamanho default mínimo é 1 e máximo 2000 caracteres.
NUMBER(p,s) | Dados numéricos de comprimento variável, onde p é o tamanho total e s a parte correspondente aos decimais. O tamanho (p) pode variar de 1 a 38, e a escala (s) de -84 a 127 caracteres.
DATE | Valores de data e hora.
LONG | Dados de caractere de comprimento variável até 2 gigabytes.
RAW | Dados binários brutos. O tamanho máximo é de 2000 caracteres e deve ser especificado.
LONG RAW | Dados binários brutos de tamanho variável. O tamanho máximo é de 2 gigabytes.
CLOB | Dados de caractere de um byte de até 4 gigabytes.
BLOB | Dados binários de até 4 gigabytes.
BFILE | Dados binários armazenados em um arquivo externo de até 4 gigabytes.
ROWID | Um sistema numérico de base 64 que representa o endereço exclusivo de uma linha na tabela.
TIMESTAMP[frações de segundo] | Data e hora armazenadas com frações de segundo, que podem ser um valor entre 0 e 9. O valor default é 6.
TIMESTAMP[frações de segundo] WITH TIME ZONE | Armazena, além de data e hora com frações de segundo, o deslocamento de fuso horário, a diferença entre o horário local e o UTC (Coordinated Universal Time).
TIMESTAMP[frações de segundo] WITH LOCAL TIME ZONE | O Oracle retorna os dadosno fuso horário local da sessão dos usuários. Obs.: o deslocamento de fuso horário não é armazenado.
INTERVAL TO MONTH | Intervalos de anos e meses, armazena a diferença entre dois valores de datas e horas, as partes importantes são mês e ano.
INTERVAL DAY TO SECOND | Intervalos de dias, horas, minutos e segundos, armazena a diferença entre dois valores de datas e horas.

</div>

## 1.4 Descrevendo os principais tipos de dados (Oracle)

- podemos dividir os tipos de dados no Oracle em três categorias básicas: caracteres, numéricos e um grupo que representa os outros tipos de dados.

### 1.4.1 Tipo Char
- armazena uma cadeia de caracteres de tamanho fixo. 
  - pode-se opcionalmente definir o tamanho máximo de um campo do tipo CHAR. 
  - se o tamanho máximo não for definido, o valor-padrão utilizado é 1.
  - a capacidade em caracteres de um tipo CHAR depende do número de bytes utilizado para cada caractere.
- a capacidade máxima de armazenamento do tipo CHAR é de 2.000 bytes.
- para se compatibilizar com o padrão ANSI/ISO, o tipo CHAR possui um subtipo chamado CHARACTER, que possui exatamente as mesmas características.

### 1.4.2 Tipo Varchar2
- armazena caracteres de tamanho variável, com tamanho máximo de 4.000 bytes.
- tem como subtipos: VARCHAR e STRING, com características semelhantes, apenas para se compatibilizar com os padrões ANSI/ISO e tipos IBM.

> No tipo CHAR, em decorrência dotamanho ser fixo, são armazenados os caracteres e, caso não ocupe o n°. máximo, o Oracle completa as posições não utilizadas com espaços em branco. Já o tipo VARCHAR2, o tamanho é variável, é armazenado apenas o dado informado, as demais posições são disponibilizadas, desse modo, o tamanho do campo é ajustado ao espaço ocupado.

### 1.4.3 Tipo Number
- podem armazenarvalores inteiros ou de ponto flutuante entre 1E-130 e 1E125 (ponto flutuante representa as casas decimais de um número).
- pode-se especificar a precisão (número de dígitos entre 1 e 38) e a escala (número de decimais entre –84 e 127). 
- para representar valores inteiros, define-se a escala como zero (a escala representa o número de casas decimais).
- caso a escala não seja definida, o Oracle assume o valor-padrão, que é 0.
- a precisão-padrão é 38.
- no padrão Oracle, o separador decimal é o ponto (.).
- para ser compatível com os tipos ANSI/ISO, o tipo NUMBER tem subtipos com definições idênticas às dos padrões de origem. São eles: DEC, DECIMAL, DOUBLE PRECISION, FLOAT, INTEGER, INT, NUMERIC, REAL e SMALLINT.

### 1.4.4 Tipo Data/Hora

- no Oracle, mesmo que informe apenas o dia, mês e ano de uma data, ela será armazenada completa, composta de século, ano, mês, dia, hora, minuto, segundo e o dia da semana. E
- uma data válida é qualquer uma que esteja entre 1/1/4712 a.C. e 31/12/9999 d.C.
- o tipo de dado DATE armazena dados de data e hora. 
- o tipo de dado TIMESTAMP armazenadados de data e hora, mas com precisão de até 9 casas decimais para segundos (6 casas por padrão), para que possamos armazenar as frações de segundos com maior precisão.

### 1.4.5 Outros tiposde dados

- CLOB: Utilizado para armazenar caracteres de tamanho extenso, com informações superiores a 4.000 bytes.
- BLOB: Usado para armazenar dados binários. Exemplos: vídeos, músicas e imagens.
- NCHAR e NVARCHAR: Utilizado para armazenar outros tipos de caracteres, possibilitando a implementação do idioma local, por exemplo, com base no NLS = National Language Set.
- JSON: Utilizado para armazenar estruturas JSON nativamente em formato binário, possibilitando aumento de performance, uma vez que o texto não precisará mais ser convertido.

---

## FAST TEST

### 1. O tipo de dado que armazena dinamicamente uma string sem ocupar espaços desnecessários é:
> VARCHAR2.

### 2. Qual é a melhor definição para o tipo de dado BLOB?
> Usado para armazenar dados binários, como imagens, músicas e vídeos.

### 3. Como declarar um tipo de dado numérico com precisão de casas decimais no Oracle?
> Todas as anteriores.

--- 

[Voltar ao início!](https://github.com/monicaquintal/fintech)