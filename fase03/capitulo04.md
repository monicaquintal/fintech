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

- exemplos:

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