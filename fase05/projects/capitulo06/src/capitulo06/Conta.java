package capitulo06;

public class Conta {
	public static void main (String[] args) {
	
	Conta cc = new Conta();
	Conta poupanca = new Conta();
	
	  int numero;
	  int agencia;
	  double saldo;
	  // Calendar dataAbertura;
	  String tipo;
	  // Cliente cliente;
	
	}
		
	/* ----------------------- */
	
	
	public double recuperarSaldo() {
		return saldo;
	}
	
	public void depositar(int agencia, String numeroConta, double valor) {
		saldo = saldo + valor;
	}
	
	public double somar(double valor1, double valor2) {
		return (valor1 + valor2);
	}
	
	/* ----------------------- */
	
	public void retirar(double valor) {
		saldo = saldo - valor;
	}
	
	public void retirar(double valor, double taxa) {
		saldo = saldo - valor - taxa;
	}
	
	/* ----------------------- */
	
	int agencia;

	public void setAgencia (int agencia) {
		this.agencia = agencia;
	}
	
	/* ----------------------- */
	
	double saldo;
	
	public Conta(double saldo) {
		this.saldo = saldo;
		System.out.println("Criando uma instância de conta!");
		
		new Conta(100);
	}
	
	
}
