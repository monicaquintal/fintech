package br.com.cashpro;

	/**
	 * Registra Operações realizadas na Conta
	 * @author Monica Quintal
	 * @version 1.0
	 */

	public class Operacao extends Conta {	
		
		private String tipo;
		private String data;
		private String categoria;
		private double valor;
		
		public Operacao() {
			
		}
		
		public Operacao(String tipo, String data, String categoria, double valor, double saldo){
			super();
			this.tipo = tipo;
			this.data = data;
			this.categoria = categoria;
			this.valor = valor;
		}
		
		/**
		 * Métodos Seletores e 
		 * Construtores da Classe Operação
		 */
		
		public String getTipo() {
			return tipo;
		}
		
		public void setTipo(String tipo) {
			this.tipo = tipo;
		}
		
		public String getData() {
			return data;
		}
		
		public void setData(String data) {
			this.data = data;
		}
		
		public String getCategoria() {
			return categoria;
		}
		
		public void setCategoria(String categoria) {
			this.categoria = categoria;
		}
		
		public double getValor() {
			return valor;
		}
		
		public void setValor(double valor) {
			this.valor = valor;
		}
		
		/**
		 * Verifica o Saldo da Conta
		 * @return Valor do Saldo da Conta
		 */
		
		public double getSaldoDisponivel() {
			return getSaldo() + this.valor;
		}
		

		
}