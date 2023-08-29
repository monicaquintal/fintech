package br.com.fiap.banco.teste;

import br.com.fiap.banco.Conta;

public class Teste {
	
	public static void main(String[] args) {
		
		Conta cc = new Conta();
		cc.setSaldo(50);
		cc.setAgencia(123);
		cc.setNumero(321);
		
		cc.depositar(100);
		
		System.out.println(cc.verificarSaldo());
		
		Conta poupanca = new Conta(254, 123, 1000);
		
		poupanca.retirar(50);
		
		System.out.println(poupanca.verificarSaldo());
	}
	
}