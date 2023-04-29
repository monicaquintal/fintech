<div id="fase02" align="center">
<h1>FASE 3 - MODELING</h1>
<h2>Capítulo 03: Como guardar as informações?</h2>
</div>

<div align="center">
<h2>Ciclo de vida de um banco de dados</h2>
</div>

O ciclo de vida de um banco de dados é composto pelas fases de:
- “Requisitos de Informação”, 
- “Projeto Lógico”, 
- “Projeto Físico” e 
- “Implementação”.

<br>
<div align="center">
<img src="../assets/imagens-fase03/ciclo-vida-bd.png"><br>
<em>Ciclo de vida de um banco de dados.</em>
</div>
<br>

### A) Análise de Requisitos (Requisitos de Informação): 
- determinados a partir da entrevista com os usuários do banco de dados, que envolve a obtenção das seguintes informações: 
  - dados exigidos para o processamento,
  - relacionamentos dos dados e 
  - plataforma de software para implementação do banco de dados.

### B) Projeto Lógico:
- representado por um modelo de dados conceitual que mostra todos os dados e seus relacionamentos e realiza a normalização dos dados.
- dentro do Projeto Lógico, temos:
  - **Modelo de dados conceitual:** requisitos são modelados por meio de um Diagrama ER (Entidade-Relacionamento).
  - **Integração da visão:** quando temos projetos grandes com vários envolvidos na análise de requisitos, existem várias visões dos dados e relacionamento.
  - **Transformação do modelo de dados em tabelas:** entidades e relacionamentos do modelo são transformados em tabelas relacionais.
  - **Normalização:** técnicas padronizadas, eliminação de redundâncias e preservação da integridade.

### C) Projeto Físico: 
- envolve a seleção de índices (métodos de acesso) e eventuais desnormalizações de dados, quando couberem.

### D) Implementação, monitoração e modificação de banco de dados: 
- após finalização do projeto, o banco de dados é implementado usando a linguagem de definição de dados de um SGBD.
- a monitoração envolve indicar se os requisitos de desempenho estão sendo atendidos e mudanças podem ser feitas para melhor desempenho. 
- Outras alterações podem ocorrer quando os requisitos mudam ou são inseridos novos requisitos!

---

<div align="center">
<h2>Modelagem de dados</h2>
</div>

## 1. Introdução a modelagem de dados

- modelagem de dados permite que as informações coletadas na fase de análise de requisitos possam ser estudadas e analisadas dentro de seu contexto, permitindo decidir a melhor maneira de armazená-las.
- nesse momento, não há preocupação com qual SGBD será utilizado, pois possuem particularidades inerentes às suas estruturas físicas. 
- na modelagem lógica, o foco são os dados que precisam ser armazenados e suas relações!
- ***o estudo do modelo lógico é tão independente do SGBD que pode ser feito antes mesmo de decidir qual deles usar.***

## 2. Níveis de abstração da modelagem de dados

- é um método de análise que, a partir das necessidades apontadas pelos usuários dentro de um contexto, apresenta os dados de uma estrutura de armazenamento, organizada e inter-relacionada, expressa por meio de uma representação gráfica.
- a modelagem de dados permite que o analista/desenvolvedor conheça melhor o contexto de negócio, facilitando a criação de uma estrutura de armazenamento que descreva mais adequadamente as necessidades.
  - Isso possibilita compartilhar e unificaros dados, além de propiciaruma integração mais eficiente dos sistemas envolvidos.

## 3. Tipos de modelos de dados

### A) Modelo conceitual:
- primeira etapa do projeto.
- representa a realidade (contexto de negócio) de uma visão global e genérica dos dados e seus relacionamentos.
- **objetivo:** 
  - englobar todas as informações dentro do contexto de negócio que ficarão armazenadas no banco de dados, sem que se retratem aspectos relativos ao SGBD que será utilizado.
- **foco:** 
  - entidades de sistema e como as entidades se relacionam.
- **funções:**
  - Entender os processos e regras de negócio.
  - Expressar as necessidades de informação da organização.
  - Apoiar a definição da abrangência do sistema, delimitando seu escopo.
  - Estabelecer as necessidades, possibilitando uma melhor definição da estrutura de armazenamento, de modo que seja apresentada uma estrutura de armazenamento flexível, facilitando sua manutenção.
- apresenta, por meio de uma visão global, as principais necessidades de armazenamento dentro de um contexto de negócio, ou seja, sem detalhamento e seus relacionamentos!
- a técnica de modelagem conceitual mais difundida é a ***Entidade-Relacionamento (ER)***.
  - O modelo conceitual é representado por um diagrama, **denominado Diagrama Entidade-Relacionamento (DER)**.

  págs 8 e 9