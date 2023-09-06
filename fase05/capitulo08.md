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

---

## 1.2 Herança

- é um dos principais pilares da programação orientada a objetos.
- a ideia é criar classes com base em classes existentes: 
  - a classe que for criada herdará todos os comportamentos e atributos de uma classe já existente.
  - também é possível alterar os comportamentos existentes da classe pai.

> Uma classe que herda de outra classe é chamada de `subclasse`, e a classe herdada é chamada de `superclasse`.

- a herança é utilizada como uma forma de reutilizar atributos e métodos de classes já definidas, permitindo derivar uma nova classe mais especializada a partir de outra classe mais genérica existente.

> Uma classe só pode ter uma superclasse (não é possível ter herança múltipla de classes, apenas de interfaces). Porém, uma classe pode ter um número ilimitado de subclasses. 

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

- o método retorna o valor da soma do cheque especial com o saldo da conta. 
	- para acessar o saldo da conta foi necessário utilizar o método getSaldo(), pois o atributo saldo está definido na classe pai como private, por isso, não é visível na classe filha.

### Podemos utilizar um objeto de uma subclasse sempre que o programa esperar por um objeto da superclasse:

- logo, é possível atribuir um objeto do tipo Conta-Corrente em uma variável do tipo Conta!
- exemplo:

~~~java
Conta conta = new Conta();
Conta cc = new ContaCorrente();
~~~

- as variáveis que armazenam uma referência a um objeto são polimórficas. 
	- ou seja, uma variável de uma superclasse pode receber qualquer objeto de suas subclasses!
- podemos atribuir o objeto que está referenciado na variável cc a uma variável do tipo ContaCorrente, para isso é necessário realizar um cast:

~~~java
ContaCorrente c1 = (ContaCorrente) cc;
~~~

- `cast` é forçar um objeto a ser de outro tipo em um momento.
- neste caso, forçamos o objeto a ser do tipo ContaCorrente para atribuirmos em uma variável do tipo ContaCorrente. 
- o cast é composto pelos parênteses () e a classe que queremos forçar o objeto a se transformar naquele momento.
- se tentarmos realizar o cast e o objeto não for do tipo ou subtipo da classe que queremos forçar, o Java irá lançar a exceção ClassCastException:

~~~java
ContaCorrente c2 = (ContaCorrente) conta;
~~~

- a variável conta faz referência a um objeto do tipo Conta e não do tipo ContaCorrente. Assim, a exceção será lançada.
- para verificar se o objeto é do tipo de uma classe, podemos utilizar a `instrução instanceof`. 
	- retorna true caso o objeto à esquerda do operador seja do tipo (classe) especificado à direita do operador.
	- exemplo testando se a variável cc possui um objeto do tipo Conta:

~~~java
package br.com.fiap.tds;
public class Program {
	public static void main(String[] args){
		Conta cc = new Conta();
		if(cc instanceof Conta) {
			System.out.println("cc é do tipo Conta");
		} else {
			System.out.println("cc não é do tipo Conta");
		}
	}
}
// resultado: “cc é do tipo Conta”!
~~~

- se alterarmos o programa para instanciar um objeto do tipo ContaCorrente ao invés do tipo Conta:

~~~java
package br.com.fiap.tds;
public class Program {
	public static void main(String[] args) {
		Conta cc = new ContaCorrente();
		if(cc instanceof Conta) {
			System.out.println("cc é do tipo Conta");
		} else {
			System.out.println("cc não é do tipo Conta");
		}
	}
}
// a resposta é que cc é do tipo conta, pois uma ContaCorrente também é uma Conta!
~~~

- se alterar novamente o programa:

~~~java
package br.com.fiap.tds;
public class Program {
	public static void main(String[] args) {
		Conta cc = new Conta();
		if(cc instanceof ContaCorrente) {
			System.out.println("cc é do tipo ContaCorrente");
		} else {
			System.out.println("cc não é do tipo ContaCorrente");
		}
	}
}
// a resposta é “cc não é do tipo Conta Corrente”,pois uma Conta não é necessariamente uma ContaCorrente.
~~~

---

## 1.3 Sobrescrita de métodos

- outra diferença é que, neste exemplo, para a conta poupança não há taxa para efetuar um saque. 
- na conta-corrente existe uma taxa para a retirada de dinheiro.
- portanto, precisamos sobrescrever o comportamento do método retirar na classe ContaCorrente. 

> Sobrescrever um método é redefinir na subclasse um método existente na superclasse. 

- assim, quando o método retirar for chamado de um objeto do tipo ContaCorrente, o método chamado será o retirar definido na classe ContaCorrente e não da classe Conta.
- poranto, implementar na classe ContaCorrente um método retirar que tenha a mesma assinatura do método retirar da classe Conta.

~~~java
@Override
public void retirar(double valor){
	valor = valor + 10;
	super.retirar(valor);
}
~~~

- a `anotação @Override` marca o método, identificando que está sobrescrevendo um método de sua superclasse.
- o método "retirar" soma a taxa de retirada (10) ao valor a ser subtraído do saldo. 
- como não temos acesso direto ao saldo e não podemos alterar o seu valor na subclasse (não existe o método setSaldo() na classe Conta), precisamos usar o método retirar que está na classe Conta. 
- a palavra super é utilizada para referenciar a superclasse, assim a instrução super.retirar(valor)está chamando o método retirar que está na classe Conta.

~~~java
package br.com.fiap.tds;
public class Conta {
	public void retirar(doublevalor){
		saldo = saldo – valor;
	}
}

public class ContaCorrente extends Conta {
	@Override 
	public void retirar(double valor){
		valor = valor + 10;
		super.retirar(valor);
	}
}
~~~

- isso faz parte de um dos pilares da Orientação a Objetos: o `polimorfismo`.
	- a palavra polimorfismo significa "várias formas".
	- na orientação a objetos, representa que um objeto pode ser referenciado de várias formas.
- quando sobrescrevemos um método na subclasse, o que determina se o método que será chamado é da subclasse ou da superclasse é o tipo de instância do objeto.
- exemplo:

~~~java
Conta conta = new Conta();
conta.retirar(100);
// o método chamado será o definido na classe Conta
~~~

~~~java
ContaCorrente conta = new ContaCorrente();
conta.retirar(100);
// o método chamado será o definido na classe ContaCorrente
~~~

~~~java
Conta conta = new ContaCorrente();
conta.retirar(100);
// o método definido na ContaCorrente será invocado, pois o objeto que está em conta é do tipo ContaCorrente.
~~~

> podemos redefinir o comportamento de uma classe em sua subclasse e, assim, um objeto pode se comportar de maneira diferente ao invocar um método, dependendo do seu tipo de criação.

---

## 1.4 Construtores em Classes Estendidas

- construtores das subclasses sempre precisam chamar um construtor da superclasse (a `instrução super` é utilizada).
- atentar-se aos exemplos abaixo:

~~~java
public class Conta{
};
~~~

~~~java
public class ContaCorrente extends Conta {
};
~~~

- atributos e métodos foram omitidos para focarmos nos construtores.
- `essas classes possuem construtores`.
	- apesar de não estar definido, possuem o construtor padrão (sem argumentos) que é fornecido pelo Java. 
- o construtor padrão chama o construtor da superclasse direta (o construtor da classe ContaCorrente chama o construtor da classe Conta e o construtor da classe Conta chama o construtor da classe Object).
- definir um construtor para a classe ContaCorrente, o qual recebe como parâmetro o valor do tipo da Conta:

~~~java
package br.com.fiap.tds;
public class ContaCorrente extends Conta {
	private String tipo;
	public ContaCorrente(String tipo){
		this.tipo = tipo;
	}
}
~~~

- agora temos um construtor para a classe ContaCorrente.
	- esse construtor chama o construtor de sua  superclasse, feito automaticamente pelo Java, pois a classe Conta possui o construtor padrão. 
	- logo, ainstrução super() na primeira linha do construtor é redundante, pois o Java irá fornecer a instrução caso não seja definido!

~~~java
package br.com.fiap.tds;
public class ContaCorrente extends Conta {
	private String tipo;
	public ContaCorrente(String tipo) {
		super();
		this.tipo= tipo;
	}
}
~~~

- `outras duas regras dos construtores` são: 
	- 1) Não são herdados. 
	- 2) A chamada do construtor da superclasse deve ser sempre feita na primeira linha do construtor da subclasse.
- logo, se implementarmos um construtor que recebe um parâmetro na classe Conta, a classe ContaCorrente não vai herdar esse construtor:

~~~java
package br.com.fiap.tds;
public class Conta {
	private int numero;
	public Conta (int numero){
		this.numero = numero;
	}
}
~~~

- a partir do momento em que implementamos esse construtor na classe Conta, a classe ContaCorrente começa a exibir um erro de compilação.
- oisso ocorre porque o construtor da classe ContaCorrente deve chamar o construtor da classe Conta, porém, agora, a classe Conta tem somente o construtor que recebe um parâmetro do tipo int.
- para corrigir o erro, fazer com que o construtor da classe ContaCorrente chame o construtor definido na classe Conta. 
- para isso, utilizamos a instrução super, passando o parâmetro do tipo inteiro:

~~~java
package br.com.fiap.tds;
public class ContaCorrente extends Conta{
	private String tipo;
	public ContaCorrente(int numero, String tipo){
		super(numero);
		this.tipo= tipo;
	}
}
// dessa forma, o construtor da subclasse chama o construtor da superclasse.
~~~

- resumindo: se o super não for chamado, o compilador acrescenta uma chamada ao construtor padrão: super().
- se não existir um construtor padrão na superclasse, haverá um erro de compilação e será necessário chamar explicitamente a instrução super, passando os parâmetros do construtor da superclasse.
- a chamada para o construtor da superclasse sempre deve ser implementada na primeira linha do construtor da subclasse!

---

## FAST TEST

### 1. A palavra-chave extends é utilizada na declaração de uma classe para determinar a sua:
> Superclasse.

### 2. "É um dos principais pilares da programação orientada a objetos. A ideia é criar classes com base em classes existentes, dessa forma, a classe que for criada herdará todos os comportamentos e atributos de uma classe já existente".
> Herança.

### 3. Uma classe que herda de outra classe é chamada de:
> Subclasse.

---

## Atividade Cap 8 - Como a herança pode me ajudar a programar melhor? - Implementação de herança nas classes do sistema fintech!

<em>
"Revise o diagrama de classe e suas implementações, que foram entregues nos capítulos anteriores. Nas outras entregas não era obrigatório o uso da Herança, porém, se você já o utilizou, parabéns! Poderá reaproveitá-lo para esta atividade.
<br>
Crie um projeto Java, conforme os capítulos anteriores, e implemente todas as classes do projeto Fintech. Não se esqueça de utilizar o encapsulamento para proteger os atributos e métodos. Os métodos gets e sets não aparecem no diagrama de classe.
<br>
Implemente uma classe de teste com o método main, escolha duas classes implementadas e crie objetos, instanciando-as. Coloque alguns valores em seus atributos e invoque seus métodos.
<br>
Ajuste o Diagrama de Classe para mapear as classes que utilizam herança. Faça as modificações utilizando a notação de generalização ou herança que foi vista no capítulo “Diagramando as Estruturas!”.
<br>
Depois, modifique o código-fonte para implementar a herança nas classes Java, de acordo com o diagrama de classe que foi ajustado. Crie os construtores para as superclasses e subclasses.
<br>
Para a entrega da atividade, exporte o diagrama de classe como imagem e copie, para um arquivo Microsoft Word, somente a parte da herança. Copie também os códigos-fonte que foram implementados em Java com a herança. Exporte como PDF e entregue para a gente. Dúvidas?
<br>
Você vai precisar entregar o projeto também, para isso, exporte o projeto no formado zip. "
</em>

--- 

[Voltar ao início!](https://github.com/monicaquintal/fintech)