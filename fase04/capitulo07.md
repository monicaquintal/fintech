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

pág 22