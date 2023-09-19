package capitulo02_fase06;

import java.util.Scanner;

public class Exemplo_For {
	public static void main (String[] args) {
		Scanner scanner = new Scanner(System.in);
		
		float[] notas = new float[4];
		float totalNotas = 0;
		
		for (int i = 0; i < notas.length; i++) {
			System.out.println("Digite a nota do aluno: ");
			notas[i] = scanner.nextFloat();
			totalNotas = totalNotas + notas[i];
		}
		
		float mediaNotas = totalNotas / notas.length;
		System.out.println("A média dos alunos é: "+ mediaNotas);
		
		scanner.close();
	}
}
