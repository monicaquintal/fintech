# Solicitando os dados do cliente:
valor_compra = input("Informe o valor da compra realizada: ")
cupom = input("Digite o cupom de desconto: ")

#realizando o teste lógico
if cupom.upper() == "NIVER10":
# o .upper() converte as letras em caracteres maiusculos!
    valor_final = float(valor_compra) * 0.9 # cálculo de 10% de desconto!
else:
    valor_final = float(valor_compra)
    print("CUPOM INVÁLIDO! :(")

# Exibindo o valor final da compra
print("O valor final da compra é {}".format(valor_final))