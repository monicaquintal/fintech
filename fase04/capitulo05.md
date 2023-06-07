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

