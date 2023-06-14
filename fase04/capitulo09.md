<div id="fase03" align="center">
<h1>FASE 4 - VIEW</h1>
<h2>Capítulo 09: Muito estilo sem sofrimento! 😲</h2>
</div>

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
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">
</head>
<body>
  <h1>Hello, world!</h1>
  ...
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-kenU1KFdBIe4zVF0s0G1M5b4hcpxyD9F7jL+jjXkk+Q2h455rYXK/7HAuoJl+0I4" crossorigin="anonymous">
  </script>
</body>
</html>
~~~

## 1.3 Paleta de cores