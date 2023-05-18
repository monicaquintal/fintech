#método para validar a categoria informada
def validar_categoria(categoria_usuario):
    #verificando se a categoria digitada pelo usuário está presente na lista
    if categoria_usuario.upper() in categorias:
        #se estiver, é exibida essa mensagem
        print("Categoria válida!")
    else:
        #se não estiver, é exibida essa mensagem
        print("Categoria inválida!")

#lista com categorias de habilitação do DETRAN
categorias=["A", "B", "C", "D", "E"]

#importando o módulo que lida com as habilitacoes
import habilitacoes

#pedindo que o usuário a categoria
categoria_digitada  =  input("Digite  a  categoria  de habilitação")

#incluindo uma nova categoria falsa em tempo de execução
habilitacoes.categorias.append("ESPECIAL")

#utilizando o método validar_categoria para verificar se o que foi digitado é válido
habilitacoes.validar_categoria(categoria_digitada)