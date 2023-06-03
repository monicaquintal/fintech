<div id="fase03" align="center">
<h1>FASE 4 - VIEW</h1>
<h2>Capítulo 03: HTML - Falando a língua da Internet. 💻</h2>
</div>

<div align="center">
<h2>1. HTML: FALANDO A LINGUAGEM DA INTERNET</h2>
</div>

- `tag`: uma marcação HTML que informa ao browser qual é o tipo de conteúdo.
- os browsers interpretam as tags HTMLe renderizam o respectivo conteúdo.

## 1.1 Histórico

- HTML = HyperText Markup Language (Linguagem de Marcação de Hipertexto).
- criado no início da década de 1990, por Timothy John Berners-Lee.
- atualmente utilizamos como versão padrão o `HTML5`.

> O site [Can I use](http://caniuse.com) é utilizado para identificar imcompatibilidades entre tags e navegadores; basta acessar a página e digitar o nome da tag ou componente Web que deseja pesquisar.

## 1.2 Linguagem de marcação

- ***HTML não é uma linguagem de programação, e sim, de marcação!***
- a única função a ela atribuída é marcar onde começa e onde deve terminar um determinado conteúdo.

## 1.3 Compreendendo as tags

- um conjunto de tags dentro de uma estrutura padrão forma uma página web, e um conjunto de páginas forma um site. 
- é estática, ou seja, nunca irá mudar o seu conteúdo.

> a tag deve ter um nome entre os sinais de maior e menor, &lt;nome da tag&gt;. Por boa prática, em letras minúsculas.

- ***atributos***: escritos junto ao nome da tag, podem fornecer informações sobre o conteúdo e melhorar a experiência do usuário.
- a maioria das tags deve ser aberta e fechada. Aquelas que não requerem fechamento são chamadas de elementos vazios. 

## 1.4 Criando as pastas do projeto no VS Code

- utilizar estruturade pastas: boa prática, e garante maior organização.

## 1.5 Criando o arquivo index

- por padrão, a página principal do site deverá ser chamada de [index.html](./projetos/pages/index.html).
- digitar ponto de exclamação (!) e pressionar ENTER.
  - o editor possui uma extensão nativa chamada `Emmet`, que possui muitos atalhos para criação de estruturas HTML.

## 1.6 Entendo a estrutura básica HTML 

~~~html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width,initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  Aqui ficará todo o conteúdo da página
</body>
</html>
~~~

### 1. &lt;!DOCTYPE html&gt;:
- primeira linha do código.
- indica ao browser qual especificação de código HTML estará na página.

### 2. &lt;html lang="en"&gt;:
- indica o início do código.
- todos os elementos existentes na página deverão ser inseridos abaixo dessa tag.
- informar o idioma principal do documento através do atributo lang (pt-br).
- fechamento &lt;/html&gt; indica o dinal do código e da página.

### 3. &lt;head&gt;:
- seu conteúdo é o primeiro a ser lido no carregamento da página.
- nele, definir estilos, links, título do documento e até os ***metadados*** (dados gerados sobre a própria página).
- fechamento &lt;/head&gt;.

### 4. &lt;meta charset="utf-8"&gt;:
- sempre ficará na seção &lt;head&gt;.
- indica qual cadeia de caracteres o documento usará.
- `utf-8`: indica a cadeia de caracteres que possui letras com acentuação.
- metatags não possuem fechamento.

### 5. &lt;meta name="viewport" content="width=device-width, initial-scale=1"&gt;:
- metatag que também fica na seção &lt;head&gt;.
- através dela o navegador detecta o tamanho da área disponível para exibição de conteúdo, no dispositivo que o usuário está utilizando para fazer o acesso (celular, notebook, tablet etc).
- content="width=device-width":
  - detecta o tamanho da área.
- "initial-scale=1":
  - define o zoom inicial da página.
  - 1 = 100%.

### 6. &lt;title&gt;:
- na seção &lt;head&gt;.
- define o título da página.
- os robôs de pesquisa do Google leem o seu conteúdo e entendem que ali há uma descrição que pode indicar o assunto principal da página.
- possui fechamento representado por &lt;/title&gt;.

### 7. &lt;body&gt;:
- nessa seção, inserimos todo o conteúdo da página.
- o conteúdo pode ser texto, imagens, vídeos, tabelas ou qualquer tipo de elemento. 
- fechamento representado por &lt;/body&gt;.

## 1.7 Alterando a estrutura básica HTML

- alterar a sigla do idioma de “en” para “pt-BR”.
- a linha 05 possui uma metatag de compatibilidade de exibição de conteúdo para o browser Internet Explorer; como a Microsoft definiu o fim desse navegador, excluir essa linha.
- definir o title.

<div align="center">
<h2>2. TAGS INICIAIS</h2>
</div>

