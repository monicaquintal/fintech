package br.com.fiap.bean;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.Calendar;
import java.util.List;

import br.com.fiap.bean.Colaborador;
import br.com.fiap.bean.EmpresaDBManager;

public class ColaboradorDAO {
    
    private Connection conexao;
  
    // CADASTRAR
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
    
    // LISTAR
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
    
    // REMOVER
    public Colaborador remover(int codigo){
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
      
    
    // BUSCAR POR ID
    
    public Colaborador buscarPorId(int codigoBusca) {
    Colaborador colaborador = null;
    PreparedStatement stmt = null;
    ResultSet rs = null;
    
    try {
      conexao = EmpresaDBManager.obterConexao();
      stmt = conexao.prepareStatement("SELECT * FROM TAB_COLABORADOR WHERE CODIGO_COLABORADOR = ?");
      stmt.setInt(1, codigoBusca);
      rs = stmt.executeQuery();
    
      if (rs.next()){
        int codigo = rs.getInt("CODIGO_COLABORADOR");
        String nome = rs.getString("NOME");
        String email = rs.getString("EMAIL");
        double salario = rs.getDouble("SALARIO");
        java.sql.Date data = rs.getDate("DATA_CONTRATACAO");
        Calendar dataContratacao = Calendar.getInstance();
        dataContratacao.setTimeInMillis(data.getTime());
        colaborador = new Colaborador(codigo, nome, email, salario, dataContratacao);
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
    return colaborador;
    }
    
    // ATUALIZAÇÃO
    
    public void atualizar(Colaborador colaborador){
        PreparedStatement stmt = null;
      
        try {
          conexao = EmpresaDBManager.obterConexao();
          String sql = "UPDATE TAB_COLABORADOR SET NOME = ?, EMAIL = ?, SALARIO = ?, DATA_CONTRATACAO = ? WHERE CODIGO_COLABORADOR = ?";
          stmt = conexao.prepareStatement(sql);
          stmt.setString(1, colaborador.getNome());
          stmt.setString(2, colaborador.getEmail());
          stmt.setDouble(3, colaborador.getSalario());
          java.sql.Date data = new java.sql.Date(colaborador.getDataContratacao().getTimeInMillis());
          stmt.setDate(4, data);
          stmt.setInt(5, colaborador.getCodigo());
      
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