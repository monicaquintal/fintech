package br.com.cashpro;

/**
 * Registra Usuários (Pessoas Jurídicas)
 * @author Monica Quintal
 * @version 1.0
 */


public class UsuarioPessoaJuridica extends Usuario {
	
	  private String razaoSocial;
	  private int cnpj;

	  public UsuarioPessoaJuridica() {
		  
	  }
	  
	/**
	 * Métodos Seletores e 
	 * Construtores da Classe 
	 * Usuário Pessoa Jurídica
	 */
	  
	  public String getRazaoSocial() {
		  return razaoSocial;
	  }
	  
	  public void setRazaoSocial (String razaoSocial) {
		  this.razaoSocial = razaoSocial;
	  }
	  
	  public int getCnpj() {
		  return cnpj;
	  }
		  
	  public void setCnpj (int cnpj) {
		  this.cnpj = cnpj;
	  }
	  
	  /* Cadastra Pessoa Jurídica
	   * @param dados pessoais: cnpj, razao social, email, login e senha
	   * @void
	   */
	  
	  public void cadastrarPessoaJuridica (String razaoSocial, int cnpj, String email, String login, String senha){
		  	this.razaoSocial = razaoSocial;
			this.cnpj = cnpj;
			getEmail();
			getLogin();
			getSenha();
	  }
}