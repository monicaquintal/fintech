package br.com.cashpro;

public class Teste {
	public static void main(String[] args) {
		
		/*
		 * Instanciando um Objeto do tipo Conta Corrente:
		 */
		
		ContaCorrente cc = new ContaCorrente();
		
		/*
		 * Atribuindo valores:
		 */
		
		cc.setAgencia(1111);
		cc.setNumero(2222);
		cc.setSaldo(1000);
		cc.setLimite(100);

		/*
		 * Verificando se o objeto "Conta Corrente" é do tipo da classe Conta, 
		 * utilizando a instrução instanceof. 
		 */
		
		if (cc instanceof Conta){
			System.out.println("cc é do tipo Conta");
		} else {
			System.out.println("cc não é do tipo Conta");
		}
		
		if (cc instanceof ContaCorrente){
			System.out.println("cc é do tipo ContaCorrente");
		} else {
			System.out.println("cc não é do tipo ContaCorrente");
		}
		
		System.out.println("---------------------------");
		
		/*
		 * Invocando métodos
		 */
		
		System.out.println("Número da agência: " + cc.getAgencia());
		System.out.println("Número da conta: " + cc.getNumero());
		System.out.println("Saldo: " + cc.getSaldo());
		System.out.println("Limite da Conta Corrente: " + cc.getLimite());
		
		System.out.println("---------------------------");
		
		// ------------------------------------------------------------------- //
		
		/*
		 * Instanciando um Objeto do tipo Operacao:
		 */
		
		Operacao op = new Operacao();
		
		/*
		 * Atribuindo valores:
		 */
		
		op.setValor(-10);
		op.setSaldo(100);
		
		/*
		 * Invocando método que verifica o saldo disponível:
		 * getSaldoDisponivel()
		 */

		System.out.print("O saldo disponível, após operação no valor de " + op.getValor() + " reais, será de " + op.getSaldoDisponivel() + " reais.");
		
	}
	
	
}
