<div id="fase03" align="center">
<h1>FASE 4 - VIEW</h1>
<h2>Capítulo 10: Tornando a interface com o usuário mais dinâmica. 🤖</h2>
</div>

[Mais Javascript aqui!](https://github.com/monicaquintal/estudandoJavaScript) 🚀

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

- permite definir como ficarão as strings, inserindo variáveis, expressões, funções e métodos, sem a necessidade de concatenar. 
- permite a criação de strings mais complexas que contenham elementos dinâmicos.
- `para criar uma Template String`:
  - iniciar e finalizar com crase (`), em substituição a aspas. 
  - é possível fazer o uso dos placeholders em seu interior, que representam uma variável, cálculo, função, etc. 
  - os elementos devem ser precedidos do sinal de cifrão $ e da abertura e fechamento de chaves ${...}.
- exemplo:

~~~javascript
let userId = 12345;
let userName = 'Clark Kent';
//Exibindo no console com template string
console.log(`Id do usuário: ${userId}`);
console.log(`Nome do usuário: ${userName}`);
~~~

## 1.8 Caixas de diálogo

- há três caixas de diálogo, que podem ser usadas para permitir alguma interação com o usuário. 

### 1.8.1 Alert()

- o `método alert()` abre uma caixa de diálogo modal que exibe alguma mensagem.
- a caixa ficará aberta enquanto o usuário não der um clique no botão do OK da modal.
- pode receber uma string como argumento, que será a mensagem visualizada pelo usuário.

~~~javascript
//criando a variável
let userName = 'Clark Kent';
//chamando o método alert()
alert(`Olá ${userName}, seja bem-vindo!!!`);
~~~

### 1.8.2 Confirm()

- o `método confirm()` abre uma caixa de diálogo modal que exibe alguma mensagem para o usuário em conjunto com os **botões de OK e Cancelar**. 
- quando o usuário clicar em um dos botões, será retornado um valor booleano:
  - true, caso clique no botão OK.
  - false, caso clique no botão Cancelar.

~~~javascript
//criando a variável
let userName = 'Clark Kent';
//chamando o método confirm()
confirm(`${userName}, deseja finalizar a aplicação?`);
~~~

### 1.8.3 Prompt()

- o `método prompt()` abre uma caixa de diálogo modal, que **solicita ao usuário a entrada de algum conteúdo**.
- pode receber dois argumentos opcionais: 
  - título da modal.
  - valor para o campo de texto.
- quando o usuário digitar o conteúdo, ele será armazenado como uma string.

~~~javascript
//criando a variável
let userName = 'Clark Kent';
//chamando o método prompt()
prompt(`${userName}, digite a sua data de nascimento:`);
~~~

## 1.9 Operadores

### 1.9.1 Operadores aritméticos

- realizam a maioria dos cálculos matemáticos entre dois ou mais valores que podem estar armazenados em variáveis ou que serão atribuídos ao script.
- operadores:

<div align="center">

Operador | Sinal | Definição
---------|--------|------------
Soma | + | Executa a soma entre dois ou mais números
Subtração | - | Executa a subtração entre dois ou mais números
Multiplicação | * | Executa a multiplicação entre dois ou mais números
Divisão | / | Executa a divisão entre dois ou mais números
Módulo | % | Consiste na divisão entre dois números, retornando o resto obtido nessa divisão
Potência | ** | Executa o cálculo da potência entre dois números, elevando o primeiro número à potência do segundo número

</div>

- exemplos:

~~~javascript
//criando variáveis
const firstValue = 50;
const secondValue = 10;
let result = 0; 
// soma
result = (firstValue + secondValue);
console.log(`${firstValue} + ${secondValue} = ${result}`);
//subtração
result = (firstValue -secondValue);
console.log(`${firstValue} -${secondValue} = ${result}`);
// multiplicação
result = (firstValue * secondValue);
console.log(`${firstValue} * ${secondValue} = ${result}`);
// divisão
result = (firstValue / secondValue);
console.log(`${firstValue} / ${secondValue} = ${result}`);
// módulo
result = (firstValue % secondValue);
console.log(`${firstValue} % ${secondValue} = ${result}`);
// potência
result = (firstValue ** secondValue);
console.log(`${firstValue} ** ${secondValue} = ${result}`);
~~~

### 1.9.2 Operadores relacionais

- permitem a comparação entre dois ou mais valores, retornando apenas true (verdadeiro) ou false (falso).

<div align="center">

Operador | Sinal | Definição
---------|------|----------
Maior que | > | Retornará verdadeiro quando o primeiro valor for maior que o segundo valor.
Menor que | < | Retornará verdadeiro quando o primeiro valor for menor que o segundo valor.
Maior ou igual a | >= | Retornará verdadeiro quando o primeiro valor for maior ou igual ao segundo valor.
Menor ou igual a | <= | Retornará verdadeiro quando o primeiro valor for menor ou igual ao segundo valor.
Igual a | == | Retornará verdadeiro quando os dois valores forem iguais.
Diferente de | != | Retornará verdadeiro quando os dois valores forem diferentes.
Estritamente igual a | === | Retornará verdadeiro quando os dois valores forem iguais e do mesmo tipo.
Estritamente diferente a | !== | Retornará verdadeiro quando os dois valores não forem iguais ou não forem do mesmo tipo.

</div>

- exemplos:

~~~javascript
//criando variáveis
let firstValue = 50;
let secondValue = 50;
let result;
// maior que
result = (firstValue > secondValue);
console.log(`${firstValue} > ${secondValue} = ${result}`);// false
//menor que
result = (firstValue < secondValue);
console.log(`${firstValue} < ${secondValue} = ${result}`);// false
// maior ou igual a
result = (firstValue >= secondValue);
console.log(`${firstValue} >= ${secondValue} = ${result}`);// true
// menor ou igual a
result = (firstValue <= secondValue);
console.log(`${firstValue} <= ${secondValue} = ${result}`);// true
// igual a
result = (firstValue == secondValue);
console.log(`${firstValue} == ${secondValue} = ${result}`);// true
// diferente de
result = (firstValue != secondValue);
console.log(`${firstValue} != ${secondValue} = ${result}`);// false
// convertendo o segundo valor em uma string
secondValue = '50';
// estritamente igual a
result = (firstValue === secondValue);
console.log(`${firstValue} === ${secondValue} = ${result}`);// false
// estritamente diferente de
result = (firstValue !== secondValue);
console.log(`${firstValue} !== ${secondValue} = ${result}`);// true
~~~

### 1.9.3 Operadores lógicos

- permitem a criação de expressões através da união entre expressões relacionais. 
- esses operadores retornam apenas true (verdadeiro) ou false (falso).

<div align="center">

Operador | Sinal | Definição
---------|-------|----------
E | && | Para retornar verdadeiro, todas as expressões devem ser verdadeiras.
OU | &#124;&#124; | Para retorna verdadeiro, basta apenas uma expressão ser verdadeira.
NÃO | ! | Inverte o resultado da expressão: se o resultado for verdadeiro retornará falso, se o resultado for falso retornará verdadeiro.

</div>

- exemplos:

~~~javascript
//criando variáveis
let firstValue = 50;
let secondValue = 10;
let result;
// Operador OU
result = (firstValue === secondValue) || (firstValue >= secondValue);
console.log(`O resultado da expressão é: ${result}`);// true
// Operador E
result = (firstValue === secondValue) && (firstValue >= secondValue);
console.log(`O resultado da expressão é: ${result}`);// false
// Operador Não
result = !((firstValue === secondValue) && (firstValue >= secondValue));
console.log(`O resultado da expressão é: ${result}`);// true
~~~

### 1.9.4 Operadores de incremento e decremento

- somam ou subtraem 1 do valor atribuído a alguma variável.

<div align="center">

Operador | Sinal | Definição
---------|---------|---------
Incremento | ++ | Adiciona 1 ao valor da variável.
Decremento | -- | Subtrai 1 do valor da variável.

</div>

- é possível criar operações de duas formas diferentes:

<div align="center">

Operação | Sinal | Definição
----------|-----|-------------
Pré-fixada | ++ variável<br>--variável | O valor da variável é incrementado ou decrementado antes de ser usado em uma expressão.
Pós-fixada | variável++<br>variável-- | O valor da variável é incrementado ou decrementado após ser usado em uma expressão.

</div>

- exemplos:

~~~javascript
//criando variáveis
let value1 = 50;
let value2 = 30;
let total = 0;
console.log(`Valor 1 = ${value1}`);
console.log(`Valor 2 = ${value2}`);
console.log('--------------------------');
//aplicando os operadores
value1++;
value2--;
console.log(`Novo Valor 1 = ${value1}`);// 51
console.log(`Novo Valor 2 = ${value2}`);// 29
console.log('--------------------------');
//operação pré-fixada
console.log(`Operação pré-fixada`);
value1 = 50;
total = ++value1 + 50;
console.log(`Valor total = ${total}`);// 101
console.log(`Novo Valor 1 = ${value1}`);// 51
console.log('--------------------------');
//operação pós-fixada
console.log(`Operação pós-fixada`);
value1 = 50;
total = value1++ + 50;
console.log(`Valor total = ${total}`);// 100
console.log(`Novo Valor 1 = ${value1}`);// 51
console.log('--------------------------');
~~~

### 1.9.5 Operadores de atribuição

- permitem que algum valor seja atribuído a alguma variável.
- opções:

<div align="center">

Operador | Sinal | Definição
---------|-------|-----------
Atribuição | = | Atribui um valor a uma variável.
Atribuição de adição | += | Atribui um valor efetuando uma soma.
Atribuição de subtração | -= | Atribui um valor efetuando uma subtração.
Atribuição de multiplicação | *= | Atribui um valor efetuando uma multiplicação.
Atribuição de divisão | /= | Atribui um valor efetuando uma divisão.
Atribuição de resto | %= | Atribui um valor efetuando um módulo.
Atribuição de exponencial | **= | Atribui um valor efetuando uma potenciação.

</div>

- exemplos:

~~~javascript
//criando variáveis
let value = 50;
console.log(`Valor = ${value}`);// 50
//aplicando operadores
Value+=10;
console.log(`Novo valor = ${value}`);// 60
value -= 10;
console.log(`Novo valor = ${value}`);// 50
value *= 10;
console.log(`Novo valor = ${value}`);// 500
value /= 10;
console.log(`Novo valor = ${value}`);// 50
value **= 10;
console.log(`Novo valor = ${value}`);// 97656250000000000
value %=10;
console.log(`Novo valor = ${value}`)// 0
~~~

## 1.10 Objeto Math

- o [`método math`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math) permite a realização de qualquer operação aritmética.
- possui uma série de métodos e propriedades que auxiliam em tarefas que envolvem cálculos.

<div align="center">

Método | O que faz
-------|----------
Math.ceil() | Retorna o próximo número inteiro.
Math.floor() | Retorna o número inteiro anterior.
Math.round() | Retorna o número inteiro mais próximo, para isso ele verifica:<br>Parte decimal do número maior ou igual a 49, retornará o número inteiro anterior.<br>Parte decimal do número maior ou igual a 50, retornará o próximo número inteiro.
Math.max() | Retorna o maior valor encontrado no intervalo.
Math.min() | Retorna o menor valor encontrado no intervalo.
Math.pow() | Retorna a potência de um número. 
Math.random() | Retorna um número aleatório entre 0 e 1.
Math.sqrt() | Retorna a raiz quadrada de um número.
Math.cbrt() | Retorna a raiz cúbica de um número.

</div>

- exemplos:

~~~javascript
const numero = 50.79;
//Math.ceil()
console.log(`Número retornado: ${Math.ceil(numero)}`);// 51
//Math.floor()
console.log(`Número retornado: ${Math.floor(numero)}`);// 50
//Math.round()
console.log(`Número retornado: ${Math.round(25.34)}`);// 25
console.log(`Número retornado: ${Math.round(25.84)}`);// 26
//Math.max()
console.log(`Número retornado:${Math.max(13,45,23,89,12,11,2)}`);// 89
//Math.min()
console.log(`Número retornado:${Math.min(13,45,23,89,12,11,2)}`);// 2
//Math.pow()
console.log(`Número retornado: ${Math.pow(2,10)}`);// 1024
//Math.random()
console.log(`Número retornado: ${Math.random()}`);// 0.5484...
// Math.sqrt()
console.log(`Número retornado: ${Math.sqrt(81)}`);// 9
//Math.cbrt()
console.log(`Número retornado: ${Math.cbrt(27)}`);// 3
~~~

## 1.10.1 Sorteando um número qualquer

- o uso do `método Math.random()` permite o sorteio de um valor aleatório entre 0 e 1.
- para sortear um número inteiro qualquer, seguir os passos:
  - multiplicar o número que será obtido por 100.
    - qualquer número decimal multiplicado por 100 fará com que o ponto flutuante desse número, avance duas casas decimais para a direita. 
  - utilizar o método Math.floor() para retornar o número inteiro anterior.

~~~javascript
//criando as variáveis e sorteando os números
const numero1 = Math.floor(Math.random() * 100);const numero2 = Math.floor(Math.random() * 100);const numero3 = Math.floor(Math.random() * 100);
//exibindo os números sorteados
console.log(`Número sorteado: ${numero1}`);// 56
console.log(`Número sorteado: ${numero2}`);// 94
console.log(`Número sorteado: ${numero3}`);// 22
~~~

## 1.11 Objeto String

- representa uma cadeia de caracteres que poderá ser manipulada através de uma série de métodos. 
- podemos também acessar individualmente os caracteres que formam a string, usando os índices (assim como é feito nos arrays).
  - o primeiro caracter da string está no índice 0.

<div align="center">

Método | O que faz
-------|---------
Propriedade length | Retorna o número de caracteres existente na string.
toUpperCase() | Retorna toda a string em letras maiúsculas.
toLowerCase() | Retorna toda a string em letras minúsculas.
charAt() | Retorna o caractere que está posicionado no índice declarado.
indexOf() | Retorna o índice da primeira ocorrência de uma substring declarada. Caso não encontre nada retornará -1.
lastIndexOf() | Retorna o índice da última ocorrência de uma substring declarada. Caso não encontre nada retornará -1.
concat() | Concatena duas ou mais strings.
replace() | Substitui a primeira substring encontrada por outra.
replaceAll() | Substitui todas as substrings encontradas por outra.
substring() | Retorna uma parte da substring. Devemos definir o índice inicial e final.
slice() | Extrai uma parte da string retornando uma nova string.
split() | Converte uma string em um array.
trim() | Remove espaços em branco existentes no início e no fimda string. Bem útil para a manipulação de dados em formulários.
includes() | Verifica se uma string existe em outra string, retornando apenas true ou false.
startsWith() | Verifica se a string começa com o prefixo especificado, retornando apenas true ou false.
endsWith() | Verificase a string termina com o sufixo especificado, retornando apenas true ou false.

</div>

- exemplos:

~~~javascript
const minhaString = 'Javascript é uma linguagem de programação poderosa!';
console.log(minhaString);// Javascript é uma linguagem de programação poderosa!
//propriedade length
console.log(`Tamanho da string: ${minhaString.length}`);// 51
//toUpperCase()
console.log(`Letras maiúsculas: ${minhaString.toUpperCase()}`);// JAVASCRIPT É UMA LINGUAGEM DE PROGRAMAÇÃO PODEROSA!
//toLowerCase()
console.log(`Letras minúsculas: ${minhaString.toLowerCase()}`);// javascript é uma linguagem de programação poderosa!
//charAt()
console.log(`Caracter retornado: ${minhaString.charAt(15)}`);// a
//indexOf()
console.log(`Caracter encontrado no índice:${minhaString.indexOf('s')}`);// 4
//lastIndexOf()
console.log(`Caracter encontrado no índice:${minhaString.lastIndexOf('s')}`);// 48
//concat()
console.log(`Concatenado strings:${'abc'.concat('def').concat('xyz')}`);// abcdefxyz
//replace()
console.log(`Substituindo a primeira letra a:${minhaString.replace('a','@')}`);// J@vascript é uma linguagem de programação poderosa!
//replaceAll()
console.log(`Substituindo todas as letras a:${minhaString.replaceAll('a', '@')}`);// J@v@script é um@ lingu@gem de progr@m@ção poderos@!
//substring()
console.log(`Pegando uma parte da string:${minhaString.substring(4,15)}`);// script é um
//slice()
let novaString = minhaString.slice(11,38);
console.log(`Nova string gerada: ${novaString}`);// é uma linguagem de programa
//split()
console.log(`Convertendo array em string:${minhaString.split('')}`);// J,a,v,a,s,c,r,i,p,t, ,é, ,u,m,a, ,l,i,n,g,u,a,g,e,m, ,d,e, ,p,r,o,g,r,a,m,a,ç,ã,o, ,p,o,d,e,r,o,s,a,!
//trim()
console.log(`Removendo espaços no início e fim:${minhaString.trim()}`);// Javascript é uma linguagem de programação poderosa!
//includes()
console.log(`Verificando se existe na string:${minhaString.includes('ava')}`);// true
//includes()
console.log(`Verificando se começa com a string:${minhaString.startsWith('Java')}`);// true
//includes()
console.log(`Verificando se termina com a string:${minhaString.endsWith('rosa!')}`);// true
~~~

## 1.12 Objeto Date

- possui métodos que permitem a manipulação de datas e horas.
- para isso, estanciar o objeto utilizando o método construtor, que retornará a data e hora atual.

~~~javascript
//utilizando o método construtor
const dataAtual = new Date();
//exibindo o objeto
console.log(`Data atual: ${dataAtual}`);
~~~

