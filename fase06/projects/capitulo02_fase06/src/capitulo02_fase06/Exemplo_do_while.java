package capitulo02_fase06;

import java.util.Scanner;

public class Exemplo_do_while {
	public static void main (String[] args) {
		Scanner sc = new Scanner(System.in);
		
		String opcao;
		do {
			System.out.println("Digite um número: ");
			int n1 = sc.nextInt();
			System.out.println("Digite outro número: ");
			int n2 = sc.nextInt();
			int soma = n1 + n2;
			System.out.println("A soma é: "+ soma);
			System.out.println("Deseja somar outro número? (S/N)");
			opcao = sc.next();
		} while (opcao.equals("S"));
		
		sc.close();
	}
}
