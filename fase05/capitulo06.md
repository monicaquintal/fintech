<div id="fase05" align="center">
<h1>FASE 5 - OOP</h1>
<h2>Capítulo 06: Software de classe.</h2>
</div>

<div align="center">
<h2>1. SOFTWARE DE CLASSE</h2>
</div>

## 1.1 Introdução

- relembraremos as classes, entendendo como declará-las na linguagem Java e como instanciá-las, ou seja, como obter um objeto, que é a instância da classe, para que seja possível utilizá-la.

---

## 1.2 Classe

- uma classe possui o modelo ou estrutura a partir do qual os objetos serão criados.
- o processo de criação de um objeto a partir de uma classe é chamado de `instanciação`.

> [`EXEMPLO`](./projects/): As informações relevantes para uma conta bancária podem ser saldo, número da conta, agência, tipo de conta etc. Já as ações ou comportamentos importantes de uma classe Conta são: sacar, depositar, verificar o saldo etc. 

- podemos desenvolver uma classe ***Conta***, que contenha informações e comportamentos. Porém, essa classe é somente o modelo para o conceito de Conta Bancária dentro do sistema.
- assim como em um Banco Financeiro real, antes de guardar dinheiro na conta, é preciso ir ao Banco para abrir uma Conta.
- na orientação a objetos, primeiro precisamos criar um objeto utilizando a classe Conta, para depois utilizá-la.

> Em resumo, um ***objeto é uma instância de uma Classe***!

~~~java
// Para instanciar uma classe, utilizamos o operador new:
new Conta();
~~~

- precisamos armazenar o objeto em alguma variável para utilizá-lo posteriormente.
- portanto, ***declarar uma variável do tipo da Classe (Conta) e atribuir o objeto à variável com o operador de atribuição (=)***.

~~~java
Conta cc = new Conta();
Conta poupanca = new Conta();
~~~

- as variáveis cc e poupança armazenam a referência de seus respectivos objetos.
- podemos instanciar várias classes do mesmo tipo; nesse caso, há vários objetos do tipo Conta.
- classes Java são definidas em arquivos separados com a extensão .java e o nome do arquivo deve ser igual ao nome da Classe. 
  - por convenção, o nome segue o padrão UpperCamelCase, no qual as palavras sempre se iniciam com a letra em maiúscula.
- sintaxe:

~~~java
[modificador] class [NomeDaClasse] {
  // código
}
~~~

---

## 1.3 Atributos

- uma classe ***pode conter nenhum, um ou vários atributos***. 
- depois de instanciar a classe, os atributos serão utilizados para armazenar informações do objeto. 
  - as informações diferenciam um objeto do outro!!
- atributos são ***definidos por variáveis***, que podem ser:
  - ***tipo primitivo*** ou
  - ***tipo de referência***: a variável armazena uma referência ao objeto. 
- nomes do atributos:
  - lowerCamelCase (primeira letra é minúscula e as demais palavras começam com letra maiúscula).
  - utilizar substantivos e nomes bem definidos para os atributos.
  - nomes pouco sugestivos devem ser evitados.
- variáveis que definem um atributo em uma classe são chamadas de `variáveis de instância` (só é possível armazenar informações nessas variáveis após a instanciação da classe, ou seja, no objeto).
- declarar uma variável de instância segue a mesma sintaxe das variáveis locais.
- exemplo:

~~~java
public class Conta {
  int numero;
  int agencia;
  double saldo = 100;
  Calendar dataAbertura;
  String tipo;
  Cliente cliente;
}
~~~

- variáveis de instância recebem valores-padrão quando não atribuímos valores à sua declaração:
  - para números, o valor padrão é 0 (zero), 
  - para booleanos é falso (false) e 
  - para referência é vazio (null).

<div align="center">

Data type | Default value (for fields)
----------|---------------------------
byte | 0
short | 0
int | 0
long | 0L
float | 0.0f
double | 0.0d
char | '\u0000'
String (or any object) | null
boolean | false

</div>

---

## 1.4 Métodos

- métodos definem os comportamentos (ações ou serviços) que o objeto possui. 
- método é comportamento específico, residente no objeto, que define como ele deve agir quando exigido, definindo, assim, as habilidades do objeto.
- nomes dos métodos:
  - assim como os seus atributos, devem sempre ser escritos em lowerCamelCase.
  - geralmente utilizamos verbos para os nomes.
- sintaxe:

~~~java
<modificador> <tipo de retorno> <nomeDoMetodo>(<[lista de argumentos]>){
  [instrucoes];
}
~~~

~~~java
public class Conta {
	double saldo;
	
	public double recuperarSaldo() {
		return saldo;
	}
	
	public void depositar(int agencia, String numeroConta, double valor) {
		saldo = saldo + valor;
	}
}
~~~

- devemos definir o ***tipo de retorno*** que o método deve devolver. 
  - no exemplo acima, o método recuperarSaldo retorna um valor do tipo double. 
  - a `instrução return` é utilizada para retornar o valor.
  - o método retorna o valor do atributo saldo.
- caso o método não precise retornar nenhum valor, podemos definir o retorno como `void`. 
  - no exemplo, o método depositar não retorna nenhum valor. 
- métodos podem receber valores, como o método depositar.
  - os `parâmetros dos métodos` são declarados pela ***[lista de argumentos]***, conjunto de declarações de variáveis separadas por vírgulas e definidas dentro dos parênteses. 
  - os parâmetros se tornam variáveis locais no método, recebendo seus valores quando o método for chamado.

### 1.4.1 Sobrecarga de métodos

- sobrecarregar um método significa ***prover mais de uma versão de um mesmo método***. 
- as versões devem, *necessariamente*, conter parâmetros diferentes, seja no tipo ou no número desses parâmetros.
- o tipo de retorno não é relevante.
- LOGO, ***duas características diferenciam os métodos com o mesmo nome: o número de parâmetros e o tipo deles***, características que fazem parte da assinatura de um método.
- o uso de vários métodos com o mesmo nome e assinaturas diferentes é chamado de sobrecarga de métodos.

~~~java
public class Conta {
  double saldo;

  public void retirar(double valor) {
		saldo = saldo - valor;
	}
	
	public void retirar(double valor, double taxa) {
		saldo = saldo - valor - taxa;
	}
}
~~~

- no exemplo acima, a classe Conta possui dois métodos com o nome retirar, com assinaturas diferentes. 
  - um método recebe somente um parâmetro: o valor para retirada e 
  - o outro recebe dois parâmetros: o valor de retirada e o valor da taxa de retirada.

- a sobrecarga de métodos permite que os métodos se comportem de modo diferente, dependendo dos argumentos que recebem. 
- quando chamamos um método em um objeto, o Java verifica o nome do método e os parâmetros enviados para escolher o melhor método a ser invocado. 
- a `palavra reservada this` faz referência ao próprio objeto. É por meio dela que é possível acessar atributos, métodos e construtores do objeto em questão. 
- quando houver duas variáveis com o mesmo nome, uma sendo uma variável de instância (atributo da classe) e outra pertencente ao método, utilizar a palavra this para referenciar o atributo da classe, como a seguir:

~~~java
public class Conta {
  int agencia;

  public void setAgencia (int agencia) {
    this.agencia = agencia;
  }
}
~~~

---

## 1.5 Construtores

- 






--- 

[Voltar ao início!](https://github.com/monicaquintal/fintech)