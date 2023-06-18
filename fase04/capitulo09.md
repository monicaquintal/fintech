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
  - `classe container`: largura máxima de 1320px (e centraliza o container na tela).
  - `classe container-fluid`: tamanho flexível, ocupando 100% da largurada página ou do componente.
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
  - `classe col`: deve ser usada para dispositivos de tamanho máximo de 575px (smartphones).
  - `classe col-sm`: para dispositivos de tamanho mínimo de 576px (alguns smartphones e tablets).
  - `classe col-md`: dispositivos de tamanho mínimo de 768px (tablets).
  - `classe col-lg`: para dispositivos de tamanho mínimo de 992px (notebooks e desktops).
  - `classe col-xl`: para dispositivos de tamanho mínimo de 1200px (telas grandes).
  - `classe col-xxl`: deve ser usada para dispositivos de tamanho mínimo de 1400px, as maiores telas para o projeto.

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

### 1.7.3 Tamanho da fonte

- `classe fs` define o tamanho da fonte dos textos.
- mesmo conceito dos headings: quanto maior o valor,menor o tamanho da fonte.

### 1.7.4 Alinhamento de texto

- `classe text-start`: alinha o texto à esquerda do container.
- `classe text-end`: alinha o texto à direita do container.
- `classe text-center`: alinha o texto ao centro do container.

## 1.8 Bordas:

- `classe border`: define que o elemento receberá uma borda.
- `classe border-valor`: define a largura da borda.
  - usar valores entre 1 (mais fina) e 5 (mais grossa).
- `classe border-color`: define a cor que a borda terá.
  - usar qualquer cor válida dentro do padrão de cores do framework
- `classe rounded-valor`: define arredondamento dos cantos da borda. 
  - valores entre 0 (sem arredondamento) e 5 (mais arredondada).

## 1.9 Margin – Padding:

- as classes para margin e padding são nomeadas no formato property-{sides}:{size}.
  - property:
    - p (padding).
    - m (margin).
  - sides:
    - t (top).
    - b (bottom).
    - e (end) - right.
    - s (start) - left.
    - x (start + end).
    - y (top + bottom).
  - size (16px):
    - 0 (16&#42;0 = 0).
    - 1 (16&#42;0.25 = 4px).
    - 2 (16&#42;0.5 = 8px).
    - 3 (16&#42;1 = 16px).
    - 4 (16&#42;1.5 = 24px).
    - 5 (16&#42;3 = 48px).

## 1.10 Imagens responsivas

- `classe img-fluid` ou classe `img-thumbnail` (que além da responsividade, insere uma borda contornando a imagem).

## 1.11 Tabelas

- `classe table`: faz a formatação de texto e insere linhas entre as tags &lt;tr&gt;.
- `classe table-dark`: inverte as cores da tabela, deixando o background na cor preta e o conteúdo na cor branca.
- `classe table-striped`: alterna o background das linhas, facilitando a leitura das informações em tabelas com quantidade muito grande de dados.
- `classe table-bordered`: adiciona bordas em todos os elementos da tabela.
- `classe table-borderless`: retira todas as bordas da tabela.
- `classe table-hover`: quando o mouse passar por cima de algum conteúdo da tabela, o background da linha onde ele está posicionado mudará de cor, ficando em destaque.
- `classe table-sm`: deixa a tabela mais compacta, retirando o padding anteriormente atribuído pela classe table.
- `classe table-responsive`: a tabela fica responsiva, adaptando-se ao container onde foi inserida.

## 1.12 Botões

### 1.12.1 Botões comuns

- `classe btn`.
- aplicar as cores padrão do Bootstrap.

### 1.12.2 Tamanho de botões

- `classe btn-lg`: altera o tamanho do botão, deixando-o maior.
- `classe btn-sm`: altera o tamanho do botão, deixando-o menor.

### 1.12.3 Grupo de botões

- os botões podem ser posicionados em grupos.
- criar um container HTML que receberá a `classe btn-group`, e inserir os botões em seu interior.

### 1.12.4 Botão dropdown

- quando você clica, abre novas opções, como se fosse um submenu.
- como fazer:
  - inserir a `classe dropdown` em um container.
  - em seu interior, inserir um elemento HTML &lt;button&gt;, com a `classe dropdown-toggle`.
  - criar uma lista HTML e atribuir a `classe dropdown-menu`. 
  - cada opção do menu deve ter a `classe dropdown-item`.

## 1.13 Menus de navegação

- há vários exemplos de menus de navegação responsivos e adaptáveis. 
- esse componente é composto pelas classes:
  - `classe navbar`: indica a criação de uma barra de navegação.
  - `classe navbar-expand-lg`: em telas grandes, teremos a visualização  de todas as opções existentes no menu de navegação. Em telas menores, teremos a visualização de um menu sanduíche que quando for clicado, será expandido, exibindo assim as opções do menu.
  - `classe navbar-brand`: permite que insira o logotipo e/ou nome da empresa ou do projeto.
  - `classe navbar-toggler`: ativa ou desativa visualização do menu-sanduíche.
  - `classe nav-item`: como os menus são inseridos em elementos de lista &lt;ul&gt; ou &lt;ol&gt;, essa classe deve ser inserida na tag &lt;li&gt;, pois define as opções existentes no menu.
  - `classe nav-link`: é dentro do elemento com essa classe que será inserido o conteúdo que ficará visível ao internauta, são as opções do menu.
  - `classe navbar-toggler-icon`: Bootstrap usa essa classe para inserir o ícone do menu-sanduíche.

> há diversas opções de menus, que podem ser acessadss [aqui](https://getbootstrap.com/docs/5.2/components/navbar/).

## 1.14 Formulários

- `classe form-control:` utilizada na maioria dos campos de texto, define espaçamento e formatação do texto, e ajuda na parte responsiva do campo.
- `classe form-label:` usada para estilizar qualquer elemento &lt;label&gt; dentro de um formulário.
- `classe form-check-input`: usada em componentes de formulário do tipo radio e checkbox.
- `classe form-check-label`: usada em elementos &lt;label&gt; que serão atribuídos aos componentes radio e checkbox.
- `classe form-select`: usada apenas no elemento &lt;select&gt; do formulário.
- `classe form-range`: usada no componente de formulário do tipo range.
- `classe form-floating`: permite que o elemento &lt;label&gt; mude sua posição inicial, indo para o topo do campo de texto assim que esse campo ganhar foco. O valor atribuído ao label ficará flutuando no campo.
- `classe input-group`: permite que textos, botões ou grupo de botões sejam agrupados no início ou no fim do componente do formulário. Muitas vezes há ícones agrupados no início de um campo, substituindo o elemento label.

## 1.15 Cards

- é um container flexível que pode armazenar uma grande variedade de conteúdo.
- na maioria das vezes juntamos em um só container: um título, uma imagem, alguma descrição e um botão para acessar o conteúdo exibido. 
- classes:
  - `classe card`: define o container pai que receberá todo o conteúdo.
  - `classe card-img-top`: receberá a imagem do card.
  - `classe card-body`: define o corpo do card: título, texto e link.
  - `classe card-title`: define o título para o card.
  - `classe cart-text`: define o texto que será inserido no card.

> na documentação do framework há várias opções de cards; para conhecer outros estilos desse componente, [acessar aqui](https://getbootstrap.com/docs/5.2/components/card/).

## 1.16 Janela modal

- uma janela Modal deixará o conteúdo da página congelado em segundo plano, enquanto uma nova janela estiver aberta. O conteúdo da página voltará ao primeiro plano assim que esse elemento for fechado.
- para montar um modal, usar um botão ou link que fará sua chamada, e receberá o `atributo data-bs-target`, que indica qual janela o botão chamará, o valor a ser atribuído é o id definido da janela que será aberta.
  - `classe modal`:indica que o container será um elemento modal.
  - `classe fade`: faz o modal aparecer ou desaparecer suavemente.
  - `classe modal-dialog`: define o container principal do modal.
  - `classe modal-content`: receberá o conteúdo do modal.
  - `classe modal-header`: define o container de cabeçalho do modal. Nele também ficará o botão que fechará o modal.
  - `classe modal-title`: título do modal.
  - `classe modal-body`: corpo do modal, conteúdo a ser exibido.
  - `classe modal-footer`: rodapé do modal; é opcional.

## 1.17 Accordion

- é um container que inicia exibindo apenas o título, seu conteúdo fica todo escondido. Assim que efetuamos um clique no título, esse container é aberto e o seu conteúdo visualizado.
- se houver outros componentes como esse elemento e, caso cliquemos em outro título, o conteúdo anterior volta a ficar escondido e o novo será exibido.
- para utilizá-lo:
  - criar um container HTML com a `classe accordion` e, em seu interior, outro container HTML com a `classe accordion-item`.
  - inserir um elemento de título com a `classe accordion-header` e o id que identificará os conteúdos visíveis. 
  - deve possuir também uma tag &lt;button&gt; com a `classe accordion-button`, e nesse elemento ficará o título que será visível ao usuário.
  - inserir abaixo outro container com o id definido anteriormente, seguido das `classes: accordion-collapse e collapse`, que farão abertura e fechamento dos conteúdos.
  - a `classe show` fará com que o conteúdo inicie visível para o usuário.
  - `classe accordion-body` é onde ficará o conteúdo a ser visualizado pelo usuário.

## 1.18 Vídeos

- acessar o vídeo desejado no YouTube, clicar na opção compartilhar e,em seguida, em incorporar.
- será aberta uma caixa de diálogo com uma imagem do vídeo e um código HTML com o elemento &lt;iframe&gt;.
- copiar todo o conteúdo desse elemento, ou apenas o conteúdo inserido no atributo src do &lt;iframe&gt;.
- usar o `componente ratios` do Bootstrap, que irá controlar a responsividade do vídeo incorporado. 
  - para ver as opções, acessar [aqui](https://getbootstrap.com/docs/5.2/helpers/ratio).
- o `aspect-ratios` é a proporção matemática obtida pela divisão entre a largura e a alturado vídeo. 
  - existem alguns padrões, sendo os mais comuns: 21x9, 16x9, 4x3 e 1x1.
- é necessário inserir a `classe ratio` para que o vídeo seja corretamente posicionado no container.
- é necessário alterar o `atributo src` do iframe, substituindo o valor inicial pelo endereço do vídeo no Youtube.

## 1.19 Carousel

- é formado por um conjunto de imagens que ficam em um container, conforme um tempo definido ou uma ação do usuário, temos a exibição de outra imagem com um efeito de transição entre elas.
- para utilizá-lo, inserir um container HTML com a `classe carousel` e `classe slide`, que fará a animação de transição das imagens. Esse container deverá ter um identificador id e terá três partes distintas:
  - área de indicadores:
    - são marcações que ficarão na parte inferior das imagens, possibilitando a navegação por esses elementos.
    - inserir um container com a `classe carousel-indicators`.
    - cada imagem do carousel terá o seu indicador, então inserir um elemento &lt;button&gt; para cada uma.
    - esse elemento deverá possuir `dois atributos`: `data-bs-target` (receberá como valor o id do container HTML) e `data-bs-slide-to`(receberá uma numeração iniciando em 0, que representa as imagens usadas no carousel). 
  - área de imagens:
    - abaixo da lista de indicadores, inserir um container HTML com a `classe carousel-inner`.
    - nesse container ficarão as imagens que deseja exibir.
    - cada imagem deve ficar dentro de um container próprio, que terá a `classe carousel-item`.
    - inserir também a `classe active` na imagem que deseja que inicie o carousel.
  - área das setas de navegação:
    - podemos inserir setas de navegação para avançar ou voltar as imagens. 
    - inserir a tag &lt;button&gt; com a `classe carousel-control-prev` para voltar na imagem anterior e outro &lt;button&gt; com a `classe carousel-control-next` para avançar para a próxima imagem.

> para um melhor resultado visual, todas as imagens do elemento carousel devem possuir o mesmo tamanho.

---