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

- na tabela, há varias informações que se repetem, como:
  - há vários produtos em uma mesma nota fiscal, portanto esses elementos precisam ser tirados da estrutura 
  - nessa estrutura desnormalizada, se vender 3 produtos, haverá 3 ocorrências.
  - portanto, é possível criar dois grupos: tabelas ***Nota_Fiscal*** e ***Itens_Nota_Fiscal***.
    - “Número da Nota Fiscal” como chave primária do grupo original (NOTA FISCAL).

### Entidades “NOTA FISCAL” e “ITENS NOTA FISCAL”, após a aplicação da 1FN:

- Entidade “NOTA_FISCAL”:
  - elementos (atributos) que compõem a estrutura original, excluindo os elementos repetidos.
  - depois da aplicação da 1FN, haverá o grupo “NOTA FISCAL”, com os atributos: #Número Nota Fiscal, data da emissão, CNPJ cliente, nome do cliente, endereço do cliente, transportadora, ICMSe total da nota.

<div align="center">

Nº Nota Fiscal | Data Emissão | CNPJ Cliente | Nome Cliente | Endereço Cliente | Transportadora | ICMS | Total da Nota
-------------|---------------|-----------|-------------|-----------------|-------|----------|-------------
456789 | 10/09/2010 | 1111111 | Pedro Luis | Rua Serafim de Gusmão, 34 | Rio Grandense | 25% | R$ 3.290,00
456789 | 10/09/2010 | 1111111 | Pedro Luis | Rua Serafim de Gusmão, 34 | Rio Grandense | 25% | R$ 3.290,00
123456 | 12/09/2010 | 2222222 | Amaro Godoi | Av. Rudge, 345 | Rio Grandense | 25% | R$ 5.650,00
654321 | 13/09/2010 | 3333333 | Celso Araujo | Av. Sto Amaro, 321 | Rio Grandense | 25% | R$ 4.050,00
654322 | 14/09/2010 | 5555555 | Paula Maria | Rua Frei João, 42 | Rio Grandense | 25% | R$ 1780,00
123456 | 12/09/2010 | 2222222 | Amaro Godoi | Av. Rudge, 345 | Rio Grandense | 25% | R$ 5.650,00
212135 | 16/09/2010 | 3333333 | Celso Araujo | Av. Sto Amaro, 321 | Entrega Expressa | 25% | R$ 3.560,00
635241 | 17/09/2010 | 4444444 | Joaquina Ramalho | Rua Frei João, 42 | Entrega Expressa | 25% | R$ 550,00
123456 | 12/09/2010 | 2222222 | Amaro Godoi | Av. Rudge, 345 | Entrega Expressa | 25% | R$ 5.650,00
843221 | 19/09/2010 | 2222222 | Amaro Godoi | Av. Rudge, 345 | Entrega Expressa | 25% | R$ 4.680,00
654321 | 13/09/2010 | 3333333 | Celso Araujo | Av. Sto Amaro, 321 | Entrega Expressa | 25% | R$ 4.050,00

</div>

- Entidade “ITEM_NF”:
  - dados (atributos) que compõem os elementos repetidos da estrutura original.
  - depois da 1FN, teremos o grupo “ITEM_NF”,contendo: #Número Nota Fiscal, #Código do Produto, descrição do produto, valor do IPI, preço unitário do produto e quantidade vendida.
  - chave primária: atributos “Nr. Nota Fiscal” e o “Código do Produto”.

<div align="center">

Nº Nota Fiscal | Produto | IPI | Preço Unitário | Qtd
-------------|---------------|-----------|-------------|-----------------
456789 | Refrigerador | 8% | R$ 1.200,00 | 2
456789 | Televisão | 8% | R$ 890,00 | 1
123456 | Aquecedor a gás | 8% | R$ 550,00 | 1
654321 | Aquecedor a gás | 8% | R$ 550,00 | 3
654322 | Televisão | 8% | R$ 890,00 | 2
123456 | Refrigerador | 8% | R$ 1.200,00 | 2
212135 | Televisão | 8% | R$ 890,00 | 4
635241 | Aquecedor a gás | 8% | R$ 550,00 | 1
123456 | Computador | 8% | R$ 1.350,00 | 2
843221 | Freezer | 8% | R$ 1.560,00 | 3
654321 | Refrigerador | 8% | R$ 1.200,00 | 2

</div>

--- 

<div align="center">
<h2>1.3 Segunda Forma Normal (2FN)</h2>
</div>

> Uma entidade está na segunda forma normal, se estiver na 1FN e quando todos os seus atributos não chave (atributos descritores) dependerem unicamente da chave.

### `Solução`: Separar os atributos repetidos que não fazem parte (dependência parcial) exclusivamente da chave primária e criar uma nova entidade.

### Aplicando a 2FN no exemplo proposto:

- no exemplo que o atributo “Descrição do Produto” não depende da chave “Nr. Nota Fiscal e Código do Produto”. A descrição do produto depende apenas do “CÓDIGO DO PRODUTO”.
- o atributo “QUANTIDADE VENDIDA” depende de forma total da chave primária “Nr. Nota Fiscal e Código do Produto”, pois a quantidade vendida só existe, quando o item (Produto) for vendido.
- a descrição do produto pode ser escrita de forma diferente em cada ocorrência nessa entidade (exemplo original).

> Essa técnica é utilizada em entidades que contêm mais de um atributo compondo a chave primária!

Há, ainda, outros problemas no modelo original:

- só poderemos inserir detalhes sobre um “PRODUTO”, “CLIENTE” ou “TRANSPORTADORA” apenas quando uma “VENDA” (Nota Fiscal) for realizada.
- quando uma “VENDA” (Nota Fiscal) for eliminada do cadastro, serão eliminados os dados do Cliente, Produto e Transportadora.
- para atualizar os dados (características) do “CLIENTE”, teremos que pesquisar todas as ocorrências da “VENDA” (Nota Fiscal) e atualizá‐las uma a uma. Para um cliente com muitas vendas, serão necessárias várias atualizações redundantes.

### Entidade "Produto"

- contém os atributos que dependem do “CÓDIGO PRODUTO”.
- depois da aplicação da 2FN, teremos o grupo “PRODUTO”, contendo os atributos: #Código do produto, descrição do produto, valor IPI e preço unitário do produto.

<div align="center">

Código Produto | Produto | IPI | Preço Unitário
-------------|---------------|-----------|-------------
1 | Refrigerador | 8% | R$ 1.200,00
2 | Televisão | 8% | R$ 890,00
3 | Aquecedor a gás | 8% | R$ 550,00
4 | Computador | 8% | R$ 1.350,00
5 | Freezer | 8% | R$ 1.560,00

</div>

> Caso exista a necessidade de armazenar o valor unitário do produto como histórico de vendas, pode‐se replicar o atributo “PRECO UNITARIO” na entidade “ITEM_NF” (Desnormalização) ou implementar uma entidade responsável por manter o preço unitário do produto historicamente.

### Entidade "ITEM_NF":

- contém os elementos (atributos) originais, excluídos os atributos que são dependentes apenas do “PRODUTO”.
- a chave primária será o atributo participante da chave primária da tabela origem, ou seja, serão os atributos:“Nr. NOTA FISCAL”e “CÓDIGO PRODUTO”.

<div align="center">

Nº Nota Fiscal | Produto | Qtd
---------------|---------|------
456789 | 1 | 2
456789 | 2 | 1
123456 | 3 | 1
654321 | 3 | 3
654322 | 2 | 2
123456 | 1 | 2
212135 | 2 | 4
635241 | 3 | 1
123456 | 4 | 2
843221 | 5 | 3
654321 | 1 | 2

</div>

---

<div align="center">
<h2>1.4 Terceira Forma Normal (3FN)</h2>
</div>

> Uma entidade está na terceira forma normal, se estiver na 2FN e quando todos os seus atributos não chave não dependerem de nenhum outro atributo não chave; em outras palavras, um atributo não deve depender de outro atributo (dependência transitiva).Isso ocorre normalmente em cálculos e em atributos “perdidos” na entidade errada.

### `Solução`: realizar a análise: se o atributo for resultado de um cálculo matemático, devemos simplesmente excluir esse atributo, pois ele não acrescenta nada no modelo de dados. Se for um grupo de informações relacionadas, aplicar a segunda forma normal. Se for um atributo “perdido”, devemos reconduzi‐lo à entidade da qual depende.

