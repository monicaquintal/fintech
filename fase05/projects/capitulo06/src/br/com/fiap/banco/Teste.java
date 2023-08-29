package br.com.fiap.banco;

public class Teste {
	public static void main(String[] args) {
		Conta cc = new Conta();
		cc.saldo = 50;
		cc.agencia = 123;
		cc.numero = 321;
		
		cc.depositar(100);
		
		System.out.println(cc.verificarSaldo());
		
		Conta poupanca = new Conta (111, 222, 1000);
		
		poupanca.retirar(50);
		
		System.out.println(poupanca.verificarSaldo());
		
	}
}
