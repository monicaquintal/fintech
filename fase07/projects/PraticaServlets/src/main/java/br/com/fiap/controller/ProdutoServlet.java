package br.com.fiap.controller;

import java.io.IOException;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 * Servlet implementation class ProdutoServlet
 */
@WebServlet("/produto")
public class ProdutoServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public ProdutoServlet() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		int codigo = Integer.parseInt(request.getParameter("codigo"));
		
		System.out.println("Coódigo: " + codigo);
		
		request.setAttribute("cod", codigo);
		request.setAttribute("nome", "Hello!");
		
		request.getRequestDispatcher("busca-produto.jsp").forward(request, response);
	}

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub

		// Recuperar os parâmwetros do formulário HTML
		String nome = request.getParameter("nome");
		int qtd = Integer.parseInt(request.getParameter("quantidade"));
		double valor = Double.parseDouble(request.getParameter("valor"));
		
		// Exibe os valores no console
		System.out.println(nome + " " + qtd + " " + " " + valor);
		
		// Adiciona atributos no request para exibir na página
		request.setAttribute("nomeProduto", nome);
		request.setAttribute("quantidade", qtd);
		request.setAttribute("valorProduto", valor);
		
		request.getRequestDispatcher("sucesso.jsp").forward(request, response);
	}

}
