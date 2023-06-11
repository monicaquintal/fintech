<div id="fase03" align="center">
<h1>FASE 4 - VIEW</h1>
<h2>Capítulo 06: Semântica e Grids.</h2>
</div>

<div align="center">
<h2>1. SEMÂNTICA E GRIDS</h2>
</div>

- `CSS Grid Layout`: conjunto de propriedades CSS que permitem a criação de layouts bidirecionais através da declaração de linhas e colunas. 

## 1.1 Terminologia Grid Layout

### 1.1.1 Grid Container

- representa o elemento HTML, que será convertido em um grid através da propriedade display.
- é o pai de todos os itens do grid.

### 1.1.2 Grid Item

- representa os filhos do elemento convertido em um grid.

### 1.1.3 Grid Line

- são as linhas que formam a estrutura do grid.
- podemos ter as linhas horizontais, que definem as linhas do grid, e as linhas verticais, que definem as colunas do grid.

### 1.1.4 Grid Cell

- representam as células do grid, o ponto de encontro entre uma linha e uma coluna.

### 1.1.5 Grid Area

- representa um conjunto de células.
- pode conter quantas células desejar, desde que sejam adjacentes.

### 1.1.6 Grid Track

- representa o espaçamento entre duas linhas consecutivas do grid, podendo ser horizontais ou verticais.

### 1.1.7 Grid Gap

- representa a distância entre as células do grid.

## 1.2 Criando linhas e colunas

### 1.2.1 Grid-template-columns

- define as colunas que farão parte do grid. 
- declarar um valor para definir a largura da coluna (utilizar qualquer medida CSS válida).
- o CSS Grid permite a utilização da `medida fr`(fração).
  - o browser irá calcular a largura das colunas baseando-se no valor que for atribuído à fração. 
  - caso defina uma coluna com 2fr e outra com 1fr, a coluna do 2fr terá duas vezes o tamanho da coluna com 1fr.

### 1.2.2 Repeat

- quando quiser definir colunas com a mesma largura, utilizar a propriedade repeat seguida do número de colunas e o valor que elas devem possuir.

### 1.2.3 Minmax

- permite definir a largura mínima e máxima que a coluna deve possuir.

### 1.2.4 Auto-fit

- com essa propriedade, o browser tentará colocar o máximo de itens em uma única linha, tentando não efetuar a sua quebra. 
  - caso os itens sejam pequenos, serão esticados para preencher todo o espaço.
- para essa propriedade funcionar, precisamos utilizá-la em conjunto com a propriedade minmax().

### 1.2.5 Auto-fill

- também irá inserir a maior quantidade de itens na mesma linha, mas não irá esticar os itens caso não ocupem todo o espaço. 
- também necessita da propriedade minmax() para funcionar.

## 1.3 Grid-template-rows

- define as linhas que farão parte do grid. 
- possui as mesmas propriedades usadas em grid-template-columns.

## 1.4 Alinhamento

### 1.4.1 Gap

- define o espaçamento entre os itens do grid. 
- opções:
  - Column-gap: define o espaço entre as colunas do grid.
  - Row-gap: define o espaço entre as linhas do grid.
  - Gap: define o espaçamento para as linhas e colunas. Pode receber apenas um valor (será aplicado tanto para as linhas quanto para as colunas), ou dois valores (o primeiro será aplicado para a linha e o segundo para a coluna).

### 1.4.2 Justify-content

- define o alinhamento horizontal.
- opções:
  - Start: é o valor padrão, os itens ficam alinhados na parte esquerda do container pai.
  - End: os itens ficam alinhados na parte direita do container pai.
  - Stretch: permite que os itens sejam esticados para que ocupem toda a largura do container.
  - Space-between: faz o alinhamento pelas extremidades do container pai.
  - Space-around: faz o alinhamento pelo centro do container pai. Teremos um espaçamento maior no centro do que nas extremidades.
  - Space-evenly: faz o alinhamento pelo centro do container pai. O espaçamento dos itens será igual tanto no centro quanto nas extremidades.
  - Center: deixa os itens centralizados horizontalmente. 

### 1.4.3 Align-content

- define o alinhamento vertical. 
- opções:
  - Start: valor padrão, os itens ficam alinhados na parte superior do container pai.
  - End: os itens ficam alinhados na parte inferior do container pai.
  - Stretch: permite que os itens sejam esticados para queocupem toda a altura do container. 
  - Space-between: faz o alinhamento pelas extremidades do container pai.
  - Space-around: faz o alinhamento pelo centro do container pai. Teremos um espaçamento maior no centro do que nas extremidades.
  - Space-evenly: faz o alinhamento pelo centro do container pai. O espaçamento será igual tanto no centro quanto nas extremidades.
  - Center: deixa os itens centralizados verticalmente.

### 1.4.4 Justify-items

- define o alinhamento horizontal para o conteúdo dos itens. 
- possui as seguintes opções:
  - Start: é o valor padrão, o conteúdo fica alinhado na parte esquerda do container item.
  - End: o conteúdo fica alinhado na parte direita do container item.
  - Stretch: permite que os itens sejam esticados horizontalmente.
  - Center: deixa o conteúdo centralizado.

### 1.4.5 Align-items

- define o alinhamento vertical para o conteúdo dos itens. 
- opções:
  - Start: valor padrão, o conteúdo fica alinhado na parte superior do container item.
  - End: o conteúdo fica alinhado na parte inferior do container item.
  - Stretch: permite que os itens sejam esticados verticalmente.
  - Center: deixa o conteúdo centralizado.

## 1.5 Criando layouts

### 1.5.1 Grid-column

- deve ser aplicada aos itens do grid.
- definirá a coluna que devem ocupar no grid.

### 1.5.2 Grid-column-start

- define a coluna inicial de um item no grid.

### 1.5.3 Grid-column-end

- define a coluna final de um item no grid.

### 1.5.4 Grid-column: start / end

- podemos declarar a coluna inicial e final fazendo uma declaração única.
- os valores devem estar separados por um sinal de barra ( / ), sendo que primeiro valor indica o start e o segundo o end.

### 1.5.5 Grid-row

- deve ser aplicada aos itens do grid.
- definirá a linha que eles devem ocupar no grid.

### 1.5.6 Grid-row-start

- define a linha inicial de um item no grid.

### 1.5.7 Grid-row-end

- define a linha final de um item no grid.

### 1.5.8 Grid-row: start / end

- podemos declarar a linha inicial e final fazendo uma declaração única.
- os valores devem estar separados por um sinal de barra ( / ), e primeiro valor indica o start e o segundo o end.

## 1.6 Grid-template-areas

- o CSS Grid possui um recurso onde você pode “desenhar” como deverá ficar o layout.
- utilizar a propriedade grid-template-areas, atribuindo nomes para cada um dos itens do grid. 
  - é possível repetir esses nomes, e o navegador entenderá que eles devem ocupar mais de uma linha ou coluna. 
  - para atribuir os nomes definidos aos elementos HTML, utilizar a propriedade grid-area que receberá o nome desejado.

---

## Laboratório CSS Grid Layout: [HTML](./projetos/projeto6/pages/index.html) e [CSS](./projetos/projeto6/css/style.css).

---

<div align="center">
<h2>2. CONTAINERS SEMÂNTICOS</h2>
</div>

- `tags semânticas` são containers com as mesmas características e funcionalidades das divs.
  - é uma boa prática utilizar essas tags, gerando um código HTML semântico.
- benefícios do HTML semântico:
  - garante um significado maior para a página: essas tags têm uma relevância maior.
  - fornece mais acessibilidade: permitirá que tecnologias assistivas possam ter um melhor acesso ao conteúdo da página.
  - melhora a visibilidade do site em uma busca feita por sites como o Google.
  - deixa o código mais claro, facilitando futuras manutenções.
  - ajuda os navegadores na renderização da página: indicam que tipo de conteúdo há naquela parte do código.

### Ou seja:

> Se está preocupado apenas em posicionar conteúdo e fazer estilização, use &lt;div&gt;. Se também estiver preocupado com a forma que o conteúdo será lido, interpretado e acessado, então use tags semânticas!

- tags semânticas possuem nomes que facilitam o entendimento do código e o tipo de conteúdo que está ali inserido.

## 2.1 Header

- define o cabeçalho para a página ou para outros containers.
- indica o início de um elemento ou seção.
- muito usado para a inserção de logotipos, áreas de navegação e campos para busca.
- em um mesmo documento podemos ter vários elementos &lt;header&gt;.

## 2.2 Main

- define o container que receberá o conteúdo principal da página.
  - conteúdo principal = tudo que possuí total relação com o assunto central da página. 
- por boa prática, não devemos ter mais de um elemento &lt;main&gt; no mesmo documento HTML.
- sempre deverá ser descendente direto da tag &lt;body&gt;.

## 2.3 Section

- define uma ou mais seções da página.
  - uma seção deve abordar algum determinado conteúdo ou assunto.
- em um mesmo documento podemos ter vários elementos &lt;section&gt;.
- não usar esse elemento apenas como um container mais genérico, pois para isso há a tag &lt;div&gt;.
- é recomendado que toda &lt;section&gt; possua algum elemento de título.

## 2.4 Article

- define um container de conteúdo mais específico, independente e que pode ser reutilizável em outras páginas, ou partes diferentes da mesma página, sem perder o seu sentido. 
- em um mesmo documento podemos ter vários elementos &lt;article&gt;.
- todo &lt;article&gt; deve possuir um elemento de título.

## 2.5 Aside

- define um container de conteúdo separado, mas vinculado a um determinado assunto. 
- na maioria das vezes é posicionado ao lado do conteúdo que foi associado, como uma barra lateral. 
- em um mesmo documento podemos ter vários elementos &lt;aside&gt;.

## 2.6 Nav

- define um container que agrupa os links criados pela tag &lt;a&gt;. 
  - não é necessário que todos os links estejam dentro de um container &lt;nav&gt;, apenas os que formarem o sistema de navegação de sua aplicação.
- a tag &lt;nav&gt; é comumente encontrada em elementos &lt;header&gt;, mas também podem ser inseridos em outros containers.
- em um mesmo documento podemos ter vários elementos &lt;nav&gt;.

## 2.7 Figure / Figcaption

- tag &lt;figure&gt; define um container que deve agrupar imagens existentes na página. 
- a tag &lt;figcaption&gt; pode ser usada no interior da tag figure,e definirá uma legenda a ser usada por um grupo de imagens.
- também é possível utilizar em cada imagem um &lt;figcaption&gt; diferente.
- o uso da tag &lt;figcaption&gt; é opcional.

## 2.8 Footer

- define o rodapé para a página ou para outros containers, indicando o final de um elemento ou seção.
- em um mesmo documento podemos ter vários elementos &lt;footer&gt;.

## 2.9 Em

- a tag &lt;em&gt; é utilizada para dar ênfase maior a uma palavra, ou parte de um texto. 
- o conteúdoque estiver no seu interior será entendido como mais relevante.

## 2.10 Strong

- a tag &lt;strong&gt; é utilizada para definir que um texto, ou parte dele, é muito importante.
- o conteúdo que estiver em seu interior ficará em negrito.

## 2.11 Address

- a tag &lt;address&gt; é utilizada para definir as informações de contato. 
- pode ser usada para: endereço, telefone, email, url etc.

## Outras dicas:

- ter um código semântico também diz respeito em colocar o conteúdo nas tags corretas. 
  - quando inserir um título, usar as tags de título: h1, h2, h3, etc; se quiser um parágrafo, deve ficar na tag p, e assim por diante. 
  - não adianta inserir conteúdo em qualquer tag e depois usar CSS para fazer a estilização, pois não será semântico.
- HTML deve ser usado apenas para definir a estrutura e o conteúdo dodocumento.
  - sempre usar tags baseando-se em seu significado semântico.
- sempre que a div não possui valor semântico, ela é um container genérico.
- HTML semântico garante que navegadores apliquem recursos de acessibilidade aos elementos.
  - a tag button tem um estilo padrão e é um elemento clicável, quando inserida na páginao browser irá disponibilizar os recursos de acessibilidade que esse elemento possui. 
  - poderíamos estilizar a tag a para parecer com um botão, mas o link não terá os mesmos recursos de acessibilidade de um botão.
- sites de busca como o Google, indexam de forma melhor HTML semântico, então use!!!

---

## Laboratório Containers Semânticos: [HTML](./projetos/projeto7/index.html) e [CSS](./projetos/projeto7/css/style.css).

---

## FAST TEST

### 1. Em relação aos seletores, assinale a alternativa correta: 
> O seletor adjacente pode ser identificado pelo sinal de adição (+) e precisa ser utilizado quando o próximo elemento após o elemento citado será formatado.

### 2. Qual sinal é utilizado para representar o seletor de filhos diretos?
> &gt;

### 3. Sobre pseudo-classes, assinale a alternativa correta:
> A pseudo-classe nth-child aplica formatação a um elemento, conforme sua posição dentro de um grupo.

---

[Voltar ao início!](https://github.com/monicaquintal/fintech)