<div id="fase07" align="center">
<h1>FASE 7 - INTEGRATION</h1>
<h2>Capítulo 04: Frameworks em Java!</h2>
</div>

<div align="center">
<h2>1. FRAMEWORKS EM JAVA!</h2>
</div>

- chegou o momento de utilizar a Expression Language e as bibliotecas de tags, que tornarão a implementação das aplicações mais simples, limpas e produtivas.
- `Expression Language (EL)`:
  - é uma linguagem de expressão utilizada em páginas JSP. 
  - começou como parte do projeto JSTL (Java Standard Tag Libraries), e foi originalmente chamada SPEL (Spring Expression Language). Era uma linguagem de scripts que permitia o acesso a componentes Java(JavaBeans) por meio de JSP.
  - a utilização de JSTL e EL torna o código mais limpo e claro, já que é possível implementar as páginas com código Java por meio de tags. 

## 1.1 Recuperando dados com EL

- a grande vantagem de utilizar EL nas páginas é a facilidade de recuperar os atributos que foram inseridos em algum escopo (request, session, application, pageContext).
- a sintaxe é simples, utilizamos o caractere $ e as chaves ${ }. Dentro das chaves, colocamos o valor da chave em que o atributo foi inserido. 
- exemplo:

~~~xml
<%@ page language="java" contentType="text/html; charset=ISO-8859-1" pageEncoding="ISO-8859-1"%>
<!DOCTYPE html>
<html lang="pt-br">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<meta name="viewport" content="device-width">
<title>Exemplo EL</title>
</head>
<body>
  <a href="Servlet">Enviar para Servlet</a>
  <h1>${atributoDoRequest}</h1>	
<body>
</html>
~~~

- com a EL, só precisamos saber o nome do atributo, não é necessário nenhum código Java.
- exemplo de Servlet realizando request para JSP, que mistura código Java com tags; em contrapartida, poderíamos receber esse atributo por meio da EL de uma forma mais simples e clara.

~~~java
protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
    String nome = "Alexandre";
    request.setAttribute("usuario", nome);
    request.getRequestDispatcher("pagina.jsp").forward(request, response);	
}
~~~

- na Servlet acima, criamos o atributo “usuario” no request. Agora, vamos analisar o código para recuperar o atributo que foi enviado para a página utilizando EL:

~~~xml
<%@ page language="java" contentType="text/html; charset=ISO-8859-1" pageEncoding="ISO-8859-1"%>
  <!DOCTYPE html>
  <html lang="pt-br">
  <head>
  <meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
  <meta name="viewport" content="device-width">
  <title>Exemplo EL</title>
  </head>
  <body>
      <h1>${usuario}</h1>	
  <body>
  </html>
~~~

- a utilização da EL se dá pela chamada `${}`.
- no exemplo acima, ${usuario} é chamado dentro da página JSP, e o atributo que iremos retornar deve estar entre chaves “{}”.
- não é necessário colocar aspas no nome do atributo.

> A EL pode fazer muito mais do que recuperar valores de atributos! Exemplo:

~~~xml
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Exemplo EL</title>
</head>
<body>
  <h1>Operação com EL : ${((((10 * 26)/57)+9))}</h1>
</body>
</html>
~~~

- além de operações matemáticas, como no exemplo acima, podemos realizar comparações e operações com Strings, como concatenação (no exemplo a seguir, é realizada uma operação ternária).

~~~xml
<%@ page language="java" contentType="text/html; charset=UTF-8"
  pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Exemplo EL</title>
</head>
<body>
  <h1>Operação ternária</h1>
  <h2>Você recebeu dois números verifique se a soma desses
    números é maior ou igual a 20, caso seja realize a impressão na tela
    da mensagem "O número é maior ou igual à 20.", caso contrário faça a
    impressão da mensagem "O número é menor do que 20.":</h2>
  
  <p>${(17 > 7) ? 'O número é maior ou igual à 20.' : 'O número é menor do que 20.' }</p>
</body>
</html>
~~~

- praticamente podemos executar qualquer operação básica com EL, como comparações, operações matemáticas e acesso a objetos e coleções que estão em algum escopo.
- operadores que podemos utilizar com a EL em páginas JSP:

<div align="center">

Operador | Descrição
---------|------------------
. | Acessar uma propriedade de bean ou escopo.
[] | Acessar um elemento de array ou list.
() | Agrupar uma subexpressão para alterar a ordem de avaliação.
&#43; | Adição.
&minus; | Subtração ou negação de um valor.
&lowast; | Multiplicação.
/ ou div | Divisão.
% ou mod | Módulo (resto).
== ou eq | Igualdade.
!= ou ne | Diferente.
&lt; ou lt | Menor que.
&gt; ou gt | Maior que.
&lt;= ou le | Menor ou igual.
&gt;= ou ge | Maior ou igual.
&& ou and | AND lógico.
|| ou ou | OR lógico.
! ou not | Unário, negação.
empty | Teste de valores de variáveis vazias.

</div>

## 1.2 Objetos implícitos

- podemos acessar os objetos e coleções que estão em algum escopo, objetos que estão implícitos nas páginas JSP. 
- nome e a descrição desses objetos implícitos:

<div align="center">

PageScope | Variáveis de escopo do escopo da página.
requestScope | Variáveis de escopo do escopo solicitação.
sessionScope | Variáveis de escopo da sessão.
ApplicationScope | Variáveis de escopo do escopo da aplicação.
param | Solicitar parâmetros como sequências de caracteres.
ParamValues | Solicitar parâmetros como coleções de Strings.
header | Cabeçalhos de solicitação HTTP como sequências de caracteres.
headerValues | Cabeçalhos de solicitação HTTP como coleções de strings.
initParam | Parâmetros de inicialização de contexto.
cookie | Valores de cookie.
pageContext | O objeto PageContext JSP para página atual.

</div>

- quando não especificamos o escopo, a EL procura pelo atributo em todos. 
- para `procurar em um escopo específico`, utilizar o nome do escopo, junto do nome do atributo, exemplo: 
  - ${requestScope.usuario} - neste exemplo, a EL procura pelo atributo somente no escopo de request.
- exemplo que trabalha com o objeto implícito param:

~~~xml
<!-- Página exemplo1.jsp, que envia dados para outra página JSP -->
<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
  <!DOCTYPE html>
  <html>
  <head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Exemplo EL / Objetos Implicitos</title>
  </head>
  <body>
    <div class="container">
      <h1>Envio de parâmetros para outra página JSP.</h1>
  <form action="exemplo2.jsp" method="get">
  <fieldset>
    <legend>Formulário</legend>
    <div>
      <label for="pNome">Nome</label> 
           <input type="text" name="nome"
      id="pNome" placeholder="Digite o seu nome">
    </div>
    <div>
      <label for="pIdade">Idade</label> 
           <input type="number" name="idade"
      id="pIdade" placeholder="Digite a sua idade">
    </div>
    <div>
      <input type="submit" value="Enviar">
    </div>
  </fieldset>
  </form>
  <div>
  </body>
  </html>
~~~

- exemplo2.jsp recebendo os dados da página exemplo1.jsp.
- utiliza a EL e o objeto implícito param para recuperar o nome e a idade do formulário HTML. 

~~~xml
<%@ page language="java" contentType="text/html; charset=ISO-8859-1" pageEncoding="ISO-8859-1"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Página do :${param.nome}</title>
</head>
<body>
  <h1>Recuperando os parâmetros do objeto implicito param.</h1>
  <p>Nome: ${param.nome}</p>
  <p>Idade: ${param.idade}</p>
</body>
</html>
~~~

## 1.3 EL e JavaBeans

- a EL facilita a leitura e o acesso aos JavaBeans. 
- podemos criar uma classe JavaBean para armazenar as informações como atributos dessa classe (Usuario), e depois instanciá-lo, colocar todas as informações em seus atributos e finalmente adicionar esse objeto como um atributo no request.
- exemplo:

~~~java
protected void doGet(HttpServletRequest req, HttpServletResponse resp)
  throws ServletException, IOException {
  Cliente cliente = new Cliente("Alexandre",40);
  request.setAttribute("cli",cliente);
  request.getRequestDispatcher("pagina.jsp").forward(request, response);
  }
~~~

- no código acima, há um método de uma Servlet que cria uma instância de um JavaBean (Cliente) e define um atributo no request chamado “cli”, que será enviado para a página JSP. Agora, veremos na página JSP a recuperação desse atributo com a EL:

~~~jsp
<%@ page language="java" contentType="text/html; charset=ISO-8859-1" pageEncoding="ISO-8859-1"%>
<!DOCTYPE html>
<html lang="pt-br">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<meta name="viewport" content="device-width">
<title>Exemplo JavaBean com EL</title>
</head>
<body>
  <h2>${cli.nome}</h2>	
  <h2>${cli.idade}</h2>	
<body>
</html>
~~~

- ou seja, basta chamar o atributo que foi enviado por meio do request,nesse caso, “cli”. 
- para ser possível recuperar os atributos de um JavaBean, que foi enviado como atributo, implementar a estrutura completa, com os métodos get e set.

~~~java
package br.com.fiap.ead;
  public class Cliente {
    
    private String nome;
    private int idade;
    
    public Cliente(){}
      public Cliente(String nome, int idade){
          this.nome = nome;
          this.idade = idade;
      }
    public String getNome() {
      return nome;
    }
    public void setNome(String nome) {
      this.nome = nome;
    }
    public int getIdade() {
      return idade;
    }
    public void setIdade(int idade) {
      this.idade = idade;
    }
  }
~~~

- a regra para que funcione é que tenha os **métodos get e set**, a EL internamente realiza acesso aos atributos por meio desses métodos.
- portanto, para recuperar a informação o JavaBean precisa do método get, já para adicionar uma informação, será preciso o método set.Entretanto, na EL sempre referenciamos o nome do atributo, já que existe um padrão de nomenclatura para os métodos get e set.

~~~xml
<h2>${cli.nome}</h2>	
<h2>${cli.idade}</h2>
~~~

## 1.4 JSTL (JavaServer Pages Standard Tag Library), TagLibrary ou TagLibs

- é uma coleção de tags que possuem funções da linguagem Java.
- assim, podemos utilizarum laço for, uma estrutura de decisão do tipo if/else ou switch-case diretamente no JSP por meio de tags. 
- facilita desenvolvimento 4 manutenção das páginas em JSP.
- exemplo:

~~~jsp
<!-- Página JSP exemplo1.jsp com Scriptlets -->

<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Exemplo JSP / Scriptlets</title>
</head>
<body>
  <%
    String msg = "Alô mundo!";
  %>
  <p>Mensagem :<%=msg%></p>
</body>
</html>
~~~

~~~jsp
<!-- Página JSP exemplo1.jsp com TagLibs -->

<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<!DOCTYPE html>
<html>
<head>
<metacharset="UTF-8">
<metaname="viewport" content="width=device-width, initial-scale=1.0">
<title>Exemplo JSP / Scriptlets</title>
</head>
<body>
  <c:setvar="msg" value="Alô mundo!"/>
  <p>Mensagem :${msg}</p>
</body>
</html>
~~~ 

## 1.5 Utilização

- é fácil utilizar as TagLibs dentro das páginas JSP. 
- para começar, precisamos das bibliotecas, dos jars das TagLibs - assim como utilizamos jars externos para conectar no banco de dados oracle (jdbc), precisaremos de outros jars, porque as TagLibs são um projeto da Apache do grupo Jakarta.
- para fazer o download dos jars, [acesse aqui](http://tomcat.apache.org/taglibs/index.html).
  - Impl: taglibs-standard-impl-1.2.5.jar (pgp, sha512)
  - Spec: taglibs-standard-spec-1.2.5.jar (pgp, sha512)
- armazená-los em: WebContent > WEB-INF > lib.
  - não é preciso adicionar os jars no build path, pois como é uma aplicação web, existe essa pasta específica para adicionar as bibliotecas.
  - caso copie os jars em qualquer outra pasta e adicione no build path, o projeto pode até compilar, porém, quando executar, o servidor não será capaz de encontrar as bibliotecas e o erro ClassNotFoundException vai acontecer.

~~~jsp
<!-- Diretiva taglib com o import para a biblioteca core -->
<%@taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
~~~

- sobre o exemplo:
  - taglib: nome da diretiva.
  - prefix: propriedade que permite criar um token (identificador da tag na página JSP). Ex: &lt;c:if test=””&gt;&lt;/c:if&gt;. Existe uma convenção que pede o uso da letra “c”, por estar trabalhando com a biblioteca “core”.
  - uri: caminho relativo da api (biblioteca local). O servidor de aplicação usa esse caminho relativo para carregar o conjunto de tags específicas para o token selecionado em prefix.
- há quatro grupos de bibliotecas nos quais podemos classificar as TagLibs: Core tags, Formatting tags, SQL tags e XML tags.

## 1.6 TagLibs – Core

- resume, em seu interior, as principais instruções da linguagem Java no formato de tag. 

<div align="center">

Tag | Descrição
----|-----------------------------------

</div>








--- 

[Voltar ao início!](https://github.com/monicaquintal/fintech)