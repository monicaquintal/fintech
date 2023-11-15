<%@ page language="java" contentType="text/html; charset=ISO-8859-1" pageEncoding="ISO-8859-1"%>
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