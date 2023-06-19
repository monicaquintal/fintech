<div id="fase03" align="center">
<h1>FASE 4 - VIEW</h1>
<h2>Capítulo 10: Tornando a interface com o usuário mais dinâmica. 🤖</h2>
</div>

<div align="center">
<h2>1. TORNANDO A INTERFACE COM O USUÁRIO MAIS DINÂMICA</h2>
</div>

`Javascript`:
- linguagem de programação criada em 1995 pela equipe do antigo navegador Netscape.
- foi desenvolvido inicialmente para dar mais dinamismo para as páginas Web
- podemos usá-lo para:
  - criar páginas mais dinâmicas.
  - criar aplicações Web.
  - criar aplicativos que possam se comunicar com algum servidor, com a utilização de Node.js.
  - desenvolver aplicativos móveis, usando React Native.
  - desenvolver aplicações para Arduíno e IOT.
  - desenvolver aplicações desktop com o framework Electron.
- o desenvolvimento front-end pode ser dividido em três camadas: 
  - camada de conteúdo: terá todos os elementos da página representados pelas tags HTML.
  - camada de apresentação: definirá como o conteúdo será exibido, sendo a CSS responsável por esta camada.
  - camada de comportamento: define como os elementos que compõem a página se comportarão, possibilitando um pouco mais de interação ao usuário. 
    - ***o Javascript será o responsável por essa camada!***

## 1.1 Observações sobre a linguagem

> Atualmente utiliza-se `ECMAScript` como especificação para a criação de código Javascript, sendo que a especificação [ECMA-262](https://www.ecma-international.org/publications-and-standards/standards/ecma-262/), possui toda a documentação da linguagem.

> Todo ano um projeto de especificação é lançado, e pode ser conferido [aqui](https://tc39.es/ecma262/).

`ATENÇÃO`:
<br>

- Javascript é uma ***linguagem case sensitive***!
- aceita o uso de aspas simples (' ') ou duplas (" "), sendo ***mais comum o uso de aspas simples***.
- o ***uso do sinal de ponto e vírgula (;), que indica a finalização da linha de comando, não é obrigatório***. 
- ***linguagem de alto nível e dinâmica*** (originalmente era apenas interpretada pelo browser).
- hoje podemos fazer uso do Node.js para que o Javascript seja executado diretamente no VS Code ou em algum servidor, dependendo do tipo de aplicação.
- ***linguagem fracamente tipada***, não é necessário definir o tipo de informação que será armazenada em uma variável (***tipagem dinâmica***).

## 1.2 Inserindo Javascript

- criar um arquivo distinto com a `extensão .js`.
- a separação em pastas é uma boa prática (pasta js).
- para realizar a chamada do arquivo:

~~~html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" 
  content="width=device-width, initial-scale=1.0">
  <title>Meu projeto Web</title>
</head>
<body>
  <!--Seu conteúdo HTML -->
  <!--Chamada do arquivo Javascript -->
  <script src="./js/app.js"></script>
</body>
</html>
~~~

## 1.3 Comentários em Javascript

### 1.3.1 Comentário de única linha

- inserir duas barras de datas ("//").
- o browser ignorará essas linhas e o conteúdo não será exibido no navegador.

~~~javascript
// Eu sou um comentário de única linha!
~~~

### 1.3.2 Comentário de múltiplas linhas

- utilizar os caracteres barra e asterisco ("/&#42;"), na linha inicial do comentário, e os caracteres asterisco e barra ("&#42;/") na linha final do comentário.

~~~javascript
/*
Oi,
eu sou um comentário de múltiplas linhas!
:)
*/
~~~

## 1.4 Console.log

- o browser é o responsável pela interpretação do código Javascript.
  - lerá linha por linha e efetuará a renderização das informações.
  - caso o código possua algum erro, essa renderização não ocorrerá e não será exibido na tela o que está dando errado.
- para verificar possíveis erros e outras informações, utilizar as ferramentas do desenvolvedor.
  - clique direito em qualquer parte da página, será aberto um menu suspenso e ali devemos ativar a opção Inspecionar. 
  - outra forma de acesso é pressionando a tecla F12.
- na `opção Console`, podemos:
  - utilizar para depuração do código.
  - exibir valores das variáveis.
  - visualizar o que foi interpretado pelo navegador.
  - identificar problemas.
  - verificarse o código está funcionando corretamente.
  - é possível também direcionar informações para serem exibidas ali, podendo testar alguma parte dos scripts para:
    - verificar a informação que estamos manipulando em alguma parte do script.
    - verificar o fluxo de programação.
    - verificar se o processamento está sendo realizado da forma correta.
    - exibir o conteúdo que foi buscado ou inserido na página HTML.

~~~javascript
console.log('Olá eu sou o console.');
console.log('Aqui você poderá verificar o que está acontecendo em sua página.');
~~~

## 1.5 Executando o Javascript no VS Code

- instalação do [`Node.js`](https://nodejs.org/).
  - plataforma de código aberto.
  - permite a execução de JavaScript no lado do servidor.
  - possibilita a criação de aplicações back-end, utilizando o ecossistema Javascript.
- acessar o Terminal do VS Code, clicar na opção New Terminal e digitar o `comando node -v`: será exibida a versão do Node.js instalada em sua máquina.

> Para executar o arquivo Javascript, digitar no terminal o `comando node seguido do nome do arquivo` (incluir a pasta em que está localizado).

## 1.6 Variáveis

- `variável`:
  - consiste em uma pequena parte da memória RAM que receberá um identificador (nome), e a ela será atribuído um valor que pode mudar no decorrer da execução do script.
  - um script pode ter múltiplas variáveis, desde que tenham nomes diferentes.

- para nomear as variáveis, devemos seguir alguns padrões:
  - o nome não pode ser iniciado com um número.
  - não é uma boa prática acentuar os nomes das variáveis.
  - é case sensitive.
  - padrão camelCase para definir nomes compostos. 
  - únicos caracteres especiais aceitos são o underline “_“ e o cifrão “$”.
  - por boa prática, os nomes devem ser auto-explicativos.

### 1.6.1 Declarando variáveis

- utilizar a `palavra-chave let` seguido do nome da variável e, caso desejado, atribuir um valor inicial.
  - a partir do Ecmascript 6, foi recomendado utilizar "let" em substituição ao "var" (boa prática).

~~~javascript
//declarando as variáveis
let userId = 4567;
let userName = 'usuarioJavascript';
let userLogged = true;
let userEmail;
//exibindo no console
console.log(userId);
console.log(userName);
console.log(userLogged);
console.log(userEmail);
~~~

- “undefined”: significa que nenhuma atribuição de valor foi feita à variável.

### 1.6.2 Declarando constantes

- utilizar a `palavra-chave const` para a declaração de constantes.
- funcionam como se fossem uma variável, só que o ***seu valor inicial nunca poderá ser alterado***.
- existe o padrão de ***declarar o nome usando apenas letras maiúsculas***.
  - quando o valor da constante é atribuído por alguma funcionalidade do script, declaramos o nome usando o padrão camelCase.

~~~javascript
// declarando constantes
const DATA_NASCIMENTO= '01/01/1995';
const CPF = '252.433.368-04';
const RG_SP = '29.365.924-6';
// exibindo no console
console.log(DATA_NASCIMENTO);
console.log(CPF);
console.log(RG_SP);
~~~

### 1.6.3 Tipos de dados

- quando uma variável é criada, automaticamente o JavaScript define o tipo de dados conforme a informação atribuída a essa variável (`tipagem automática`).
- há oito tipos de dados no Javascript:
  - Number: números inteiros e com casas decimais.
  - BigInt: o tipo de dado Number não pode armazenar números menores que -(2⁵³-1) ou maiores que (2⁵³-1), então para números gigantescos foi criado o BigInt.
  - String: cadeia de caracteres.
  - Boolean: representa um valor lógico, podendo receber apenas true (verdadeiro) e false (falso).
  - Undefined: representa um valor que ainda não foi definido (variável foi criada, mas não teve seu valor inicial declarado).
  - Null: valor nulo ou vazio que não pertence a nenhum tipo de dados citado anteriormente.
  - Object: representa um objeto, uma coleção de dados.
  - Symbol: usado para criar identificadores que serão usados exclusivamente pelos objetos.

> Para verificar qual tipo de dado o Javascript atribuiu às variáveis, podemos utilizar o `operador typeof`, que retornará o tipo atribuído.

~~~javascript
// declarando as variáveis
let userName = 'Clark Kent';
let userId = 12345;
let userEmail;
let userLogged = true;
//exibindo no console
console.log(userId, typeof userId); // 'number'
console.log(userName, typeof userName); // string
console.log(userLogged, typeof userLogged); // 'boolean'
console.log(userEmail, typeof userEmail); // undefined
~~~

### 1.6.4 Coerção de tipos

- considerando a tipagem dinâmica, tomar cuidado ao alterar os dados das variáveis: se passar algum valor que não seja do mesmo tipo anteriormente armazenado, o Javascript tentará arrumar executando automaticamente a `coerção implícita`.

~~~javascript
//declarando as variáveis
let userName = 'Clark Kent';
let userId = 12345;
//exibindo no console
console.log(userName, typeof userName);// string
console.log(userId, typeof userId);// number
//alterando os valores
userName = 56789;
userId = 'false';
console.log('---------------------');
//exibindo no console
console.log(userName, typeof userName);// number
console.log(userId, typeof userId);// string
~~~

- há também a `coerção explícita`, para conversão para algum tipo específico.
  - usar as funções: Number(), String() e Boolean().

~~~javascript
//declarando as variáveis
let initialValue = true;
console.log(initialValue, typeof(initialValue));// boolean
//convertendo para string
initialValue = String(initialValue);
console.log(initialValue, typeof(initialValue));// string
//--------------------------------
// convertendo para boolean
initialValue = Boolean(initialValue);
console.log(initialValue, typeof(initialValue));// boolean

let firstNumber = '12345';
console.log(firstNumber, typeof(firstNumber));// string
//--------------------------------
//convertendo para Number
firstNumber = Number(firstNumber);
console.log(firstNumber, typeof (firstNumber));// number
~~~

### 1.6.5 Escopo e diferenças entre var let e const

- `escopo de variável`:
  - representa o contexto em que uma variável é declarada e poderá ser usada.
- há dois tipos principais de escopo:
  - `global`: permite que seja usada em todo o código.
  - `local`: restringe o seu uso apenas ao bloco ou função onde foi declarada.
- quando declaramos uma ***variável var***, ela terá escopo global e de função; declarações feitas com ***let e com const***, possuem um escopo de bloco ou de função.
  - `VAR`:
    - a declaração feita com var permitirá que as variáveis tenham comportamento de `hoisting` (consiste em mover as variáveis e funções para o início do escopo onde foram declaradas, independente de onde estiverem no código).
    - variável é tratada como se tivesse sido definida sempre no início do escopo.
    - essa prática pode gerar erros.

~~~javascript
//exibindo as variáveis
console.log(userName);
console.log(userAge);
//declarando e atribuindo valores às variáveis
var userName = 'Clark Kent';// undefined
var userAge = 35;// undefined
~~~

  - `LET`:
    - declarações feitas com let e com const ***não têm hoisting***.
    - só estarão disponíveis para uso após as linhas onde foram declaradas, e caso tente usá-las antes da declaração, será gerado um erro na execução.

> Outra diferença está na possibilidade de redeclararmos variáveis que foram declaradas com uso do var. Quando usamos let ou const não podemos redeclarar a mesma variável ou constante.

~~~javascript
//declarando a variável
let userId = 12345;
console.log(userId);
//redeclarando a variável ---ERRO
let userId = 45678;// ERRO
console.log(userId);// ERRO
~~~

- quando usamos var ou let, podemos redefinir os valores quantas vezes quisermos, só não podemos fazer isso quando forem declaras como constantes.

<div align="center">

Palavra-chave| const | let | var
------------|--------|------|-------
Escopo Global | NÃO | NÃO | SIM
Escopo de Função | SIM | SIM | SIM
Escopo de Bloco | SIM | SIM | NÃO
Pode ser reatribuída | NÃO | SIM | SIM

</div>

## 1.7 Template String (ou Template Literal)