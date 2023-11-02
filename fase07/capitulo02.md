<div id="fase07" align="center">
<h1>FASE 7 - INTEGRATION</h1>
<h2>Capítulo 02: Mais dinamismo na interface com o usuário.</h2>
</div>

<div align="center">
<h2>1. MAIS DINAMISMO NA INTERFACE COM O USUÁRIO.</h2>
</div>

## 1.1 Introdução: Servlets

- `Servlet` é o componente da plataforma Java Web que será responsável por fazer o “meio de campo” entre a página (interface do usuário) e o modelo de negócio (model).
- são classes Java que realizam o direcionamento de requisições HTTP feitas por clientes, como os navegadores (Mozilla, Firefox, Chrome), eles são responsáveis por receber os dados para serem processados e devolver uma resposta a esses clientes.Essas classes são instaladas em um Servlet Container ou WebContainer (Servidor), o que permite à servlet tratar as requisições.

## 1.2 Requisição e resposta

- para promover a interação entre os diversos componentes envolvidos na programação Web dinâmica, a servlet deve receber uma requisição e devolver uma resposta ao cliente.
- uma servlet tem a função de recuperar as informações enviadas pelo usuário (por meio de uma requisição) e passar essas informações para outros componentes da aplicação para que sejam processadas. Depois, esses componentes devem retornar algum valor para que a servlet possa enviar uma resposta para o usuário.

## 1.3 Requisição a uma Servlet

- cada requisição a uma servlet é executada em uma thread.
- o objeto servlet é único na aplicação.
- a servlet é acessada por vários clientes simultaneamente, o que é possível pelo fato de terem sido criados threads (linhas de execução paralelas) para cada um dos clientes.

## 1.4 Ciclo de vida de uma servlet

- as servlets são instanciadas pelo container, na primeira vez que são acessadas.
- após iniciadas, as servlets podem atender a requisições.
- o container decide a hora de destruir as servlets(chamando o método destroy()).








--- 

[Voltar ao início!](https://github.com/monicaquintal/fintech)