package br.com.fiap.bean;
  
  import br.com.fiap.bean.ColaboradorDAO;
  
  public class TesteRemocao {
  
    public static void main(String[] args) {
      ColaboradorDAO dao = new ColaboradorDAO();
      //Remove o colaborador com código 1
      dao.remover(1);
    }
}