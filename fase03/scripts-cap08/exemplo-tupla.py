#criação de uma tupla com as categorias dos Jedi
categorias = ("Youngling", "Padawan", "Knight", "Master")

#exibindo a tupla inteira
print(categorias)

#exibindo o segundo item da tupla -> Padawan
print(categorias[1])
print("---")

#usando um índice negativo para exibir o último item da tupla -> Master
print(categorias[-1])
print("---")

#exibindo cada item da tupla usando um loop
for categoria in categorias:
    print(categoria)
print("---")

#importando o módulo sys para conseguirmos usar ogetsizeof
import sys

#criando uma lista e uma tupla vazias, respectivamente
lista_vazia = []
tupla_vazia = ()

#printando o tipo e tamanho de cada estrutura
print("O objeto lista_vazia é do tipo {} e ocupa {} bytes na memória".format(type(lista_vazia), sys.getsizeof(lista_vazia)))
print("O objeto tupla_vazia é do tipo {} e ocupa {} bytes na memória".format(type(tupla_vazia), sys.getsizeof(tupla_vazia)))
