package br.com.fiap.tds;

import java.util.Scanner;

public class LeituraDeDados {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.print("Informe o seu peso: ");
		float peso = sc.nextFloat();
		System.out.println("Peso informado: " + peso);
		sc.close();
	}
}