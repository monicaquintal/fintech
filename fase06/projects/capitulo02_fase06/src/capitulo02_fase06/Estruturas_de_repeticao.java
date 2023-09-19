package capitulo02_fase06;

public class Estruturas_de_repeticao {
	public static void main(String[] args) {
		// 1. While
		int numero = 0;
		
		System.out.println("Utilizando WHILE:");
		while (numero < 10) {
			numero = numero + 1;
			System.out.println(numero);
		}
			
		
		
		// ------------------------------------------------------ //
		System.out.println("-------------------------------------");
		// ------------------------------------------------------ //
		
		
		
		// 2. Do-While
		int numero2 = 0;
		
		System.out.println("Utilizando DO-WHILE:");
		do {
			numero2 = numero2 + 1;
			System.out.println(numero2);
		} while (numero2 < 10);
		
		
		
		// ------------------------------------------------------ //
		System.out.println("-------------------------------------");
		// ------------------------------------------------------ //
		
		
		
		// 3. For
		
		System.out.println("Utilizando FOR:");
		for (int i = 0; i <= 10; i++) {
			System.out.println(i);
		}
		

		
		
		
		
		
		
		
	}

}
