<div id="fase03" align="center">
<h1>FASE 4 - VIEW</h1>
<h2>Capítulo 07: Formulários. 📑</h2>
</div>

<div align="center">
<h2>1. FORMULÁRIOS</h2>
</div>

- permitem interação com a aplicação, canal direto de comunicação entre a aplicação e o público-alvo.
- `formulário` é uma página HTML com componentes (campos) que podem ser preenchidos/selecionados pelo usuário, e ao final poderá clicar em um botão que enviará as informações digitadas para um servidor web. 
- o HTML não consegue fazer esse envio sozinho, precisa da ajuda de uma linguagem de programação para conseguir realizar essa tarefa.

> Se o seu formulário não tiver uma linguagem de programação trabalhando em conjunto com o HTML, ao tentar enviar a página, ela será atualizada e os dados digitados serão apagados!

### As tags e atributos estão exemplificados aqui: [HTML](./projetos/projeto8/pages/estudo-conteudo-aula.html) e [CSS](./projetos/projeto8/css/estudo-conteudo-aula.css).

## 1.1 Tag form

- no interior da tag &lt;form&gt;&lt;/form&gt; são definidos os componentes que deverão ser vistos e utilizados pelos usuários. 
- a tag &lt;form&gt; possui alguns atributos que identificam o formulário e controlam como as informações digitadas serão enviadas.

### 1.1.1 Atributo name

- define um nome a ser atribuído ao formulário. 
- é um atributo importante pois algumas linguagens farão uso dele para recuperar o que foi selecionado ou digitado pelo usuário. 
- os campos existentes no formulário também podem receber esse atributo.

### 1.1.2 Atributo id

- define um identificador para o formulário, e o valor atribuído não pode ser usado por mais nenhum outro elemento na mesma página.
- algumas linguagens de programação farão uso dele para conseguir acessar o que foi selecionado/digitado pelo usuário. 
- os campos do formulário também podem receber esse atributo.

### 1.1.3 Atributo action

- define o que irá acontecer com os dados digitados quando o usuário pressionar o botão de envio(submeter). 
  - os dados poderão ser enviados para: uma nova página, um e-mail, uma tabela em algum banco de dados ou algum servidor web onde serão processados. 
- é comum inserir como valor do atributo action o endereço de algum script que irá recuperar as informações digitadas e efetuar o seu envio. 
- se deixar o valor desse atributo em branco, o browser tentará submeter o formulário, porém os campos preenchidos terão seus valores apagados.

### 1.1.4 Atributo method

- define qual método será usado para enviar os dados digitados, sendo eles `GET` e `POST`.
  - método GET: 
    - é o padrão.
    - utiliza a URL e o local onde você digita o endereço de um site no browser, para enviar as informações digitadas ao servidor.
    - muito usado para formulários de pesquisas para passar as informações de um produto, fazer paginação, etc. 
  - método POST:
    - envia as informações incluídas (encapsuladas) no corpo da mensagem, evitando sua visualização. 
    - muito usado para formulários de contato, formulários de login, envio de arquivos, etc.

## 1.2 Tag fieldset

- pode ser usada para agrupar/hierarquizar um conjunto de dados que tenham algum tipo de relação entre si.
  - será inserida uma borda envolvendo seus elementos descendentes. 
- seu usonão é obrigatório.

## 1.3 Tag legend

- insere uma legenda para o elemento &lt;fieldset&gt;.
- funcionará como um identificador ao usuário, no momento de preenchimento dos dados.

## 1.4 Tag label

- insere um identificador para um respectivo campo do formulário, podendo ser uma palavra ou frase. 
- possui o **atributo for**, que permitirá criação de um vínculo entre o identificador e algum campo. 
  - se o usuário clicar neste identificador, o campo linkado ganhará foco automaticamente, melhorando a usabilidade do componente.
  - o atributo for deve possuir o mesmo valor que será atribuído ao id do campo.

## 1.5 Tag input

- responsável pela inserção da maioria dos componentes do formulário. 
- possui vários atributos, entre eles o `type` (que recebe como valor o tipo de campo que desejamos inserir no formulário).
- os navegadores possuem padrões diferentes para renderização desses componentes.
- possui as seguintes opções:

### 1.5.1 Text

- insere um campo de texto para digitação dos dados pelo usuário.
- nesse campo ele poderá digitar letras, números e caracteres especiais.
- é um dos componentes mais comuns nos formulários.

### 1.5.2 Password
- insere um campo para digitação de uma senha pelo usuário.
- poderá digitar letras, números e caracteres especiais.
- toda informação digitada será mascarada (caracteres digitados não poderão ser entendidos).

### 1.5.3 Date 

- insere um campo para digitação ou seleção de datas.
- assim que for clicado, aparecerá um calendário.

### 1.5.4 Time

- insere um campo para digitação ou seleção da hora e, assim que for clicado, aparecerá uma caixa para o usuário selecionar a hora e os minutos.

### 1.5.5 Datetime-local

- insere um campo para a digitação ou seleção da data e da hora (os dois campos anteriores abordados em apenas um).

### 1.5.6 Month

- insere um campo para a digitação ou seleção de um determinado mês e ano.

### 1.5.7 Week

- insere um campo para a digitação ou seleção de uma determinada semana do ano.

### 1.5.8 Email

- insere um campo para digitação de um endereço de email.
- é um campo do tipo text que consegue oferecer algumas vantagens:
  - tem validação própria, não permite que o formulário seja enviado caso o conteúdo digitado não seja um e-mail válido: deve possuir sinal de arroba (@) e ponto final (.).
  - smartphones reconhecem este campo e exibem o teclado já com a opção “.com” e o símbolo de arroba(@).

### 1.5.9 URL

- insere um campo para digitação de uma URL (endereço de um site).
- a exibição desse elemento é basicamente igual a de um campo “text”.

### 1.5.10 Search

- insere um campo de texto que poderá ser utilizado na implementação de um sistema de busca, o que só ocorrerá com a utilização de alguma linguagem de programação auxiliando o HTML. 
- a exibição desse elemento é basicamente igual a de um campo “text”.

### 1.5.11 Number

- insere um campo para a digitação de um número. 
- na parte final do campo, há setas para aumentar ou diminuir o valor digitado. 
- podemos definir os seguintes atributos para escalonar valores:
  - atributo min: define o menor valor do intervalo. Ex: min=“10” - irá iniciar o intervalo de valores no número 10.
  - atributo max: define o maior valor possível do intervalo. Ex: max=“100” - irá finalizar o intervalo de valores no número 100.
  - atributo step: define um intervalo de valores. Ex: step=“5” – exibirá os valores iniciando pelo menor valor definido, pulando de 5 em 5 até chegar ao valor máximo.

### 1.5.12 Range

- insere uma barra deslizante para receber um valor de um intervalo previamente determinado. 
- o intervalo padrão é de 0 a 100, podendo ser alterado conforme a necessidade.
- também aceita os atributos: min, max e step.

### 1.5.13 Tel

- insere um campo para a digitação do número de telefone. 
- a renderização será a mesmo de um campo “text”.

### 1.5.14 Color

- insere um campo que permitirá que o usuário selecione uma cor em uma paleta definida. 
- com a utilização de alguma linguagem de programação, podemos utilizar a cor selecionada em qualquer parte da página.

### 1.5.15 Radio

- insere campos de seleção, permitindo que o usuário a escolha uma única opção entre as apresentadas. 
- o usuário poderá mudar a seleção efetuada, mesmo assim ficará apenas com uma opção selecionada. 
- para que funcione de forma correta, usar o atributo name contendo o mesmo valor para todos os elementos inseridos.

### 1.5.16 Checkbox

- insere campos de seleção, permitindo que o usuário escolha quantas opções quiser.
- também poderá alterar as opções selecionadas quantas vezes forem necessárias.

### 1.5.17 File

- insere um campo que permite a seleção e o envio de arquivos. 
- composto por um botão e uma área onde o usuário pode selecionar o arquivo que deseja enviar.
- o envio só será concretizado com a utilização de alguma linguagem de programação.

## 1.6 Tag select / option

- a tag &lt;select&gt;&lt;/select&gt; cria um campo de seleção, no qual o usuário poderá selecionar uma das opções que serão listadas.
- as opções serão criadas pela tag &lt;option&gt;&lt;/option&gt;.
  - devem possuir o atributo value, recebendo algum valor que representa a opção selecionada pelo usuário.

## 1.7 Tag datalist
- tag &lt;datalist&gt;&lt;/datalist&gt; cria uma lista de opções que poderá ser associada ao elemento &lt;input&gt;, assim o usuário pode fazer uma busca entre as opções.
- atribuir o elemento id à tag &lt;datalist&gt;, e na tag &lt;input&gt; utilizaremos o atributo list recebendo o mesmo valor do id. 
- quando o usuário iniciar a digitação nesse campo, ele visualizará as opções que correspondem ao conteúdo digitado, como se estivesse sendo realizado um filtro de busca.

## 1.8 Tag textarea

- insere um campo de texto de múltiplas linhas. 
- muito usado para que os usuários escrevam alguma mensagem, comentário, sugestão etc.

## 1.9 Tag button

- insere um botão na página.
- o tipo de botão será definido no atributo type, que permite os valores:
  - **submit**: 
    - quando o botão for pressionado, o browser procurará o atributo action da tag &lt;form&gt;, e verificará para onde as informações deverão ser enviadas.
  - **reset**:
    - quando o botão for pressionado, todas as informações digitadas/selecionadas no formulário serão apagadas.
  - **button**:
    - quando clicado, pode executar uma função definida por uma linguagem de programação.
    - muito utilizado para chamar alguma funcionalidade que a página deve executar desenvolvida em Javascript.

## 1.10 Outros atributos para os campos (além do "type")

### 1.10.1 Required

- define que o campo deve ter o seu preenchimento obrigatório.
- caso o usuário tente enviar o formulário sem preencher este campo, uma mensagem será exibida e o envio só será feito após o seu preenchimento.

### 1.10.2 Value

- define o valor inicial que será atribuído ao campo.
- o Javascript usa esse atributo para recuperar o que foi selecionado ou digitado pelo usuário.

### 1.10.3 Readonly

- define que o valor do campo seja apenas de leitura, não permitindo alteração por parte do usuário.

### 1.10.4 Disabled

- define que campo fique desabilitado, não permitindo a inserção de dados.

### 1.10.5 Maxlength

- define a quantidade máxima de caracteres permitidos no campo.

### 1.10.6 Minlength

- define a quantidade mínima de caracteres que o campo deve possuir.

### 1.10.7 Autofocus

- define o campo que ganhará foco. 
- quando a página está sendo carregada, o browser localizará o campo que possuir esse atributo e automaticamente o cursor será posicionado nele. 
- ***usar esse atributo em apenas um campo!***

### 1.10.8 Placeholder

- define uma palavra ou frase que ficará visível dentro dos campos, permitindo sugerir como o usuário pode efetuar seu preenchimento.
- esse conteúdo ficará visível até que algo seja digitado. 
  - caso a informação digitada seja apagada, o valor inicial voltará a ser exibido no campo. 

### 1.10.9 Submit – Reset – Button

- o atributo type também pode ser usado para a inserção de botões, atribuindo os valores: submit, reset e button.
- esses valores possuem as mesmas funcionalidades e aparência da tag &lt;button&gt;.

## 1.11 Exemplo de formulário

> [HTML](./projetos/projeto8/pages/exemplo-de-formulario.html) e [CSS](./projetos/projeto8/css/exemplo-de-formulario.css).

---

## Laboratório Formulários: [HTML]() e [CSS]().