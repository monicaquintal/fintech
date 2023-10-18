package br.com.fiap.bean;

import java.sql.Connection;
import java.sql.DriverManager;

public class EmpresaDBManager {

	public static Connection obterConexao() {
		
		Connection conexao = null;
		
		try {
		
			Class.forName("oracle.jdbc.driver.OracleDriver");
			conexao = DriverManager.getConnection("jdbc:oracle:thin:@oracle.fiap.com.br:1521:ORCL","login", "senha");

		} catch(Exception e) {
		
			e.printStackTrace();
		
		}
		
		return conexao;
		
	}
	
}
