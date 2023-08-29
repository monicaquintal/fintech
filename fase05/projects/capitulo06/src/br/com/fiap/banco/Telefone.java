package br.com.fiap.banco;

public class Telefone {
	private String ddd;
	private String numero;
	
	//métodos gets e sets
	public String getTelefoneFormatado(){
		return formatarTelefone(ddd,numero);
	}
	
	private String formatarTelefone(String ddd, String numero){
		return "(" + ddd + ") " + numero;
	}
}
