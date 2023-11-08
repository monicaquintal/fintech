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

- deriva da classe HttpSession e é criado a partir do primeiro request do cliente para o servidor. 
- possui um ciclo de vida maior do que o request, permitindo adicionar atributos que permanecerão enquanto o cliente estiver conectado ao sistema.
- as duas formas de terminar uma sessão do usuário são por `timeout` (por tempo de inatividade do usuário no sistema), e por um `método do próprio objeto de sessão`, que pode ser utilizado na funcionalidade de logout, por exemplo.
- o objeto session é muito utilizado nos sistemas para identificar o usuário na aplicação.
- exemplo: páginas login.jsp, index.jsp e servicos.jsp.
	- no login, colocar o nome do usuário na sessão e replicar esse atributo pelas páginas, capturando-o em cada uma delas.

~~~html
<!-- Página login.jsp com o objeto session sendo criado -->

<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>Exemplo Sessão</title>
</head>
<body>
	<%
	   if(request.getParameter("nomeUsuario") != null)
		session.setAttribute("attrUsuario", request.getParameter("nomeUsuario"));
	%>
	<form method="post" action="login.jsp">
		<fieldset>
			<legend>Login</legend>
			<div>
				<label>Nome de Usuário</label><br/>
				<input type="text" name="nomeUsuario">
			</div>
			<div>
				<label>Senha</label><br/>
				<input type="password" name="senha">
			</div>
			<div>
				<input type="submit" value="LOGIN">
			</div>
		</fieldset>
	</form>
	
	<p><a href="servicos.jsp">SERVIÇOS</a></p>
	<p><a href="index.jsp">INÍCIO</a></p>
	
</body>
</html>
~~~ 

~~~html
<!-- Página index.jsp recebendo o atributo que foi criado na sessão -->

<h2>Bem vindo usuário [<%=session.getAttribute("attrUsuario")%>] 
	a página Inicial do Sistema!</h2>
<p><a href="servicos.jsp">SERVIÇOS</a></p>
<p><a href="login.jsp">LOGIN</a></p>
~~~

~~~html
<!-- Página serviços.jsp recebendo o atributo que foi criado na sessão -->

<h2>Bem vindo usuário [<%=session.getAttribute("attrUsuario")%>] 
	a página de Serviços do Sistema!</h2>
	
<p><a href="index.jsp">INÍCIO</a></p>
<p><a href="login.jsp">LOGIN</a></p>
~~~

## 2.2 Objeto application

- criado assim que o servidor é inicializado e removido logo que o servidor é finalizado.
- um atributo no objeto application fica disponível para todas as páginas e usuários da aplicação web.
- exemplo: contador de visitas. 
	- utilizar:
		- método application.setAttribute(String Key, Object Value); para definir um atributo no objeto application;
		- método application.getAttribute(String Key); para recuperar esse valor que foi armazenado.
	- primeiro recupera o valor do atributo armazenado no objeto application e depois valida se está vazio ou com o valor 0. Caso esteja vazio ou zero, o contador é inicializado com o valor 1, caso contrário, o contador é incrementado em 1. Depois o valor é adicionado novamente na application e, finalmente, é apresentado na página por meio da expression.

~~~jsp
<%
	Integer hitsCount = (Integer)application.getAttribute("hitCounter");
	if( hitsCount == null || hitsCount == 0 ) {
			/* First visit */
			out.println("Welcome to my website!");
			hitsCount = 1;
	} else {
			/* return visit */
			out.println("Welcome to my website!");
			hitsCount += 1;
	}
	application.setAttribute("hitCounter", hitsCount);
%>
<p>Total number of visits: <%= hitsCount %></p>
~~~

## 2.3 Objeto pageContext

- utilizado como um meio de acesso às informações da página. 
- está em contato direto com a parte da memória que lida com os erros gerados por meio da URL, bem como o `errorPageURL` (códigos de erros gerados por meio das páginas, como Erro - 404).
- permite acesso a todos os outros objetos já citados anteriormente e diversos métodos, com destaque para o método `removeAttribute`, que aceita um ou dois argumentos.
	- exemplo: "pageContext.removeAttribute("attrName");" remove o atributo de todos os escopos, bem como PAGE_SCOPE, REQUEST_SCOPE, SESSION_SCOPE e APPLICATION_SCOPE.
	- enquanto o código a seguir remove apenas do escopo de página: "pageContext.removeAttribute("attrName", PAGE_SCOPE);"
- no segundo argumento, determinar o escopo alvo de onde queremos remover o atributo. 
- lembrando que esses métodos devem ser chamados dentro de Scriptlets!

## 2.4 JSP actions

- usam tags na sintaxe XML para controlar o comportamento do mecanismo da Servlet.
- é possível inserir dinamicamente um arquivo, reutilizar componentes JavaBeans, encaminhar o usuário para outra página ou gerar HTML dinamicamente, etc.
- há apenas uma sintaxe para o elemento Action, já que está em conformidade com padrão XML:

~~~xml
<jsp:action_name attribute="value" />
~~~

- os elementos das Actions são basicamente funções predefinidas. 
- algumas das mais importantes:

### 2.4.1 Action &lt;jsp:include&gt;

- permite inserir outros arquivos na página que está sendo gerada.
- sintaxe:

~~~xml
<jsp:include page="menu.jsp" />
~~~

- é muito útil quando se trata de modularizar a aplicação, ou seja, fazer de sua página um verdadeiro "lego".
- exemplo:

~~~xml
<!-- pagina_inicio.jsp -->

<body>
<!-- Aqui está inserido o menu. -->
<nav> <jsp:include page="menu.jsp"></jsp:include> </nav>
<hr/>
<p>Conteúdo da página</p>
</body>
~~~

~~~html
<!-- SNIPPET menu.jsp -->
<p>SCRIPTS WEB</p>
<ul>
	<li>JSP</li>
	<li>ASP</li>
	<li>PHP</li>
	<li>CFM</li>
	<li>CGI</li>
</ul>
~~~

- a Action e a Directiva include produzem o mesmo resultado, com algumas pequenas diferenças: 
	- a Directiva include insere o JSP no tempo de compilação, assim gera somente uma Servlet.
	- a Action include insere o JSP em tempo de execução, dessa forma gera uma Servlet para cada JSP. Também pode inserir além de JSP, Servlets e HTML.
- ou seja, podemos utilizar qualquer um dos métodos para adicionar o menu na aplicação. O importante é não duplicar os códigos!!!

### 2.4.2 Action &lt;jsp:forward&gt;

- utilizada para transferir permanentemente o controle para outro local,onde a propriedade page indicar (redirecionar o cliente para qualquer lugar da aplicação). 
- o local sempre é indicado por uma URL relativa. 
- exemplo de redirecionamento:

~~~xml
<body>
	<jsp:forward page="sucesso.jsp"/>
</body>
~~~

- exemplo, implementando uma página que envia e encaminha dois parâmetros para outra página.

~~~xml
<!-- Sintaxe Action forward com parâmetros com URL relativa -->
<jsp:forward page="index.jsp">
	<jsp:param value="Jorginho" name="nome"/>
	<jsp:param value="25" name="idade"/>	
</jsp:forward>

<!-- Página index.jsp recebendo os parâmetros da Action forward -->
<p>Nome :<%=request.getParameter("nome")%></p>
<p>Idade :<%=request.getParameter("idade")%></p>
~~~

- o endereço na barra do navegador será o da página inicial, e não o da página que está na Action forward.
- a URL não muda pelo fato de o contexto da página atual ser encaminhado ao alvo, dando oportunidade para recuperar as informações que foram enviadas.

---

## 2.5 Prática

> s desenvolver algumas páginas JSP para criar um menu e separar as partes comuns a todas as páginas, ganhando na produtividade e na manutenção de nossas páginas.

1. Criar um projeto. Clique na opção “File” > “New” > “Dynamic Web Project”.
2. Dar um nome ao projeto (“JSPs”). Não esquecer de configurar o servidor. Clique em “New Runtime...”, escolha a opção “Apache Tomcat v9.0”, configure o caminho onde o servidor está em sua máquina, por meio do botão “browser” e finalize o processo.
3. Depois de configurar o nome do projeto e o servidor, clicar no botão “Next”. Na última tela, marque a opção de criar o arquivo “web.xml” e Content Directory "WebContent".
4. Para construir a interface do sistema Fintech, iremos utilizar o bootstrap. Baixar os arquivos no [site](http://getbootstrap.com/), clicar para obter o CSS e JS compilados.
5. Para deixar a aplicação organizada, criar uma pasta para agrupar os arquivos de css, javascript, imagens, ícones etc. Clique com o botão direito do mouse na pasta “Web Content” e escolha a opção “New” > “Folder”.
		- a pasta pode possuir qualquer nome, porém os arquivos css e js geralmente ficam em uma pasta chamada “resources”, ou recursos. 
		- copiar os arquivos para dentro dessa pasta. Dentro da pasta resources, deixar a separação dos arquivos javascript e css, cada um em sua respectiva pasta.
6. Não esquecer que o bootstrap depende do [Jquery](https://jquery.com/), por isso precisamos copiar o arquivo do Jquery para dentro da pasta resources/js.
7. Criar uma página JSP para adicionar o código de &lt;link&gt; e &lt;script&gt; que se repetem, e fazer com que as outras páginas JSP a utilizem. Assim, caso seja necessária alguma alteração, basta modificar essa página.
		- criar o JSP para ter o link do css. Clique com o botão direito do mouse na pasta “Web Content” e escolha a opção “New” > “JSP File”,colocar o nome de “header” e finalizar o processo.
		- como as outras páginas vão “incluir” o código dessa página, não é necessário que tenha a estrutura completa de uma página HTML: como vamos utilizar somente o css do boostrap, adicionaremoso link para esse css. É aqui que você também pode adicionar o link para o seu arquivo de css para customização.

~~~xml
<link rel="stylesheet" type="text/css" href="resources/css/bootstrap.min.css">
~~~

> Porque esse código não tem os javascripts? Esse JSP deve ser “incluído” no cabeçalho (head) das páginas, e é recomendado adicionar os javascripts no final da página, já que uma página é carregada de cima para baixo e é melhor carregar primeiramenteas informações visuais, para dar a sensação de que a página é carregada mais rápido.

8. Criar outra página JSP (footer.jsp) para adicionar os javascripts, que possa ser incluída no final das páginas.

~~~xml
<script type="text/javascript" src="resources/jquery-3.7.1.min.js"></script>
<script type="text/javascript" src="resources/js/bootstrap.min.js"></script>
~~~

9. Criar uma página de exemplo, que será a página inicial da aplicação, e terá a estrutura completa de uma página. No cabeçalho, vamos incluir a página header.jsp, e no final, vamos incluir o código da página footer.jsp.

~~~xml
<%@ page language="java" contentType="text/html; charset=ISO-8859-1" pageEncoding="ISO-8859-1"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>Home - JSPs</title>
<%@ include file="header.jsp" %>
</head>
<body>
	<div class="container">
		<h1>JSP - Java ServerPages</h1>
		<p>Hello World!</p>
	</div>
	<%@ include file="footer.jsp" %>
</body>
</html>
~~~

10. Criar um menu para a aplicação. Crie um novo jsp, chamado de “menu.jsp”. Nesse menu, adicione o código da navbar do bootstrap. Adicionar o include na página inicial.

~~~xml
<!-- menu.jsp -->

<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
  <a class="navbar-brand" href="#">Navbar</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarSupportedContent">
    <ul class="navbar-nav mr-auto">
      <li class="nav-item active">
        <a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#">Link</a>
      </li>
      <li class="nav-item">
        <a class="nav-link disabled" href="#">Disabled</a>
      </li>
    </ul>
    <form class="form-inline my-2 my-lg-0">
      <input class="form-control mr-sm-2" type="text" placeholder="Search" aria-label="Search">
      <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
    </form>
  </div>
</nav>
~~~

~~~xml
<!-- adicionando incluse na página inicial -->

<%@ page language="java" contentType="text/html; charset=ISO-8859-1" pageEncoding="ISO-8859-1"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>Home - JSPs</title>
<%@ include file="header.jsp" %>
</head>
<body>
	<%@ include file="menu.jsp" %>
	<div class="container">
		<h1>JSP - Java ServerPages</h1>
		<p>Hello World!</p>
	</div>
	<%@ include file="footer.jsp" %>
</body>
</html>
~~~

---

## FAST TEST

### 1. Qual é o objeto implícito responsável pela transmissão de parâmetros, atributos e redirecionamentos? 
> Objeto request.

--- 

[Voltar ao início!](https://github.com/monicaquintal/fintech)