package br.com.cashpro;

/**
 * Registra Usuários
 * @author Monica Quintal
 * @version 1.0
 */

public class Usuario {
	
	  private String email;
	  private String login;
	  private String senha;

	  public Usuario() {
		  
	  }
	  		  
	/**
	 * Métodos Seletores e 
	 * Construtores da Classe Usuário
	 */
	  
	  public String getEmail() {
		  return email;
	  }
	  
	  public void setEmail (String email) {
		  this.email = email;
	  }
	  
	  public String getLogin() {
		  return login;
	  }
	  
	  public void setLogin (String login) {
		  this.login = login;
	  }
	  
	  public String getSenha() {
		  return senha;
	  }
	  
	  public void setSenha (String senha) {
		  this.senha = senha;
	  } 
	  
}