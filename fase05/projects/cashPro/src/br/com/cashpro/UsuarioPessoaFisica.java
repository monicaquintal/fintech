package br.com.cashpro;

/**
 * Registra Usuários (Pessoas Físicas)
 * @author Monica Quintal
 * @version 1.0
 */

public class UsuarioPessoaFisica extends Usuario {
	
	  private String nome;
	  private String sobrenome;
	  private int cpf;
	  private String dataNascimento;

	  public UsuarioPessoaFisica() {
		  
	  }
	  
	/**
	 * Métodos Seletores e 
	 * Construtores da Classe 
	 * Usuário Pessoa Física
	 */
	  
	  public String getNome() {
		  return nome;
	  }
	  
	  public void setNome (String nome) {
		  this.nome = nome;
	  }
	  
	  public String getSobrenome() {
		  return sobrenome;
	  }
		  
	  public void setSobrenome (String sobrenome) {
		  this.sobrenome = sobrenome;
	  }
		  
	  public int getCpf() {
		  return cpf;
	  }
			  
	  public void setCpf (int cpf) {
		  this.cpf = cpf;
	  }
			  
	  public String getDataNascimento() {
		  return dataNascimento;
	  }
				  
	  public void setDataNascimento (String dataNascimento) {
		  this.dataNascimento = dataNascimento;
	  }
	  
	  /* Cadastra Pessoa Física
	   * @param dados pessoais: nome, sobrenome, cpf, nascimento, email, login e senha
	   * @void
	   */
	  
	  public void cadastrarPessoaFisica (String nome, String sobrenome, int cpf, String dataNascimento, String email, String login, String senha){
		  	this.nome = nome;
			this.sobrenome = sobrenome;
			this.cpf = cpf;
			this.dataNascimento = dataNascimento;
			getEmail();
			getLogin();
			getSenha();
	  }
	
}