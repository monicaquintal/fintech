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

- por padrão, a página principal do site deverá ser chamada de [index.html](./projetos/projeto1/pages/index.html).
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
- normativa, tipo de HTML que há no código.
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

## 2.1 Comentários em HTML

- são informações que podem ser inseridas em seu código para explicar o que significa uma determinada linha ou até mesmo um bloco de comandos.
- as linhas comentadas não serão exibidas pelo navegador, apenas no código.
- não exagerar na quantidade de comentários, podem deixar o código poluído.

~~~html
<!--comentário -->
~~~

## 2.2 Headings (h) – Cabeçalhos HTML

- são os cabeçalhos de títulos.
- há seis níveis possíveis (1 a 6).
  - o maior título possível é o &lt;h1&gt;&lt;/h1&gt; e o menor é o &lt;h6&gt;&lt;/h6&gt;.
- boas práticas:
  - usar apenas um único elemento &lt;h1&gt; em cada página, e conter o assunto principal ou título.
  - seguir a ordem numérica para manter a organização (título principal, subtítulo, tópicos do subtítulo, etc).

## 2.3 Visualizando o código no browser

- salvar com ctrl + S (ou ativar opção Auto Save, localizada no menu File).
- opções:
  - duplo clique em index.html.
  - extensão Live Server (ALT+L ALT+O).

## Criando parágrafos

- tag &lt;p&gt;&lt;/p&gt; (paragraph).
- não existe limite para o número de palavras.
- a tag p deverá ser fechada.
- observação:
  - o VS Code possui recurso de simulação de texto através do Emmet, gerando texto Lorem ipsum (digitar lorem e pressionar Enter).
  - caso queira um número definido de palavras, digitar lorem e o número de palavras desejado.

## 2.5 Inserindo Imagens

- tag &lt;img&gt;.
- é uma tag vazia (não existe fechamento).
- atributos:
  - ***src***: 
    - indica o caminho da imagem, local onde o arquivo está armazenado.
  - ***alt***:
    - insere um pequeno texto que descreve a imagem, e será exibido caso a imagem não seja carregada pelo navegador.
    - ajuda na acessibilidade a pessoas que tenham deficiência visual e façam uso de leitores de tela. 
    - o uso do atributo alt é uma boa prática!
  - ***title***:
    - texto que será quando posicionar o ponteiro do mouse sobre a imagem. 
    - não é exclusivo para as imagens, praticamente todos os elementos HTML podem usar.
    - na maioria das vezes o valor atribuído é o mesmo utilizado no alt.

> [Primeiro site criado no mundo!](http://info.cern.ch/hypertext/WWW/TheProject.html)

## 2.6 Listas

- há três tipos de listas:
  - listas ordenadas.
  - listas não ordenadas.
  - listas de definição.
- podemos inserir uma lista dentro de outra lista, conhecidas como listas aninhadas.

### 2.6.1 Lista ordenada

- criada com o uso da tag &lt;ol&gt;&lt;/ol&gt;.
- cada item da lista deverá estar dentro da tag &lt;li&gt;&lt;/li&gt;.

### 2.6.2 Lista não ordenada

- criada com o uso da tag &lt;ul&gt;&lt;/ul&gt;.
- cada item da lista deverá estar dentro da tag &lt;li&gt;&lt;/li&gt;.

### 2.6.3 Lista de definição

- permite a criação de um conjunto de palavrase as suas respectivas definições.
- deve ser criada com o uso da tag &lt;dl&gt;&lt;/dl&gt;.
- cada palavra da lista a ser definida deverá estar dentro da tag &lt;dt&gt;&lt;/dt&gt;. 
- a definição da palavra deverá estar dentro da tag&lt;dd&gt;&lt;/dd&gt;.

## 2.6.4 Lista aninhada

- montar uma nova lista dentro de um elemento &lt;li&gt; para criar uma lista aninhada (lista dentro de outra lista).
- os navegadores colocam um recuo maior para a lista interna além de modificar o estilo do seu marcador.

## 2.7 Links

- permitem navegação entre documentos.
- tag &lt;a&gt;Link&lt;/a&gt;, e pode possuir qualquer conteúdo entre abertura e fechamento.
- utilizar o ***atributo href***, que deve receber como valor o endereço do conteúdo.

### 2.7.1 Links para outros sites – links externos

- o atributo href deve receber o endereço completo do site desejado (chamada url absoluta).

### 2.7.2 Links para páginas no mesmo site – links internos

- definir o endereço do arquivo HTML desejado no atributo href da tag &lt;a&gt;.

### 2.7.3 Abrindo links em novas abas

- sempre que clicamos em um link, o comportamento padrão é ser aberto na mesma aba do navegador que você está usando. 
- podemos usar na tag &lt;a&gt; o atributo ***target="_blank"***, que permite que o link seja aberto em uma nova aba!
- esse recurso pode ser usado tanto para links internos quanto externos. 

### 2.7.4 Link para números de telefone

- se o usuário estiver usando um smartphone, a ligação será realizada automaticamente. 
- caso esteja utilizando um notebook ou desktop, poderá fazer a sincronização dos dispositivos para realizar a chamada.
- colocar no atributo href o valor tel: seguido do código DDD da cidade e o número do telefone!

### 2.7.5 Link para download de arquivos

- colocar no atributo href o endereço do arquivo que será baixado pelo usuário, depois inserir o atributo download.

### 2.7.6 Link para seções na mesma página

- utilizar o `atributo id`, que corresponde a um identificador que qualquer elemento HTML pode utilizar (inclusive usamos esse atributo em linguagens como a CSS e o Javascript).
- atribur o valor do id para o elemento HTML desejado.
- em nenhuma circunstância podemos ter dois ou mais elementos com o mesmo id.
- para criar os links para as seções:
  - identificar as seções com os ids desejados.
  - na tag &lt;a&gt;,o atributo href deverá receber como valor o sinal de hashtag (#), seguido do id da seção que queremos acessar com aquele link.

<div align="center">
<h2>Laboratório</h2>
</div>

---

## FAST TEST

### 1. A principal forma de interação, no que diz respeito à entrada de dados, são os formulários. Identifique uma tag que NÃO faz parte do formulário.
> Tableless.

### 2. Pensando na linguagem HTML, qual destas afirmações é FALSA?
> A tag &lt;head&gt; é a primeira tag de um documento, colocada antes mesmo da tag &lt;html&gt;.

### 3. Identifique a tag que está INCORRETA:
> A tag &lt;script&gt; é utilizada para inserir comandos e efeitos especiais na página.

--- 

[Voltar ao início!](https://github.com/monicaquintal/fintech)