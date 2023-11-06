<div id="fase07" align="center">
<h1>FASE 7 - INTEGRATION</h1>
<h2>Capítulo 03: JSP, a interface do usuario em Java.</h2>
</div>

<div align="center">
<h2>1. JSP, A INTERFACE DO USUÁRIO EM JAVA.</h2>
</div>

## 1.1 JSP

- a arquitetura MVC separa a aplicação em três principais camadas, sendo a camada View responsável por fazer a interface da aplicação com o usuário, nesse caso, as telas web. É nessa camada que a tecnologia JSP estará!
- `Java Server Pages (JSP)` é uma tecnologia que permite a criação de páginas web geradas dinamicamente e baseadas em HTML, XML ou outros tipos de documentos. 
- é similar ao PHP, porém utiliza a linguagem de programação Java. 
- para implantar e executar Java Server Pages é requerido um servidor web compatível com um container servlet, como Apache Tomcat, Jetty ou Glassfish.
- permite ao desenvolvedor web produzir aplicações que acessem banco de dados, manipulem arquivos, capturem informações a partir de formulários e captem informações sobre o visitante eo servidor.
- uma página criada com a tecnologia JSP, após ser instalada em um servidor de aplicação compatível com a tecnologia Java EE, é transformada em uma Servlet.
- exemplo:

~~~jsp
<%@ page language="java" contentType="text/html; charset=ISO-8859-1" pageEncoding="ISO-8859-1"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>Exemplo JSP</title>
</head>
<body>
	<ul>
	<%for(int x = 0; x < 10 ; x++){%>
				
			<li><%=x %></li>
			
	<%}%>
	</ul>
</body>
</html>
~~~

- o exemplo acima possui extensão .jsp, porém tem características de um arquivo HTML comum, com o diferencial de permitir o uso de código Java embutido.

## 1.2 Vantagens de utilizar JSP

- é mais amigável desenvolver uma página web em um editor que entenda as tags e tenha suporte a essa tecnologia. 
- separação de responsabilidades em camadas, o que deixa o sistema com uma arquitetura mais adequada.
- permite a criação de páginas dinâmicas.

## 1.3 Processamento do JSP

- 1. Ocorre uma requisição HTTP do browser para servidor onde está a aplicação web.
- 2 e 3. Os componentes JSP presentes no servidor de aplicação realizam a conversão do texto do JSP para o código Java, transformando-o em uma Servlet.
- 4. Esses mesmos componentes JSP realizam a compilação do arquivo transformado.
- 5. O servidor de aplicação executa a Servlet que foi gerada a partir do JSP e gera uma resposta HTML para o cliente.
- 6. O servidor de aplicação encaminha a resposta HTML para o cliente.

## 1.4 Elementos do JSP

- cada elemento é responsável por alguma funçãona página.

## 1.5 Scriptlets 

- são blocos de código Java inseridos dentro das páginas JSP.
- devem iniciar com <% e terminar com %>:

~~~jsp
<% 
	String str = "JSP"; 
%>
~~~

- mas também podem ser escritos no formato de tag XML:

~~~xml
<jsp:scriptlet>
	String str = "JSP";
</jsp:scriptlet>
~~~

- entre esses sinais ou tags podemos inserir código Java e, assim que o JSP for processado, será interpretado e executado.
- os elementos HTML devem estar fora dos Scriptlets, somente código Java pode ser inserido nesse bloco.
- exemplo:

~~~jsp
<%@ page language="java" contentType="text/html; charset=ISO-8859-1" pageEncoding="ISO-8859-1"%>
<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>Alô Mundo!</title>
</head>
<body>
	<p>Alô Mundo!</p>
	<p> 
		<%
			out.println("Seu IP é : " + request.getRemoteAddr());
		%>
	</p>
</body>
</html>
~~~

- neste caso, há a implementação dos Scriptlets, utilizando um método do objeto request para recuperar o IP do usuário.
- quando inspecionamos o código, podemos ver apenas o resultado do processamento da página JSP, ou seja, HTML regular puro, gerado pelo servidor de aplicação, pois o browser consegue interpretar o código HTML, mas ele não consegue compreender código Java.

### 1.5.1 Declarations

- é a forma de declarar variáveis ou métodos que podem ser utilizados dentro da página JSP. 
- exemplos:

~~~jsp
<%! String nome = "JSP"; %>
<%! int nr = 0; %>
<%! Object obj = new Object(); %>
~~~

- uma Declaration começa com o sinal de &lt;%! e termina com %&gt;.
- é muito parecido com Scriptlets, porém o início da declaração possui o caractere “!” (exclamação).

### 1.5.2 Expressions

- parecido com os Scriptlets e Declarations.
- a principal diferença é que o utilizamos para dar saída em informações que serão apresentadas nas páginas JSP.
- a sintaxe, diferentemente dos outros dois elementos, não se utiliza de ponto e vírgula para encerrar a linha. 
- para apresentar a informação, utiliza-se operador de atribuição (sinal de igual).
- exemplo:

~~~jsp
<%@ page language="java" contentType="text/html; charset=ISO-8859-1" pageEncoding="ISO-8859-1"%>
<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>Expression</title>
</head>
<body>
	
  A data de hoje é : <%=(new java.util.Date()).toLocaleString()%>

</body>
</html>
~~~

### 1.5.3 Directivas

- são utilizadas para alterar informações em um contexto geral das páginas JSP.
- é formada pela mesma sintaxe dos Scriptlets, porém no sinal que abre o elemento deve ser adicionado o caractere @ (arroba).
- sintaxe:

~~~jsp
<%@ nome_directiva atributos %>

<%@ page language="java" contentType="text/html; charset=ISO-8859-1" pageEncoding="ISO-8859-1"%>
~~~

- podemos definir juntamente com as Directivas:
	- propriedades na página.
	- incluir código de uma fonte externa na página.
	- definir `TagLibs`(conjunto de tags HTML customizadas para utilização específica em páginas JSP. Seu formato é igual ao de uma tag HTML,porém no momento do processamento são interpretadas de maneira diferente).

### 1.5.3.1 Directiva Page

- responsável por definir propriedades da página, como a linguagem que será utilizada, tipo de texto que será formatado, charset para a codificação da página.

~~~jsp
<%@ page import="java.util.*" language="java" contentType="text/html; charset=ISO-8859-1" pageEncoding="ISO-8859-1"%>
~~~

- entre as propriedades dessa Directiva, destacam-se a ***import***, que permite utilizar toda a API Java na página JSP.
- no exemplo acima, a Directiva page utiliza o ***import*** do pacote ***java.util***. Com isso, podemos utilizar as classes e interfaces desse pacote, como o ***Liste*** o ***ArrayList***, lembrando que, para utilizar o código Java na página JSP, precisamos dos Scriptlets.

### 1.5.3.2 Directiva include

- responsável por realizar a inclusão de um arquivo na página atual.
- o include pode ser utilizado para adicionar arquivos, a fim de compor a página atual (desenvolvimento modularizado).
- quando o arquivo é incluído na página atual, se torna parte dela, então o ideal é criar `“SNIPPETS”` (trechos de códigos independentes do contexto em queestá inserido).
- exemplo de página JSP que inclui um menu (páginas inicial.jsp e SNIPPETmenu.jsp).

~~~jsp
<!-- inicial.jsp -->
<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
  pageEncoding="ISO-8859-1"%>
<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<link rel="stylesheet" type="text/css" href="css/estilo.css">
<title>Página Inicial</title>
</head>
<body>
	<!-- Aqui está inserido o menu. -->
	<nav> <%@ include file="menu.jsp" %> </nav>
</body>
</html>
~~~

~~~jsp
<!-- SNIPPETmenu.jsp -->
<p>SCRIPTS WEB</p>
<ul>
	<li>JSP</li>
	<li>ASP</li>
	<li>PHP</li>
	<li>CFM</li>
	<li>CGI</li>
</ul>
~~~

### 1.5.3.3 Directiva taglib

- responsável por referenciar TagLibraries na página JSP. 
- com essa Directiva é possível utilizar uma infinidade de tags customizadas para a construção das páginas JSP.

~~~jsp
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
~~~

### 1.5.4 Comentários

- parecidos com comentários em HTML, porém não aparecem no resultado do processamento da página.
- são iguais à notação dos Scriptlets, contudo em seu interior eles possuem dois hífens.

~~~jsp
<%-- Comentário em páginas JSP --%>
~~~

- diferença entre comentários JSP e HTML:

~~~jsp
<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>Comentários</title>
</head>
<body>
	
	<p>Aqui foi feito um comentário JSP</p>
	<%-- JAVA SERVER PAGES --%>
	<p>Aqui foi feito um comentário HTML</p>
	<!-- HYPER TEXT MARKUP LANGUAGE -->
</body>
~~~

> No código HTML final, podemos ver somente o comentário HTML, pois elementos JSP são processados no servidor e o comentário com JSP é retirado do HTML final.

- além dos comentários que podemos lançar diretamente nas páginas, podemos nos utilizar dos comentários da linguagem Java dentro dos Scriptlets normalmente, como se estivéssemos em uma classe.

~~~jsp
<%
	//Comentário de Linha
	/*
	Comentário de Bloco
	*/
%>
~~~ 

---

<div align="center">
<h2>2. OBJETOS IMPLÍCITOS</h2>
</div>

- são componentes que o servidor disponibiliza em cada página sem a necessidade de declaração.
- esses objetos já estão prontos para utilização, disponíveis e podem ser acessados diretamente dentro dos Scriptlets.

## 2.1 Objeto out

- derivado da ***classe JspWriter***, que permite dar saída aos dados. 
- utiliza um método chamado `print()` ou `println()` para imprimir as informações na tela.
	- `print()`: imprime as informações sem a quebra de linha.
	- `println()`: imprime as informações com uma quebra de linha.

~~~jsp
<%
	//Objeto out
	out.println("Objetos Implícitos JSP!");
%>
~~~

## 2.1.1 Objeto request

- um dos objetos mais importantes.
- responsável pela transmissão de parâmetros, atributos e redirecionamentos.
- derivado da classe HttpServletRequest, é responsável por realizar requisições internas e externas.
- para exemplificar, criadas duas páginas JSP: origem.jsp e destino.jsp para passar um parâmetro por meio do request.

~~~jsp
<!-- origem.jsp -->

<%@ page language="java" contentType="text/html; charset=ISO-8859-1" pageEncoding="ISO-8859-1"%>
<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>ORIGEM DOS DADOS</title>
</head>
<body>
	
	<!-- Link para o envio de parâmetro para a página origem.jsp -->
	<p><a href="destino.jsp?parametro1=JavaServer_Pages">ENVIO DOS DADOS<a></p>
	
</body>
</html>
~~~

~~~jsp
<!-- destino.jsp -->

<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
	pageEncoding="ISO-8859-1"%>
<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>DESTINO DOS DADOS</title>
</head>
<body>
	<!-- Bloco de Scriptlets para receber o parâmetro da página origem.jsp utilizando o objeto implícito request -->
	<% 
		String dados = request.getParameter("parametro1");
	%>
		<!-- Bloco de Expression para apresentar o parâmetro recebido -->
		<p>Parâmetro que foi enviado : <%=dados%></p>
</body>
</html>
~~~

## 2.1.2 Objeto response

- trabalha em conjunto com o request: sempre que for realizada uma requisição, deverá ser gerada uma resposta ao cliente! 
	- o request é o input (entrada) e o response é o output (saída).
- o objeto response deriva da classe HttpServletResponse e, assim como os demais objetos, pode ser utilizado implicitamente dentro dos blocos Scriptlets.
- com esse objeto, podemos controlar o refresh (atualização) da página, conforme o exemplo.

~~~jsp
<%
	response.setIntHeader("Refresh", 1);
%>
~~~

## 2.1.3 Objeto session


























--- 

[Voltar ao início!](https://github.com/monicaquintal/fintech)