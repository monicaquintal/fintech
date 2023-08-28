package br.com.fiap.tds;

public class ConversaoTiposPrimitivos {
	public static void main(String[] args) {
		int x = 10; //declaração de uma variável do tipo int
		double d = x; // variável double recebe um tipo int
		long l = x; // variável long recebe um tipo int
		float f = x; // variável float recebe um tipo int
		short s = 20; //declaração de uma variável do tipo short
		x = s; // variável int recebe um tipo short
		
		System.out.println(x); // 20
		System.out.println(d); // 10.0
		System.out.println(l); // 10
		System.out.println(f); // 10.0
		System.out.println(s); // 20
	}
}
