<div id="fase05" align="center">
<h1>FASE 5 - OOP</h1>
<h2>Capítulo 08: Como a herança pode me ajudar a programar melhor? 🤔</h2>
</div>

<div align="center">
<h2>1. COMO A HERANÇA PODE ME AJUDAR A PROGRAMAR MELHOR?</h2>
</div>

## 1.1 Introdução

- ao desenvolver um sistema:
  - lembrar da manutenção e evolução da aplicação.
  - escrever código limpo, bem formatado, estruturado e documentado.
  - evitar o código duplicado.

## 1.2 Herança

- é um dos principais pilares da programação orientada a objetos.
- a ideia é criar classes com base em classes existentes: 
  - a classe que for criada herdará todos os comportamentos e atributos de uma classe já existente.
  - também é possível alterar os comportamentos existentes da classe pai.

> Uma classe que herda de outra classe é chamada de `subclasse`, e a classe herdada é chamada de `superclasse`.

- a herança é utilizada como uma forma de reutilizar atributos e métodos de classes já definidas, permitindo derivar uma nova classe mais especializada a partir de outra classe mais genérica existente.

> Uma classe só pode ter uma superclasse (não é possível ter herança múltipla). Porém, uma classe pode ter um número ilimitado de subclasses. 

- uma subclasse recebe todas as características da superclassee de todas as outras classes acima dela. 
- a hierarquia de classes se inicia com a `classe Object`, isto é, todas as classes a herdam direta ou indiretamente.
- a `palavra-chave extends` é utilizada na declaração de uma classe para determinar a sua superclasse. 
  - caso a classe não tenha a palavra-chave em sua declaração, a herança que existe é diretamente da classe Object.

Sintaxe:

~~~java
[public] class <subclasse> extends <superclasse> {
  ...
}
~~~

## Praticando:

> ajustar a classe Conta para que ela possua as subclasses ContaCorrente e ContaPoupanca. A classe Conta continuará herdando da classe Object.

- a ***classe ContaCorrente*** possui o atributo tipo de conta, que define se a conta é básica, especial ou premium. Já a ContaPoupanca não possui esse tipo de definição.

~~~java
package br.com.fiap.tds;

public class ContaCorrente extends Conta {
// 
}
~~~

- após definir que a classe ContaCorrente é uma subclasse de Conta, vamos adicionar um atributo para definir o tipo de conta-corrente.

~~~java
package br.com.fiap.tds;

public class ContaCorrente extends Conta {
  private String tipo;

  public String getTipo() {
    return tipo;
  }
  
  public void setTipo(String tipo) {
    this.tipo= tipo;
  }
}

// utilizado o encapsulamento para proteger o atributo "tipo" de conta-corrente.
~~~

- adicionar outro atributo que será utilizado para armazenar o valor do cheque especial, ou seja, o valor que o cliente pode utilizar junto do saldo da conta.

~~~java
package br.com.fiap.banco;

public class ContaCorrente extends Conta {
	private String tipo;
	private double chequeEspecial;
	
	public String getTipo() {
		return tipo;
	}
	
	public void setTipo(String tipo) {
		this.tipo= tipo;
	}
	
	public double getChequeEspecial() {
		return chequeEspecial;
	}
	
	public void setChequeEspecial(double chequeEspecial) {
		this.chequeEspecial= chequeEspecial;
	}
}
~~~

- adicionar métodos específicos na classeContaCorrente.
- uma conta-corrente tem o comportamento de retornar o saldo disponível, que é a soma do saldo da conta com o limite do cheque especial:

~~~java
package br.com.fiap.banco;

public class ContaCorrente extends Conta {
	private String tipo;
	private double chequeEspecial;
	
	public String getTipo() {
		return tipo;
	}
	
	public void setTipo(String tipo) {
		this.tipo= tipo;
	}
	
	public double getChequeEspecial() {
		return chequeEspecial;
	}
	
	public void setChequeEspecial(double chequeEspecial) {
		this.chequeEspecial= chequeEspecial;
	}
	
	public double getSaldoDisponivel(){
		return getSaldo() + this.chequeEspecial;
	}
}
~~~








--- 

[Voltar ao início!](https://github.com/monicaquintal/fintech)