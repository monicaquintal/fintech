valor1 = input("Digite o primeiro número: ")
valor2 = input("Digite o segundo número: ")

#print(type(valor1))
#print(type(valor2))

soma = float(valor1) + float(valor2)
print("A soma entre os dois valores é igual a {}".format(soma))
# .format() é um recurso do Python que permite escrever um texto,
# indicando os locais onde serão incluídos valores de variáveis!

subtracao = float(valor1) - float(valor2)
print("A subtração entre os dois valores é igual a {}".format(subtracao))

multiplicacao = float(valor1) * float(valor2)
print("A multiplicação entre os dois valores é igual a {}".format(multiplicacao))

divisao = float(valor1) / float(valor2)
print("A divisão entre os dois valores é igual a {}".format(divisao))