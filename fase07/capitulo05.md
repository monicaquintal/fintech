<div id="fase07" align="center">
<h1>FASE 7 - INTEGRATION</h1>
<h2>Capítulo 05: A alternativa do Facebook.</h2>
</div>

<div align="center">
<h2>1. A ALTERNATIVA DO FACEBOOK</h2>
</div>

## 1.1 Introdução

- mantido pelo Facebook, vem sendo utilizado em aplicativos como Airbnb e Instagram.
- é um dos frameworks mais exigidos do mercado.

## 1.2 Sobre o React

- originalmente desenvolvido no Facebook em 2012; neste mesmo ano, outro framework já era consolidado como “padrão” por muitas indústrias: AngularJS. 
- esses frameworks são bibliotecas JavaScript capazes de criar componentes e gerenciar estados e eventos no browser (Front-End).

## 1.3 Pré-requisito deste capítulo

- noções de lógica de programação ou desenvolvimento de algoritmos.
- temas abordados sobre HTML, CSS e JavaScript.

## 1.4 NodeJS: quando o JavaScript sai do browser

- JavaScript é uma linguagem interpretada nos browsers; o componente dos browsers que faz essa tarefa se chama “interpretador JavaScript”, sendo que um dos mais rápidos conhecidos atualmente é o V8, utilizado no Chrome.
- NodeJS é um programa que isola o V8 num programa executável, tornando-o capaz de interpretar códigos JavaScript. Assim, o NodeJS é simplesmente um programa que entende JavaScript.
- o NodeJS pode ser utilizado de diversas formas diferentes. 
  - a primeira, e mais frequente, é interpretar códigos no Back-End (servidor) para gerar páginas e mandá-las para o cliente.
  - a segunda forma é utilizá-lo a fim de executar códigos para aplicações Desktop. O Visual Studio Code é um bom exemplo, uma vez que ele é escrito em JavaScript e roda como um programa qualquer.
  - a terceira forma é utilizá-lo como uma ferramenta para o desenvolvedor. Nesse caso, podemos utilizar códigos JavaScript para gerar outros códigos JavaScript. Um exemplo prático disso é o processo de “minificação”, que reescreve um arquivo js de forma a diminuir seu tamanho sem alterar a lógica de seu código. 
  
> O React utiliza o NodeJS para gerar códigos que o browser entende.

- junto à instalação do NodeJS, há outro programa, chamado `npm` (node package manager), que gerencia bibliotecas de códigos JavaScript. 
- com npm, é possível fazer downloads automaticamente de bases de dados de código públicas para usar em qualquer projeto, o React está cadastrado no npm. 
- o NodeJS pode ser baixado [aqui](https://nodejs.org/en/).
  - assim que instalado, abrir um “prompt de comando” (windows + r) e digitar “cmd”. Clique em “OK” e um terminal será apresentado.
  - digite “node -v” e pressione a tecla enter no terminal. A versão do Node deve ser, no mínimo, v16.17.1.

## 1.5 Visual Studio Code

- é um IDE (Integrated Development Environment), ambiente de desenvolvimento integrado muito utilizado para programação WEB.
- um IDE integra diversas ferramentas que tornam o desenvolvimento muito mais ágil e prático, como: terminal integrado, substituição de palavras em múltiplos arquivos, formatação de códigos-fonte, etc. 
- para a instalação, basta [acessar o site](https://code.visualstudio.com/) e fazer o download da aplicação. 
  - para criar um projeto no VS Code, criar uma pasta nova e abri-la pelo menu File → Open Folder.

### 1.5.1 Explorer

- é um módulo do VS Code capaz de exibir os arquivos e as pastas do seu projeto. 

### 1.5.2 Terminal integrado

- útil para executar comandos de sistema, como mkdir (criação de pastas), del (deletar arquivos e/ou pastas), node (executar o node), npm (instalar pacotes no node), entre outros. 

### 1.5.3 Controle de versionamento

- é possível utilizar diversos sistemas de versionamento, contudo o GIT apresenta a melhor integração.

### 1.5.4 Gerenciamento de extensões

- extensões são módulos adicionais que trazem novas ferramentas ao VS Code. 
- neste capítulo, usaremos o plug-in “ES7 React/Redux/GraphQL/React-Native snippets”.

## 1.6 Preparando o ambiente

- para manter os arquivos organizados, este capítulo manterá todos os códigos dentro da pasta local C:\CodigosReact.
- logo, a primeira coisa a fazer é criar essa pasta em sua máquina!

## 1.7 Sua primeira aplicação React

- para a criação de uma aplicação React, utilizaremos uma ferramenta de auxílio chamada “Create ReactApp”, que pode ser instalada e executada por meio do npx (executor de comandos npm) em um terminal aberto por meio do método da Seção “Erro! Fonte de referência não encontrada.”, ou pelo método da Seção “Erro! Fonte de referência não encontrada.”
- o primeiro passo é abrir o Visual Studio Code. Acesse um novo terminal e digite: 

~~~
cd C:\CodigosReact\npx 
create-react-app primeiro_app
~~~

- o primeiro comando altera a pasta de trabalho do terminal para a nossa pasta de códigos. O segundo comando executa um módulo do node para a criação de uma aplicação padrão React. 
- após a execução, uma árvore de pastas e arquivos é criada em uma pasta chamada primeiro_app.
- o próximo passo é abrir o projeto primeiro_appno VS Code. Clique no menu File → Open Folder... e selecione a pasta C:\primeiro_app. Agora, abra um novo terminal e digite `npm start`. Espere até que um browser seja aberto e apareça uma tela.

## 1.8 Principais conceitos

- o React é baseado em componentes.
- cada componente apresenta uma representação em HTML (para ser renderizado) e comportamentos programados em JavaScript (para interações com o usuário ou o próprio sistema).
- há três pastas: 
  - `node_modules`: contém os pacotes (instalados com o npm) que são necessários para a utilização do React.
  - `public`: contém entre seus arquivos o index.html, a página principal do site. É um arquivo muito simples e, se você o abrir diretamente em seu navegador, verá apenas uma página em branco.
  - `src`: contém diversos arquivos JavaScript, CSS, entre outros. Aqui está a parte mais importante da aplicação.
- arquivo index.js que está na pasta src:

~~~javascript
import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import * as serviceWorker from './serviceWorker';

ReactDOM.render(<App />, document.getElementById('root'));

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
~~~

- a primeira observação sobre esse código é a `instrução import`, interpretada pelo NodeJS para inserir códigos-fonte que estão em outros arquivos, permitindo a modularização (separação) de códigos-fonte. 
- outra parte interessante do código é a `tag <App />`, um componente que foi importado anteriormente (na linha 4 do código). Usamos um componente da mesma forma como se fôssemos escrever um código HTML – por meio de tags.
- exemplo: trocar o conteúdo a seguir

~~~javascript
const root =
ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
~~~

- por:

~~~javascript
const root =
ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
   <div>Teste</div>
  </React.StrictMode>
);
~~~














--- 

[Voltar ao início!](https://github.com/monicaquintal/fintech)