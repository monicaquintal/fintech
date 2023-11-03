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












--- 

[Voltar ao início!](https://github.com/monicaquintal/fintech)