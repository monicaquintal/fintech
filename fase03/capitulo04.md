<div id="fase02" align="center">
<h1>FASE 3 - MODELING</h1>
<h2>Capítulo 04: O Modelo de Entidade-Relacionamento.</h2>
</div>

<div align="center">
<h2>1. O MODELO DE ENTIDADE-RELACIONAMENTO (MER)</h2>
</div> 

- conjunto de objetos (entidades e relacionamentos), obtidos a partir da análise das necessidades de armazenamento de um determinado negócio (perspectiva do mundo real).
- representado pelo Diagrama Entidade-Relacionamento (DER).
- o `DER` é um artefato essencial na definição de uma forma organizada para o armazenamento de dados!

## 1.1 Cardinalidade dos atributos

- indica quantidade de valores que um atributo pode ter.
- a cardinalidade de um atributo define quantos valores desse atributo podem estar associados a uma ocorrência da entidade/relacionamento a qual ele pertence.
- todo atributo possui cardinalidade mínima e cardinalidade máxima:

  - `cardinalidade mínima`:
    - indica quantos valores, no mínimo, um atributo pode possuir;
    - pode ter dois valores válidos: 
      - `0` (no diagrama,será representado graficamente pelo sinal O), que indica que um atributo não terá nenhum valor preenchido em cada ocorrência da entidade, ou seja, será um ***atributo opcional***!
      - `1` (no diagrama, será representado graficamente pelo sinal &lowast;), que indica que um atributo terá um valor preenchido obrigatoriamente em cada ocorrência da entidade, ou seja, será um ***atributo mandatório (obrigatório)***.

  - `cardinalidade máxima`:
    - aponta quantos valores, no máximo, um atributo pode ter.
    - poderá ter dois valores válidos: 
      - `1`, o qual mostra que um atributo terá no máximo um único valor preenchido em cada ocorrência da entidade, ou seja, será um ***atributo monovalorado (único valor)***!
      - `N`, o qual representa que um atributo terá no máximo vários valores (dois ou mais) para cada ocorrência da entidade, ou seja, será um ***atributo multivalorado (vários valores)***!

<div align="center">

Cardinalidade | Valores
:--------------:|------------
Mínima | MIN = 0 -> atributo opcional<br>MIN = 1 -> atributo mandatório (obrigatório)
Máxima | MAX = 1 -> atributo monovalorado<br>MAX = N -> atributo multivalorado

</div>

Exemplos:<br>

a) Nome do aluno (todo aluno possui um e apenas um nome):
  - Cardinalidade mínima = 1 ⟶ atributo mandatório (obrigatório).
  - Cardinalidade máxima = 1 ⟶ atributo monovalorado.

b) Telefone (nem todas as pessoas tem telefone e, se tiver, pode ser residencial, comercial e/ou celular):
  - Cardinalidade mínima = 0 → atributo opcional.
  - Cardinalidade máxima = N → atributo multivalorado.

c) Nota (nem todos os alunos realizam avaliação na data marcada, podendo ter notas não informadas):
  - Cardinalidade mínima = 0 → atributo opcional.
  - Cardinalidade máxima = 1 → atributo monovalorado.

## 1.2 Decomposição de atributos

- atributos compostos: 
  - possuem muitos dados agrupados para formar a informação.
  - exemplos: telefone (DDI + DDD + telefone + ramal + nome) e endereço (tipo logradouro, nome, número, complemento, bairro, cep, cidade, estado).
- o nível de decomposição de um atributo depende dos requerimentos do negócio.
  - alguns atributos nunca são decompostos, como data e hora.

## 1.3 Convenção de nomenclatura para atributos e entidades

- é considerado boa prática utilizar uma nomenclatura padronizada para os atributos e entidades.
- normalmente, cada empresa cria um padrão a ser seguido. 
- neste caso, será utilizada a padronização considerando o SGBD Oracle.

### 1.3.1 Nomenclatura de tabelas e campos

- bancos de dados modernos permitem tamanhos maiores, porém convencionou-se (padrão SQL-ANSI) tamanho máximo do nome da tabela (por enquanto, conhecido como entidade) e do nome de um campo (no momento, conhecido como atributo) em, `no máximo, 30 caracteres`.

### 1.3.2 Caracteres permitidos

- letras.
- números.
- underline (_).
- cifrão ($) e cerquilha (#).

Embora números sejam permitidos, não podem iniciar o nome da entidade ou atributo, que geralmente começa com uma letra.

### 1.3.3 Padrão recomendado

<div align="center">

Tabela (Entidade) | Campos (atributos)
------------------|--------------------
SINGULAR | SINGULAR
Primeiro caractere deve ser uma letra | Primeiro caractere deve ser uma letra
***Letras maiúsculas*** | ***Letras minúsculas***

</div>

### 1.3.3.1 Nomenclatura para nomes de TABELAS (ENTIDADES)

- inicializar o nome com a letra `T`.
- utilizar 3 caracteres como prefixo para indicar a sigla do sistema.
- nome atribuído à tabela.
- utilize o underline (_) como separador.
- nomes compostos separar com o underline (_).

Exemplo de convenção de nomes de Tabelas (Entidades):
- Entidade: Funcionário
- Sistema: Sistema de Controle de Implantação de Projetos – Sigla: SIP
- Exemplo: T_SIP_FUNCIONARIO
  - T → Indica tabela
  - SIP → Nome do sistema
  - FUNCIONARIO → Nome da tabela

### 1.3.3.2 Nomenclatura para nomes de CAMPOS(ATRIBUTOS)

- utilizar 2 ou 3 caracteres como prefixo para indicar o significado da coluna.
- utilizar o underline (_) como separador.
- nome atribuído à coluna (sufixo).
- nomes compostos separar com o underline (_).

Exemplo de convenção de nomes de Campos (Atributos):
- Entidade: Funcionario
- Exemplo: nr_matricula
  - nr → indica o prefixo do nome
  - matricula → indica o nome da coluna

<div align="center">

T_SIP_FUNCIONARIO atributos | Nome dos atributos (convenção)
----------------------------|-------------------
matrícula funcionario | nr_matricula
nome | nm_nome
data nascimento | dt_nascimento
data admissão | dt_admissao
endereço | ds_endereco
salário | vl_salario
código departamento | cd_departamento

</div>

### 1.3.3.3 Lista de prefixos comumente utilizados

<div align="center">

Prefixo (2 caracteres) | Prefixo (3 caracteres) | Significado
-----------------------|------------------------|-----------------
Nr | Num | Número (pode identificar exclusivamente)
Cd | cod | Código (assinala esclusivamente uma ocorrência)
Id | Idt | Identificador (aponta excluivamente uma ocorrênca)
Ds | Des | Descrição
Nm | Nom | Nome
Dt | Dat | Data
Vl | Val | Valor
Qt | Qtd | Quantidade
Sq | Seq | Número sequencial que reconhece algo do mundo real
In | Ind | Indicador
St | Sta | Status
Ob | Obs | Observação
Tx | Txt | Texto extenso

</div>

## 1.4 Representação gráfica de entidades e atributos

### 1.4.1 Visão Lógica

- utilizamos `#` para identificar a `chave primária` ou atributo identificador na representação gráfica da entidade. 
- há diversas notações (formas de retratar ou expressar informações de forma gráfica ou por sinais, a fim de simplificar a representação de ideias, problemas e soluções). 
- as mais utilizadas são as notações de Barker e da Engenharia da Informação (a seguir).

<br>
<div align="center">
<img src="../assets/imagens-fase03/ex1-barker.png" width="40%"><br>
<em>Exemplo de notação de Barker.</em>
</div>
<br>

<div align="center">
<img src="../assets/imagens-fase03/ex1-ei.png" width="40%"><br>
<em>Exemplo de notação da Engenharia da Informação.</em>
</div>
<br>

<div align="center">
<img src="../assets/imagens-fase03/aplicando-data-modeler.png" width="40%"><br>
<em>Exemplo de aplicação das notações, utilizando Oracle SQL Developer Data Modeler.</em>
</div>
<br>

### 1.4.2 Visão Física ou Relacional

<div align="center">
<img src="../assets/imagens-fase03/ex1-visao-fisica.png" width="40%"><br>
<em>Exemplo de visão física ou relacional.</em>
</div>
<br>

### 1.4.3 Notação de Peter Chen

<div align="center">
<img src="../assets/imagens-fase03/ex1-peter-chen.png" width="40%"><br>
<em>Exemplo de notação de Peter Chen.</em>
</div>
<br>

---

<div align="center">
<h2>2. RELACIONAMENTOS</h2>
</div>

- um relacionamento é a representação de uma ação ou fato que associa as ocorrências de uma entidade com as de outra entidade.
- ou seja, é o conjunto de associações entre ocorrências de entidades!
- ***identificação dos relacionamentos***:
  - analisar as entidades sempre aos pares.
  - todo relacionamento tem:
    - ***Nome***: normalmente um verbo: gravar, escrever, indicar etc.
    - ***Opcionalidade***> deve ou pode.
    - ***Cardinalidade***: nenhuma, uma única, uma ou mais ocorrências associadas.

## 2.1 Cardinalidade do relacionamento

- indica a quantidade de ocorrências de uma entidade A relacionadas com as de uma entidade B (é sempre colocada no lado oposto à entidade, quando fazemos o diagrama).
- há ***três tipos de relacionamentos***:
  - Relacionamento Um-para-Um (1:1). 
  - Relacionamento Um-para-Muitos (1:n).
  - Relacionamento Muitos-para-Muitos (m:n).
- todo relacionamento possui cardinalidade mínima e cardinalidade máxima:
  - mínima: indica com quantas ocorrências no mínimo uma entidade irá se associar com outra entidade.
  - cardinalidade máxima: aponta com quantas ocorrências no máximo uma entidade irá se associar com outra entidade.

<div align="center">

Cardinalidade | Significado
--------------|---------------
Mínima | min = 0 → pode (condicional)<br>min = 1 → deve (incondicional)
Máxima | 1 : 1<br>1 : N<br>M : N

</div>

- ***importante***:
  - **linha tracejada** indica um **relacionamento opcional** (Condicional – cardinalidade mínima igual a zero).
  - **linha contínua** aponta um **relacionamento obrigatório** (Incondicional – cardinalidade mínima igual a um).

> Durante a análise de uma associação, a ***Chave Estrangeira deve ficar na entidade em que a cardinalidade máxima desse atributo (Chave Estrangeira) for igual a 1***, ou seja, a Chave Estrangeira é sempre um atributo MONOVALORADO!

## 2.2 Caracterização dos relacionamentos

### 2.2.1 Relacionamento 1:1

- quando cada ocorrência da entidade (A) se associa,no máximo, a uma ocorrência da entidade (B).
- e cada ocorrência da entidade (B) associa-se, no máximo, com uma ocorrência da entidade (A).
(É necessário analisar sempre os dois sentidos do relacionamento)

<details>
<summary><strong>Exemplo 1 💭</strong></summary>
<em>
Dada a situação de um homem ser casado com uma mulher e uma mulher ser casada com um homem.<br>Lembrando que nem todas as pessoas são casadas.<br>
E considerando a regra:

- No Brasil, o casamento é monogâmico, portanto, um homem só pode ser casado com uma mulher e uma mulher só pode ser casada com um único homem.
</em>

### Temos:

- associação “RELACIONAMENTO” é **CONDICIONAL** (só haverá ocorrências associadas para os indivíduos que forem casados).

<div align="center">
<img src="../assets/imagens-fase03/diagrama-exemplo1.png" width="40%"><br>
<em>Exemplo de diagrama de relacionamento entre as entidades homem e mulher.</em>
</div>
<br>

<div align="center">
<img src="../assets/imagens-fase03/exemplo-homem-mulher.png" width="40%"><br>
<em>Exemplo de relacionamento entre as entidades homem e mulher.</em>
</div>
<br>

- representação gráfica por meio da ferramenta SQL Developer Data Modeler (notação de Barker).

<div align="center">
<img src="../assets/imagens-fase03/exemplo-homem-mulher2.png" width="40%"><br>
<em>Exemplo de relacionamento entre as entidades homem e mulher.</em>
</div>
<br>

- exemplo da relação entre ocorrências nas tabelas:

<img src="../assets/imagens-fase03/exemplo-tabelas-homem-mulher.png" width="40%"><br>
<em>Exemplo das tabelas homem e mulher com registros.</em>
</div>
<br>

- Nota: exemplo de Relacionamento 1:1 – Não obrigatório (CONDICIONAL), cardinalidade mínima igual a zero.
- Leia-se: um homem pode ser casado, se casado será com uma única mulher. Uma mulher pode ser casada, se casada será com um único homem.
  - cada ocorrência da entidade “T_HOMEM” se associa,no máximo, com uma ocorrência da entidade “T_MULHER”.
  - cada ocorrência da entidade “T_MULHER” se associa, no máximo, com uma ocorrência da entidade “T_HOMEM”.
- Atenção: em toda a associação 1:1, deve-se indicar a entidade DOMINANTE, a entidade dominada ou filha receberá a Chave Estrangeira. 
  - Lembrando que a Chave Estrangeira ficará na entidade em que a cardinalidade máxima do relacionamento é igual a 1, nesse caso, pode ser qualquer uma das entidades. 
  - A Chave Estrangeira é sempre um atributo monovalorado.

</details>


<details>
<summary><strong>Exemplo 2 💭</strong></summary>

<em>Dada a situação hipotética de um departamento possuir um único gerente e um gerente gerenciar um único departamento.<br>
Lembrando que nem todos os funcionários gerenciam departamentos.<br>
Considerando a regra abaixo:

- Levando em conta um momento no tempo e não um histórico de possíveis alterações no quadro funcional ou na divisão de departamentos, períodos de férias etc.

### Temos:

- associação “RELACIONAMENTO” é **INCONDICIONAL**, pois todas as ocorrências serão associadas entre as entidades.

<div align="center">
<img src="../assets/imagens-fase03/exemplo-departamento-funcionario.png" width="40%"><br>
<em>Exemplo de relacionamento entre entidades departamento e gerente.</em>
</div>
<br>

- representação gráfica por meio da ferramenta SQL Developer Data Modeler (notação de Barker).

<div align="center">
<img src="../assets/imagens-fase03/exemplo-departamento-funcionario2.png" width="40%"><br>
<em>Exemplo de modelo lógico entre departamento e gerente.</em>
</div>



</details>