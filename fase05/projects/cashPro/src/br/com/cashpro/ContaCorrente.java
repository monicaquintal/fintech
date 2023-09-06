package br.com.cashpro;

/**
 * Classe que abstrai uma Conta Corrente
 * @author Monica Quintal
 * @version 1.0
 */

public class ContaCorrente extends Conta {
	
	private boolean possuiLimite;
	private double limite;
	private double taxaManutencao;
	
	/**
	 * Métodos Seletores e 
	 * Construtores da Classe 
	 * Conta Corrente
	 */
	
	
	public boolean getPossuiLimite() {
		return possuiLimite;
	}
	
	public void setPossuiLimite(boolean possuiLimite) {
		this.possuiLimite = possuiLimite;
	}
	
	public double getLimite() {
		return limite;
	}
	
	public void setLimite(double limite) {
		this.limite = limite;
	}
	
	public double getTaxaManutencao() {
		return taxaManutencao;
	}
	
	public void setTaxaManutencao(double taxaManutencao) {
		this.taxaManutencao = taxaManutencao;
	}
	
}
