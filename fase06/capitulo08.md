<div id="fase06" align="center">
<h1>FASE 6 - MODEL</h1>
<h2>Capítulo 08: Quando o café javanês consulta o oráculo.</h2>
</div>

<div align="center">
<h2>1. QUANDO O CAFÉ JAVANÊS CONSULTA O ORÁCULO</h2>
</div>

## 1.1 Introdução

- neste capítulo vamos ver o que o sistema deve fazer para interagir com os dados em um banco de dados.
- quais são os procedimentos necessários para que o sistema faça uso desse recurso tão essencial?

## 1.2 Recapitulando banco de dados

- a maioria dos sistemas precisa armazenar dados e informações para serem recuperados posteriormente. 

### a) `Sistemas de Gerenciamento de Banco de Dados` (SGBD):
- são sistemas especializados no armazenamento de dados, que oferecem funcionalidades e recursos avançados, como backup e pesquisas eficientes.
- SGBD é um conjunto de programas de computador responsáveis pelo gerenciamento de uma base de dados. 
- seu principal objetivo é retirar da aplicação cliente a responsabilidade de gerenciar acesso, manipulação e a organização dos dados. 
- o SGBD disponibiliza uma interface para que seus clientes possam realizar as operações de inclusão, alteração, exclusão e consulta de dados.
- os principais SGBDs utilizados aplicam o Modelo Relacional para armazenar informações e a linguagem (Structure Query Language) é utilizada para realizar as operações na base de dados. 
- principais SGBDs utilizados no mercado: Oracle Database, Microsoft SQL Server, PostgreSQL, Sysbase, MySQL Server, Apache Derby.

### b) `Modelo Relacional`:
- é um modelo de dados baseado em entidades e relacionamentos.
  - uma tabela armazena as informações relevantes da entidade.
  - a atribuição de valores de uma entidade constrói um registro da tabela.
  - a relação determina como cada registro da tabela se associa a registros de outras tabelas.
  - uma tabela é formada por registros (linhas) e os registros são formados por campos (colunas).
  - tabelas normalmente têm uma chave primária, que é um identificador único que garante que nenhum registro será duplicado. 

### c) SQL (Structured Query Language) ou Linguagem de Consulta Estruturada:
- é uma linguagem de pesquisa declarativa padrão para banco de dados relacional.
- por meio dela, os principais SGBDs interagem com os bancos de dados.
- alguns dos principais comandos SQL para manipulação de dados são: INSERT (inserção), UPDATE (atualização), SELECT (consulta) e DELETE(exclusão). 
- possibilita também criar tabelas, relações, controle de acesso, etc.

> Sistemas desenvolvidos na plataforma Java comunicam-se com o SGBD e manipulam seus dados utilizando a API Java DataBase Connectivity (JDBC)!

## 1.3 Java Database Connectivity

- é uma API (Application Programming Interface).
- contém um conjunto de regras que permite uma padronização no acesso aos diversos SGDBs disponíveis no mercado.
- define um conjunto de interfaces que devem ser implementadas pelas empresas fornecedoras de SGDB que desejam ser compatíveis com a plataforma Java.

> São os SGDBs que se adaptam à plataforma Java, por meio da implementação de um JDBC, e não o contrário! Todo o código implementado para sistema será o mesmo, pois as bibliotecas de acesso aos bancos de dados seguem os mesmos padrões.

- as bibliotecas de classes que permitem a integração de um SGDB à aplicação Java são chamadas `driver`.
- geralmente, as empresas fornecedoras de SGDBs oferecem o driver de conexão que seguem as especificações JDBC.

<div align="center">
<img src="./assets/estrutura-jdbc.png" width="50%">
<p><em>Estrutura JDBC.</em></p><br>
</div>

- uma das poucas classes que é implementada é a `DriverManager`, responsável por identificar o conjunto de bibliotecas (driver) que será utilizada: Oracle Driver, JDBC-ODBC Driver ou Sybase Driver.
- principais interfaces e a classe principal utilizadas para acesso ao banco de dados por meiodos padrões JDBC:

<div align="center">

Componente | Descrição
-----------|------------------
DriverManager | Responsável por encontrar o drive e estabelecer a conexão com o SGBD.
Conection | Representa a conexão com o SGBDR por onde serão passados os comandos SQL.
Statement<br>PreparedStatement<br>CallableStatement | Representa os registros de um Statement, PreparedStatement ou CallableStatement.

</div>

- as classes para manipulação de um banco de dados estão no `pacote java.sql`. 
- para conectar-se a um banco de bados (SGDB) é preciso solicitar a abertura de uma conexão com o banco de dados utilizando o Driver Manager, que é o gerenciador de drivers.
  - caso o DriverManager consiga estabelecer uma conexão com o SGDB, um `objeto do tipo java.sql.Connection` é retornado, caso contrário, uma exceção é gerada.
- quando uma implementação (driver) é carregada, é registrada utilizando o Driver Manager, a partir do qual serão criadas as conexões para a base de dados utilizando o `método getConnection()` (que recebe uma String que identifica o banco de dados que será conectado).
- após a conexão, é possível utilizar os objetos do tipo java.sql.Statement, java.sql.PreparedStatement e java.sql.CallableStatement para executar comandos SQL no SGDB.
- todas as interfaces e classes da estrutura do JDBC podem ser encontradas no `arquivo rt.jar`, contido no pacote JDK do Java.

> O desenvolvimento de sistemas que acessam banco de dados segue alguns passos comuns, independente da linguagem de programação utilizada.

### a) para a comunicação de um sistema a um BD:
  - primeiro, é necessário ter o “número” do banco de dados destinatário, considerando o endereço de IP (Internet Protocol) como endereço físico e a porta como endereço lógico.
  - com o banco disponível, obter uma conexão para realizar a comunicação.
  - por meio da conexão, é possível enviar comandos SQL, que serão executados no banco de dados.
  - por fim, a conexão é fechada, encerrando-se o processo.

### b) importante:
- deve ser realizado o tratamento dos possíveis problemas que podem ocorrer no processo da comunicação com o BD.
- o próprio programa deve prever e tratar as possíveis situações de erro.

## 1.4 Banco de dados Oracle e comandos SQL

### a) Criar a tabela para armazenar os dados dos colaboradores de uma empresa:
- A tabela deverá conter as colunas:
  - CODIGO_COLABORADOR: chave primária da tabela, campo obrigatório e com valores únicos. 
  - NOME: nome do colaborador. 
  - EMAIL: e-mail do funcionário. 
  - SALARIO: valor do salário do colaborador. 
  - DATA_CONTRATACAO: data de contratação.

> Para criar a tabela, podemos utilizar o comando SQL CREATE TABLE ou fazê-lo de forma visual, por meio do Oracle SQL Developer.

### b) Criar uma sequence para gerar os valores do código do colaborador.
- `sequence` é um objeto do banco de dados Oracle que gera sequências numéricas automaticamente.

## 1.4.1 Cadastrando informações na tabela

- utilizando o ***comando INSERT*** para cadastrar um registro em uma tabela. 
- podemos utilizá-lo de duas formas:
  - omitindo o nome das colunas e informando somente os valores para as colunas (os dados serão inseridos conforme a ordem das colunas na tabela) OU
  - informando os nomes das colunas e os valores que serão cadastrados. Nesse caso, cada valor será inserido na respectiva coluna, conforme a ordem estabelecida na instrução.

> O mais indicado é utilizar a segunda opção, pois caso a estrutura da tabela seja alterada, os valores ainda serão inseridos nas colunas corretas.

## 1.4.2 Leitura de dados de uma tabela

- para recuperar os registros de uma ou mais tabelas, utilizar o ***comando SELECT***.
- adicionar filtros às buscas, pois permitem recuperar os registros de acordo com condições, além de trazer registros mais específicos, e de utilizarem menos capacidade de processamento.
- para criar condições, precisamos utilizar os operadores relacionais e lógicos.

## 1.4.3 Atualizando valores na tabela

- utilizar o ***comando UPDATE***: permite a alteração do conteúdo de um ou mais campos (colunas) pertencentes a um ou mais registros (linhas) de uma tabela.
- é possível alterar várias colunas em um mesmo comando UPDATE, basta separar o nome das colunas por vírgula.

## 1.4.4 Remoção de registros de uma tabela (Delete)

- o ***comando DELETE*** permite remover um registro de uma tabela.
- precisamos especificar uma acondição, pois, sem ela, todos os registros da tabela serão apagados.

## 1.4.5 Conectando a base de dados

- no Eclipse, criar um novo projeto para manipular a base de dados: “File” > “New” > “Java Project”.
- configurar o ambiente (pois precisamos do driver JDBC do banco de dados Oracle). Logo, vamos adicionar o arquivo .jar ao projeto. Para isso: 
  - criar uma pasta chamada `lib` e adicionar o driver do Oracle (ojdbc11).
  - adicionar o driver no build path do projeto para que as classes e interfaces fiquem disponíveis para o uso dentro do projeto (botão direito do mouse no driver > “BuildPath” > “Add to Build Path).
- agora estamos prontos para começar a desenvolver um programa!!!

### para estabelecer uma conexão com a base de dados:
- precisamos criar um objeto do tipo Connection que representará a conexão. 
- depois, poderemos realizar qualquer operação (Cadastrar, Atualizar, Apagar e Buscar) na base de dados.
- exemplo de classe de teste que realiza a conexão com o banco de dados:

~~~java
package br.com.fiap.teste;
  
  import java.sql.Connection;
  import java.sql.DriverManager;
  import java.sql.SQLException;
  
  public class TesteView {
  
    public static void main(String[] args) {
      try {
        //Registra o Driver
        Class.forName("oracle.jdbc.driver.OracleDriver");
  
        //Abre uma conexão
        Connection conexao = DriverManager.getConnection(
            "jdbc:oracle:thin:@192.168.60.15:1521:ORCL", "OPS$PF0392", "123456");
        
        System.out.println("Conectado!");
        
        //Fecha a conexão
        conexao.close();
        
      //Tratamento de erro 
      } catch (SQLException e) {
        System.err.println("Não foi possível conectar no Banco de Dados");
        e.printStackTrace();
      } catch (ClassNotFoundException e) {
        System.err.println("O Driver JDBC não foi encontrado!");
        e.printStackTrace();
      }
    }
  }
~~~

## 1.4.6 Statements

- há três objetos do tipo Statement:
  - `Statement`: utilizado para executar um comando SQL estático. 
  - `Prepared Statement`: utilizado para executar um comando SQL que recebe um ou mais parâmetros. 
  - `Callable Statement`: utilizado para chamar stored procedures ou functions.
  
- os principais métodos dessas implementações são:
  - `executeUpdate`: executa um comando SQL (INSERT, UPDATE, DELETE) e retorna o número de linhas afetadas. 
  - `executeQuery`: executa um comando SQL (SELECT) e retorna o(s) resultado(s) por meio de um objeto do tipo ResultSet.

- para recuperar o objeto do tipo Statement, utilizamos o método createStatement(), da interface Connection.

### a) Inclusão:

~~~java
Statement stmt = conexao.createStatement();
  stmt.executeUpdate("INSERT INTO TAB_COLABORADOR(CODIGO_COLABORADOR, NOME, EMAIL, SALARIO, DATA_CONTRATACAO) VALUES (SQ_COLABORADOR.NEXTVAL, 'Leandro', 'leandro@gmail.com', 1500, TO_DATE('10/12/2009','dd/mm/yyyy'))");
~~~

### b) Alteração:

~~~java
Statement stmt = conexao.createStatement();
  stmt.executeUpdate("UPDATE TAB_COLABORADOR SET SALARIO = 5000 WHERE CODIGO_COLABORADOR = 1");
~~~

### c) Exclusão:

~~~java
Statement stmt = conexao.createStatement();
  stmt.executeUpdate("DELETE FROM TAB_COLABORADOR WHERE CODIGO_COLABORADOR = 1");
~~~

### d) Busca:

~~~java
Statement stmt = conexao.createStatement();
  ResultSet rs = stmt.executeQuery("SELECT * FROM TAB_COLABORADOR");
~~~

> Nos exemplos acima, os comandos SQL são estáticos (os valores já estão definidos diretamente na string). Quando precisamos de comandos SQL configuráveis, devemos utilizar a interface `PreparedStatement`!

- assim, podemos parametrizar o comando SQL com o ponto de interrogação(?) por meio dos métodos set.
- também é possível atribuir valores a esses parâmetros, evitando ataques do tipo SQL Injection.
- é indicado utilizar o PreparedStatement para manipular a base de dados, sempre que possível, pois ele proporciona melhor performance e clareza do código-fonte.
- para obter o objeto PreparedStatement, utilizamos o método prepareStatement() da interface Connection.
- exemplo:

~~~java
PreparedStatement stmt = conexao.prepareStatement("INSERT INTO TAB_COLABORADOR(CODIGO_COLABORADOR, NOME, EMAIL, SALARIO, DATA_CONTRATACAO) VALUES (SQ_COLABORADOR.NEXTVAL, ?, ?, ?, ?)");
  stmt.setString(1, "Thiago"); //Primero parâmetro (Nome)
  stmt.setString(2, "thiago@gmail.com");//Segundo parâmetro (Email)
  stmt.setDouble(3, 5000); //Terceiro parâmetro (Salário)
  //Instancia um objeto do tipo java.sql.Date com a data atual
  java.sql.Date data = new java.sql.Date(new java.util.Date().getTime());
  stmt.setDate(4,data);//Quarto parâmetro (data contratação)
        
  stmt.executeUpdate();
~~~

> IMPORTANTE: no exemplo acima, no lugar dos dados dos parâmetros, foram adicionados `pontos de interrogação (?)` para que, posteriormente,informemos os respectivos valores por meio dos métodos set, que serão escolhidos de acordo com o tipo de dado. Esse método recebe dois parâmetros: o primeiro é a posição do ponto de interrogação (?), que se inicia em 1, e o segundo é o valor que será atribuído a essa posição.

- para cada uma das operações em SQL, é possível utilizar o PreparedStatement:

### a) Alteração:

~~~java
PreparedStatement stmt = conexao.prepareStatement("UPDATE TAB_COLABORADOR SET SALARIO = ? WHERE CODIGO_COLABORADOR = ?");
  stmt.setDouble(1, 5000);
  stmt.setInt(2, 100);
  stmt.executeUpdate();
~~~

### b) Exclusão:

~~~java
PreparedStatement stmt = conexao.prepareStatement("DELETE FROM TAB_COLABORADOR WHERE CODIGO_COLABORADOR = ?");
~~~

### c) Busca:

~~~java
PreparedStatement stmt = conexao.prepareStatement("SELECT * FROM TAB_COLABORADOR WHERE NOME = ?");
  stmt.setString(1, "Thiago");
  ResultSet result = stmt.executeQuery();
~~~

## 1.4.7 ResultSet

- a interface ResultSet é responsável pelo conjunto de registros retornados de um comando SELECT do SQL.
- permite navegar por seus registros de forma sequencial. Dessa forma, precisamos ***chamar o método next*** para mover o cursor para o próximo registro.
  - esse método retorna false quando não conseguir ir para o próximo registro, caracterizando o final dos registros. 
  - as colunas do registro podem ser acessadas por meio de um índice que representa a posição da coluna (inicia em 1) ou por meio do próprio nome da coluna.
- ***principais métodos***:
  - `next`: move o cursor para a próxima linha.
  - `getInt`: retorna os dados da coluna designada como int do Java.
  - `getString`: retorna os dados da coluna designada como uma String do Java.
  - `getBoolean`: retorna os dados da coluna designada como boolean do Java.
  - `getDouble`: retorna os dados da coluna designada como double do Java.

Exemplo:

~~~java
import java.sql.Connection;
  import java.sql.DriverManager;
  import java.sql.PreparedStatement;
  import java.sql.ResultSet;
  import java.sql.SQLException;
  
  public class TesteView {
  
    public static void main(String[] args) {
      try {
    //Registra o Driver
    Class.forName("oracle.jdbc.driver.OracleDriver");
  
    //Abre uma conexão
    Connection conexao = DriverManager.getConnection(
  "jdbc:oracle:thin:@oracle.fiap.com.br:1521:ORCL", "OPS$PF0392", "123456");
        
    System.out.println("Conectado!");
        
  PreparedStatement stmt = conexao.prepareStatement("SELECT * FROM TAB_COLABORADOR WHERE NOME = ?");
    stmt.setString(1, "Thiago");
    ResultSet result = stmt.executeQuery();
        
    //Percorre todos os registros encontrados
    while (result.next()){
      //Recupera os valores de cada coluna
      int codigo = result.getInt("CODIGO_COLABORADOR");
      String nome = result.getString("NOME");
      String email = result.getString("EMAIL");
      double salario = result.getDouble("SALARIO");
      java.sql.Date data = result.getDate("DATA_CONTRATACAO");
      //Exibe as informações do registro
      System.out.println(codigo + " " + nome + " " + email + " " + salario + " " + data);
  }
        
    //Fecha a conexão
    conexao.close();
        
    //Tratamento de erro  
    } catch (SQLException e) {
      System.err.println("Não foi possível conectar no Banco de Dados");
      e.printStackTrace();
    } catch (ClassNotFoundException e) {
      System.err.println("O Driver JDBC não foi encontrado!");
      e.printStackTrace();
    }
  }
  }
~~~

## 1.4.8 CallableStatement

- utilizado para chamar stored procedures ou functions de forma padronizada para todas as bases de dados.
- é possível chamar uma stored procedure utilizando ou não o parâmetro de resultado.

### a) sintaxe básica para chamada de stored procedure com parâmetro de resultado:

~~~java
CallableStatement cs = conexao.prepareCall("{call proc(?)}");
~~~

### b) sem parâmetro de resultado:

~~~java
CallableStatement cs = conexao.prepareCall("{call proc()}");
~~~

- para definir os parâmetros de entrada, utilizamos o mesmo padrão do PreparedStatement, e os parâmetros de saída são definidos por meio do método registerOutParameter.

~~~java
//Cria o CallableStatement
  CallableStatement cs = conexao.prepareCall("{call SP_Contar_Colaboradores(?,?)}");
        
  //Define o tipo do parâmetro de saída (primeiro ?)
  cs.registerOutParameter(1, java.sql.Types.INTEGER);
        
  //Define o valor do parâmetro de entrada (segundo ?)
  cs.setDouble(2, 1500);
        
  //Executa a procedure
  cs.executeUpdate();
        
  //Recupera o valor do parâmetro de saída
  int total = cs.getInt(1);
  System.out.println("Total de colaboradores com salário maior que 1500: " + total);
~~~

- exemplo de Stored Procedure que retorna o resultado de um SELECT:

~~~java
//Cria o CallableStatement
  CallableStatement cs = conexao.prepareCall("{call SP_Retornar_Todos_Colaboradores(?,?)}");
        
  //Define o valor do parâmetro de entrada 
  cs.setDouble(1,1500);
  
  //Define o tipo do parâmetro de saída
  cs.registerOutParameter(2, OracleTypes.CURSOR);
        
  //Executa a procedure
  cs.execute();
        
  //Recupera o valor do parâmetro de saída
  ResultSet cursor = (ResultSet) cs.getObject(2);
        
  //Percorre todos os registros encontrados
  while (cursor.next()){
    //Recupera os valores de cada coluna
    int codigo = cursor.getInt("CODIGO_COLABORADOR");
    String nome = cursor.getString("NOME");
    System.out.println(codigo + " " + nome);
  }
~~~

---

<div align="center">
<h2>Implementando o exemplo</h2>
</div>

## 1. Começar desenvolvendo o Java Bean Colaborador:
- essa classe irá representar a nossa tabela do banco de dados, devendo possuir atributos que representam cada coluna da tabela. 
- utilizaremos o encapsulamento, deixando os atributos com o modificador de acesso private, e disponibilizaremos os métodos assessores (gets e sets). 
- implementaremos o construtor padrão e com parâmetros.
- para armazenar a data de contratação, utilizamos a classe java.util.Calendar. 

> Essa classe possui grande importância por facilitar o processo de passagem de valores do banco de dados para a aplicação Java e vice-versa.

~~~java
package br.com.fiap.bean;

import java.util.Calendar;

public class Colaborador {

	private int codigo;
	private String nome;
	private String email;
	private double salario;
	private Calendar dataContratacao;
	
	public Colaborador(int codigo, String nome, String email, double salario, Calendar dataContratacao) {
		super();
		this.codigo = codigo;
		this.nome = nome;
		this.email = email;
		this.salario = salario;
		this.dataContratacao = dataContratacao;
	}
	
	public Colaborador() {
		super();
	}
	
	public int getCodigo() {
		return codigo;
	}
	
	public void setCodigo(int codigo) {
		this.codigo = codigo;
	}
	
	public String getNome() {
		return nome;
	}
	
	public void setNome(String nome) {
		this.nome = nome;
	}
	
	public String getEmail() {
		return email;
	}
	
	public void setEmail(String email) {
		this.email = email;
	}
	
	public double getSalario() {
		return salario;
	}
	
	public void setSalario(double salario) {
		this.salario = salario;
	}
	
	public Calendar getDataContratacao() {
		return dataContratacao;
	}
	
	public void setDataContratacao(Calendar dataContratacao) {
		this.dataContratacao = dataContratacao;
	}	
}
~~~

## 2. Criar uma classe que será responsável por fornecer uma conexão com o BD:
- para cada operação no banco dados (INSERT, UPDATE, SELECT e DELETE),foi necessário primeiro obter uma conexão. 
- com essa classe, não vamos precisar escrever códigos repetidos, utilizando os conceitos de orientação a objetos.

> Essa classe possui somente um método estático que cria e retorna uma conexão com o banco. O método é estático para que a classe não precise de uma instância para ser invocada, bastando referenciá-la por meio do nome da classe: `EmpresaDBManager.obterConexao()`.

~~~java
package br.com.fiap.jdbc;
  
  import java.sql.Connection;
  import java.sql.DriverManager;
  
  public class EmpresaDBManager {
  
    public static Connection obterConexao() {
      Connection conexao = null;
      try {
        Class.forName("oracle.jdbc.driver.OracleDriver");
  
        conexao = DriverManager.getConnection(
            "jdbc:oracle:thin:@oracle.fiap.com.br:1521:ORCL",
            "OPS$XXXX", "XXXXX");
  
      } catch (Exception e) {
        e.printStackTrace();
      }
      return conexao;
    }
  
  }
~~~

## 3. Desenvolver a classe ColaboradorDAO, responsável pela manipulação da tabela TAB_COLABORADOR.
- a classe possui essa nomenclatura pois segue um padrão de projeto chamado DAO (`Data Access Object`), responsável pelo código de acesso aos dados, centralizando a implementação dessa responsabilidade no projeto. 
- a classe DAO deve terum atributo para armazenar o objeto que representa a conexão com o BD.

~~~java
package br.com.fiap.dao;
  
  public class ColaboradorDAO {
  
    private Connection conexao;
  
  }
~~~

- desenvolver o primeiro método, que será responsável por cadastrar um colaborador.
- para isso, ele deve receber um objeto do tipo Colaborador para ser inserido no banco:

~~~java
public class ColaboradorDAO {
    
      private Connection conexao;
    
      public void cadastrar(Colaborador colaborador) {
        PreparedStatement stmt = null;
    
        try {
          conexao = EmpresaDBManager.obterConexao();
          String sql = "INSERT INTO TAB_COLABORADOR(CODIGO_COLABORADOR, NOME, EMAIL, SALARIO, DATA_CONTRATACAO) VALUES (SQ_COLABORADOR.NEXTVAL, ?, ?, ?, ?)";
          stmt = conexao.prepareStatement(sql);
          stmt.setString(1, colaborador.getNome());
          stmt.setString(2, colaborador.getEmail());
          stmt.setDouble(3, colaborador.getSalario());
          java.sql.Date data = new java.sql.Date(colaborador.getDataContratacao().getTimeInMillis());
          stmt.setDate(4, data);
    
          stmt.executeUpdate();
        } catch (SQLException e) {
          e.printStackTrace();
        } finally {
          try {
            stmt.close();
            conexao.close();
          } catch (SQLException e) {
            e.printStackTrace();
          }
        }
      }
    }
~~~

- não se esquecer dos imports! 
- um atalho do eclipse é o CTRL + SHIFT + o para fazer o import automático.

~~~java
import java.sql.Connection;
  import java.sql.PreparedStatement;
  import java.sql.SQLException;
  
  import br.com.fiap.bean.Colaborador;
  import br.com.fiap.jdbc.EmpresaDBManager;
~~~

## 4. Desenvolver uma classe de teste para verificar se está tudo correto.
- criar uma classe com o método main:

> Essa classe cria uma instância da classe ColaboradorDAO e do Colaborador e, por meio do método cadastrar do ColaboradorDAO, é realizado o cadastro no banco de dados.

~~~java
package br.com.fiap.teste;
  
  import java.util.Calendar;
  
  import br.com.fiap.bean.Colaborador;
  import br.com.fiap.dao.ColaboradorDAO;
  
  public class TesteCadastro {
  
    public static void main(String[] args) {
      //Instancia o DAO
      ColaboradorDAO dao = new ColaboradorDAO();
  
      //Instancia o Colaborador
      Colaborador colaborador = new Colaborador();
      colaborador.setNome("Pedro");
      colaborador.setEmail("pedro@fiap.com.br");
      colaborador.setSalario(5000);
      colaborador.setDataContratacao(Calendar.getInstance());
  
      //Cadastra no banco de dados
      dao.cadastrar(colaborador);
  
      System.out.println("Cadastrado!");
    }
  
  }
~~~

## 5. Implementar a próxima funcionalidade no DAO: listar.
- voltar à classe ColaboradorDAO e criar o novo método.

> Esse método retorna uma lista comtodos os colaboradores cadastrados. Não se esqueça de adicionar os imports do List, ArrayList e ResultSet.

- para cada registro no ResultSet, é instanciado um objeto Colaborador para armazenar as informações encontradas. Esse objeto é adicionado à lista que será retornada.

~~~java
public List<Colaborador> listar() {
    //Cria uma lista de colaboradores
    List<Colaborador> lista = new ArrayList<Colaborador>();
    PreparedStatement stmt = null;
    ResultSet rs = null;
    try {
      conexao = EmpresaDBManager.obterConexao();
    stmt = conexao.prepareStatement("SELECT * FROM TAB_COLABORADOR");
    rs = stmt.executeQuery();
  
    //Percorre todos os registros encontrados
    while (rs.next()) {
    int codigo = rs.getInt("CODIGO_COLABORADOR");
    String nome = rs.getString("NOME");
        String email = rs.getString("EMAIL");
        double salario = rs.getDouble("SALARIO");
        java.sql.Date data = rs.getDate("DATA_CONTRATACAO");
        Calendar dataContratacao = Calendar.getInstance();
        dataContratacao.setTimeInMillis(data.getTime());
        //Cria um objeto Colaborador com as informações encontradas
        Colaborador colaborador = new Colaborador(codigo, nome, email, salario, dataContratacao);
        //Adiciona o colaborador na lista
        lista.add(colaborador);
      }
    } catch (SQLException e) {
      e.printStackTrace();
    }finally {
      try {
        stmt.close();
        rs.close();
        conexao.close();
      } catch (SQLException e) {
        e.printStackTrace();
      }
    }
    return lista;
  }
~~~
## 6. Criação de uma classe de teste para listagem.
- essa classe irá instanciar o ColaboradorDAO e chamar o método listar() para receber a lista de colaboradores cadastrados no banco de dados.
- implementado um laço de repetição foreach para percorrer toda a lista e imprimir os valores dos atributos do colaborador.

~~~java
package br.com.fiap.teste;
  
  import java.util.List;
  import br.com.fiap.bean.Colaborador;
  import br.com.fiap.dao.ColaboradorDAO;
  
  public class TesteListagem {
  
    public static void main(String[] args) {
  
      ColaboradorDAO dao = new ColaboradorDAO();
      
      List&lt;Colaborador> lista = dao.listar();
      for (Colaborador item : lista) {
        System.out.println(item.getCodigo() + " " + item.getNome() + " " + item.getEmail() + " " + item.getSalario() + " " + item.getDataContratacao().getTime());
      }
    }
    
  }
~~~

## 7. Implementando a funcionalidade para remover um colaborador do BD.
- esse método, que deve ser implementado na classe ColaboradorDAO, recebe o código do colaborador, que será excluído do banco de dados.

~~~java
public void remover(int codigo){
    PreparedStatement stmt = null;
  
    try {
      conexao = EmpresaDBManager.obterConexao();
      String sql = "DELETE FROM TAB_COLABORADOR WHERE CODIGO_COLABORADOR = ?";
      stmt = conexao.prepareStatement(sql);
      stmt.setInt(1, codigo);
      stmt.executeUpdate();
    } catch (SQLException e) {
      e.printStackTrace();
    } finally {
      try {
        stmt.close();
        conexao.close();
      } catch (SQLException e) {
        e.printStackTrace();
      }
    }
  }
~~~

## 8. Criação de uma nova Classe para testes.
- a classe de teste instancia o ColaboradorDAO para chamar o método remover, passando o ID do colaborador que será excluído do banco de dados.

~~~java
package br.com.fiap.teste;
  
  import br.com.fiap.dao.ColaboradorDAO;
  
  public class TesteRemocao {
  
    public static void main(String[] args) {
      ColaboradorDAO dao = new ColaboradorDAO();
      //Remove o colaborador com código 1
      dao.remover(1);
    }
}
~~~

## 9. Implementar o método patra buscar por código, para posteriormente implementar o método de atualização.










--- 

[Voltar ao início!](https://github.com/monicaquintal/fintech)