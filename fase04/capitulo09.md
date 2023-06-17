<div id="fase03" align="center">
<h1>FASE 4 - VIEW</h1>
<h2>Capítulo 09: Muito estilo sem sofrimento! 😲</h2>
</div>

[Mais Bootstrap aqui!](https://github.com/monicaquintal/bootstrap) 🚀

<div align="center">
<h2>1. MUITO ESTILO SEM SOFRIMENTO</h2>
</div>

> `Framework`: conjunto de classes prontas para serem usadas, e que podem ser alteradas conforme a necessidade do desenvolvedor.

- `Bootstrap`:
  - framework front-end responsivo.
  - permite maior agilidade no desenvolvimento de páginas ou interfaces para a Internet.
  - código aberto (qualquer pessoa pode utilizar o framework sem custo).
  - possui uma série de classes CSS prontas que podem ser inseridas no elemento HTML. 
  - possui também uma série de componentes que podem ser utilizados em sua aplicação, como menus de navegação, carrossel de imagens, cards, formulários etc.
  - também usa o JavaScript para executar algumas funcionalidades e disponibilizar uma experiência de interação mais rica ao usuário.

> [Documentação do Bootstrap](https://getbootstrap.com/).

## 1.1 Iniciando o Bootstrap

- é possível baixar o framework **ou** apenas linkar os arquivos necessários, via um servidor CDN, diretamente na página.

### 1.1.1 Baixando o Bootstrap

- acessar o [site do Bootstrap](https://getbootstrap.com/).
- para fazer o download dos arquivos, clicar na opção Docs, encontrada no menu principal. 
- clicar na opção Download, localizada no menu lateral, para baixar os arquivos.
- com a página de download aberta, pressionar o botão para baixar os arquivos necessários.
- descompactar o arquivo baixado. 
  - dentro dessa pasta há outras duas: uma contendo arquivos CSS e outra arquivos JavaScript. 
  - essas pastas deverão estar no projeto!

> os arquivos baixados encontram-se no repositório fase 04 > [bootstrap](./bootstrap).

### 1.1.2 Linkando diretamente – CDN

- caso não queira baixar o framework, é possível fazer um link direto com o servidor CDN onde estão armazenados os arquivos necessários para o Bootstrap funcionar.
- para linkar o arquivo CSS responsável pela estilização do framework, colocar na seção &lt;head&gt;, a seguinte linha de código:

~~~html
<link 
  href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" 
  rel="stylesheet" 
  integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" 
  crossorigin="anonymous"/>
~~~

- é necessário também linkar o arquivo Javascript, que será responsável por permitir uma interação maior por parte do usuário. 
- colocar antes do fechamento do &lt;body&gt; a seguinte linha de código:

~~~html
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js"
integrity="sha384-kenU1KFdBIe4zVF0s0G1M5b4hcpxyD9F7jL+jjXkk+Q2h455rYXK/7HAuoJl+0I4" 
crossorigin="anonymous">
</script>
~~~

## 1.2 Template inicial

- o Bootstrap disponibiliza um template básico contendo a estrutura HTML inicial e os links CDN para os arquivos do framework, disponível [aqui](https://getbootstrap.com/docs/5.2/getting-started/introduction/). 
  - essa estrutura deverá ser salva em um arquivo com extensão .html.
- para os exemplos da aula, será utilizado o template baixado diretamente do site do BootStrap.

~~~html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Bootstrap demo</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" 
  rel="stylesheet" 
  integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" 
  crossorigin="anonymous">
</head>
<body>
  <h1>Hello, world!</h1>
  ...
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js" 
  integrity="sha384-kenU1KFdBIe4zVF0s0G1M5b4hcpxyD9F7jL+jjXkk+Q2h455rYXK/7HAuoJl+0I4" 
  crossorigin="anonymous">
  </script>
</body>
</html>
~~~

## 1.3 Paleta de cores

- O Bootstrap possui um padrão de cores com uma paleta bem definida. 
- as cores podem ser aplicadas a textos, backgrounds, botões e containers, utilizando as respectivas classes CSS do framework.
- são elas:
  - primary;
  - danger;
  - light;
  - secondary;
  - warning;
  - dark;
  - success;
  - info.
- o Bootstrap possui uma nomenclatura para atribuir uma cor a algum elemento específico; para isso, ele define um nome para o elemento seguido da cor.

Elemento | Nomenclatura Bootstrap | Exemplo de cor
---------|-----------------------|----------------
Background | bg | bg-info
Texto | text | text-dark
Botão | btn | btn-danger
Tabela | table | table-primary
Borda | border | border-success

## 1.4 Variáveis Bootstrap

- o Bootstrap também usa o recurso de variáveis CSS para definição de cores, margem, padding, bordas etc.
- no código do framework, encontra-se uma grande quantidade de variáveis, que podem ser utilizadas nas aplicações. 

> Link para documentação [aqui](https://getbootstrap.com/docs/5.0/customize/css-variables/).

## 1.5 Containers

- são elementos de layout nos quais o conteúdo da página ficará armazenado. 
- utilizando o framework, os containers serão criados através de classes CSS inseridas nos elementos HTML: &lt;div&gt;, &lt;section&gt;, &lt;article&gt;, &lt;aside&gt; etc. 
- há duas classes principais:
  - classe container: largura máxima de 1320px (e centraliza o container na tela).
  - classe container-fluid: tamanho flexível, ocupando 100% da largurada página ou do componente.
  - **importante**: por padrão, a altura dos elementos que utilizarem essas classes, será definida pela quantidade de conteúdo que receberão.

## 1.6 Sistema de grid

- bem definido e responsivo.
- composto por uma série de containers posicionados em conjunto, formando linhas e colunas do layout.
- flexível.
- composto por doze colunas em cada linha.
- conta com seis breakpoints que facilitam a criação de aplicações responsivas.

### 1.6.1 Breakpoints

- o sistema de grid do Bootstrap é totalmente responsivo, e consegue se adaptar a qualquer tipo de dispositivo. 
- há classes específicas para determinados breakpoints, que deverão ser aplicadas nas colunas do grid:
  - classe col: deve ser usada para dispositivos de tamanho máximo de 575px (smartphones).
  - classe col-sm: para dispositivos de tamanho mínimo de 576px (alguns smartphones e tablets).
  - classe col-md: dispositivos de tamanho mínimo de 768px (tablets).
  - classe col-lg: para dispositivos de tamanho mínimo de 992px (notebooks e desktops).
  - classe col-xl: para dispositivos de tamanho mínimo de 1200px (telas grandes).
  - classe col-xxl: deve ser usada para dispositivos de tamanho mínimo de 1400px, as maiores telas para o projeto.

### 1.6.2 Aplicando classes do grid

- dentro do elemento que possuir a classe “container” ou “container-fluid”, criar as linhas do grid com a utilização da classe “row”. 
- dentro das linhas é feita a divisão em colunas.
  - cada linha possui no máximo 12 colunas. 
  - utilizar a classe “col” seguida do número de colunas desejadas.

## 1.7 Tipografia

- o Bootstrap possui estilos básicos para fontes.
- ele usa o tamanho padrão da fonte em 16px e, em suas regras CSS faz uso da unidade de medida rem (16px = 1rem).

### 1.7.1 Classe Display

- utilizada em qualquer elemento heading, alterando altura e espessura do título.
- atribuir também o tamanho desejado (que varia entre 1 e 6).

### 1.7.2 Classe Lead

- aplica formatação parecida com a da classe display, mas a lead deve ser usada nos parágrafos.