<div id="fase03" align="center">
<h1>FASE 4 - VIEW</h1>
<h2>Capítulo 11: Javascript Essencial. 💻</h2>
</div>

[Mais Javascript aqui!](https://github.com/monicaquintal/estudandoJavaScript) 🚀

<div align="center">
<h2>1. JAVASCRIPT - ESSENCIAL</h2>
</div>

## 1.1 Funções

- são blocos de comandos.
- permitem a execução de um conjunto de ações previamente definidas.
- possuem em seu interior algum código que será executado, podendo ser reaproveitado quantas vezes quiser. 
- o código existente na função não poderá ser acessado por ninguém que estiver fora dela.
- podem receber **parâmetros**: valores que serão enviados para dentro delas, e utilizados em seu processamento.
- funções também podem ser usadas como valores, passadas como argumentos para outras funções e retornadas como resultados de outras (parte fundamental do paradigma de programação funcional).

## 1.2 Criando funções

### 1.2.1 Function Declaration

- forma mais comum de declarar uma função em Javascript.
- utilizada a `palavra-chave function` seguida do nome da função. 
- nesse tipo de declaração, ocorre o ***function hoisting***: assim que a função for declarada, será elevada para o topo do código, procedimento comum às variáveis declaradas com var.

- sintaxe:
~~~javascript
function nomeFuncao (parâmetro1, parâmetro2,...) {
  //corpo da função
}
//chamando a função
nomeFuncao(paramêtro1, parâmetro2,...);
~~~

- o nome da função deve seguir o mesmo padrão da declaração de variáveis.
- é recomendável definir um nome que tenha relação com o que a função executará. 

- exemplo: “Somando números” - criada a função somarNumeros(), que irá sortear e exibir no console,cinco números entre 0 e 100. Também somará esses números, exibindo o total. Realizada a chamada duas vezes.

~~~javascript
//criando a função
function somarNumeros() {
  let numeros;
  let total = 0;
  /* o escopo dessas variáveos é apenas a própria função 
  (se tentar utilizá-las fora da função, um erro será gerado) */
  for (let i = 0; i <= 4; i++) {
    numeros = Math.floor(Math.random() * 101);
    console.log(`Número sorteado: ${numeros}`);
    total += numeros;
  }
  console.log(`Total da somatória: ${total}`);
  console.log(`----------------------------`);
} //fim da função
//chamando a função
somarNumeros();
somarNumeros();
~~~

### 1.2.2 Passagem de parâmetros

- osparâmetros devem ser declarados no momento da criação da função.
- cada vez que chamar a função, poderá passar um novo valor que será utilizado por ela (chamado de argumento).
- é possível definir um valor inicial para os parâmetros, basta fazer a atribuição de valores junto à declaração dos parâmetros.
  - serão utilizados caso a função seja chamada sem a passagem dos argumentos.

~~~javascript
//criando a função com um parâmetro
function calcularTabuada (numero = 0) {
  console.log(`Fazendo a tabuada do ${numero}:`);
  for (let i = 0; i <= 10; i++) {
    console.log(`${numero} * ${i} = ${numero*i}`);
  }
  console.log(`-----Fim da Tabuada----`);
} //fim da função
//chamando a função e passando um argumento
calcularTabuada(8); // tabuada do 8
~~~

### 1.2.3 Retornando valores

- a`palavra-chave return` permite criar funções que efetuam o processamento e retornam o resultado obtido. 
- exemplo: função que recebe um valor em Reais e a cotação do dólar; a função fará a conversão das moedas e retornará para a variável, que fez a sua chamada, o valor obtido:

~~~javascript
console.log(`Função de conversão em Dólar`);
// criando a função
function conversaoDolar (valorReal, cotacao) {
  return (valorReal / cotacao);
}
// sorteando um valor para Reais
const valorReal = Math.floor(Math.random()*1000);
const cotacaoDolar = 5.23;
// criando a variável e chamando a função
const cotacaoDia = conversaoDolar(valorReal,cotacaoDolar);
//exibindo as informações no console
console.log(`Valor em Real = ${valorReal.toFixed(2)}`);
console.log(`Cotação Dólar = ${cotacaoDolar}`);
console.log(`Valor final em Dólar = ${cotacaoDia.toFixed(2)}`);
~~~

### 1.2.4 Function Expression

- consiste na declaração de uma função diretamente em uma variável ou uma propriedade de um objeto. 
- essas funções não possuem nome (função anônima)e poderão ser utilizadas como argumentos para outras funções.
- sintaxe:

~~~javascript
const nomeVariavel = function() {
  //corpo da função
}
~~~

- exemplo: declaração de uma variável que receberá uma função com quatro parâmetros - as notas de um aluno. A função deve retornar sua média. Quando utilizar essa variável, passar os argumentos necessários para o cálculo da média.

~~~javascript
console.log(`Função de cálculo de média`);
//criando a função
const media = function (n1, n2, n3, n4) {
  const media = (n1+n2+n3+n4) / 4;
  return media.toFixed(1);
}
//chamando a função
console.log(`Média do aluno 1 = ${media(8,9,7,9)}`);
console.log(`Média do aluno 2 = ${media(10,8,9,10)}`);
console.log(`Média do aluno 3 = ${media(8,8,8,10)}`);
~~~

### 1.2.5 Arrow Function

- consiste na declaração de uma Function Expression de uma maneira mais resumida. 
- para isso:
  - criar uma variável.
  - sinal de atribuição (=).
  - abertura e fechamanto dos parênteses () para receber parâmetros, caso necessário.
  - inserir o sinal de igual (=), seguido do sinal de maior (>): **representam a arrow function**.
  - abrir e fechar as chaves {} parao corpo da função.
- sintaxe:

~~~javascript
const nomeVariavel = (parâmetro1, parâmetro2) => {
  //corpo da função
  return...
}
~~~

- exemplo: declarar uma variável que receberá uma Arrow Function, que sorteará uma senha de 20 caracteres. Usar uma string que receberá os caracteres, e um loop que sorteará vinte vezes um número que corresponde à posição do caracter nessa string. O caracter será atribuído a uma variável, formando assim a senha. Após o término do loop, a função retornará a senha gerada.

~~~javascript
//declarando a variável e criando a função
const gerarSenha = () => { 
  const caracteres ='ABCDEFGHIJKLMNOPQRSUVWXYZabcdefghijklmnopqrsuvwxyz1234567890!@#$%&*';
  let novaSenha = '';
  for (let i = 0; i <= 19; i++) { 
    const indice = Math.round(Math.random() * caracteres.length);
    novaSenha += caracteres[indice];
  }
  return novaSenha;
}
//chamando a função atribuída à variável
console.log(`A senha gerada foi: ${gerarSenha()}`);
console.log(`A senha gerada foi: ${gerarSenha()}`);
console.log(`A senha gerada foi: ${gerarSenha()}`);
~~~

### 1.2.6 Callback Function

- no JS, funções são objetos, e por isso podem receber outras funções como argumentos.
- quando uma função é passada como argumento, é chamada de callback function, e é executada quando a função principal for concluída. 
- normalmente utilizada para executar algum processo assim que alguma execução assíncrona for finalizada, podendo também ser utilizada em execuções síncronas. 
  - **operações síncronas:** aquelas que ocorrem em sequência, uma após a outra, bloqueando o fluxo de execução do script até que a operação principal seja finalizada.
  - **operações assíncronas:** ocorrem em segundo plano, sem bloquear o fluxo de execução do script. Muito útil quando temos funcionalidades que podem levar algum tempo para serem concluídas, como ler uma base de dados.

~~~javascript
function mensagem1() {
  console.log(`Exibindo a mensagem 1`)
}
function mensagem2() {
  console.log(`Exibindo a mensagem 2`)
} 
function mensagem3() {
  console.log(`Exibindo a mensagem 3`)
}
// console.log('');
console.log(`-----Fluxo normal-----`);
mensagem1();
mensagem2();
mensagem3();
console.log('');

console.log(`-----Usando o callback-----`);
mensagem1();
//definindo o método setTimeout para função mensagem2()
setTimeout(mensagem2, 1000);
mensagem3();
~~~

- no exemplo, é usado o `método setTimeout()`, que permite a execução de um bloco de código depois de um intervalo de tempo definido em milisegundos. Esse método é assíncrono, o fluxo de execução do script não é bloqueado enquanto aguardamos o término da execução do código.
- podemos também passar uma função como argumento.
  - no código abaixo, “Cálculos com callback()”, há uma função que calcula a somatória entre três valores, e outra que faz a média entre eles. Temos também a função calcular(), que receberá como parâmetros “x”, “y” e “z”, um para cada valor, além do parâmetro “cb” que receberá o nome da função para efetuar o cálculo desejado.

~~~javascript
const somar = (x, y, z) => {
  return (x + y + z);
};
const media = (x, y, z) => {
  return (x + y + z) / 3;
} 
const calcular = (x, y, z, cb) => {
  return cb (x, y, z);
} 
console.log(`Chamando o callback para realizar os cálculos:`);
console.log(`Valores: 10, 20, 30`);
console.log(`Calculando a soma: ${calcular(10, 20, 30, somar)}`);
console.log(`Calculando a média: ${calcular(10, 20, 30, media)}`);
~~~

### 1.2.7 Funções imediatas IIFE (Immediately-invoked function expression)

- permite a execução da função imediatamente após a sua criação. 
- em JS as variáveis têm como escopo a função, ou bloco onde foram declaradas. Ao usarmos uma IIFE, "fechamos o escopo" e damos mais segurança ao código, pois tanto as variáveis como as funções não serão reutilizadas indevidamente em outro lugar.

~~~javascript
const calcularValores = (valor1, valor2) => {
  console.log(`Resultado da Soma: ${valor1 + valor2}`);
  console.log(`Resultado da Multiplicação: ${valor1 * valor2}`);
}
calcularValores(20, 10);
~~~

- a função acima está disponível para qualquer pessoa que acessar a sua página. Podemos usar uma função IIFE para resolver esse problema, já que são úteis para criar escopos privados, ocultando as variáveis ou funções do escopo global:

~~~javascript
(() => {
  const calcularValores = (valor1, valor2) => {
    console.log(`Resultado da Soma: ${valor1 + valor2}`);
    console.log(`Resultado da Multiplicação: ${valor1 * valor2}`);
    console.log(`Sem escopo global – não são acessadas`);
}
calcularValores(30, 30);
})();
~~~

- para utilização de IIFE, realizar:
  - abertura de parênteses.
  - declaração da função, nesse caso uma Arrow Function.
  - abertura de chaves.
  - bloco de comandos.
  - fechamento de chaves e dos parênteses.
  - abertura e fechamento de parênteses, para execução automática da função.
- se tentarmos chamar a função diretamente no browser, será devolvida uma mensagem de erro dizendo que ela não foi definida, ou seja, o seu escopo está fechado!
- **observação:**
  - outra forma, sem usar IIFE, é criar uma função inicial que envolverá todo o código, assim o escopo será a própria função. 
  - não esquecer de fazer a chamada dessa função para executá-la.

~~~javascript
function init() {
  console.log(`Usando uma função inicial`);
  const calcularValores = (valor1, valor2) => {
    console.log(`Resultado da Soma: ${valor1 + valor2}`);
    console.log(`Resultado da Multiplicação: ${valor1 * valor2}`);
  }
  calcularValores(20, 10);
}
init();
~~~

## 1.3 Arrays

- são estruturas de dados que podem receber vários valores simultaneamente, inclusive de tipos diferentes.
- os valores que o compõem ficarão dentro de índices, que poderão ser totalmente acessados e manipulados.
- para declarar um array, há duas opções:
  - criar uma variável e atribuir a ela o método construtor Array().
  - criar uma variável, seguida da abertura e fechamento de colchetes [].

~~~javascript
//usando o método construtor
const xMen = new Array ('Ciclope', 'Wolverine', 'Fênix', 'Fera', 'Vampira');
//usando a declaração literal
const vingadores = ['Homem de Ferro', 'Capitão América', 'Thor', 'Valquíria', 'Capitã Marvel'];
//exibindo os array
console.log(xMen);
console.log(vingadores);
~~~

- ***o índice inicial sempre será “0”***. 
- no final da exibição de conteúdo, há a quantidade de elementos existente no array, obtido pela ***propriedade length***.

### 1.3.1 Manipulando arrays

<div align="center">

Método | O que faz
-------|-----------
Propriedade length | Retorna a quantidade de itens existentes no array.
unsfhit() | Insere um novo conteúdo no primeiro índice do array.
push() | Insere um novo conteúdo no último índice do array.
shift() | Remove o primeiro índice do array.
pop() | Remove o último índice do array.
splice() | Exclui e/ou insere elementos em um array partindo de um índice definido.
slice() | Copia elementos de um array para outro. Você deve indicar o índice inicial e o final. Não altera o array original.
indexOf() | Retorna o índice da primeira ocorrência de um elemento procurado no array.Retornará -1 se nada for encontrado.
lastIndexOf() | Retorna o índice da última ocorrência de um elemento procurado no array.Retornará -1 se nada for encontrado.
concat() | Permite que dois ou mais arrays sejam concatenados, gerando assim um novo array.
sort() | Organizar os conteúdos do array, colocando-os em ordem alfabética ou numérica.
reverse() | Inverte os índices de um array.
join() | Retorna uma string com os conteúdos de um array. É possível também definir um separador para cada conteúdo.
includes() | Verifica se um determinado elemento está presente em um array. Retornará true ou false.
every() | Verifica se todos os elementos do array satisfazem uma mesma condição. Retornará true ou false.
some() | Executa um teste lógico verificando se pelo mesmo um conteúdo do array satisfaz a condição definida. Ele retornará true ou false.
find() | Executa um teste lógico e retornará o valor do primeiro elemento que satisfaça a condição definida.
filter() | Executa um teste lógico, retornando um novo array com os valores que satisfação a condição definida.
map() | Aplica uma função a cada elemento de um array, e retorna um novo array com os resultados obtidos.
reduce() | Aplica uma função a cada elemento de um array, e retorna apenas um único valor.

</div>

1. Propriedade length:

~~~javascript
const vingadores = ['Homem de Ferro', 'Capitão América', 'Thor', 'Valquíria', 'Capitã Marvel'];
const xMen = new Array('Ciclope', 'Wolverine', 'Fênix', 'Fera', 'Vampira');
console.log(`Array Vingadores`);
console.log(vingadores);
console.log(`Total de heróis no array: ${vingadores.length}`);
console.log(`Array Xmen`);
console.log(xMen);
console.log(`Total de heróis no array: ${xMen.length}`);
~~~

2. Métodos unshift() – push() – shift() – pop():

~~~javascript
const vingadores = ['Homem de Ferro', 'Capitão América', 'Thor', 'Valquíria', 'Capitã Marvel'];
console.log(`Array original: `);
//exibindo o array
console.log(vingadores);
//inserindo no primeiro índice
vingadores.unshift('Gavião Arqueiro');
//inserindo no último índice
vingadores.push('Viúva Negra');
//exibindo o array com os novos heróis
console.log(`Novos hérois inseridos: `);
console.log(vingadores);
//excluindo o primeiro índice
vingadores.shift();
//excluindo o último índice
vingadores.pop();
//exibindo o array sem os novos heróis
console.log(`Novos hérois excluídos:`);
console.log(vingadores);
~~~ 

3. Métodos splice() – slice():

~~~javascript
const vingadores = ['Homem de Ferro', 'Capitão América', 'Thor', 'Valquíria', 'Capitã Marvel'];
console.log(`Array original:`);
//exibindo o array
console.log(vingadores);
//excluindo dois elementos do array a partir do índice 2
vingadores.splice(2,2);
//exibindo o array com os heróis excluídos
console.log(`Array com os hérois excluídos:`);
console.log(vingadores);
//inserindo dois elementos do array a partir do índice 2
vingadores.splice(2, 0, 'Thor', 'Valquíria');
//exibindo o array com os heróis novamente inseridos
console.log(`Array com os hérois novamente inseridos`);
console.log(vingadores);
//copiando uma parte do array vingadores para o novo Array
const novoArray = vingadores.slice(1,4);
console.log(`Novo array com alguns heróis copiados`);
console.log(novoArray);
~~~

4. Métodos indexOf() – lastIndexOf():

~~~javascript
const vingadores = ['Homem de Ferro', 'Capitão América', 'Thor', 'Valquíria', 'CapitãMarvel'];
console.log(`Array original`);
console.log(vingadores);
//procurando pelo Capitão América
let indice = vingadores.indexOf('Capitão América');
console.log(`O Capitão América está no índice ${indice} do array`);
//procurando pela Capitã Marvel
indice = vingadores.lastIndexOf('Capitã Marvel');
console.log(`A Capitã Marvel está no índice ${indice} do array`);
~~~

5. Método concat():

~~~javascript
const vingadores = ['Homem de Ferro', 'Capitão América', 'Thor', 'Valquíria', 'Capitã Marvel'];
const xMen = ['Ciclope', 'Wolverine', 'Fênix', 'Fera', 'Vampira'];
console.log(`Arrays originais`);
console.log(vingadores);
console.log(xMen);
//gerando novo array
const todosHerois = vingadores.concat(xMen);
//exibindo o novo array
console.log(`Novo array de heróis`);
console.log(todosHerois);
~~~

6. Métodos sort() – reverse():

~~~javascript
const vingadores = ['Homem de Ferro', 'Capitão América', 'Thor', 'Valquíria', 'Capitã Marvel'];
console.log(`Array original`);
console.log(vingadores);
//colocando em ordem alfabética
console.log(`Exibindo em ordem alfabética`);
vingadores.sort();
console.log(vingadores);
//invertendo a ordem alfabética
console.log(`Invertendo a ordem alfabética`);
vingadores.reverse();
console.log(vingadores);
~~~

7. Método join() - converter array em string:

~~~javascript
const vingadores = ['Homem de Ferro', 'Capitão América', 'Thor', 'Valquíria', 'Capitã Marvel'];
console.log(`Array original`);
console.log(vingadores);
// convertendo em string: deixará um espaço vazio entre cada elemento do array
const string1 = vingadores.join(' ');
console.log(`Nova string com um espaço entre os elementos`);
console.log(string1);
// convertendo em string e mudando o separador
const string2 = vingadores.join(' - ');
console.log(`Nova string com espaço e hífen separando os elementos`);
console.log(string2);
~~~

8. Métodos includes() – every() – some() – find():

~~~javascript
const vingadores = ['Homem de Ferro', 'Capitão América', 'Thor', 'Valquíria', 'Capitã Marvel'];
console.log(`Array original`);
console.log(vingadores);
// includes(): verifica se Thor está no array
const heroiExiste = vingadores.includes('Thor');
console.log(`Thor está no array: ${heroiExiste}`); 
//every(): verifica se todos os heróis tem a letra “e” em seu nome
// passada uma função de callback para essa verificação
const todosHeroisTemLetraE = vingadores.every(vingador => vingador.includes('e'));
console.log(`Todos heróis tem a letra 'e' em seu nome: ${todosHeroisTemLetraE}`);
//some(): verifica se PELO MENOS UM herói tem a letra “e” em seu nome
// passada uma função de callback para essa verificação
const umHeroitemLetraE = vingadores.some(vingador => vingador.includes('e'));
console.log(`Pelo menos um herói tem a letra 'e' em seu nome: ${umHeroitemLetraE} `); 
//find(): exibe o primeiro herói com nome maior que 10 caracteres.
// passada função de callback para fazer a verificação
const exibeHeroi = vingadores.find(vingador => vingador.length > 10);
console.log(`Qual é o primeiro herói com o nome maior que 10 caracteres: ${exibeHeroi}`);
~~~

9. Métodos filter() – map() – reduce():

~~~javascript
const vingadores = ['Homem de Ferro', 'Capitão América', 'Thor', 'Valquíria', 'Capitã Marvel'];
console.log(`Array original`);
console.log(vingadores);
//filter(): novo array contendo nomes dos heróis com mais de 9 caracteres
const novoArray = vingadores.filter(vingador => {return vingador.length > 9;});
console.log(`Novo array apenas com nomes de heróis com mais de 9 caracteres`);
console.log(novoArray);
//map(): novo array contendo a quantidade de caracteres existentes em cada nome do herói
const quantidadeCaracteresNomes = vingadores.map(vingador => { 
  return vingador.length;
});
console.log(`Novo array contendo a quantidade de caracteres de cada nome`);
console.log(quantidadeCaracteresNomes);
//reduce(): total de caracteres de todos os nomes dos heróis
const totalCaracteres = vingadores.reduce((acc,vingador) => {
  return acc + vingador.length;
},0); // O 0 é o valor inicial da variável acc
console.log(`Total de caracteres dos nomes dos heróis: ${totalCaracteres}`);
~~~

### 1.3.2 Percorrendo um array

- podemos usar laços de repetição para percorrer os elementos de um Array.

1. `for`:
- é o laço de repetição mais comumente usado para essa finalidade.
- fará a iteração do array, tendo uma variável que será a responsável em garantir que o array seja inteiramente percorrido.

~~~javascript
const vingadores = ['Homem de Ferro', 'Capitão América', 'Thor', 'Valquíria', 'Capitã Marvel'];
for (let i = 0; i < vingadores.length; i++) {
  console.log((`Índice ${i} do array Vingadores: ${vingadores[i]}`));
}
~~~

2. `for in`:
- percorrerá cada índice do array de forma automática.
- deixará a sintaxe mais simples, pois não precisa: definir onde o array começa, onde ele termina, e muito menos o incremento.

~~~javascript
const vingadores = ['Homem de Ferro', 'Capitão América', 'Thor', 'Valquíria', 'Capitã Marvel'];
for (const vingador in vingadores) {
  console.log((`Índice ${vingador} do array Vingadores: ${vingadores[vingador]}`));
}
~~~

3. `for of`:
- percorrerá o array e retornará apenas seus respectivos valores.
- não usa os índices, percorre diretamente todos os elementos do array.

~~~javascript
const vingadores = ['Homem de Ferro', 'Capitão América', 'Thor', 'Valquíria', 'Capitã Marvel'];
for (const vingador of vingadores) { 
  console.log(`Herói: ${vingador}`);
}
~~~

4. `forEach`:
- percorrerá todo o array, e para cada elemento encontrado, executará uma função previamente definida.

~~~javascript
const vingadores = ['Homem de Ferro', 'Capitão América', 'Thor', 'Valquíria', 'Capitã Marvel'];
vingadores.forEach( vingador => {
  const agilidade = Math.ceil(Math.random()*100);
  console.log(`Nome do herói: ${vingador} - Agilidade: ${agilidade}`);
})
~~~

## 1.4 Objetos 

- um objeto é uma coleção de propriedades que são usados para representar algo do mundo real.

### 1.4.1 Criando objetos literais
- é uma das formas mais comuns.
- como fazer:
  - criar uma variável, abrir chaves {}, definir suas propriedades e seus respectivos valores, separando-as por vírgulas.
  - as propriedades devem estar separadas dos valores recebidos através de dois pontos (:).
  - no final da declaração usamos o sinal de vírgula (,) para indicarmos que a aquela propriedade foi finalizada. 
  - para termos acesso às propriedades, usar o nome do objeto seguido do sinal de ponto final (.), e a propriedade desejada

~~~javascript
const usuario = {
  nome: 'Clark Kent',
  id: 12345,
  idade: 38,
  profissao: 'Repórter',
  email: 'clark@planetadiario.com'
} 
console.log(usuario);
console.log(`------------`);
console.log(`Nome: ${usuario.nome}`);
console.log(`Id: ${usuario.id}`);
console.log(`Email: ${usuario.email}`);
~~~

### 1.4.2 Usando um método construtor

- é possível usar um método construtor para criar os objetos. 
- são chamadas de construtores porque usam a `palavra-chave new` para criar um objeto.
- o objeto criado terá suas propriedades e métodos definidos dentro da função usando a `palavra-chave this`.

~~~javascript
//criando um objeto
function Usuario (nome, id, idade, profissao, email) {
  this.nome = nome;
  this.id = id;
  this.idade = idade;
  this.profissao = profissao;
  this.email = email;
}
const usuario1 = new Usuario ('Bruce Wayne', 78945, 40, 'Empresário', 'bruce@gotham.com');
const usuario2 = new Usuario('Diana Prince', 36985, 35, 'Enfermeira', 'diana@temiscira.com');
const usuario3 = new Usuario('Peter Parker', 741233, 22, 'Fotógrafo', 'parker@photo.com');
//exibindo os objetos
console.log(usuario1);
console.log(usuario2);
console.log(usuario3);
~~~

### 1.4.3 Usando uma factory function

- é uma função que retorna um objeto, sendo uma forma muito comum de criar objetos em JS.
- em vez de usar a palavra-chave new, podemos chamar a factory para criar e retornar o objeto.

~~~javascript
function criarHeroi (nome, velocidade, agilidade, forca) {
  return {nome, velocidade, agilidade, forca};
}
//criando os objetos
const heroi1 = criarHeroi("Eu", 88, 87, 91);
const heroi2 = criarHeroi("Tu", 86, 82, 92);
const heroi3 = criarHeroi("Ele", 92, 98, 94);
//exibindo os objetos
console.log(heroi1);
console.log(heroi2);
console.log(heroi3);
~~~

### 1.4.4 Criando métodos 

- é possível também definir funcionalidades aos objetos (chamamas de métodos).
- a declaração é feita definindo um nome para o método ,seguido do bloco de instruções.

~~~javascript
function criarHeroi (nome, velocidade, agilidade, forca) {
  return {
    nome,
    velocidade,
    agilidade,
    forca,
    falar: function () {
      console.log(`Olá, eu sou o ${nome}! – velocidade: ${velocidade} - agilidade: ${agilidade} - força: ${forca}`);
    }
  };
}
const heroi1 = criarHeroi("Superman", 98, 92, 99);
const heroi2 = criarHeroi("Batman", 86, 82, 88);
const heroi3 = criarHeroi("Hulk", 92, 98, 94);
//exibindo os objetos
heroi1.falar();
heroi2.falar();
heroi3.falar();
~~~

### 1.4.5 Adicionar ou remover propriedades

- para adicionar propriedades, acessar o objeto,declarar a propriedade desejada e atribuir um valor a ela.
- para remover, usar o operador delete seguido do nome da propriedade desejada.

~~~javascript
function criarHeroi(nome, velocidade, agilidade, forca) {
  return {
    nome,
    velocidade,
    agilidade,
    forca 
  }
}
const heroi1 = criarHeroi("Superman", 98, 92, 99);
const heroi2 = criarHeroi("Batman", 86, 82, 88);
//adicionando uma propriedade ao heroi1
console.log(`Adicionando a propriedade ponto fraco ao heroi 1`);
heroi1.pontoFraco = 'Kryptonita';
console.log(heroi1);
//removendo uma propriedade do heroi2
console.log(`Removendo a propriedade nome do heroi 2`);
delete heroi2.nome;
console.log(heroi2);
~~~

## 1.5 Spread Operator 

- permite que os elementos de um objeto sejam passados para outro objeto. 
- representado por três pontos finais seguidos (...), em conjunto do nome do objeto que deseja espalhar. 
- é útil principalmente quando queremos manipular objetos ou arrays.

~~~javascript
//primeiro array
const xMen = new Array('Ciclope', 'Wolverine', 'Fênix', 'Fera', 'Vampira');
//segundo array
const vingadores = ['Homem de Ferro', 'Capitão América', 'Thor', 'Valquíria', 'Capitã Marvel'];
//gerando um novo array com o spread
const novoArray = [...xMen, ...vingadores];
//exibindo o novo array
console.log(novoArray);
// (10) ['Ciclope', 'Wolverine', 'Fênix', 'Fera', 'Vampira', 'Homem de Ferro', 'Capitão América', 'Thor', 'Valquíria', 'Capitã Marvel']
~~~

- copiando um array:

~~~javascript
//array original
const vingadores = ['Homem de Ferro', 'Capitão América', 'Thor', 'Valquíria', 'Capitã Marvel'];
//copiando o array original para outro
const novoArray = [...vingadores];
//exibindo o novo array
console.log(novoArray);
// (5) ['Homem de Ferro', 'Capitão América', 'Thor', 'Valquíria', 'Capitã Marvel']
~~~

- utilizando o operador para gerar um outro objeto com novas propriedades:

~~~javascript
//criando o objeto original
const vingador = { 
  nome: 'Clint Barton', 
  email: 'clint@arqueiro.com'
};
//exibindo o objeto original
console.log(vingador);
//criando um novo objeto com novas propriedades
const upgradeVingador = {...vingador, forca: 82, pontaria: 100};
//exibindo o novo objeto
console.log(upgradeVingador);
// {nome: 'Clint Barton', email: 'clint@arqueiro.com', forca: 82, pontaria: 100}
~~~

## 1.6 Rest Operator

- permite que uma função receba um número indefinido de argumentos e os armazene em um array.
- representado por três pontos finais sequenciais, ( ... ) e deve ser colocado como parâmetro em uma função.
- exemplo:

~~~javascript
//criando a função passando o operador como parâmetro
function somar(...numeros) {
  let total = 0;
  numeros.forEach(numero => {
    total += numero;
    })
  return total;
}
console.log(`Somando os valores: ${somar(1, 2, 3, 4, 5, 6, 7, 8, 9)}`);
console.log(`Somando os valores: ${somar(1, 2, 3, 4, 5, 6, 7, 8)}`);
console.log(`Somando os valores: ${somar(1, 2, 3, 4, 5, 6, 7)}`);
console.log(`Somando os valores: ${somar(1, 2, 3, 4, 5, 6)}`);
~~~

## 1.7 Desestruturação

- permite acessar os valores existentes em objetos ou arrays e atribuí-los a qualquer variável ou até mesmo gerar um novo objeto.

### 1.7.1 Desestruturação em arrays

- para desestruturar um array, usar colchetes "[]".
- dentro deles serão declaradas as variáveis que receberão os valores existentes no array, seguindo a posição de seus índices.
- também é possível usar o ***spread operator*** em conjunto com a desestruturação, gerando um novo array:

~~~javascript
const vingadores = ['Homem de Ferro', 'Capitão América', 'Thor', 'Valquíria', 'Capitã Marvel'];
console.log(`Array originial`);
console.log(vingadores);
//fazendo a desestruturação com três variáveis e um array
const [vingador1, vingador2, vingador3, ...outrosVingadores] = vingadores;
console.log(`Exibindo as variáveis criadas`);
console.log(`Vingador 1: ${vingador1}`);
console.log(`Vingador 2: ${vingador2}`);
console.log(`Vingador 3: ${vingador3}`);
console.log(`Exibindo o novo array`);
console.log(`Demais vingadores: ${outrosVingadores}`);
~~~

### 1.7.2 Desestruturação em objetos

- usar as chaves "{}".
- declarar os nomes das propriedades que serão utilizadas na desestruturação do objeto.
- também poderá ser usado o spread operator, gerando assim um novo objeto.

~~~javascript
const usuario = {
  nome: 'Clark Kent',
  id: 12345,
  idade: 38,
  profissao: 'Repórter',
  email: 'clark@planetadiario.com'
}
console.log(`Exibindo o objeto original`);
console.log(usuario);
//fazendo a desestruturação com três variáveis e um objeto
const {nome, id, profissao, ...demaisDados} = usuario;
console.log(`Exibindo as variáveis`);
console.log(`Id: ${id}`);
console.log(`Nome: ${nome}`);
console.log(`Profissão: ${profissao}`);
console.log(`Exibindo o novo objeto`);
console.log(demaisDados);
~~~

## 1.8 DOM 

- `DOM` = Document Object Model.
- modelo de documento carregado pelos browsers, através do qual podemos definir um padrão para acessar e manipular qualquer conteúdo inserido em uma página HTML.
- a representação do documento é feita através de uma árvore de nós, e cada elemento da página é representado por um nó específico.

pág 49