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
&lt;c:out&gt; | &lt;% = ...&gt; nas expressões.
&lt;c:set&gt; | Define o resultado de uma avaliação de expressão de um 'escopo', você pode definir uma espécie de variável no escopo em que você estiver trabalhando.
&lt;c:remove&gt; | Remove uma variável de escopo (de um escopo espefícifo, se especificando).
&lt;c:catch&gt; | Captura qualquer Throwwable (Exception) que ocorrer no body e, se você quiser, pode optar por expor o resultado, é opcional.
&lt;c:if&gt; | Tag condicional simples que avalia seu body se a condição fornecida for verdadeira. O mesmo que o if, mas sem o else.
&lt;c:choose&gt; | Tag condicional simples que estabelece um contexto para operações condicionais mutuamente exclusivas, marcadas por &lt;when&gt; e &lt;otherwise&gt;. O mesmo que switch-case, que pode ser utilizado como if/else.
&lt;c:when&gt; | Subtag de &lt;choose&gt; que inclui seu body se sua condição foi alternada para 'true'.
&lt;c:otherwise&gt; | Subtag de &lt;choose&gt; que segue &lt;when&gt;, marca e executa somente se todas as condições anteriores forem avaliadas como "falso".
&lt;c:import&gt; | Recupera uma URL absoluta ou relativa e carrega o seu conteúdo para a páginaonde se está utilizando. Muito utilizado para modularização.
&lt;c:forEach&gt; | A tag de iteração básica, aceitando muitos tipos de colections e subconjuntos de suporte e outras funcionalidades. O mesmo que foreach.
&lt;c:forTokens&gt; | Iterates dobre tokens, separados por delimitadores fornecidos.
&lt;c:param&gt; | Adiciona um parâmetro a uma URL contendo a tag 'import'.
&lt;c:redirect&gt; | Redireciona para um novo URL.
&lt;c:url&gt; | Cria uma URL com parâmetros de consulta opcionais.

</div>

### 1.6.1 $lt;c:forEach$gt;

- permite iterar uma lista de elementos.
- ótima para montar tabelas e selects (combobox).
- exemplo: exibir uma tabela para o usuário. Para isso, implementar uma Servlet que envia um objeto de Collections (Lista) para a página JSP.

~~~java
protected void doGet(HttpServletRequest req, HttpServletResponse resp)
  throws ServletException, IOException {
  ArrayList<String> nomes = new ArrayList<String>();
  nomes.add("Alexandre");
  nomes.add("Carlos");
  req.setAttribute("lista", nomes);
  }
~~~

- o nome do atributo inserido no request foi “lista”, e será utilizado para recuperar as informações na página JSP.
- em relação à página JSP, que recupera esse atributo e utiliza a tag &lt;c:forEach&gt; para montar a tabela:

~~~jsp
<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
  <%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
  <!DOCTYPE html>
  <html>
  <head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Exemplo JSP / TagLibs</title>
  </head>
  <body>
  <table border="1">
    <tr>
      <th>Nome</th>
    </tr>
    <c:forEach var="n" items="${lista}">
      <tr>
        <td>${n}</td>
      </tr>
    </c:forEach>
  </table>
  </body>
  </html>
~~~

- a tag &lt;c:forEach&gt; possui dois atributos principais:
  - `var`: define o nome da variável que vai receber cada um dos itens da coleção.
  - `items`: define a coleção que será utilizada para a iteração.
- é muito parecido com o foreach do Java.
- a primeira linha da tabela não precisa estar dentro do foreach, pois ela define a coluna de cabeçalho da tabela. 

### 1.6.2 &lt;c:if&gt;

- tag que realiza uma estrutura de seleção (if).
- o atributo test recebe uma EL que realiza uma comparação e resulta em um boolean.
- não temos a tag else do if. 
- exemplos:

~~~jsp
<c:if test="${numero > 100}">
  <p>Valor Maior que 100</p>
</c:if>
<c:if test="${not empty lista }">
  <!-- Tabela -->
</c:if>
<c:if test="${usuario == 'admin' }">
  <p>Ola Administrador!</p>
</c:if>
~~~

### 1.6.3 &lt;c:choose&gt; &lt;c:when&gt; &lt;c:otherwise&gt;

- muito parecido com o switch-case do Java.
- permite testar várias condições, somente um bloco é executado.
- como não existe a tag else, podemos utilizar essas tags para ter esse comportamento, já que é possível realizar o teste com o &lt;c:when&gt; e adicionar a tag &lt;c:otherwise&gt; para funcionar como o else.
- exemplo:

~~~jsp
<c:choose>
  <c:when test="${numero > 100 }">
    <p>Valor Maior que 100</p>
  </c:when>
  <c:when test="${numero < 50}">
    <p>Valor Menor que 50</p>
  </c:when>
  <c:otherwise>
    <p>Valor entre 50 e 100</p>
  </c:otherwise>
</c:choose>
~~~

### 1.6.4 &lt;c:out&gt;

- utilizado para exibir informações na página.
- exemplo:

~~~jsp
<c:out value="${numero}"/>
~~~

### 1.6.5 &lt;c:url&gt;

- permite criar links com parâmetros (o código fica mais fácil de ser entendido, já que não é necessário criar uma String com concatenações). 
- podemos adicionar a quantidade de parâmetros que forem necessários. 
- exemplo:

~~~jsp
<c:url value="editarCliente" var="link">
  <c:param name="nome" value="${cli.nome}"/>
</c:url>
<a href="${link}">Cliente</a>

<!-- resultado: -->
<a href="editarCliente?nome=Alexandre">Cliente</a>
~~~

### 1.6.6 &lt;c:import&gt;

- permite importar páginas web do mesmo contexto web (aplicação), de contextos diferentes e até mesmo de máquinas diferentes.

<div align="center">

Atributo | Descrição | Requerido? | Padrão
----------|---------|--------------|--------------
url | URL a ser importada | Sim | Nenhum
context | "/" seguido de nome da aplicação web local | Não | Contexto corrente
var | Nome do atributo onde será armazenado o conteúdo da página importada | Não | Nenhum
scope | Escopo do atributo onde será armazenado o conteúdo da página importada. Pode ser page, request, session, application. | Não | Page

</div>

~~~jsp
<c:import url="exemplo2.jsp" scope="session"/>
~~~

## 1.7 TagLibs – Formatting

- tags de formatação JSTL são usadas para formatar e exibir texto, data, hora e números para sites internacionalizados. 
- assim como a taglib core, precisamos adicionar a taglib de formatting nas páginas que irão utilizar a formatação:

~~~jsp
<%@ taglib prefix="fmt" uri="http://java.sun.com/jsp/jstl/fmt"%>
~~~

- lista de todas as tags da biblioteca:

<div align="center">

Tag | Descrição
-----|--------------
&lt;fmt:formatNumber&gt; | Para renderizar valores numéricos com precisão ou formato específico.
&lt;fmt:parseNumber&gt; | Analisa a representação de uma sequência de caracteres de um número, moeda ou porcentagem.
&lt;fmt:formatDate&gt; | FOrmata uma data e/ou uma hora usando os estilos e padrões fornecidos.
&lt;fmt:parseDate&gt; | Analisa a representação de sequência de uma data e/ou tempo.
&lt;fmt:bundle&gt; | Carrega um pacote de recursos para ser usado plo seu corpo de tag.
&lt;fmt:setLocale&gt; | Armazena a localidade fornecida na variável de configuração de localidade.
&lt;fmt:setBundle&gt; | Carrega um bundle de recursos e o armazena na variável de escopo nomeada ou na variável de configuração do bundle.
&lt;fmt:timeZone&gt; | Especifica o fuso horário para qualquer formataçãod e tempo ou parsing de ações aninhadas em seu conteúdo.
&lt;fmt:setTimeZone&gt; | Armazena o determinado fuso horário na variável de configuraçãod e fuso.
&lt;fmt:message&gt; | Para exibir uma mensagem internacionalizada.

</div>

### 1.7.1 &lt;fmt:formatDate&gt;

- formatador de data.
- deve se passar um objeto de data (Date) e não uma String para a tag.
- exemplos:

~~~jsp
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ taglib prefix="fmt" uri="http://java.sun.com/jsp/jstl/fmt" %>
<html>
<head>
  <title>JSTL Formatação de datas</title>
</head>
<body>
<h3>Formatação de datas:</h3>
<c:set var="data" value="<%=new java.util.Date()%>" />
<p>Data Formatada (1): <fmt:formatDate type="time" value="${data}" /></p>
<p>Data Formatada (2): <fmt:formatDate type="date" value="${data}" /></p>
<p>Data Formatada (3): <fmt:formatDate type="both" value="${data}" /></p>
<p>Data Formatada (4): <fmt:formatDate pattern="dd/MM/yyyy" value="${data}" /></p>
</body>
</html>
~~~

- o atributo type determina o tipo de dado que será exibido: a data, hora ou ambos.
- o atributo value recebe o objeto Date, que representa a data e será formatado. 
- podemos ainda utilizar o atributo pattern para determinar exatamente a forma como a data será exibida, como na tabela:

<div align="center">

Código | Descrição | Exemplo
-------|-----------|------------
G | The area designator | AD
Y | The year | 2023
M | The month | Aprin & 04
d | The day of the month | 20
h | The hour (12-hour time) | 12
H | The hour (24-hour time) | 0
m | The minute | 45
s | The second | 52
S | The millisecond | 970
E | The day of the week | Tuesday
D | The day of the year | 180
F | The day of the week in the month | 2(end we in month)
w | The week in the year | 27
W | The week in the month | 2
a | The a.m./p.m. indicator | PM
k | The hour (12-hour time) | 24
K | The hour (24-hour time) | 0
z | The time zone | Central Stantard Time
' | - | The escape for text
" | - | The single quote

</div>

### 1.7.2 &lt;fmt:formatNumber&ht;

- podemos formatar números no formato de moedas e porcentagem, e utilizar a localização do usuário para mostrar o valor da moeda local.
  - o atributo value recebe o número que será formatado.
  - o atributo type recebe o tipo de formatação, como number para número, currency para valores monetários e percent para porcentagens.
- é possível utilizar o atributo pattern para definir detalhadamente o tipo de formatação.
- exemplos:

~~~jsp
<%@ page language="java" contentType="text/html; charset=UTF-8"
  pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<%@ taglib prefix="fmt" uri="http://java.sun.com/jsp/jstl/fmt"%>
<html>
<head>
<title>JSTL Formatação de Números</title>
</head>
<body>
  <h3>Formatar Números:</h3>
  <c:set var="valor" value="999.888" />
  <p>
    Número Formatado (1):
    <fmt:formatNumber value="${valor}" type="currency" />
  </p>
  <p>
    Número Formatado (2):
    <fmt:formatNumber type="number" maxIntegerDigits="3"
      value="${valor}" />
  </p>
  <p>
    Número Formatado (3):
    <fmt:formatNumber type="number" maxFractionDigits="3"
      value="${valor}" />
  </p>	
  <p>
    Número Formatado (4):
    <fmt:formatNumber type="percent" value="${valor}" />
  </p>
  <p>
    Número Formatado (5):
    <fmt:formatNumber type="number" pattern="###.###E0" value="${valor" />
  </p>	
</body>
</html>
~~~

<div align="center">
<h2>2. PRÁTICA!</h2>
</div>

- exemplo que utilizará tudo que vimos até agora: JSP, Servlets, JSTL e EL.
- desenvolver as funcionalidades de cadastro e listagem de produtos.

1. Criar um novo projeto Java web. No eclipse, utilize a opção: File > New > Dynamic Web Project. Dê um nome ao projeto e configure o servidor Tomcat7. Clique em Next e clique novamente em Next até chegar à última tela, marque para criar o web.xml e finalize o processo.

2. Para deixar a aplicação com layout profissional, utilizar o bootstrap. Para isso, configure o projeto como o que fizemos no capítulo anterior. Crie um diretório chamado resources dentro de WebContent, copie os arquivos de css e javascript do bootstrap e jquery. Vamos utilizar os arquivos JSPs para realizar o include do header, footer e menu.

3. Criar a tela com um formulário de cadastro de produto. O formulário será parecido com o desenvolvido no capítulo de Servlets, porém utilizaremos um arquivo JSP em vez de HTML e vamos utilizar o bootstrap para dar estilo ao formulário. Criar cadastro-produto.jsp.

~~~jsp
<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>Cadastro de Produto</title>
<%@ include file="header.jsp" %>
</head>
<body>
<%@ include file="menu.jsp" %>
  <div class="container">
    <h1>Cadastro de Produto</h1>
  
    <form action="produto" method="post">
      <div class="form-group">
        <label for="id-nome">Nome</label>
        <input type="text" name="nome" id="id-nome" class="form-control">
      </div>
      <div class="form-group">
        <label for="id-qtd">Quantidade</label>
        <input type="text" name="quantidade" id="id-qtd" class="form-control">
      </div>
      <div class="form-group">
        <label for="id-valor">Valor</label>
        <input type="text" name="valor" id="id-valor" class="form-control">
      </div>
      <input type="submit" value="Salvar" class="btn btn-primary">
    </form>
  </div>
<%@ include file="footer.jsp" %>
</body>
</html>
~~~

4. Criar a Servlet que receberá os dados do formulário. Clique com o botão direito do mouse na pasta src e escolha New > Servlet, sendo “br.com.fiap.controller” para o pacote e “ProdutoServlet” para a classe.

5. Para agrupar as informações do produto, precisamos de uma classe Java Bean. Dessa forma, criar uma classe “Produto”. Clique com o botão direito do mouse na pasta src e escolha “New” > "Class". Para deixar o projeto bem estruturado, criaremos um novo pacote para a classe Produto, para isso, renomeie o packagepara “br.com.fiap.bean”. Depois de dar o nome à classe, finalize o processo.

~~~java
package br.com.fiap.bean;
  public class Produto {
    private String nome;
    private int quantidade;
    private double valor;

    public Produto() {
      super();
    }

    public Produto(String nome, int quantidade, double valor) {
      super();
      this.nome = nome;
      this.quantidade = quantidade;
      this.valor = valor;
    }

    public String getNome() {
      return nome;
    }

    public void setNome(String nome) {
      this.nome = nome;
    }

    public int getQuantidade() {
      return quantidade;
    }

    public void setQuantidade(int quantidade) {
      this.quantidade = quantidade;
    }

    public double getValor() {
      return valor;
    }

    public void setValor(double valor) {
      this.valor = valor;
    } 
  }
~~~

6. Agora estamos prontos para implementar a Servlet. Essa classe tem a responsabilidade de recuperar os dados enviados pelo usuário, enviar esses dados para outra parte da aplicação, responsável pelas regras de negócio ou persistência de dados e, por fim, devolver uma informação para o usuário. Essas são as principais responsabilidades de um controlador (Controller), uma camada da aplicação da arquitetura MVC (Model, View e Controller). 

~~~java
package br.com.fiap.controller;
  import java.io.IOException;
  import java.util.ArrayList;
  import java.util.List;
  import javax.servlet.ServletException;
  import javax.servlet.annotation.WebServlet;
  import javax.servlet.http.HttpServlet;
  import javax.servlet.http.HttpServletRequest;
  import javax.servlet.http.HttpServletResponse;
  import br.com.fiap.bean.Produto;
  @WebServlet("/produto")
  public class ProdutoServlet extends HttpServlet {
    private static List<Produto> lista = new ArrayList<Produto>();
    private static final long serialVersionUID = 1L;
     protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
      	//Recupera os par?metros do formul?rio
      	String nome = request.getParameter("nome");
      	int qtd = Integer.parseInt(request.getParameter("quantidade"));
      	double valor = Double.parseDouble(request.getParameter("valor"));	
      	//Cria um objeto do tipo Produtp
      	Produto produto = new Produto(nome, qtd, valor);
      	//Adiciona o produto na lista
      	lista.add(produto);
      	//Mensagem de sucesso
      	request.setAttribute("msg","Produto cadastrado!");
      	request.getRequestDispatcher("cadastro-produto.jsp").forward(request, response);
    }
  }
~~~

7. Como ainda não vamos utilizar o banco de dados, vamos utilizar uma coleção (List) de Produtos para gravar as informações. Essa lista deve ser estática, pois deve pertencer à classe e não à instância dessa classe. Assim, todos os objetos dessa Servlet compartilham a mesma lista, ou seja, todos possuem a mesma informação.

8. Dentro do método doPost, recuperamos todas as informações do formulário por meio da request e o método getParameter(“campo”), lembre-se de que o valor do parâmetro do método deve ser o mesmo do nome do campo do formulário do qualvocê quer recuperar o valor. Depois de recuperar os valores, instanciamos uma classe Produto, passando os valores em seu construtor. Com isso, podemos adicionar esse objeto na lista para “salvar no banco de dados”. 

9. Por fim, devemos dar um feedback para o usuário. Vamos adicionar uma mensagem como um atributo do request e depois encaminhar para o usuário uma página, que nesse caso será a mesma página de cadastro de produto.

10. O último detalhe é ajustar a página JSP para exibir essa mensagem, mas antes vamos adicionar as bibliotecas JSTL na nossa aplicação. Copie e cole os dois jars dentro do diretório WebContent > WEB-INF > lib.

11. Agora podemos utilizar a tagJSTL &lt;c:if&gt; para testar se existe uma mensagem no request para exibir a caixa de mensagem.

~~~jsp
<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
      pageEncoding="ISO-8859-1"%>
  <%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
  <!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
  <html>
  <head>
  <meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
  <title>Cadastro de Produto</title>
  <%@ include file="header.jsp" %>
  </head>
  <body>
  <%@ include file="menu.jsp" %>
    <div class="container">
      <h1>Cadastro de Produto</h1>
      
      <c:if test="${not empty msg }">
        <div class="alert alert-success">
          ${msg}
        </div>
      </c:if>	
    
      <form action="produto" method="post">
        <div class="form-group">
          <label for="id-nome">Nome</label>
          <input type="text" name="nome" id="id-nome" class="form-control">
        </div>
        <div class="form-group">
          <label for="id-qtd">Quantidade</label>
          <input type="text" name="quantidade" id="id-qtd" class="form-control">
        </div>
        <div class="form-group">
          <label for="id-valor">Valor</label>
          <input type="text" name="valor" id="id-valor" class="form-control">
        </div>
        <input type="submit" value="Salvar" class="btn btn-primary">
      </form>
    </div>
  <%@ include file="footer.jsp" %>
  </body>
  </html>
~~~

12. Desenvolver a funcionalidade de listagem de produtos. O primeiro passo é ajustar a Servlet, utilizando a classe ProdutoServlet. Implementaremos o método doGet, pois a Servlet será acionada por meio de um link e não de um formulário. A Servlet precisa enviar a lista para a tela JSP e depois encaminhar o usuário para a página de listagem. São duas linhas de código! 

~~~java
@Override
  protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
    request.setAttribute("produtos", lista);
    request.getRequestDispatcher("lista-produto.jsp").forward(request, response);
  }
~~~

13. A página JSP deve se chamar “lista-produtos.jsp” e o nome do atributo com a lista é “produtos”. Agora, criar a página JSP dentro do diretório Web Content.
    - utilizamos o include para adicionar o menu, css e scripts na página. 
    - criamos uma tabela HTML com uma classe do bootstrap, para dar estilo à tabela. 
    - para exibir todos os itens cadastrados, utilizamos a taglib &lt;c:forEach&gt;, que recebe a lista no atributo itens, por isso utilizamos a EL com o nome do atributo que foi adicionado na Servlet (produtos). O atributo var define o nome da variável que irá receber cada item da lista.

~~~jsp
<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
      pageEncoding="ISO-8859-1"%>
  <%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
  <!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
  <html>
  <head>
  <meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
  <title>Cadastro de Produto</title>
  <%@ include file="header.jsp" %>
  </head>
  <body>
  <%@ include file="menu.jsp" %>
    <div class="container">
      <h1>Produtos</h1>
      <table class="table table-striped">
        <tr>
          <th>Nome</th>
          <th>Quantidade</th>
          <th>Valor</th>				
        </tr>
        <c:forEach items="${produtos }" var="p">
          <tr>
            <td>${p.nome}</td>
            <td>${p.quantidade}</td>
            <td>${p.valor}</td>
          </tr>
        </c:forEach>
      </table>
    </div>
  <%@ include file="footer.jsp" %>
  </body>
  </html>
~~~

14. Para finalizar, não podemos simplesmente executar a página como fizemos com o cadastro. Precisamos primeiro executar a Servlet, pois é ela que envia os produtos cadastrados para a página JSP exibir. Assim, podemos testar a funcionalidade de listagem executando o projeto e ajustando a URL com o endereço http://localhost:8080/JSTL/produto. Dessa forma, o browser envia uma requisição com o método GET para a nossa Servlet, que devolve a página JSP junto com a lista de produtos. Para que não seja preciso sempre modificar a URL para acessar a página, vamos arrumar os links da barra de navegação. 

~~~jsp
<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <a class="navbar-brand" href="home.jsp">FIAP</a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav mr-auto">
        <li class="nav-item">
          <a class="nav-link" href="cadastro-produto.jsp">Cadastro</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="produto">Produtos</a>
        </li>
      </ul>
      <form class="form-inline my-2 my-lg-0">
        <input class="form-control mr-sm-2" type="text" placeholder="Search" aria-label="Search">
        <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
      </form>
    </div>
  </nav>
~~~

- o link para a página de cadastro é o próprio nome da página JSP, porém, para a página de listagem, é o valor configurado na Servlet, no @WebServlet(“/produto”).
- agora é só testar! Cadastre alguns produtos e teste a listagem.

--- 

## FAST TEST

### 1. Qual é o objeto implícito para EL responsável por solicitar parâmetros como sequência de caracteres?
> Param.

### 2. Identifique qual tag não faz parte da biblioteca formatting:
> &lt;fmt:lib&gt;

### 3. Identifique qual expressão está incorreta em relação a Expression Language (EL):
> A EL dificulta a leitura e o acesso aos JavaBeans.

--- 

[Voltar ao início!](https://github.com/monicaquintal/fintech)