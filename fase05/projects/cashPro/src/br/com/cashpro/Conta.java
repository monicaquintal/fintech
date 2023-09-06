package br.com.cashpro;

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
			this.agencia = agencia;
			this.numero = numero;
			this.saldo = saldo;
		}
		
		/**
		 * Métodos Seletores e 
		 * Construtores da Classe Conta
		 */
		
		public int getAgencia() {
			return agencia;
		}
		
		public void setAgencia(int agencia) {
			this.agencia = agencia;
		}
		
		public int getNumero() {
			return numero;
		}
		
		public void setNumero(int numero) {
			this.numero = numero;
		}
		
		public void setSaldo(double saldo) {
			this.saldo = saldo; 
		}
		
		public double getSaldo() {
			return this.saldo;
		}
		
}