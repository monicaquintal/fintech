<div id="fase02" align="center">
<h1>FASE 3 - MODELING</h1>
<h2>Capítulo 05: Agregando ao modelo de dados. 🎲</h2>
</div>

<div align="center">
<h2>1. AGREGANDO AO MODELO DE DADOS</h2>
</div> 

<div align="center">

## 1.1 Sobre agregação

</div>

- um modelo de dados pode e deve passar por processo de refinamento.
- `extensões` têm a função de possibilitar a correção de particularidades, para que o modelo de dados possa ser posteriormente implementado de forma física, por meio de um SGBD.
- `agregação` é uma forma de ajustar a implementação de um relacionamento do tipo muitos para muitos.
  - ***não é possível implementar fisicamente esse tipo de relacionamento***, pois a chave estrangeira não pode ser multivalorada. 
  - trata-se de uma limitação de um sistema de BD relacional: uma chave estrangeira deve fazer referência a um único valor (é monovalorada).
  - buscamos `atributos do relacionamento`, que caracterizam o relacionamento e ainda há necessidade de manter a chave estrangeira monovalorada, transformamos o relacionamento e os atributos que caracterizam esse relacionamento em um **objeto agregado**!
    - ou seja, criamos uma nova entidade para representar a associação, chamada `entidade ASSOCIATIVA`.

### Entidade associativa:

- não existe por si só em um modelo entidade relacionamento.
- sua existência está condicionada à existência de duas ou mais entidades existentes no modelo!!!
- ela existe porque as duas outras entidades existem.
- ***é chamado de agregação, pois a nova entidade agrega atributos das duas entidades que anteriormente se associavam, mais os atributos que caracterizam o relacionamento!***
- há situações em que não encontramos atributos que caracterizam este relacionamento, então utilizamos uma `nova entidade` (com intuito de ligação e solução para as chaves estrangeiras, sendo monovaloradas)!
  - quando temos entidades apenas associativas, normalmente não conseguimos identificar um nome que represente a entidade e, ***no momento de nomeá-la, utilizamos os nomes das entidades que se associavam anteriormente!!!***

## 1.1.1 Exemplificando agregação

~~~
Suponha a seguinte situação: 

Um médico pode avaliar, examinar e consultar um paciente, 
e um paciente pode ser avaliado, examinado, consultado por um médico.

Cada médico pode avaliar, examinar, consultar vários pacientes,inclusive o mesmo paciente várias vezes.
Cada paciente pode ser avaliado, examinado, consultado por vários médicos, 
inclusive com o mesmo médico várias vezes.
~~~

<br>
<div align="center">
<img src="../assets/imagens-fase03/relacionamento-medico-paciente.png" width="50%"><br>
<em>Exemplo de relacionamento entre médico e paciente.</em>
</div>
<br>

<div align="center">
<img src="../assets/imagens-fase03/relacionamento-medico-paciente2.png" width="50%"><br>
<em>Exemplo 2 de relacionamento entre médico e paciente, de forma mais detalhada.</em>
</div>
<br>

- relacionamento com cardinalidade M:N.
- ***atributos que caracterizam o relacionamento M:N - Consulta Médica***:
  - data e hora.
  - sala ou consultório.
- portanto, cria-se a nova entidade **CONSULTA**.
  - passamos a ter dois relacionamentos 1:N:
    - um entre “MEDICO” e “CONSULTA”;
    - e outro entre “PACIENTE” e “CONSULTA”!

<br>
<div align="center">
<img src="../assets/imagens-fase03/relacionamento-medico-paciente3.png" width="50%"><br>
<em>Criação da entidade associativa "Consulta".</em>
</div>
<br>

- Características da entidade CONSULTA → { Data e hora, Sala ou consultório }.

- representação gráfica com ferramenta SQL Developer Data Modeler (notação da Engenharia da Informação).

<br>
<div align="center">
<img src="../assets/imagens-fase03/relacionamento-medico-paciente4.png" width="50%"><br>
<em>Relacionamento entre médico e paciente em um modelo lógico.</em>
</div>
<br>

- representação do relacionamento por meio da nova entidade “CONSULTA”:

<br>
<div align="center">
<img src="../assets/imagens-fase03/relacionamento-medico-paciente5.png" width="50%"><br>
<em>Relacionamento médico e paciente envolvendo a entidade associativa consulta.</em>
</div>
<br>

## 1.1.2 Regras ou soluções possíveis para determinar a chave primária em uma agregação

### 1ª Solução: 
- criar uma chave primária composta pelas chaves estrangeiras, caso garantam unicidade das ocorrências, obtendo um relacionamento identificado.

### 2ª Solução:
- criar um novo atributo para ser a chave primária desta entidade.
- chaves estrangeiras não são utilizadas como identificadores. 
- o novo atributo será utilizado para garantir a unicidade das ocorrências.
- ***solução utilizada no exemplo acima***!

### 3ª Solução:
- criar uma chave primária composta por uma das chaves estrangeiras, mais um atributo da própria entidade (desde que juntos garantam a unicidade das ocorrências). 
- teríamos um relacionamento identificado de um dos lados.
- considerando que a nova entidade é uma ***entidade FRACA*** (depende das outras entidades para existir), utilizamos a mesma regra da chave primária da entidade FRACA.

> para cada situação deve-se avaliar a melhor solução a ser aplicada de acordo com o contexto de negócio e as necessidades de armazenamento!

## 1.1.3 Evoluindo o exemplo de agregação

~~~
Suponha a situação: durante uma consulta, um Médico prescreve medicamentos para um Paciente.

Em cada consulta, o Médico pode prescrever medicamentos diferentes para o Paciente, ou até nenhum.

Mas, para existir uma prescrição, o paciente deve obrigatoriamente passar por uma consulta médica.

Portanto, a prescrição seria um relacionamento entre uma entidade Medicamento e o relacionamento consulta.

Cada consulta pode prescrever vários medicamentos ou nenhum.
Cada medicamento pode ser prescrito em várias consultas ou nenhuma.
~~~

<br>
<div align="center">
<img src="../assets/imagens-fase03/relacionamento-conculta-medicamento1.png" width="50%"><br>
<em>Relacionamento entre consulta e medicamento.</em>
</div>
<br>

págs 5 e 13
