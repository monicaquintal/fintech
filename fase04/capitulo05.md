<div id="fase03" align="center">
<h1>FASE 4 - VIEW</h1>
<h2>Capítulo 05: Organizando e posicionando seu HTML.</h2>
</div>

<div align="center">
<h2>1. ORGANIZANDO E POSICIONANDO SEU HTML</h2>
</div>

- tag &lt;div&gt;&lt;/div&gt;:
  - container utilizado para armazenar qualquer tipo de conteúdo.
  - podemos inserir nessa tag um conjunto de outras tags que irão compor o conteúdo da página, melhorando a organização do código e facilitando a formatação das informações.

## 1.1 Criando um container 

- usar a tag &lt;div&gt;&lt;/div&gt; e inserir o conteúdo dentro dessa estrutura.
- uma div pode receber qualquer tipo de conteúdo, inclusive outras divs.
- usar as propriedades width (largura) e height (altura). 
  - valores mais comuns definidos em px (pixel) e %(porcentagem). 
- tomar cuidado com o conteúdo; caso seja maior que altura definida para a div, ocorrerá o **overflow**: o conteúdo excedente ultrapassará o tamanho definido para a div.
  - podemos utilizar a `propriedade overflow`, que recebe um dos seguintes atributos:
    - Visible: valor padrão, o conteúdo que ultrapassara altura da div sempre ficará visível.
    - Hidden: o conteúdo que ultrapassar a altura da div não ficará visível.
    - Scroll: o conteúdo que ultrapassar a altura da div não ficará visível e será acessado através de barras de rolagem que serão inseridas automaticamente na div.
    - Auto: exibe apenas as barras de rolagem que serão necessárias para acessarmos todo o conteúdo da div.

## 1.2 Box Model 

- descreve como as divs devem ser montadas na página.
- composto por quatro elementos: margin, border, padding e content. 
  - essas quatro propriedades, em conjunto com a largura e altura, definirão como ficará o container.

### 1.2.1 Margin

- define a margem externa da div (distanciamento que a div terá dos demais elementos que formam a página). 
- valores: top, right, bottom e left.
- os valores da margem podem ser definidos de quatro formas, declarando:
  - um único valor: será usado para as quatro margens.
  - dois valores: o primeiro valor será usado pelas margens top e bottom, e o segundo, right e left.
  - três valores: o primeiro valor será usado pela margem top, o segundo, pelas margens right e left, e o terceiro, pela margem bottom.
  - quatro valores: primeiro valor será usado pela margem top, o segundo pela margem right, o terceiro pela margem bottom e o quarto pela margem left. 

### 1.2.2 Border

- define a borda (contorno) do elemento. 
- há borda: top, right, bottom e left.
- são opcionais.
- propriedades:
  - border-width: 
    - largura da borda. 
    - pixels (px) ou outras medidas CSS válidas.
  - border-style:
    - estilo da borda.
    - solid (linha sólida), double (dupla), dotted (pontilhada), dashed (riscada), groove (dependendo da cor, as bordas à esquerda e a superior ficam com cores diferentes das demais), ridge (inverte a ordem das cores da opção groove), inset (bordas superior e esquerda ficam mais destacadas), outset (bordas inferior e direita ficam mais destacadas).
    - border-color: 
      - cor da borda.
      - comum a cor ser hexadecimal (#), mas poderá receber outros valores.
- é possível declarar apenas uma parte da borda: top, right, bottom e left.

### 1.2.3 Padding

- define a margem interna (preenchimento) da div.
  - distanciamento que o conteúdo terá das bordas ou extremidades da div. 
- valores: top, right, bottom e left
- é possível declarar um único valor, dois valores, três valores ou quatro valores.

> `propriedade box-sizing`: em conjunto com o `valor border-box`, alterará o comportamento dos elementos com padding, permitindo que o espaçamento interno seja aplicado: o browser irá recalcular o tamanho do container e aplicar o padding ao elemento.

### 1.2.4 Content

- representa o conteúdo inserido. 
- formatado por várias outras regras, conforme o tipo de conteúdo presente no container: texto, imagem, link, tabela etc.

## 1.3 Limitando largura e altura de um elemento

- para definir valores máximos e mínimos, há as seguintes propriedades:
  - max-width: define a largura máxima da div.
  - min-width: define a largura mínima da div.
  - max-height: define a altura máxima da div.
  - min-height: define a altura mínima da div.

## 1.4 Box-shadow 

- insere uma sombra em volta de qualquer elemento.
- valores que devem ser declarados, na ordem:
  - Inset: 
    - opcional.
    - quando declarado, insere uma sombra interna.
  - Deslocamento horizontal:
    - define valores para posicionamento da sombra à direita do elemento (valores positivos), ou à esquerda do elemento (valores negativos)
  - Deslocamento vertical:
    - define valores para posicionamento da sombra acima do elemento (valores negativos), ou abaixo do elemento (valores positivos).
  - Desfoque:
    - define o desfoque da sombra.
    - quanto maior for o valor declarado, maior será a área do desfoque, e mais claro ele ficará.
  - Extensão da sombra:
    - define a expansão da sombra.
    - caso não seja declarado, a sombra terá o tamanho da caixa.
  - Cor:
    - define a cor desejada para a sombra.

> A declaração poderá ser feita apenas com os dois valores iniciais (desfoque horizontal e vertical), e a cor desejada!

## 1.5 Background-color 

- cor de fundo.
- tem como valor a cor desejada. 
  - a cor pode ser declarada em código: hexadecimal, rgb, hsl, hwb, ou usando o nome da cor em inglês. 
- por padrão, o background dos elementos é transparente. 
- lista de apps para paleta de cores:
  - [Colorhub](https://colorhub.vercel.app/)
  - [Coolors](https://coolors.co/)
  - [Schemecolor](https://www.schemecolor.com/)
  - [Adobe Color](https://color.adobe.com/)
  - [ColorSpace](https://mycolor.space/)
  - [BrandColors](http://brandcolors.net/)
  - [Material Design Color Tool](https://material.io/resources/color/)

## 1.6 Background-image

- é possível também colocar imagens de fundo.
- observações importantes:
  - o endereço da imagem deve ficar dentro url() - indicar a pasta em que a imagem está armazenada.
  - o sinal de (../) faz com que o navegador retroceda um nível na hierarquia de pastas.

### 1.6.1 Background-repeat 

- por padrão, quando inserimos imagens de fundo, elas serão repetidas para ocupar todo o espaço do elemento. 
- propriedade background-repeat: valores
  - **no-repeat**: a imagem ficará posicionada na parte superior esquerda do container e não repetirá.
  - **repeat-x ou repeat-y**: faz com que as imagens repitam apenas em um determinado eixo da caixa, sendo eixo x (horizontal) e eixo y (vertical).

### 1.6.2 Background-position

- imagens de fundo, quando não são repetidas, poderão ter um posicionamento específico dentro do container.
- usar a propriedade background-position, seguida de algum valor válido:
  - valores em pixels: pode definir dois valores, sendo o primeiro para o eixo horizontal, e o segundo, eixo vertical.
  - valores em porcentagem.
  - palavras chave: top, bottom, left, right e center.

### 1.6.3 Background-attachment

- fixa imagens na tela ou faz com que acompanhem o scroll.
- propriedade background-attachment, com os valores: 
  - fixed: a imagem ficará sempre fixa (visível) na tela, independente do scroll.
  - scroll: a imagem acompanhará o scroll da tela e só ficará visível na área em que foi posicionada.

### 1.6.4 Background-size

- redimensiona a imagem de fundo.
- propriedade background-size, que pode receber os valores:
  - definindo largura e altura: valores máximos (em px ou %) para altura e/ou largura, nessa ordem.
  - contain: a imagem tentará ocupar todo o container; caso não consiga preencher, exibirá a cor de fundo do container.
  - cover: a imagem ocupará toda o container, independente do seu tamanho.

> ***E qual a forma correta de inserir imagens em uma página:***

- Se a imagem for apenas para estilização, e não existir nenhum tipo de interação entre ela e o usuário, usar a propriedade background-image.
- Se a imagem possuir algum tipo de interação com o usuário, como sendo um link para algum conteúdo, usar a tag &lt;img&gt;. 
- Outro ponto em favor ao uso da tag &lt;img&gt;: acessibilidade; podemos e devemos usar o atributo alt para fazer uma pequena descrição da imagem (leitores de tela irão descrever o conteúdo inserido nesse atributo).

<div align="center">
<h2>2. SELETORES ESPECIAIS</h2>
</div>

## 2.1 Seletor de Id 

- representado pelo sinal de hashtag (#) seguido de um nome.
- servirá como um identificador para as tags HTML. 
- é usado tanto na parte da CSS como em JavaScript.
- para atribuir um id a uma tag, usar o atributo id seguido de = e um valor, que representa um nome para ele. 
- o mesmo valor de um id não pode ser utilizado por dois ou mais elementos na mesma página.
  - nunca repetir os valores dos ids no mesmo código.
- qualquer tag HTML pode receber um id, e seu uso não é obrigatório.
- como boa prática e padrão do HTML, sempre escreva os valores dos ids em letras minúsculas e use a notação camelCase!
- ao montar uma regra CSS usando um id, ela será utilizada apenas por um único conteúdo na página, aquele que possuir o atributo correspondente. 

## 2.2 Seletor de Classe

- representado pelo sinal de ponto final (.) seguido de um nome.
- é o seletor mais importante. 
- usadas para criar formatações que podem ser aplicadas a vários elementos ao mesmo tempo.
  - diferente dos seletores de id, os seletores de classe podem e devem ser usados por diferentes elementos HTML inseridos no código.
- todo elemento HTML pode fazer uso de **várias classes ao mesmo tempo**.
  - usar o atributo class, seguido do sinal de igualdade ( = ) e os nomes das classes desejadas.
  - é possível criar uma classe mais genérica para propriedades comuns, e classes mais específicas para definir características específicas de cada tag, por exemplo.

## 2.3 Seletor * (asterisco)

- aplicará a formatação a todos os elementos inseridos na página. 
- o uso é comum quando queremos resetar alguns padrões que os navegadores aplicam aos elementos assim que a página é renderizada. 
  - essa técnica é chamada de reset CSS.
  - é possível acessar e usar o código original [clicando aqui](https://meyerweb.com/eric/tools/css/reset/), é domínio público!

## 2.4 Seletor de descendência

- quando deseja formatar um elemento que esteja dentro de outro (um descendente).
- exemplo:

~~~css
/* formatar elementos <p> que estão em uma <div> */

div p {
  width: 300px;
  height: 50px;
}
~~~

## 2.5 Seletor adjacente

- representado pelo sinal de adição ( + ).
- pode ser usado quando deseja formatar o próximo elemento após o elemento citado.
- exemplo:

~~~css
/* formatar o próximo elemento <p> após a tag <ul> */

ul + p {
  width: 300px;
  height: 50px;
}
~~~

## 2.6 Seletor irmão

- representado pelo sinal de til ( ~ ).
- usado quando deseja formatar todos os elementos após o elemento citado. 
- exemplo:

~~~css
/* formatar todas as tags <p> após a tag <ul> */

ul ~ p {
  width: 300px;
  height: 50px;
}
~~~

## 2.7 Seletor de filhos diretos

- representado pelo sinal de maior que ( > ).
- usado quando deseja formatar apenas os descendentes diretos do elemento.
- exemplo:

~~~css
/* formatar apenas as tags <p> descendentes diretos da classe container. */

.container > p{
  width: 300px;
  height: 50px;
}
~~~

## 2.8 Pseudo-classes

- palavras-chave que podem ser colocadas ao lado do nome do seletor, e ajudarão na formatação do elemento conforme o estado dele.
  - o estado pode ser alterado por fatores externos ou ações do usuário: quando o elemento é clicado, quando passa o mouse sobre, quando é selecionado etc.

### 2.8.1 Pseudo-classe :hover

- aplica uma formatação quando o mouse passar sobre algum elemento.
- assim que o mouse sair, ele voltará o seu estado normal. 

### 2.8.2 Pseudo-classe :nth-child

- aplica uma formatação a um elemento conforme a sua posição dentro de um grupo.
- além dos números que indicam as posições dos elementos, podemos também usar as `palavras-chave odd(ímpar) e even (par)` para aplicar formatações para elementos nessas posições. 

### 2.8.3 Pseudo-classes :first-child e :last-child

- aplica uma formatação ao primeiro e ao último elemento de um grupo.

> Podemos também passar uma pequena expressão com um valor qualquer, e o navegador fará o cálculo e aplicará a formatação aos elementos encontrados.

### 2.8.4 Pseudo-classe :not

- declarar uma negação para que determinada regra não seja aplicada a um elemento.

### 2.8.5 Pseudo-classe :is e :where

- através da `pseudo-classe :is`, definir uma lista de seletores:
  - a regra que for declarada será aplicada aos elementos que ele conseguir selecionar em seu HTML. 
  - se a lista possuir algum elemento inválido, não teremos problema algum, pois esse elemento será descartado e a formatação aplicada aos demais elementos.
- a pseudo-classe :is pode ser substituída pela `pseudo-classe: where`
  - a grande diferença entre as duas é a ***especificidade***.
  - com o :where a especificidade sempre será 0 (zero), já o :is assumirá a maior especificidade dos seletores declarados na lista.

### 2.8.6 Pseudo-classe :has

- permite verificar se um determinado seletor existe dentro de um elemento pai.

## 2.9 Pseudo-elementos

- são palavras-chave que podem ser adicionadas a qualquer seletor CSS, permitindo a formatação de uma parte específica do elemento referenciado. 
- importante: 
  - colocar o sinal de dois pontos duas vezes ( :: ) irá distinguir os pseudos elementos de pseudos classes.
  - usar apenas um pseudo-elemento em cada seletor.
  - há alguns pseudos elementos que não são bem suportados pelos navegadores, podendo [consultar aqui](https://caniuse.com/).

### 2.9.1 Pseudo-elemento ::first-line

- aplica uma formatação na primeira linha da tag escolhida.

### 2.9.2 Pseudo-elementos ::before e ::after

- permitem que algum conteúdo possa ser inserido antes ou depois do seletor a ele associado.
- será a CSS que fará a inserção do conteúdo utilizando a propriedade content - o conteúdo é inserido de forma dinâmica, e pode receber qualquer tipo de formatação.

### 2.9.3 Pseudo-elemento selection

- aplica uma formatação ao conteúdo que for selecionado pelo usuário.

<div align="center">
<h2>3. TABELAS</h2>
</div>

## 3.1 Tag table

- para criar tabelas em HTML, usar a tag &lt;table&gt;&lt;/table&gt;, onde deve ficar todo o conteúdo que formará a tabela. 
- apenas com a tag &lt;table&gt; não há visualização no navegador.

## 3.2 Tag caption

- insere um título na tabela. 
- deverá estar logo após a abertura da &lt;table&gt;.

## 3.3 Tag tr

- utilizada para a criação das linhas da tabela. 
- tr significa “table row”.

## 3.4 Tag td

- utilizada para a criação das colunas na tabela. 
- devem ficar dentro da tag &lt;tr&lt;. 
- dentro da &lt;td&gt; que as informações devem ser inseridas. 
- a sigla td significa “table data”.

## 3.5 Tag th

- a primeira linha de dados da tabela define os nomes das colunas.
- portanto, podemos substituir a tag &lt;td&gt; pela tag &lt;th&gt;.
  - essa tag deixará o nome da coluna centralizado e com estilo negrito.
  - a principal diferença será a **acessibilidade** para pessoas com leitores de tela: ele informará o que significa cada uma das colunas!

## 3.6 Agrupando elementos na tabela

- o conteúdo da tabela pode ser divido em cabeçalho, corpo e rodapé. 
- a divisão não é obrigatória, mas ajuda a organizar os dados da tabela e contribui para formatação CSS. 
- tags: &lt;thead&gt;, &lt;tbody&gt; e &lt;tfoot&gt;.

### 3.6.1 Tag thead

- após o uso da tag &lt;caption&gt;, criar o cabeçalho da tabela utilizando a tag &lt;thead&gt;.
- serve para identificar a primeira linha da tabela, que provavelmente terá os nomes de cada coluna de dados. 
- em tabelas muito grandes, que forem impressas, essa linha sempre será repetida no início de uma nova página, facilitando a identificação dos dados apresentados.

### 3.6.2 Tag tbody

- o elemento &lt;tbody&gt; consiste no corpo da tabela, onde são inseridas as informações nas linhas e colunas de dados.
- permite a organização dos dados, agrupando-os em uma área específica da tabela.

### 3.6.3 Tag tfoot

- a tag &lt;tfoot&gt; representa a linha de rodapé da tabela. 
- o uso é opcional.
- na maioria das vezes, o &lt;tfoot&gt; é usado como uma linha para alguma observação sobre os dados: um comentário, marca de rodapé etc.

## 3.7 Mesclando linhas e colunas

### 3.7.1 Atributo colspan

- define o número de colunas que devem ser mescladas. 
- basta inserir na primeira &lt;td&gt; da linha, o atributo colspan com o número de colunas que desejamos mesclar.

### 3.7.2 Atributo rowspan

- define o número de linhas que devem ser mescladas.
- inserir na primeira &lt;td&gt; o atributo rowspan,seguido do número de linhas que deseja mesclar.

## 3.8 Criando e estilizando uma tabela

> Exemplo da aplicação do conteúdo aqui: [HTML](./projetos/projeto4/pages/index.html) e [CSS](./projetos/projeto4/css/style.css).

<div align="center">
<h2>4. VARIÁVEIS – UNIDADES DE MEDIDA – ÍCONES</h2>
</div>

## 4.1 Variáveis CSS

- objetivos:
  - melhorar as declarações de algumas regras.
  - facilitar o desenvolvimento (caso sejam necessárias alterações).
  - facilitar a reutilização de estilos.
- para criar uma variável, basta definir um nome e atribuir um valor.

### 4.1.1 Escopo das variáveis

- define a abrangência das variáveis (onde podem ser acessadas).
- as variáveis CSS podem ser declaradas em qualquer seletor CSS e possuem os seguintes tipos de escopo:
  - escopo local: 
    - só podem ser usadas pelos elementos dentro do seletor onde elas foram declaradas.
  - escopo global: 
    - podem ser usadas por todos os elementos do documento.
    - é a forma mais comum de declaração.

### 4.1.2 Declarando variáveis

- declarar a variável dentro do seletor no qual ela será usada. 
- apenas os descendentes desse seletor terão acesso à essas variáveis.O

> Os nomes das variáveis devem `iniciar com dois hifens (--)`, seguido do `nome desejado` e do `valor`. 

- para usar a variável, basta chamá-la dentro dos elementos que a utilizarão, utilizando a `função var()`.
  - nomes de variáveis são ***case sensitive***.

> Quando declara-se as variáveis dentro do :root, elas tem o escopo global, ou seja, todos os elementos da página podem ter acesso a essa variável.

### 4.1.3 Usando fallback 

- podemos usar um valor de fallback na chamada das variáveis. 
- caso aconteça algum erro e a variável não seja acessada, o valor definido como fallback será utilizado no lugar do valor declarado na variável.

### 4.1.4 Escopo local x escopo global 

- caso crie uma variável global e depois faça uma nova declaração de uma variável local utilizando o mesmo nome atribuído à global, a formatação que será aplicada será a da variável local.

## 4.2 Unidades de medida CSS 

### 4.2.1 Pixel – px

- unidade de medida mais comum no desenvolvimento web.
- é uma medida fixa: quando definimos um valor em pixels, esse valor não mudará, independente do dispositivo usado para acesso.

### 4.2.2 Porcentagem – % 

- é uma unidade de medida relativa, que fará os cálculos dos tamanhos dos elementos baseado no seu elemento pai.
- caso o elemento Pai seja um container, é melhor definir a largura usando porcentagem, pois o container sempre será proporcional ao tamanho da tela, evitando que seja gerada a barra de rolagem horizontal.

### 4.2.3 VW e VH

- utiliza o viewport (área que o dispositivo possui para exibir o conteúdo) do dispositivo que o usuário está usando para acessar a aplicação, por isso o uso da letra “v”. 
  - a largura é representada pela letra “w” (width).
  - a altura é representada pela letra “h” (height).
- para usar o viewport como referência, o browser fará uma pequena conversão: se definir que o container terá 100vw ou 100vh, o browser entenderá que esse container ocupará 100% da largura e da altura do viewport. 
- como se baseiam pela largura e altura do viewport, o container vai se ajustar em todos os dispositivos. 
- não esquecer de inserir a meta tag viewport na seção &lt;head&gt; da página, pois será ela a responsável por detectar o tamanho do viewport do dispositivo.

### 4.2.4 Vmin e Vmax

- as unidades vmin e vmax utilizarão, respectivamente, o menor viewport e o maior viewport: o browser detectará esses dois valores e usará para definir os tamanhos.
- exemplo: viewport de 1200px de altura e 700px de largura. 
  - o viewport que será usado pelo vmin será o de 700px (é o menor), e o que será usado pelo vmax será o de 1200px (o maior).
  - se fizermos uma declaração de 10vmin teremos 70px (10% do menor viewport), e se declararmos 10vmax teremos 120px (10% do maior viewport).

### 4.2.5 EM 

- suportada por praticamente todos os browsers.
- amplamente usada na criação de layouts, até os responsivos. 
- para que um novo valor seja definido, a unidade em usará o tamanho da fonte do elemento pai, que deverá ser em pixels, e multiplicará pelo valor atribuído aos filhos.
- exemplo:

~~~css
.container { margin: 20px;
  font-size: 16px; /* medida usada como referência */
}

.box-um {
  margin: 10px;
  font-size: 2em; /* 2 x 16px (da referência) = 32px */
}

.box-dois {
  margin: 10px;
  padding: 20px 10px;
  font-size: 1em; /* 1 x 16px (da referência) = 16px */
}
~~~

### 4.2.6 REM

- é bem parecida com a medida em.
- **porém**, ao invés de usar o tamanho da fonte do elemento pai, ela usará o tamanho da fonte do elemento root da página, ou seja, a tag <&lt;html&gt;.
- com o uso da medida rem, não importa onde os containers estarão inseridos, sempre buscará o valor do elemento root.
- ajuda nas manutenções, pois alterando o valor de apenas uma única propriedade, todos os valores com rem serão recalculados.

## 4.3 Ícones

- são muito comuns, e podem ajudar no visual deixando a informação mais clara ao usuário. 
- muitas vezes são usados ícones para identificar as redes sociais, exemplificar alguma ação ou tarefa que o usuário pode realizar.
- bibliotecas:
  - [Boxicons](https://boxicons.com/)
  - [Ionicons](https://ionic.io/ionicons)
  - [Flaticon](https://www.flaticon.com/)
  - [Iconfinder](https://www.iconfinder.com/)
  - [Bootstrap Icons](https://icons.getbootstrap.com/)
  - [Font Awesome](https://fontawesome.com)

- no caso do Font Awesome, [este link](https://cdnjs.com/libraries/font-awesome) disponibiliza o endereço de algum servidor que tenha esses ícones, sem precisar realizar o cadastro.
  - clicar no sinal de tag HTML (</>) para copiar o link, ir até a sua página e colar esse conteúdo dentro da tag head.

<details>
<summary>Tag &lt;link&gt; para colar no HTML abaixo:</summary>

~~~html
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.0/css/all.min.css" integrity="sha512-xh6O/CkQoPOWDdYTDqeRdPCVd1SpvCA9XXcUnZS2FmJNp1coAFzvtCN9BmamE+4aHK8yyUHUSCcJHgXloTyT2A==" crossorigin="anonymous" referrerpolicy="no-referrer" />
~~~

</details>

### 4.3.1 Inserindo ícones para as redes sociais

- exemplo aqui: [HTML](./projetos/projeto4/pages/index.html) e [CSS](./projetos/projeto4/css/style.css).

<div align="center">
<h2>5. POSICIONANDO ELEMENTOS</h2>
</div>

- o CSS entende cada elemento HTML como uma caixa e, por padrão, todos se comportam de duas formas: em linha (**inline**) e em bloco (**block**).
- a `propriedade display` permite controlar esse comportamento, e definirá como os containers serão montados e exibidos no navegador.
- todas as tags possuem um modo de exibição, ou seja, um display com um valor definido.
  - o objetivo é alterar essa propriedade para atingir o melhor resultado.

## 5.1 Display inline

- tags que possuem comportamento de exibição inline permitem que ***seus elementos fiquem posicionadas um ao lado do outro***, caso exista espaço suficiente.
- outra característica importante é que os elementos que utilizam o display inline ***desconsideram valores definidos para largura e altura***, sendo seu tamanho definido pelo conteúdo.
- é o padrão seguido por links &lt;a&gt;, imagens &lt;img&gt;.

## 5.2 Display block

- tags que possuem comportamento de exibição block ocupam todo o espaço da linha, não permitindo que outros conteúdos fiquem ao seu lado. 
- são posicionados um abaixo do outro, conforme são inseridos no HTML.
- é o padrão seguido por: containers &lt;div&gt;, parágrafos &lt;p&gt;, itens da lista &lt;li&gt;, etc.
- quando utilizamos o display block, ***valores definidos para altura e largura serão respeitados pelo navegador*** e aplicados aos elementos.

## 5.3 Display inline-block 

- permite posicionar os elementos um ao lado (como é feito no display inline), e definir valores válidos para a largura e altura (como é feito no display block).

## 5.4 Float

- retira um elemento da sua posição original de inserção no HTML, fluxo normal de exibição, e posiciona-o ao lado direito ou esquerdo do seu container.
- valores válidos:
  - Right: indica que o elemento deve flutuar à direita do container.
  - Left: indica que o elemento deve flutuar à esquerda do container.
  - None: indica que o elemento não deve flutuar. É o valor padrão.

## 5.5 Clear

- quando usamos a propriedade float, os conteúdos que vierem logo após o elemento que recebe essa propriedade também flutuarão, caso exista espaço disponível.
- para que o conteúdo não herde essa flutuação, podemos utilizar a propriedade clear no primeiro elemento logo após a tag que está recebendo a propriedade float, independente dela possuir valor left ou right. 
- a propriedade clear aceita os valores:
  - Left: limpa a flutuação à esquerda.
  - Right: limpa a flutuação à direita.
  - Both: limpa a flutuação tanto à esquerda quanto à direita.

## 5.6 Flexbox (ou flex)

- um conjunto de propriedades que possibilitam o alinhamento dos containers, criando layouts flexíveis.
- a ideia é aplicar ao container principal (Pai) propriedades flexíveis que possibilitem o posicionamento dos containers internos (filhos). 
- é uma das propriedades CSS mais usadas.
- possui muitas propriedades que podem ser aplicadas tanto ao elemento pai quanto aos elementos filhos. 

## 5.7 Aplicando flexbox 

- para usar o Flexbox, precisamos transformar o elemento pai em um flex container, para isso ele receberá `propriedade display` com o `valor flex`. 
  - por padrão, os filhos desse container ficarão alinhados um ao lado do outro.
- os elementos filhos são definidos como flex itens.

## 5.8 Flex-direction 

- define a direção que os filhos devem seguir dentro do flex container.

### 5.8.1 Flex-direction: row

- os flex itens ficarão um ao lado do outro. 
- é o padrão assumido automaticamente quando o container pai se torna um flex container, ou seja, esse valor não precisará ser declarado.

### 5.8.2 Flex-direction: column

- flex itens ficarão um abaixo do outro, formando uma coluna.

### 5.8.3 Flex-direction: row-reverse

- os flex itens ficarão alinhados a partir da direita do container pai.

### 5.8.4 Flex-direction: column-reverse

- Os flex itens ficarão em ordem inversa um abaixo do outro, formando uma única coluna em ordem inversa.

## 5.9 Flex-wrap

- por padrão, o Flexbox deixará todos os flex itens de um container em uma mesma linha. 
- a propriedade flex-wrap serve para definir que seja executada a quebra de linhas quando necessário. 

### 5.9.1 Flex-wrap: nowrap

- não permitirá a quebra de linhas.
- é o valor padrão, não precisará ser declarado.

### 5.9.2 Flex-wrap: wrap

- permitirá a quebra de linhas quando os flex itens não couberem na mesma linha do container. 
- com sua utilização, a largura definida aos filhos será aplicada.

### 5.9.3 Flex-wrap: wrap-reverse

- permitirá a quebra de linha, iniciando o posicionamento dos elementos da parte esquerda inferior para a parte superior do container pai.

## 5.10 Justify-content

- propriedade utilizada para definir o posicionamento dos flex itens, conforme o eixo definido (linha ou coluna).

### 5.10.1 Justify-content: flex-start

- alinha os flex itens no início do elemento pai.
- é o valor padrão, não precisa ser declarado.

### 5.10.2 Justify-content: flex-end

- alinha os flex itens no fim do elemento pai.

### 5.10.3 Justify-content: center

- centraliza os flex itens no elemento pai.

### 5.10.4 Justify-content: space-between

- faz o posicionamento dos containers pelas extremidades do elemento pai, deixando um espaçamento praticamente igual entre os flex itens.

### 5.10.5 Justify-content: space-around

- faz o posicionamento dos containers pelo centro do elemento pai, deixando os espaçamentos centrais maiores que os espaçamentos entre as extremidades do container pai.

### 5.10.6 Justify-content: space-evenly

- faz o mesmo posicionamento feito pelo space-around.
- a diferença é que todos os espaçamentos serão iguais.

## 5.11 Align-items

- alinha os flex itens de acordo com o eixo do container (linha ou coluna). 
- com essa propriedade podemos fazer o alinhamento central pelo eixo vertical.

### 5.11.1 Align-items: flex-start

- alinhará os flex itens no início do elemento pai. 
- é o valor padrão, não precisa ser declarado.

### 5.11.2 Align-items: flex-end

- alinha os flex itens no final do elemento pai.

### 5.11.3 Align-items: center

- alinha os flex itens no centro do elemento pai.
- se esse elemento receber a propriedade flex-direction com o valor row, teremos o alinhamento vertical.

### 5.11.4 Align-items: stretch

- deixa os flex itens com a mesma altura do elemento pai. 
- para essa propriedade funcionar, os flex itens não devem ter a propriedade height declarada na regra CSS.

### 5.11.5 Align-items: baseline

- faz o alinhamento dos flex itens conforme a linha base do texto.

## 5.12 Flex-grow

- essa propriedade deverá ser aplicada apenas aos flex itens.
- permite que os flex itens tenham larguras diferentes.
- o valor padrão é zero: eles ocuparão o tamanho máximo baseado no conteúdo ou na largura definida na regra CSS. 
- se definir com valor 1, o browser tentará deixá-los com a mesma largura. 
- caso algum deles tenha um conteúdo muito grande, a largura desse elemento será preservada.

## 5.13 Flex-basis

- só deve ser aplicada aos flex itens.
- define um valor fixo para a largura de um container, e acontecerá caso exista espaço suficiente. Os demais elementos terão a sua largura calculada pelo espaço restante do container pai. 
- podemos usar essa propriedade em conjunto com a flex-grow.

## 5.13 Order

- aplicado apenas aos flex itens.
- define a ordem como os elementos devem aparecer na tela.
- é uma opção legal para reorganizar conteúdo sem ter de alterar o código HTML.

## 5.14 Gap

- define o espaçamento entre as linhas e/ou colunas. - possibilidades para definir os valoresa:
  - definindo um único valor: esse valor será utilizado tanto para linhas como para as colunas.
  - definindo dois valores: o primeiro valor será utilizado para as linhas e o segundo para as colunas.
  - utilizando a propriedade row-gap: define o valor de espaçamento entre as linhas.
  - utilizando a propriedade column-gap: define o valor de espaçamento entre as colunas.

## 5.15 Position

- define a posição que um elemento ficará em relação ao body ou ao seu container pai, permitindo que ele saia do seu fluxo normal. 
- a nova posição será controlada alterando os valores das propriedades: top, bottom, lefte right. 
- todos os elementos HTML têm a propriedade position com valor padrão static (padrão). 

### 5.15.1 Position Relative

- usado para definir um novo posicionamento para o elemento.
- se baseia na posição inicial onde o elemento foi inserido.

### 5.15.2 Position absolute

- define a posição absoluta do elemento. 
- podemos usar o elemento &lt;body&gt; como referência para efetuar o novo posicionamento.
- podemos também usar o elemento pai como referência: para isso devemos atribuir a ele um position diferente de static. 
  - dessa forma, o browser entenderá que o filho usará o elemento pai para definir o seu novo posicionamento.

### 5.15.3 Position fixed

- define que um elemento deverá sempre ficar fixo na tela. 
  - mesmo que exista rolagem de tela, o elemento sempre estará visível.

## 5.16 Z-index

- assim que a propriedade position é aplicada, o elemento também poderá receber a propriedade z-index,.
- define a ordem que os elementos devem ter quando se sobrepõem. 
- o valor inicial para todos é 0, e o elemento que receber o maior valor, ficará acima dos demais.

### Laboratório Flexbox: [HTML](./projetos/projeto5/pages/index.html) e [CSS](./projetos/projeto5/css/style.css).

---

## FAST TEST

### 1. Sobre as tags, assinale a alternativa correta:
> A tag &lt;div&gt;&lt;/div&gt; é um contêiner que pode ser criado para armazenar qualquer tipo de conteúdo.

### 2. Em relação às propriedades width (largura) e height (altura), os valores mais comuns são definidos em: 
> px (pixel) e % (porcentagem).

### 3. Imagens de fundo podem ser configuradas para que fiquem fixas na tela ou acompanhem o seu scroll. Para tanto, a propriedade background-attachment deve ser utilizada com quais valores?
> fixed e scroll.

---

[Voltar ao início!](https://github.com/monicaquintal/fintech)