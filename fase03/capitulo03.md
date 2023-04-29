<div id="fase02" align="center">
<h1>FASE 3 - MODELING</h1>
<h2>Capítulo 03: Como guardar as informações?</h2>
</div>

<div align="center">
<h2>COMO GUARDAR AS INFORMAÇÕES?</h2>
</div>

## 1. Ciclo de vida de um banco de dados

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

