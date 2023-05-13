<div id="fase02" align="center">
<h1>FASE 3 - MODELING</h1>
<h2>Capítulo 06: Aprendendo a armazenar de maneira correta. 🗂️</h2>
</div>

> A normalização é um conjunto de regras com o objetivo de garantir um modelo rápido, organizado e otimizado.

<div align="center">
<h2>1.1 Instrumento de verificação - Sobre as formas normais</h2>
</div>

> Formas normais são as técnicas que evitam a redundância dos dados.

- é um instrumento para verificar a qualidade e a simplicidade (redução da complexidade) dos nossos projetos de bancos de dados.
- processo formal é um passo a passo que examina os atributos de uma entidade com o objetivo de evitar redundâncias (informações desnecessárias ou em excesso) e garantir a estabilidade do Modelo de Dados.
- aplicação de regras que irão garantir a eliminação de redundâncias e valores nulos e, por consequência, provocar reduções de tempo e acesso ao disco, além da redução da complexidade de sua estrutura!

> Embora existam 5 Formas Normais, a aplicação da 3ª regra já é suficiente para garantir estabilidade do modelo de dados e, por esta razão, o curso concentrou os estudos nas três primeiras e mais importantes regras.

### Objetivos da normalização de dados

- minimizar redundâncias e inconsistências.
- facilitar a manutenção do sistema de informações.
- facilitar manutenções dos bancos de dados.

### Ainda sobre formas normais

- são um conjunto de restrições (regras) que os dados devem satisfazer.
- introduzido por Dr. Edgar F. Codd em 1970.
- São técnicas para a retirada de “anomalias” do modelo relacional.
- O processo de normalização baseia-se no conceito de Forma Normal, uma regra que deve ser obedecida por uma tabela (entidade) para que esta seja considerada bem projetada.

## 1.1.1 Exemplificando a aplicação das 3 principais restrições ou formas normais

<div align="center">

Nº Nota Fiscal | Data Emissão | CNPJ Cliente | Nome Cliente | Endereço Cliente | Produto | IPI | Preço Unitário | Qtd | Transportadora | ICMS | Total da Nota
-------------|---------------|-----------|-------------|-----------------|-------|----------|-------------|-----------|-----------|-----------|-----------
456789 | 10/09/2010 | 1111111 | Pedro Luis | Rua Serafim de Gusmão, 34 | Refrigerador | 8% | R$ 1.200,00 | 2 | Rio Grandense | 25% | R$ 3.290,00
456789 | 10/09/2010 | 1111111 | Pedro Luis | Rua Serafim de Gusmão, 34 | Televisão | 8% | R$ 890,00 | 1 | Rio Grandense | 25% | R$ 3.290,00
123456 | 12/09/2010 | 2222222 | Amaro Godoi | Av. Rudge, 345 | Aquecedor a gás | 8% | R$ 550,00 | 1 | Rio Grandense | 25% | R$ 5.650,00
654321 | 13/09/2010 | 3333333 | Celso Araujo | Av. Sto Amaro, 321 | Aquecedor a gás | 8% | R$ 550,00 | 3 | Rio Grandense | 25% | R$ 4.050,00
654322 | 14/09/2010 | 5555555 | Paula Maria | Rua Frei João, 42 | Televisão | 8% | R$ 890,00 | 2 | Rio Grandense | 25% | R$ 1780,00
123456 | 12/09/2010 | 2222222 | Amaro Godoi | Av. Rudge, 345 | Refrigerador | 8% | R$ 1.200,00 | 2 | Rio Grandense | 25% | R$ 5.650,00
212135 | 16/09/2010 | 3333333 | Celso Araujo | Av. Sto Amaro, 321 | Televisão | 8% | R$ 890,00 | 4 | Entrega Expressa | 25% | R$ 3.560,00
635241 | 17/09/2010 | 4444444 | Joaquina Ramalho | Rua Frei João, 42 | Aquecedor a gás | 8% | R$ 550,00 | 1 | Entrega Expressa | 25% | R$ 550,00
123456 | 12/09/2010 | 2222222 | Amaro Godoi | Av. Rudge, 345 | Computador | 8% | R$ 1.350,00 | 2 | Entrega Expressa | 25% | R$ 5.650,00
843221 | 19/09/2010 | 2222222 | Amaro Godoi | Av. Rudge, 345 | Freezer | 8% | R$ 1.560,00 | 3 | Entrega Expressa | 25% | R$ 4.680,00
654321 | 13/09/2010 | 3333333 | Celso Araujo | Av. Sto Amaro, 321 | Refrigerador | 8% | R$ 1.200,00 | 2 | Entrega Expressa | 25% | R$ 4.050,00

</div>

### Problemas:

- Para saber quais clientes compraram “Refrigerador”, teríamos que ler linha a linha (ocorrências da entidade) da tabela.•
- Para atualizar o endereço de um cliente, teríamos que ler linha a linha da tabela e realizar a alteração em todos os registros associados ao cliente em questão.
- Se deletarmos o pedido da “Joaquina Ramalho”, perderemos as informações referentes ao endereço (há apenas um registro para a Joaquina Ramalho).

### Anomalias (anormalidades/irregularidades) de uma estrutura desnormalizada, considerando o exemplo:

I. Durante a INSERÇÃO de dados:
<br>

- Quando um item de uma nota fiscal for inserido, será preciso informar os dados da transportadora mesmo que eles já estejam cadastrados.
- Não será possível inserir um produto vendido (item) sem inserir também uma transportadora.
- Não é possível inserir um novo produto sem que tenha sido vendido.
- Só é possível cadastrar um cliente se uma venda for realizada.<br>

II. Durante a EXCLUSÃO de dados:
<br>

- Quando um item (produto) de uma nota fiscal for excluído (ou uma nota fiscal), se ele for um único pedido associado à transportadora, perderemos os dados da transportadora, pois terão que ser excluídos juntamente com os itens (produtos vendidos) da nota fiscal.<br>

III. Durante a ATUALIZAÇÃO de dados:
<br>

- Caso seja necessário alterar os dados de uma transportadora, será preciso atualizar os mesmos dados em todas as ocorrências que estejam referenciando essa transportadora.
- O mesmo vale para o cliente, caso um cliente mude de endereço, será preciso atualizar todas as ocorrências em que o cliente está associado a uma nota fiscal.

--- 
<div align="center">
<h2>1.2 Primeira Forma Normal (1FN)</h2>
</div>

> Uma entidade está na primeira forma normal quando nenhum de seus atributos (na estrutura) possuírem repetições.

### `Solução`: Separar informação que se repete, em uma nova entidade.
- levar a chave primária da entidade original para a nova entidade.
- podemos localizar um atributo que, unido à chave primária, formará a chave da nova entidade ou criamos um atributo identificador para essa nova entidade.

### Aplicando a 1FN no exemplo proposto:

