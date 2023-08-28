package br.com.fiap.tds;

public class OperadoresAritmeticos {
	public static void main (String[] args) {
		int x = 9;
		int y = 2;
		
		int soma = x + y;
		int subtracao = x - y;
		int multiplicacao = x * y;
		int divisao = x / y;
		int resto = x % y;
		
		System.out.println("Resultado da adição: " + soma);
		System.out.println("Resultado da subtração: " + subtracao);
		System.out.println("Resultado da multiplicação: " + multiplicacao);
		System.out.println("Resultado da divisão: " + divisao);
		System.out.println("Resultado do módulo: " + resto);
		
		x++;
		System.out.println("Resultado do incremento de x: " + x);
		y--;
		System.out.println("Resultado do decremento de y: " + y);
		
		x += 10;
		System.out.println("Resultado da atribuição aditiva: " + x);
		y -= 10;
		System.out.println("Resultado da atribuição subtrativa: " + y);
	}
}
