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