package br.com.cashpro;

/**
 * Classe que abstrai uma Conta Poupança
 * @author Monica Quintal
 * @version 1.0
 */

public class ContaPoupanca extends Conta {
	
	private double taxaJurosAnual;
	
	/**
	 * Métodos Seletores e 
	 * Construtores da Classe 
	 * Conta Poupança
	 */
	
	public double getTaxaJurosAnual() {
		return taxaJurosAnual;
	}
	
	public void seTaxaJurosAnual(double taxaJurosAnual) {
		this.taxaJurosAnual = taxaJurosAnual;
	}
	
}