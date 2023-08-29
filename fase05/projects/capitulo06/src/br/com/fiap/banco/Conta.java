package br.com.fiap.banco;
/**
 * Classe que abstrai uma Conta Bancária
 * @author Monica Quintal
 * @version 1.0
 */
public class Conta {
	
	/**
	 * Número da conta
	 */
	private int numero;
	
	/**
	 * Número da Agência
	 */
	private int agencia;
	
	/**
	 * Saldo da Conta
	 */
	private double saldo;
	
	
	public Conta(){
		
	}
	
	public Conta(int numero, int agencia, double saldo){
		this.setNumero(numero);
		this.setAgencia(agencia);
		this.setSaldo(saldo);
	}
	
	/**
	 * Acrescenta valor ao Saldo da Conta
	 * @param valor que será depositado
	 */
	public void depositar(double valor){
		this.setSaldo(this.getSaldo() + valor);
	}
	
	/**
	 * Retira um valor do Saldo da Conta
	 * @param valor
	 */
	public void retirar(double valor){
		this.setSaldo(this.getSaldo() - valor);
	}
	
	public int getNumero() {
		return numero;
	}
	
	public void setNumero(int numero) {
		this.numero = numero;
	}
	
	public int getAgencia() {
		return agencia;
	}
	
	public void setAgencia(int agencia) {
		this.agencia = agencia;
	}
	
	public double getSaldo() {
		return saldo;
	}
}